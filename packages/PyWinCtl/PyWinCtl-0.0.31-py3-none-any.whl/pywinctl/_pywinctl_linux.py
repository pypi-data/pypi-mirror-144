#!/usr/bin/python
# -*- coding: utf-8 -*-

import math
import os
import platform
import subprocess
import sys
import time
import tkinter as tk
from typing import Union, List, Tuple

import Xlib.X
import Xlib.display
import Xlib.protocol
import ewmh
from Xlib.xobject.colormap import Colormap
from Xlib.xobject.cursor import Cursor
from Xlib.xobject.drawable import Drawable, Pixmap, Window
from Xlib.xobject.fontable import Fontable, GC, Font
from Xlib.xobject.resource import Resource
from pynput import mouse

from pywinctl import pointInRect, BaseWindow, Rect, Point, Size

DISP = Xlib.display.Display()
SCREEN = DISP.screen()
ROOT = SCREEN.root
EWMH = ewmh.EWMH(_display=DISP, root=ROOT)

# WARNING: Changes are not immediately applied, specially for hide/show (unmap/map)
#          You may set wait to True in case you need to effectively know if/when change has been applied.
WAIT_ATTEMPTS = 10
WAIT_DELAY = 0.025  # Will be progressively increased on every retry

# These _NET_WM_STATE_ constants are used to manage Window state and are documented at
# https://ewmh.readthedocs.io/en/latest/ewmh.html
WM_CHANGE_STATE = 'WM_CHANGE_STATE'
WM_STATE = '_NET_WM_STATE'
STATE_MODAL = '_NET_WM_STATE_MODAL'
STATE_STICKY = '_NET_WM_STATE_STICKY'
STATE_MAX_VERT = '_NET_WM_STATE_MAXIMIZED_VERT'
STATE_MAX_HORZ = '_NET_WM_STATE_MAXIMIZED_HORZ'
STATE_SHADED = '_NET_WM_STATE_SHADED'
STATE_SKIP_TASKBAR = '_NET_WM_STATE_SKIP_TASKBAR'
STATE_SKIP_PAGER = '_NET_WM_STATE_SKIP_PAGER'
STATE_HIDDEN = '_NET_WM_STATE_HIDDEN'
STATE_FULLSCREEN = '_NET_WM_STATE_FULLSCREEN'
STATE_ABOVE = '_NET_WM_STATE_ABOVE'
STATE_BELOW = '_NET_WM_STATE_BELOW'
STATE_ATTENTION = '_NET_WM_STATE_DEMANDS_ATTENTION'
STATE_FOCUSED = '_NET_WM_STATE_FOCUSED'
STATE_NULL = 0

# EWMH/Xlib set state actions
ACTION_UNSET = 0   # Remove state
ACTION_SET = 1     # Add state
ACTION_TOGGLE = 2  # Toggle state

# EWMH/Xlib WINDOW_TYPE values
WM_WINDOW_TYPE = '_NET_WM_WINDOW_TYPE'
WINDOW_DESKTOP = '_NET_WM_WINDOW_TYPE_DESKTOP'
WINDOW_NORMAL = '_NET_WM_WINDOW_TYPE_NORMAL'

# EWMH/Xlib State Hints
HINT_STATE_WITHDRAWN = 0
HINT_STATE_NORMAL = 1
HINT_STATE_ICONIC = 3


def getActiveWindow():
    """
    Get the currently active (focused) Window

    :return: Window object or None
    """
    win_id = EWMH.getActiveWindow()
    if win_id:
        return LinuxWindow(win_id)
    return None


def getActiveWindowTitle() -> str:
    """
    Get the title of the currently active (focused) Window

    :return: window title as string or empty
    """
    win = getActiveWindow()
    if win:
        return win.title
    else:
        return ""


def getWindowsAt(x: int, y: int):
    """
    Get the list of Window objects whose windows contain the point ``(x, y)`` on screen

    :param x: X screen coordinate of the window(s)
    :param y: Y screen coordinate of the window(s)
    :return: list of Window objects
    """
    windowsAtXY = []
    for win in getAllWindows():
        if pointInRect(x, y, win.left, win.top, win.width, win.height):
            windowsAtXY.append(win)
    return windowsAtXY


def getWindowsWithTitle(title: str):
    """
    Get the list of Window objects whose title match the given string

    :param title: title of the desired windows as string
    :return: list of Window objects
    """
    matches = []
    for win in getAllWindows():
        if win.title == title:
            matches.append(win)

    return matches


def getAllTitles() -> List[str]:
    """
    Get the list of titles of all visible windows

    :return: list of titles as strings
    """
    return [window.title for window in getAllWindows()]


def getAllWindows():
    """
    Get the list of Window objects for all visible windows

    :return: list of Window objects
    """
    windows = EWMH.getClientList()
    return [LinuxWindow(window) for window in windows]


def _xlibGetAllWindows(parent: int = None, title: str = "") -> List[int]:
    # Not using window class (get_wm_class())

    if not parent:
        parent = ROOT
    allWindows = [parent]

    def findit(hwnd):
        query = hwnd.query_tree()
        for child in query.children:
            allWindows.append(child)
            findit(child)

    findit(parent)
    if not title:
        matches = allWindows
    else:
        matches = []
        for w in allWindows:
            if w.get_wm_name() == title:
                matches.append(w)
    return matches


def getAllAppsTitles() -> List[str]:
    """
    Get the list of names of all visible apps

    :return: list of names as strings
    """
    return list(getAllAppsWindowsTitles().keys())


def getAllAppsWindowsTitles() -> dict:
    """
    Get all visible apps names and their open windows titles

    Format:
        Key: app name

        Values: list of window titles as strings

    :return: python dictionary
    """
    result = {}
    for win in getAllWindows():
        appName = win.getAppName()
        if appName in result.keys():
            result[appName].append(win.title)
        else:
            result[appName] = [win.title]
    return result


def _getBorderSizes():

    class App(tk.Tk):

        def __init__(self):
            super().__init__()
            self.geometry('0x0+200+200')
            self.update_idletasks()

            pos = self.geometry().split('+')
            self.bar_height = self.winfo_rooty() - int(pos[2])
            self.border_width = self.winfo_rootx() - int(pos[1])
            self.destroy()

        def getTitlebarHeight(self):
            return self.bar_height

        def getBorderWidth(self):
            return self.border_width

    app = App()
    # app.mainloop()
    return app.getTitlebarHeight(), app.getBorderWidth()


def _getWindowAttributes(hWnd = None):
    # Leaving this as reference of using X11 library
    # https://github.com/evocount/display-management/blob/c4f58f6653f3457396e44b8c6dc97636b18e8d8a/displaymanagement/rotation.py
    # https://github.com/nathanlopez/Stitch/blob/master/Configuration/mss/linux.py
    # https://gist.github.com/ssokolow/e7c9aae63fb7973e4d64cff969a78ae8
    # https://stackoverflow.com/questions/36188154/get-x11-window-caption-height

    from ctypes.util import find_library
    from ctypes import (
        POINTER, Structure, byref, c_char_p, c_int, c_int32, c_long, c_uint,
        c_uint32, c_ulong, c_ushort, c_void_p, cast, cdll, create_string_buffer)

    x11 = find_library('X11')
    xlib = cdll.LoadLibrary(x11)

    class XWindowAttributes(Structure):

        _fields_ = [('x', c_int32), ('y', c_int32),
                    ('width', c_int32), ('height', c_int32), ('border_width', c_int32),
                    ('depth', c_int32), ('visual', c_ulong), ('root', c_ulong),
                    ('class', c_int32), ('bit_gravity', c_int32),
                    ('win_gravity', c_int32), ('backing_store', c_int32),
                    ('backing_planes', c_ulong), ('backing_pixel', c_ulong),
                    ('save_under', c_int32), ('colourmap', c_ulong),
                    ('mapinstalled', c_uint32), ('map_state', c_uint32),
                    ('all_event_masks', c_ulong), ('your_event_mask', c_ulong),
                    ('do_not_propagate_mask', c_ulong), ('override_redirect', c_int32), ('screen', c_ulong)]

    attr = XWindowAttributes()
    d = xlib.XOpenDisplay(0)
    # s = xlib.XDefaultScreen(d)
    # root = xlib.XDefaultRootWindow(d)
    # fg = xlib.XBlackPixel(d, s)
    # bg = xlib.XWhitePixel(d, s)
    # w = xlib.XCreateSimpleWindow(d, root, 600, 300, 400, 200, 0, fg, bg)
    # xlib.XMapWindow(d, w)
    # time.sleep(4)
    # a = xlib.XInternAtom(d, "_GTK_FRAME_EXTENTS", True)
    # if not a:
    #     a = xlib.XInternAtom(d, "_NET_FRAME_EXTENTS", True)
    # t = c_int()
    # f = c_int()
    # n = c_ulong()
    # b = c_ulong()
    # xlib.XGetWindowProperty(d, w, a, 0, 4, False, Xlib.X.AnyPropertyType, byref(t), byref(f), byref(n), byref(b), byref(attr))
    xlib.XGetWindowAttributes(d, hWnd.id, byref(attr))
    # r = c_ulong()
    # x = c_int()
    # y = c_int()
    # w = c_uint()
    # h = c_uint()
    # b = c_uint()
    # d = c_uint()
    # xlib.XGetGeometry(d, hWnd.id, byref(r), byref(x), byref(y), byref(w), byref(h), byref(b), byref(d))
    # print(x, y, w, h)
    xlib.XCloseDisplay(d)

    # Other references (send_event and setProperty):
    # prop = DISP.intern_atom(WM_CHANGE_STATE, False)
    # data = (32, [Xlib.Xutil.IconicState, 0, 0, 0, 0])
    # ev = Xlib.protocol.event.ClientMessage(window=self._hWnd.id, client_type=prop, data=data)
    # mask = Xlib.X.SubstructureRedirectMask | Xlib.X.SubstructureNotifyMask
    # DISP.send_event(destination=ROOT, event=ev, event_mask=mask)
    # data = [Xlib.Xutil.IconicState, 0, 0, 0, 0]
    # EWMH._setProperty(_type="WM_CHANGE_STATE", data=data, mask=mask)
    # for atom in w.list_properties():
    #     print(DISP.atom_name(atom))
    return attr


class LinuxWindow(BaseWindow):

    def __init__(self, hWnd: Union[Cursor, Drawable, Pixmap, Resource, Fontable, Window, GC, Colormap, Font]):
        super().__init__()
        self._hWnd = hWnd
        self._parent = self._hWnd.query_tree().parent
        self._setupRectProperties()
        # self._saveWindowInitValues()  # Store initial Window parameters to allow reset and other actions

    def _getWindowRect(self) -> Rect:
        # https://stackoverflow.com/questions/12775136/get-window-position-and-size-in-python-with-xlib - mgalgs
        win = self._hWnd
        geom = win.get_geometry()
        x = geom.x
        y = geom.y
        while True:
            parent = win.query_tree().parent
            pgeom = parent.get_geometry()
            x += pgeom.x
            y += pgeom.y
            if parent.id == ROOT.id:
                break
            win = parent
        w = geom.width
        h = geom.height
        # ww = DISP.create_resource_object('window', self._hWnd)
        # ret = ww.translate_coords(self._hWnd, x, y)
        return Rect(x, y, x + w, y + h)

    def getExtraFrameSize(self, includeBorder: bool = True) -> Tuple[int, int, int, int]:
        """
        Get the extra space, in pixels, around the window, including or not the border.
        Notice not all applications/windows will use this property values

        :param includeBorder: set to ''False'' to avoid including borders
        :return: (left, top, right, bottom) frame size as a tuple of int
        """
        a = DISP.intern_atom("_GTK_FRAME_EXTENTS", True)
        if not a:
            a = DISP.intern_atom("_NET_FRAME_EXTENTS", True)
        ret = self._hWnd.get_property(a, Xlib.X.AnyPropertyType, 0, 32)
        if ret:
            ret = ret.value
        else:
            ret = (0, 0, 0, 0)
        borderWidth = 0
        if includeBorder:
            titleHeight, borderWidth = _getBorderSizes()
        frame = (ret[0] + borderWidth, ret[2] + borderWidth, ret[1] + borderWidth, ret[3] + borderWidth)
        return frame

    def getClientFrame(self):
        """
        Get the client area of window including scroll, menu and status bars, as a Rect (x, y, right, bottom)
        Notice that this method won't match non-standard window decoration sizes

        :return: Rect struct
        """
        geom = self._hWnd.get_geometry()
        borderWidth = geom.border_width
        # Didn't find a way to get title bar height using Xlib
        titleHeight, borderWidth = _getBorderSizes()
        res = Rect(self.left + borderWidth, self.top + titleHeight, self.right - borderWidth, self.bottom - borderWidth)
        return res

    def _saveWindowInitValues(self) -> None:
        # Saves initial rect values to allow reset to original position, size, state and hints.
        self._init_rect = self._getWindowRect()
        self._init_state = self._hWnd.get_wm_state()
        self._init_hints = self._hWnd.get_wm_hints()
        self._init_normal_hints = self._hWnd.get_wm_normal_hints()
        # self._init_attributes = self._hWnd.get_attributes()  # can't be modified, so not saving it

    def __repr__(self):
        return '%s(hWnd=%s)' % (self.__class__.__name__, self._hWnd)

    def __eq__(self, other):
        return isinstance(other, LinuxWindow) and self._hWnd == other._hWnd

    def close(self) -> bool:
        """
        Closes this window. This may trigger "Are you sure you want to
        quit?" dialogs or other actions that prevent the window from
        actually closing. This is identical to clicking the X button on the
        window.

        :return: ''True'' if window is closed
        """
        EWMH.setCloseWindow(self._hWnd)
        EWMH.display.flush()
        return self._hWnd not in EWMH.getClientList()

    def minimize(self, wait: bool = False) -> bool:
        """
        Minimizes this window

        :param wait: set to ''True'' to confirm action requested (in a reasonable time)
        :return: ''True'' if window minimized
        """
        if not self.isMinimized:
            prop = DISP.intern_atom(WM_CHANGE_STATE, False)
            data = (32, [Xlib.Xutil.IconicState, 0, 0, 0, 0])
            ev = Xlib.protocol.event.ClientMessage(window=self._hWnd.id, client_type=prop, data=data)
            mask = Xlib.X.SubstructureRedirectMask | Xlib.X.SubstructureNotifyMask
            ROOT.send_event(event=ev, event_mask=mask)
            DISP.flush()
            retries = 0
            while wait and retries < WAIT_ATTEMPTS and not self.isMinimized:
                retries += 1
                time.sleep(WAIT_DELAY * retries)
        return self.isMinimized

    def maximize(self, wait: bool = False) -> bool:
        """
        Maximizes this window

        :param wait: set to ''True'' to confirm action requested (in a reasonable time)
        :return: ''True'' if window maximized
        """
        if not self.isMaximized:
            EWMH.setWmState(self._hWnd, ACTION_SET, STATE_MAX_VERT, STATE_MAX_HORZ)
            EWMH.display.flush()
            retries = 0
            while wait and retries < WAIT_ATTEMPTS and not self.isMaximized:
                retries += 1
                time.sleep(WAIT_DELAY * retries)
        return self.isMaximized

    def restore(self, wait: bool = False) -> bool:
        """
        If maximized or minimized, restores the window to it's normal size

        :param wait: set to ''True'' to confirm action requested (in a reasonable time)
        :return: ''True'' if window restored
        """
        self.activate(wait=wait)
        if self.isMaximized:
            EWMH.setWmState(self._hWnd, ACTION_UNSET, STATE_MAX_VERT, STATE_MAX_HORZ)
            EWMH.display.flush()
        retries = 0
        while wait and retries < WAIT_ATTEMPTS and (self.isMaximized or self.isMinimized):
            retries += 1
            time.sleep(WAIT_DELAY * retries)
        return not self.isMaximized and not self.isMinimized

    def show(self, wait: bool = False) -> bool:
        """
        If hidden or showing, shows the window on screen and in title bar

        :param wait: set to ''True'' to wait until action is confirmed (in a reasonable time lap)
        :return: ''True'' if window showed
        """
        win = DISP.create_resource_object('window', self._hWnd)
        win.map()
        DISP.flush()
        win.map_sub_windows()
        DISP.flush()
        retries = 0
        while wait and retries < WAIT_ATTEMPTS and not self._isMapped:
            retries += 1
            time.sleep(WAIT_DELAY * retries)
        return self._isMapped

    def hide(self, wait: bool = False) -> bool:
        """
        If hidden or showing, hides the window from screen and title bar

        :param wait: set to ''True'' to wait until action is confirmed (in a reasonable time lap)
        :return: ''True'' if window hidden
        """
        win = DISP.create_resource_object('window', self._hWnd)
        win.unmap_sub_windows()
        DISP.flush()
        win.unmap()
        DISP.flush()
        retries = 0
        while wait and retries < WAIT_ATTEMPTS and self._isMapped:
            retries += 1
            time.sleep(WAIT_DELAY * retries)
        return not self._isMapped

    def activate(self, wait: bool = False) -> bool:
        """
        Activate this window and make it the foreground (focused) window

        :param wait: set to ''True'' to wait until action is confirmed (in a reasonable time lap)
        :return: ''True'' if window activated
        """
        if "arm" in platform.platform():
            EWMH.setWmState(self._hWnd, ACTION_UNSET, STATE_BELOW, STATE_NULL)
            EWMH.display.flush()
            EWMH.setWmState(self._hWnd, ACTION_SET, STATE_ABOVE, STATE_FOCUSED)
        else:
            EWMH.setActiveWindow(self._hWnd)
        EWMH.display.flush()
        retries = 0
        while wait and retries < WAIT_ATTEMPTS and not self.isActive:
            retries += 1
            time.sleep(WAIT_DELAY * retries)
        return self.isActive

    def resize(self, widthOffset: int, heightOffset: int, wait: bool = False) -> bool:
        """
        Resizes the window relative to its current size

        :param wait: set to ''True'' to wait until action is confirmed (in a reasonable time lap)
        :return: ''True'' if window resized to the given size
        """
        return self.resizeTo(self.width + widthOffset, self.height + heightOffset, wait)

    resizeRel = resize  # resizeRel is an alias for the resize() method.

    def resizeTo(self, newWidth: int, newHeight: int, wait: bool = False) -> bool:
        """
        Resizes the window to a new width and height

        :param wait: set to ''True'' to wait until action is confirmed (in a reasonable time lap)
        :return: ''True'' if window resized to the given size
        """
        EWMH.setMoveResizeWindow(self._hWnd, x=self.left, y=self.top, w=newWidth, h=newHeight)
        EWMH.display.flush()
        retries = 0
        while wait and retries < WAIT_ATTEMPTS and (self.width != newWidth or self.height != newHeight):
            retries += 1
            time.sleep(WAIT_DELAY * retries)
        return self.width == newWidth and self.height == newHeight

    def move(self, xOffset: int, yOffset: int, wait: bool = False) -> bool:
        """
        Moves the window relative to its current position

        :param wait: set to ''True'' to wait until action is confirmed (in a reasonable time lap)
        :return: ''True'' if window moved to the given position
        """
        newLeft = max(0, self.left + xOffset)  # Xlib/EWMH won't accept negative positions
        newTop = max(0, self.top + yOffset)
        return self.moveTo(newLeft, newTop, wait)

    moveRel = move  # moveRel is an alias for the move() method.

    def moveTo(self, newLeft:int, newTop: int, wait: bool = False) -> bool:
        """
        Moves the window to new coordinates on the screen

        :param wait: set to ''True'' to wait until action is confirmed (in a reasonable time lap)
        :return: ''True'' if window moved to the given position
        """
        newLeft = max(0, newLeft)  # Xlib/EWMH won't accept negative positions
        newTop = max(0, newTop)
        EWMH.setMoveResizeWindow(self._hWnd, x=newLeft, y=newTop, w=self.width, h=self.height)
        EWMH.display.flush()
        retries = 0
        while wait and retries < WAIT_ATTEMPTS and (self.left != newLeft or self.top != newTop):
            retries += 1
            time.sleep(WAIT_DELAY * retries)
        return self.left == newLeft and self.top == newTop

    def _moveResizeTo(self, newLeft: int, newTop: int, newWidth: int, newHeight: int) -> bool:
        newLeft = max(0, newLeft)  # Xlib/EWMH won't accept negative positions
        newTop = max(0, newTop)
        EWMH.setMoveResizeWindow(self._hWnd, x=newLeft, y=newTop, w=newWidth, h=newHeight)
        EWMH.display.flush()
        return newLeft == self.left and newTop == self.top and newWidth == self.width and newHeight == self.height

    def alwaysOnTop(self, aot: bool = True) -> bool:
        """
        Keeps window on top of all others.

        :param aot: set to ''False'' to deactivate always-on-top behavior
        :return: ''True'' if command succeeded
        """
        action = ACTION_SET if aot else ACTION_UNSET
        EWMH.setWmState(self._hWnd, action, STATE_ABOVE)
        EWMH.display.flush()
        return STATE_ABOVE in EWMH.getWmState(self._hWnd, str=True)

    def alwaysOnBottom(self, aob: bool = True) -> bool:
        """
        Keeps window below of all others, but on top of desktop icons and keeping all window properties

        :param aob: set to ''False'' to deactivate always-on-bottom behavior
        :return: ''True'' if command succeeded
        """
        action = ACTION_SET if aob else ACTION_UNSET
        EWMH.setWmState(self._hWnd, action, STATE_BELOW)
        EWMH.display.flush()
        return STATE_BELOW in EWMH.getWmState(self._hWnd, str=True)

    def lowerWindow(self) -> bool:
        """
        Lowers the window to the bottom so that it does not obscure any sibling windows

        :return: ''True'' if window lowered
        """
        w = DISP.create_resource_object('window', self._hWnd)
        w.configure(stack_mode=Xlib.X.Below)
        DISP.flush()
        windows = EWMH.getClientListStacking()
        return windows and self._hWnd == windows[-1]

    def raiseWindow(self) -> bool:
        """
        Raises the window to top so that it is not obscured by any sibling windows.

        :return: ''True'' if window raised
        """
        w = DISP.create_resource_object('window', self._hWnd)
        w.configure(stack_mode=Xlib.X.Above)
        DISP.flush()
        windows = EWMH.getClientListStacking()
        return windows and self._hWnd == windows[0]

    def sendBehind(self, sb: bool = True) -> bool:
        """
        Sends the window to the very bottom, below all other windows, including desktop icons.
        It may also cause that the window does not accept focus nor keyboard/mouse events as well as
        make the window disappear from taskbar and/or pager.

        :param sb: set to ''False'' to bring the window back to front
        :return: ''True'' if window sent behind desktop icons

        Notes:
            - On GNOME it will obscure desktop icons... by the moment
        """
        if sb:
            # https://stackoverflow.com/questions/58885803/can-i-use-net-wm-window-type-dock-ewhm-extension-in-openbox
            w = DISP.create_resource_object('window', self._hWnd)
            # Place a Window behind desktop icons using PyQt on Ubuntu/GNOME
            # This adds the properties (notice the PropMode options), but with no effect on GNOME
            w.change_property(DISP.intern_atom(WM_STATE, False), Xlib.Xatom.ATOM,
                              32, [DISP.intern_atom(STATE_BELOW, False), ],
                              Xlib.X.PropModeReplace)
            w.change_property(DISP.intern_atom(WM_STATE, False), Xlib.Xatom.ATOM,
                              32, [DISP.intern_atom(STATE_SKIP_TASKBAR, False), ],
                              Xlib.X.PropModeAppend)
            w.change_property(DISP.intern_atom(WM_STATE, False), Xlib.Xatom.ATOM,
                              32, [DISP.intern_atom(STATE_SKIP_PAGER, False), ],
                              Xlib.X.PropModeAppend)
            DISP.flush()

            # This sends window below all others, but not behind the desktop icons
            w.change_property(DISP.intern_atom(WM_WINDOW_TYPE, False), Xlib.Xatom.ATOM,
                              32, [DISP.intern_atom(WINDOW_DESKTOP, False), ],
                              Xlib.X.PropModeReplace)
            DISP.flush()

            if "GNOME" in os.environ.get('XDG_CURRENT_DESKTOP', ''):
                pass
                # This sends the window "too far behind" (below all others, including Wallpaper, like unmapped)
                # Trying to figure out how to raise it on top of wallpaper but behind desktop icons
                # TODO: As an idea, find Wallpaper window to try to reparent our window to it, or to its same parent
                # desktop = _xlibGetAllWindows(title="gnome-shell")  # or "main", not sure...
                # if desktop:
                #     w.reparent(desktop[-1], self.left, self.top)
                #     DISP.flush()

            else:
                # Mint/Cinnamon: just clicking on the desktop, it raises, sending the window/wallpaper to the bottom!
                # TODO: Find a smarter way to raise desktop icons instead of a mouse click
                m = mouse.Controller()
                m.move(SCREEN.width_in_pixels - 1, 100)
                m.click(mouse.Button.left, 1)
            return WINDOW_DESKTOP in EWMH.getWmWindowType(self._hWnd, str=True)
        else:
            w = DISP.create_resource_object('window', self._hWnd)
            w.unmap()
            w.change_property(DISP.intern_atom(WM_WINDOW_TYPE, False), Xlib.Xatom.ATOM,
                              32, [DISP.intern_atom(WINDOW_NORMAL, False), ],
                              Xlib.X.PropModeReplace)
            DISP.flush()
            w.change_property(DISP.intern_atom(WM_STATE, False), Xlib.Xatom.ATOM,
                              32, [DISP.intern_atom(STATE_FOCUSED, False), ],
                              Xlib.X.PropModeReplace)
            DISP.flush()
            w.map()
            EWMH.setActiveWindow(self._hWnd)
            EWMH.display.flush()
            return WINDOW_NORMAL in EWMH.getWmWindowType(self._hWnd, str=True) and self.isActive

    def getAppName(self) -> str:
        """
        Get the name of the app current window belongs to

        :return: name of the app as string
        """
        # https://stackoverflow.com/questions/32295395/how-to-get-the-process-name-by-pid-in-linux-using-python
        pid = EWMH.getWmPid(self._hWnd)
        with subprocess.Popen(f"ps -q {pid} -o comm=", shell=True, stdout=subprocess.PIPE) as p:
            ret = p.communicate()
        if len(ret) > 0:
            ret = ret[0].decode(encoding="utf8").replace("\n", "")
        return ret

    def getParent(self) -> Union[Cursor, Drawable, Pixmap, Resource, Fontable, Window, GC, Colormap, Font]:
        """
        Get the handle of the current window parent. It can be another window or an application

        :return: handle of the window parent
        """
        return self._hWnd.query_tree().parent

    def getChildren(self) -> List[int]:
        """
        Get the children handles of current window

        :return: list of handles
        """
        w = DISP.create_resource_object('window', self._hWnd)
        return w.query_tree().children

    def getHandle(self) -> Union[Cursor, Drawable, Pixmap, Resource, Fontable, Window, GC, Colormap, Font]:
        """
        Get the current window handle

        :return: window handle
        """
        return self._hWnd

    def isParent(self, child: Union[Cursor, Drawable, Pixmap, Resource, Fontable, Window, GC, Colormap, Font]) -> bool:
        """Returns ''True'' if the window is parent of the given window as input argument

        Args:
        ----
            ''child'' handle of the window you want to check if the current window is parent of
        """
        return child.query_tree().parent == self._hWnd
    isParentOf = isParent  # isParentOf is an alias of isParent method

    def isChild(self, parent: Union[Cursor, Drawable, Pixmap, Resource, Fontable, Window, GC, Colormap, Font]) -> bool:
        """
        Check if current window is child of given window/app (handle)

        :param parent: handle of the window/app you want to check if the current window is child of
        :return: ''True'' if current window is child of the given window
        """
        return parent == self.getParent()
    isChildOf = isChild  # isParentOf is an alias of isParent method

    def getDisplay(self):
        """
        Get display name in which current window space is mostly visible

        :return: display name as string
        """
        screens = getAllScreens()
        name = ""
        for key in screens.keys():
            if pointInRect(self.centerx, self.centery, screens[key]["pos"].x, screens[key]["pos"].y, screens[key]["size"].width, screens[key]["size"].height):
                name = key
                break
        return name

    @property
    def isMinimized(self) -> bool:
        """
        Check if current window is currently minimized

        :return: ``True`` if the window is minimized
        """
        state = EWMH.getWmState(self._hWnd, str=True)
        return STATE_HIDDEN in state

    @property
    def isMaximized(self) -> bool:
        """
        Check if current window is currently maximized

        :return: ``True`` if the window is maximized
        """
        state = EWMH.getWmState(self._hWnd, str=True)
        return STATE_MAX_VERT in state and STATE_MAX_HORZ in state

    @property
    def isActive(self) -> bool:
        """
        Check if current window is currently the active, foreground window

        :return: ``True`` if the window is the active, foreground window
        """
        win = EWMH.getActiveWindow()
        return win == self._hWnd

    @property
    def title(self) -> str:
        """
        Get the current window title, as string

        :return: title as a string
        """
        name = EWMH.getWmName(self._hWnd)
        if isinstance(name, bytes):
            name = name.decode()
        return name

    @property
    def visible(self) -> bool:
        """
        Check if current window is visible (minimized windows are also visible)

        :return: ``True`` if the window is currently visible
        """
        win = DISP.create_resource_object('window', self._hWnd)
        state = win.get_attributes().map_state
        return state == Xlib.X.IsViewable

    isVisible = visible  # isVisible is an alias for the visible property.

    @property
    def isAlive(self) -> bool:
        """
        Check if window (and application) still exists (minimized and hidden windows are included as existing)

        :return: ''True'' if window exists
        """
        ret = True
        try:
            win = DISP.create_resource_object('window', self._hWnd)
            state = win.get_attributes().map_state
        except Xlib.error.BadWindow:
            ret = False
        return ret

    @property
    def _isMapped(self) -> bool:
        # Returns ``True`` if the window is currently mapped
        win = DISP.create_resource_object('window', self._hWnd)
        state = win.get_attributes().map_state
        return state != Xlib.X.IsUnmapped


def getAllScreens():
    """
    load all monitors plugged to the pc, as a dict

    :return: Monitors info as python dictionary

    Output Format:
        Key:
            Display name

        Values:
            "id":
                display sequence_number as identified by Xlib.Display()
            "is_primary":
                ''True'' if monitor is primary (shows clock and notification area, sign in, lock, CTRL+ALT+DELETE screens...)
            "pos":
                Point(x, y) struct containing the display position ((0, 0) for the primary screen)
            "size":
                Size(width, height) struct containing the display size, in pixels
            "workarea":
                Rect(left, top, right, bottom) struct with the screen workarea, in pixels
            "scale":
                Scale ratio, as a percentage
            "dpi":
                Dots per inch, as a tuple of (x, y) dpi values
            "orientation":
                Display orientation: 0 - Landscape / 1 - Portrait / 2 - Landscape (reversed) / 3 - Portrait (reversed) / 4 - Reflect X / 5 - Reflect Y
            "frequency":
                Refresh rate of the display, in Hz
            "colordepth":
                Bits per pixel referred to the display color depth
    """
    # https://stackoverflow.com/questions/8705814/get-display-count-and-resolution-for-each-display-in-python-without-xrandr
    # https://www.x.org/releases/X11R7.7/doc/libX11/libX11/libX11.html#Obtaining_Information_about_the_Display_Image_Formats_or_Screens
    result = {}
    res = ROOT.xrandr_get_screen_resources()
    modes = res.modes
    for output in res.outputs:
        try:
            params = DISP.xrandr_get_output_info(output, res.config_timestamp)
            crtc = DISP.xrandr_get_crtc_info(params.crtc, res.config_timestamp)
        except:
            continue
        # Check if this all also applies to physical monitors and check differences
        wa = EWMH.getWorkArea()
        mode = None
        for item in modes:
            if crtc and crtc.mode and crtc.mode == item.id:
                mode = item
                break
        if not params or not crtc or not mode:
            continue
        result[params.name] = {
            'id': crtc.sequence_number,
            'is_primary': (crtc.x, crtc.y) == (0, 0),
            'pos': Point(crtc.x, crtc.y),
            'size': Size(crtc.width, crtc.height),
            'workarea': Rect(crtc.x + wa[0], crtc.y + wa[1], crtc.x + crtc.width - (SCREEN.width_in_pixels - wa[2] - wa[0]), crtc.y + crtc.height - (SCREEN.height_in_pixels - wa[3] - wa[1])),
            'scale': -1,  # check with physical monitors using dpi, mms or other possible values or props
            'dpi': (round(SCREEN.width_in_pixels * 25.4 / SCREEN.width_in_mms), round(SCREEN.height_in_pixels * 25.4 / SCREEN.height_in_mms)),
            # 'dpi': (round(crtc.width * 25.4 / SCREEN.width_in_mms), round(crtc.height * 25.4 / SCREEN.height_in_mms)),
            # 'dpi': (round(crtc.width * 25.4 / params.mm_width), round(crtc.height * 25.4 / params.mm_height)),
            'orientation': int(math.log(crtc.rotation, 2)),  # 4 - Reflect X / 5 - Reflect Y,
            'frequency': mode.dot_clock / (mode.h_total * mode.v_total),
            'colordepth': SCREEN.root_depth
        }
        # props = DISP.xrandr_list_output_properties(output)
        # for atom in props.atoms:
        #     print(atom, DISP.get_atom_name(atom))
        #     print(DISP.xrandr_get_output_property(output, atom, 0, 0, 1000)._data['value'])
    return result


def getMousePos() -> Point:
    """
    Get the current (x, y) coordinates of the mouse pointer on screen, in pixels

    :return: Point struct
    """
    mp = ROOT.query_pointer()
    return Point(mp.root_x, mp.root_y)
cursor = getMousePos  # cursor is an alias for getMousePos


def getScreenSize(name: str = "") -> Size:
    """
    Get the width and height, in pixels, of the given screen, or main screen if no screen given or not found

    :param name: name of screen as returned by getAllScreens() and getDisplay()
    :return: Size struct or None
    """
    screens = getAllScreens()
    res = None
    for key in screens.keys():
        if (name and key == name) or (not name):
            res = screens[key]["size"]
            break
    return res
resolution = getScreenSize  # resolution is an alias for getScreenSize


def getWorkArea(name: str = "") -> Rect:
    """
    Get the Rect struct (left, top, right, bottom) of the working (usable by windows) area of the screen, in pixels

    :param name: name of screen as returned by getAllScreens() and getDisplay()
    :return: Rect struct or None
    """
    screens = getAllScreens()
    res = None
    for key in screens.keys():
        if (name and key == name) or (not name):
            res = screens[key]["workarea"]
            break
    return res


def displayWindowsUnderMouse(xOffset: int = 0, yOffset: int = 0) -> None:
    """
    This function is meant to be run from the command line. It will
    automatically display the position of mouse pointer and the titles
    of the windows under it
    """
    if xOffset != 0 or yOffset != 0:
        print('xOffset: %s yOffset: %s' % (xOffset, yOffset))
    try:
        prevWindows = None
        while True:
            x, y = getMousePos()
            positionStr = 'X: ' + str(x - xOffset).rjust(4) + ' Y: ' + str(y - yOffset).rjust(4) + '  (Press Ctrl-C to quit)'
            windows = getWindowsAt(x, y)
            if windows != prevWindows:
                print('\n')
                prevWindows = windows
                for win in windows:
                    name = win.title
                    eraser = '' if len(name) >= len(positionStr) else ' ' * (len(positionStr) - len(name))
                    sys.stdout.write(name + eraser + '\n')
            sys.stdout.write(positionStr)
            sys.stdout.write('\b' * len(positionStr))
            sys.stdout.flush()
            time.sleep(0.3)
    except KeyboardInterrupt:
        sys.stdout.write('\n\n')
        sys.stdout.flush()


def main():
    """Run this script from command-line to get windows under mouse pointer"""
    print("SCREEN SIZE:", resolution())
    print("ALL WINDOWS", getAllTitles())
    npw = getActiveWindow()
    print("ACTIVE WINDOW:", npw.title, "/", npw.box)
    print()
    displayWindowsUnderMouse(0, 0)


if __name__ == "__main__":
    main()

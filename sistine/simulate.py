from Quartz.CoreGraphics import (
    CGEventCreateMouseEvent,
    CGEventPost,
    kCGEventLeftMouseDown,
    kCGEventLeftMouseUp,
    kCGEventMouseMoved,
    kCGHIDEventTap,
    kCGMouseButtonLeft,
)


def mouse_event(type, posx, posy):
    theEvent = CGEventCreateMouseEvent(None, type, (posx, posy), kCGMouseButtonLeft)
    CGEventPost(kCGHIDEventTap, theEvent)


def mousemove(posx, posy):
    mouse_event(kCGEventMouseMoved, posx, posy)


def mousedown(posx, posy):
    mouse_event(kCGEventLeftMouseDown, posx, posy)


def mouseup(posx, posy):
    mouse_event(kCGEventLeftMouseUp, posx, posy)

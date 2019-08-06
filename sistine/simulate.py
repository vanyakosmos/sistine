from Quartz.CoreGraphics import (
    CGEventCreateMouseEvent,
    CGEventPost,
    kCGEventLeftMouseDown,
    kCGEventLeftMouseUp,
    kCGEventMouseMoved,
    kCGHIDEventTap,
    kCGMouseButtonLeft,
)


def mouseEvent(type, posx, posy):
    theEvent = CGEventCreateMouseEvent(None, type, (posx, posy), kCGMouseButtonLeft)
    CGEventPost(kCGHIDEventTap, theEvent)


def mousemove(posx, posy):
    mouseEvent(kCGEventMouseMoved, posx, posy)


def mousedown(posx, posy):
    mouseEvent(kCGEventLeftMouseDown, posx, posy)


def mouseup(posx, posy):
    mouseEvent(kCGEventLeftMouseUp, posx, posy)

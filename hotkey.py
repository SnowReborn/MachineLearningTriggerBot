
import win32api
import win32con
import time
import winsound
import win32gui

while True:
    global Lmouse
    #x , y = win32gui.GetCursorPos()
    #print(str(x) + " " + str(y))
    
    TAB = win32api.GetAsyncKeyState((win32con.VK_TAB))           
    R = win32api.GetAsyncKeyState(ord("R"))
    F6 = win32api.GetAsyncKeyState((win32con.VK_F6))                  
    F5 = win32api.GetAsyncKeyState((win32con.VK_F5))
    F7 = win32api.GetAsyncKeyState((win32con.VK_F7))
    one = win32api.GetAsyncKeyState(ord("1"))
    two = win32api.GetAsyncKeyState(ord("2"))
    five = win32api.GetAsyncKeyState(ord("5"))
    num0 = win32api.GetAsyncKeyState((win32con.VK_NUMPAD0))
    num1 = win32api.GetAsyncKeyState((win32con.VK_NUMPAD1))
    num2 = win32api.GetAsyncKeyState((win32con.VK_NUMPAD2))
    num3 = win32api.GetAsyncKeyState((win32con.VK_NUMPAD3))
    num4 = win32api.GetAsyncKeyState((win32con.VK_NUMPAD4))
    num5 = win32api.GetAsyncKeyState((win32con.VK_NUMPAD5))
    num6 = win32api.GetAsyncKeyState((win32con.VK_NUMPAD6))
    plus = win32api.GetAsyncKeyState((win32con.VK_ADD))
    minus = win32api.GetAsyncKeyState((win32con.VK_SUBTRACT))
    M = win32api.GetAsyncKeyState(ord("M"))
    Sidemouse = win32api.GetAsyncKeyState((win32con.VK_XBUTTON2))

    
    Lmouse = win32api.GetAsyncKeyState((win32con.VK_LBUTTON))
    Rightmouse = win32api.GetAsyncKeyState((win32con.VK_RBUTTON))
    print(Lmouse == False)
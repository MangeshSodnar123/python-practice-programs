import pyautogui
x = 400
while x > 0:
    print(x,0)
    pyautogui.dragRel(x,0)
    x -= 20
    print(0,x)
    pyautogui.dragRel(0,x)
    x -= 20
    print(-x,0)
    pyautogui.dragRel(-x,0)
    x -= 20
    print(0,x)
    pyautogui.dragRel(0,-x)
    x -= 20
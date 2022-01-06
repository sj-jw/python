import pyautogui

#마우스 이동

# pyautogui.moveTo(100, 100) # 지정한 위치로 마우스 이동

# pyautogui.moveTo(100, 200, duration=0.1) #0.1초 동안 이동 



# pyautogui.moveTo(100,100)
# pyautogui.moveTo(200,200)
# pyautogui.moveTo(300,300)

# print(pyautogui.position()) #값 참고하기
p = pyautogui.position() #값 출력
print(p[0], p[1])
print(p.x, p.y)


# pyautogui.move() #상대좌표로 이동(현재 커서의 위치로부터 이동)



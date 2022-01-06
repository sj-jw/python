import pyautogui

# file_menu = pyautogui.locateOnScreen("file_menu.png") #화면내에서 이 이미지를 찾아라

# print(file_menu) #좌표 
# # pyautogui.click(file_menu) #클릭

# trash_icon = pyautogui.locateOnScreen("trash_icon.png")
# print(trash_icon)
# # pyautogui.moveTo(trash_icon)
# pyautogui.click(trash_icon)

#체크박스가 여러개일떄 ㅇㅇ다 체크 첫번째부터 
# for i in pyautogui.locateAllOnScreen("checkbox.png"):
#     print(i)
#     pyautogui.click(i)

# checkbox = pyautogui.locateOnScreen("checkbox.png")
# pyautogui.click(checkbox)


#속도개선 GrayScale
# trash_icon = pyautogui.locateOnScreen("trash_icon.png", grayscale=True)
# pyautogui.moveTo(trash_icon)

#범위지정
# trash_icon = pyautogui.locateOnScreen("trash_icon.png", region=(15, 1023, 952-15, 1079-1023))
# pyautogui.click(trash_icon)

# pyautogui.mouseInfo()
# 15,1023   952,1079


#정확도 조정
run_btn = pyautogui.locateOnScreen("run_btn.png", confidence = 0.9) #90퍼센트이상일시 똑같이봄
pyautogui.click(run_btn)




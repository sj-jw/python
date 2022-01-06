import pyautogui
# 스크린샷 찍기
# img = pyautogui.screenshot()
# img.save("screenshot.png")

# pyautogui.mouseInfo()

# pyautogui.pixelMatchesColor(28, 18 (34,167,242)) / 픽셀값이 같은지 확인

# 23,11 99,172,245 #63ACF5

pixel = pyautogui.pixel(23, 11)
print(pixel)

# print(pyautogui.pixelMatchesColor(23, 11, pixel))
# print(pyautogui.pixelMatchesColor(23, 11, (99,172,245))) /픽셀값이 같은지?



from PIL import ImageGrab
import pyautogui


def isCollision(data):
    for i in range(760, 825):
        for j in range(290, 330):
            if data[i, j] < 100:
                pyautogui.keyDown("up")
                return
    return


while True:
    image = ImageGrab.grab().convert("L")
    data = image.load()
    isCollision(data)

# image.show()
# break

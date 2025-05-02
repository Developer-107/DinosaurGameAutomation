from PIL import Image, ImageGrab
import time
import pyautogui
from selenium.webdriver.chrome.options import Options
from selenium import webdriver

# Opening window with game on elgoog.im
options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.get('https://elgoog.im/dinosaur-game/')


# Defining
def click(key):
    pyautogui.keyDown(key)
    return

# Checking collision and acting
def isCollision(data):
    # Check collision for birds
    for i in range(530, 610):
        for j in range(770, 825):
            if data[i, j] < 170:
                click("down")
                return
    # Check collision for cactus
    for i in range(530, 560):
        for j in range(720, 750):
            if data[i, j] < 100:
                click("up")
                return
    return

if __name__ == "__main__":
    time.sleep(5)
    click('up')

    while True:
        image = ImageGrab.grab().convert('L')
        data = image.load()
        isCollision(data)

        # # Draw the rectangle for cactus
        # for i in range(530, 610):
        #     for j in range(770, 825):
        #          data[i, j] = 0
        #
        # # # Draw the rectangle for birds
        # for i in range(530, 560):
        #     for j in range(720, 750):
        #         data[i, j] = 171

        # image.show()
        break
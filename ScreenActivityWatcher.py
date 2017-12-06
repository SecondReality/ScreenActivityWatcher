from pushbullet import Pushbullet
from PIL import ImageGrab
import numpy as np
import time
from datetime import datetime

pushBulletApiKey = "PUSH BULLET API KEY"
notificationTitle = "NOTIFICATION TITLE"

def getScreenNorm():
    image = ImageGrab.grab()
    image_data = np.asarray(image) / 255
    norm = image_data / np.sqrt(np.sum(image_data ** 2))
    return norm

cycles = 0

while True:
    image1 = getScreenNorm()
    time.sleep(30)
    image2 = getScreenNorm()
    difference = np.sum(image1*image2)
    if difference > 0.999 and cycles > 10:
        cycles = 0
        pb = Pushbullet(pushBulletApiKey)
        push = pb.push_note(notificationTitle, "No motion detected at "+str(datetime.now()))
    time.sleep(30)
    cycles = cycles+1



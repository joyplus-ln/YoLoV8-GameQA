import datetime
import os
from datetime import time

from adbutils import adb, AdbDevice
from PIL import Image

class AndroidDevice:
    def __init__(self,device:AdbDevice):
        self.device = device

    #截图
    def TakeShot(self)-> Image.Image:
        image = self.device.screenshot()
        return image

    def TakeShotAutoSave(self):
        image = self.device.screenshot()
        timeName = formatted_time = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        path = f'd:/{self.device.get_serialno()}'
        if not os.path.exists(path):
            os.makedirs(path)

        image.save(f'{path}/{timeName}.png')
    #点击屏幕
    def Click_Screen(self, x, y) :
        self.device.shell(f'input tap {x} {y}')
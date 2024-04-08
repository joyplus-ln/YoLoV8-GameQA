import threading

import adbutils

import ADBControl
from AndroidDevice import AndroidDevice
from ultralytics import YOLO

#每隔一段时间给当前连接的所有设备截图一张
def screenshot():
    for device in devicelist:
        device.TakeShotAutoSave()

def setTimer():
    screenshot()
    threading.Timer(0.5,setTimer).start()

if __name__ == "__main__":
    devices = adbutils.adb.device_list()
    devicelist = []
    if devices:
        for device in devices:
            devicelist.append(AndroidDevice(device))
    setTimer()





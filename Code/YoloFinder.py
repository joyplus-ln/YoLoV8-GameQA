import asyncio

from PIL.Image import Image

from Code import ADBControl
from Code.Init import tableManager
from GenCode.schema import ActionConfig
from ultralytics import YOLO
from adbutils import adb, AdbDevice

class YoloFinder:
    def __init__(self):
        self.model = YOLO("../runs/detect/train7/weights/best.pt")


    #检测逻辑
    def predict(self,image:Image,_classes,_conf) -> list:
        results = self.model.predict(image, save=False, vid_stride=100, conf=_conf, max_det=100,
                                     classes=_classes)
        return results


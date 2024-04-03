import ADBControl
from ultralytics import YOLO

if __name__ == "__main__":
    # Load a model
    model = YOLO("yolov8s.yaml")  # build a new model from scratch
    # model = YOLO("weight/yolov8s.pt")  # load a pretrained model (recommended for training)
    model = YOLO("runs/detect/train/weights/best.pt")

    # source = 'weight/斗地主4.mp4'
    # Use the model
    # model.train(data="datasets/epgame/epgame.yaml", epochs=3)  # train the model
    # metrics = model.val()  # evaluate model performance on the validation set
    # results = model.predict(source,save=True,vid_stride=100)  # predict on an image
    # path = model.export(format="onnx")  # export the model to ONNX format

    #通过截图安卓屏幕来预测
    # image = ADBControl.Get_ScreenShot()
    # results = model.predict(image,save=True,vid_stride=100,conf=0.7,max_det=20)

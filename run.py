import ADBControl
from ultralytics import YOLO

if __name__ == "__main__":


    # #训练模型
    # model = YOLO("yolov8s.yaml")  # build a new model from scratch
    # model = YOLO("weight/yolov8s.pt")  # load a pretrained model (recommended for training)
    # model.train(data="datasets/epgame/epgame.yaml", epochs=100)  # train the model
    # metrics = model.val()  # evaluate model performance on the validation


    # Load a model
    # model = YOLO("yolov8s.yaml")  # build a new model from scratch
    # # model = YOLO("weight/yolov8s.pt")  # load a pretrained model (recommended for training)


    # source = 'weight/斗地主4.mp4'
    # Use the model
    # model.train(data="datasets/epgame/epgame.yaml", epochs=3)  # train the model
    # metrics = model.val()  # evaluate model performance on the validation set
    # results = model.predict(source,save=True,vid_stride=100)  # predict on an image
    # path = model.export(format="onnx")  # export the model to ONNX format

    #通过截图安卓屏幕来预测
    model = YOLO("runs/detect/train7/weights/best.pt")
    device,image = ADBControl.Get_ScreenShot()
    results = model.predict(image,save=True,vid_stride=100,conf=0.6,max_det=100)
    for result in results:
        infos = result.summary()
        for info in infos:
            print(info)
            centx = (info["box"].get("x1") + info["box"].get("x2")) / 2
            centy = (info["box"].get("y1") + info["box"].get("y2")) / 2
            print("==>",info.get("name"),centx,centy)
            ADBControl.Click_Screen(device,centx,centy)
        # result.show()
        # for box in result.boxes:
        #     print(box.cls)
        # print(result.tojson())

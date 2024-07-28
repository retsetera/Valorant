import math
import torch
from ultralytics import YOLO
from roboflow import Roboflow
def train_model(_model:str ='yolov8n.pt', epochs=100, time=None, patience=None, batch=16, imgsz=3840, save=True, device=(0,1), project='model', rect=False, plots=True):
    model = YOLO(_model)

    #get dataset
    rf = Roboflow(api_key="XvY02AW0H3jRkUWWRYhJ")
    project = rf.workspace("david-hong").project("valorant-enemy")
    version = project.version(2)
    dataset = version.download("yolov8")

    #train
    results = model.train(data=dataset, epochs=epochs, time=time, patience=patience, batch=batch, imgsz=imgsz, save=save, device=device, project=project, rect=rect, plots=plots)

train_model()
print()
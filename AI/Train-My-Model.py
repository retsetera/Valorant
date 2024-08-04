import math
from ultralytics import YOLO
from roboflow import Roboflow



def train_model(_model:str ='yolov8n.pt', epochs=100, _time=None, patience=None, batch=16, imgsz=3840, save=True, device=(0,1), project='model', rect=False, plots=True):
    model = YOLO(_model)

    #get dataset
    rf = Roboflow(api_key="XvY02AW0H3jRkUWWRYhJ")
    _project = rf.workspace("david-hong").project("valorant-enemy")
    version = _project.version(2)
    dataset = version.download("yolov8")
    #train
    results = model.train(data=dataset.location+'\\data.yaml', epochs=epochs, patience=patience, batch=batch, imgsz=imgsz, save=save, device=device, project=project, rect=rect, plots=plots)

train_model(device='cpu')
print()
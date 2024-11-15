import torch

# Load the YOLO model (this will download it if it's not already cached)
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

# Get the path of the loaded model's state_dict
print(model.state_dict())

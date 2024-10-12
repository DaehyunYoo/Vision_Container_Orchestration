# Pytorch model 
# Segmentation

import torch
import torchvision.transforms as T
from torchvision.models.segmentation import deeplabv3_resnet50

def load_model():
    model = deeplabv3_resnet50(pretrained=True)
    model.eval()
    return model

def predict(model, image):
    transform = T.Compose([
        T.ToTensor(),
        T.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ])
    input_tensor = transform(image).unsqueeze(0)
    
    with torch.no_grad():
        output = model(input_tensor)['out'][0]
    
    return output.argmax(0).byte().cpu().numpy()
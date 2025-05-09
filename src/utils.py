import io
import os
import base64
import torch
import torchvision.transforms as transforms
from PIL import Image
from model import ConvNet, types_inverse

mean = torch.tensor([0.7993, 0.7868, 0.7648])
std = torch.tensor([0.2696, 0.2697, 0.2848])

def transform_image(img_b64):

    transform = transforms.Compose([
        transforms.Resize((256, 256)),
        transforms.ToTensor(),
        transforms.Normalize(mean, std)
    ])

    img_bytes = base64.b64decode(img_b64)
    image = Image.open(io.BytesIO(img_bytes))
    return transform(image).unsqueeze(0)


def get_model():
    cwd = os.getcwd()
    root = os.path.dirname(cwd)
    notebooks = os.path.join(root, "notebooks")
    model = os.path.join(notebooks, "type_classifier_net.pth")

    return model

def get_type(tensor):
    return [types_inverse[i.item()] for i in tensor.nonzero(as_tuple=False)[:,1]]

net = ConvNet()
net.load_state_dict(torch.load(get_model(), weights_only=True, map_location="cpu"))
net.eval()

def get_prediction(img_b64):
    out = net(transform_image(img_b64))
    out = torch.sigmoid(out)

    pred = torch.zeros(18)

    if (out > 0.5).sum().item() > 2:
        _, indicies = torch.topk(out, 2)
        
        pred[indicies[0]] = 1
        pred[indicies[1]] = 1
            
    elif (out > 0.5).sum().item() <= 0:
        _, indicies = torch.topk(out, 1)
        pred[indicies[0]] = 1
    else:
        pred = torch.where(out > 0.5, 1, 0)

    return get_type(pred)
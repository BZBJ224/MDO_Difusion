from torchvision.transforms import transforms
from PIL import Image
import os, torch

def labeldata(path):
    ts = transforms.Compose([transforms.ToTensor()])

    label = os.listdir(path)
    images, texts = [], []
    for i in label:
        path_1 = path+'/'+i
        for j in os.listdir(path_1):
            images.append(ts(Image.open(os.path.join(path_1,j))))
            texts.append(i)

    images = torch.stack(images[:],0)
    
    if torch.cuda.is_available(): images=images.cuda()

    return images, texts

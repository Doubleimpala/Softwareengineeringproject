from min_dalle import MinDalle
import torch
from PIL import Image

model = MinDalle(
    models_root='./pretrained',
    dtype=torch.float32,
    device='cpu',
    is_mega=True,
    is_reusable=True
)
def generateImage(proompt):
    image = model.generate_image(
        text=proompt,
        seed=-1,
        grid_size=4,
        is_seamless=False,
        temperature=1,
        top_k=256,
        supercondition_factor=32,
        is_verbose=False
        )
    return image

def test(proompt):
    image = Image.open('fish.png')
    
    return image

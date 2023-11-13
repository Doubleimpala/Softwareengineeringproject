from IPython import display
from min_dalle import MinDalle
import torch

model = MinDalle(
    models_root='./pretrained',
    dtype=torch.float32,
    device='cuda',
    is_mega=True,
    is_reusable=True
)


def generate():

    image = model.generate_image(
        text='Nuclear explosion broccoli',
        seed=-1,
        grid_size=4,
        is_seamless=False,
        temperature=1,
        top_k=256,
        supercondition_factor=32,
        is_verbose=False
        )

    display(image)

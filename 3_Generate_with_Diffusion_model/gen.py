from imagen_pytorch import Unet, Imagen, ImagenTrainer
from torchvision.utils import save_image

# unets for unconditional imagen

unet = Unet(
    dim = 32,
    cond_dim = 512, 
    dim_mults = (1, 2, 4, 8),
    num_resnet_blocks = (2, 4, 8, 8),
    layer_attns = (False, False, False, True),
    layer_cross_attns = (False, False, False, True)
)


# imagen, which contains the unet above

imagen = Imagen(
    unets = unet, 
    image_sizes = 128,
    timesteps = 1000,
    cond_drop_prob = 0.1
)

trainer = ImagenTrainer(imagen).cuda()

# load model
trainer.load('./diff.pt')

# working sample loop

A,B,C,D = ['A' for i in range(32)],['B' for i in range(32)],\
                 ['C' for i in range(32)],['D' for i in range(32)]

label  = {'A':A,'B':B,'C':C,'D':D}

for i in range(25):
    for j, jj in label.items():
        images = trainer.sample(texts=jj,cond_scale=3.,return_pil_images = True)
        for k in range(len(images)):
            images[k].save(f'./gen/{j}/sample-{i}-{k}.png')

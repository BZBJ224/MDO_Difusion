import torch
from imagen_pytorch import Unet, Imagen, NullUnet, ImagenTrainer
from torchvision.utils import save_image
from src.labeldata import labeldata
# unet for imagen

unet = Unet(
    dim = 32,
    cond_dim = 512,
    dim_mults = (1, 2, 4, 8),
    num_resnet_blocks = (2, 4, 8, 8),
    layer_attns = (False, False, False, True),
    layer_cross_attns = (False, False, False, True)
)

# imagen, which contains the unets above (base unet and super resoluting ones)

imagen = Imagen(
    unets = unet,
    image_sizes = 128,
    timesteps = 1000,
    cond_drop_prob = 0.1
).cuda()

# wrap imagen with the trainer class

trainer = ImagenTrainer(imagen)

# mock images (get a lot of this) and text encodings from large T5

img, texts = labeldata('./png')

# feed images into imagen, training each unet in the cascade
low = 1000
loss = 1000
for i in range(200000):
    if loss < low:
        low = loss
        trainer.save('./diff.pt')
    loss = trainer(img,texts=texts,max_batch_size=16)
    trainer.update()
    print(f'loss: {loss}')

    if not (i % 500) and trainer.is_main: # is_main makes sure this can run in distributed
        images = trainer.sample(texts=['A','A','A','A','B','B','B','B',\
                                       'C','C','C','C','D','D','D','D'],cond_scale=3.) # returns List[Image]
        save_image(images[:].view(-1,3,128,128), "images/%d.png" % (i // 100), nrow=4, normalize=True)
   

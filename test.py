import argparse
import jittor as jt
import numpy as np

from PIL import Image
from CGAN import Generator

parser = argparse.ArgumentParser()
parser.add_argument('--number', type=str, required=True, help='Numbers wanted to be generated.')
args = parser.parse_args()

generator = Generator()
generator.eval()
generator.load('generator_last.pkl')

latent_dim = 100
number = args.number
n_row = len(number)
z = jt.array(np.random.normal(0, 1, (n_row, latent_dim))).float32().stop_grad()
labels = jt.array(np.array([int(number[num]) for num in range(n_row)])).float32().stop_grad()
gen_imgs = generator(z,labels)

img_array = gen_imgs.data.transpose((1,2,0,3))[0].reshape((gen_imgs.shape[2], -1))
min_=img_array.min()
max_=img_array.max()
img_array=(img_array-min_)/(max_-min_)*255
Image.fromarray(np.uint8(img_array)).save("result.png")
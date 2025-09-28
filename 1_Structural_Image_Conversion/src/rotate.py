from PIL import Image
import numpy as np

def rotate(img):
	k=1
	j=0
	# print(np.array(img)[:7,:7])
	while k:
		# print(np.mean(np.array(img)[:7,:7])/255)
		if np.mean(np.array(img)[:7,:7])/255 <= 0.1: #and \
		   # np.mean(np.array(img)[7:,7:])/255 >= 0.1:
			k = 0
		else:
			img = np.fliplr(img)
			j += 1
		if j == 5:
			k = 0
	return np.array(img)


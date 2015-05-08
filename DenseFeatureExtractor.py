from vlfeat import vl_dsift, vl_imsmooth, vl_rgb2gray
from cv2 import imread, resize, equalizeHist
from numpy import transpose

class DenseFeatureExtractor:

	def __init__(self, image, memory):
		self.image = image
		self.memory = memory

	def extract_feature_vector(self):
		img = imread(self.image.get_path()) if self.memory == False else self.image
		imgResized = resize(img, (300,250))
		grayScaleImg = vl_rgb2gray(imgResized).astype('uint8')
		histEqualizedImage = equalizeHist(grayScaleImg)
		sizeOfSpatialBins = 8
		step = 10
		fast = False #if set to True it uses a flat window rather than a Gaussian window
		verbose = True
		norm = False
		bounds = -1
		[frames,descriptors] = vl_dsift(histEqualizedImage,step,bounds,sizeOfSpatialBins,fast,verbose,norm)
		descriptors = descriptors.transpose()
		return descriptors.astype('float32')


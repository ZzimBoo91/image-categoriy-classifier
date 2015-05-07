from vlfeat import vl_dsift, vl_imsmooth, vl_rgb2gray
from cv2 import imread, resize, equalizeHist

class DenseFeatureExtractor:

	def __init__(self, image, memory):
		self.image = image
		self.memory = memory

	def extract_feature_vector(self):
		img = imread(self.image.get_path()) if self.memory == False else self.image
		imgResized = resize(img, (300,250))
		grayScaleImg = vl_rgb2gray(imgResized).astype('uint8')
		histEqualizedImage = equalizeHist(grayScaleImg)
		sizeOfSpatialBins = 3 #binSize, i.e. 3x3 region
		step = 10
		fast = True #if set to True it uses a flat window rather than a Gaussian window
		verbose = norm = False
		bounds = -1
		[frames,descriptors] = vl_dsift(histEqualizedImage,step,bounds,sizeOfSpatialBins,fast,verbose,norm)
		return descriptors.astype('float32')


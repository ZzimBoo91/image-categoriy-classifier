from FeatureExtractor import FeatureExtractor
from DenseFeatureExtractor import DenseFeatureExtractor

class FeatureExtractorFactory:

    @staticmethod
    def newInstance(image,memory,type="denseSIFT"):
    	if type == "denseSIFT":
    		return DenseFeatureExtractor(image, memory)

    	if type == "SIFT":
        	return FeatureExtractor(image,memory)
from VLFeatKMeansCluster import VLFeatKMeansCluster
from OpenCVKMeansCluster import OpenCVKMeansCluster

class ClusteringFactory:

    @staticmethod
    def newInstance(clusters_count,type="VLFeat"):
    	if type == "VLFeat":
    		return VLFeatKMeansCluster(clusters_count)

    	if type == "OpenCV":
        	return OpenCVKMeansCluster(clusters_count)
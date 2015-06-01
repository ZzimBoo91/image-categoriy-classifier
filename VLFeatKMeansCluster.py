from numpy import vstack, transpose
import cv2 as cv
from vlfeat import vl_ikmeans

class VLFeatKMeansCluster:

    def __init__(self, clusters_count):
        self.clusters_count = clusters_count
        self.vector = None 
        
    def add_to_cluster(self, vector):
        if self.vector == None:
            self.vector = vector
        else:       
            self.vector = vstack((self.vector, vector))

    def cluster(self):
        self.vector = self.vector.transpose()
        centers, _ = vl_ikmeans(self.vector, self.clusters_count,method='elkan', verbose=0)
        return centers.transpose()


        

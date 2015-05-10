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
        print "2eddy", len(self.vector)==128
        print "rows da5elo", len(self.vector)
        print "cols da5elo", len(self.vector[0])
        centers, _ = vl_ikmeans(self.vector, self.clusters_count,200, method='lloyd', verbose=0)
        #print "el rows now teb2a el mafrud 128", len(centers)
        #print "el cols now teb2a el mafrud 100", len(centers[0])
        #OpenCVKMeansCluster
        #VLFeatKMeansCluster
        return centers.transpose()


        

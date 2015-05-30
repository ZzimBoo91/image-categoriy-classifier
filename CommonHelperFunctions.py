from sklearn.metrics import average_precision_score
from sklearn.preprocessing import label_binarize
import numpy as np
import getopt, sys, os, traceback
import cv2, csv
from random import sample

class CommonHelperFunctions:
	def __init__(self):
		pass

	def check_dir_condition(self,path):
		if not os.path.isdir(path):
			print("%s: No such directory" % (path)) 
			sys.exit(2)

	def check_file_condition(self,file):
		if not os.path.isfile(file):
			print("%s: No such file" % (file)) 
			sys.exit(2)

	def get_image_name_from_path(self,path):
		imgName = path.split("/")
		return imgName[len(imgName)-1]

	def load_image(self,img):
		return cv2.imread(img)

	def get_category_name_from_file_name(self,file_name):
		categoryName = file_name.split("_")
		categoryName = categoryName[1].split(".csv")[0]
		return categoryName

	def from_array_to_matrix(self,array_data):
		return np.matrix(array_data).astype('float32')

	def file_len(self,fname):
		with open(fname) as f:
			for i, l in enumerate(f):
				pass
		return i + 1

	def csv_references_at_least_one_image(self,path,csv_file_name):
		try:
			file_name = ("%s/%s" % (path, csv_file_name))
			with open(file_name) as fileReader:
				reader = csv.reader(fileReader, delimiter=' ')
				for j in reader:
					if os.path.isfile(file_name):
						return True
		except Exception, Argument:
			print "Exception happened: ", Argument
			return False

	def belongs_to_class(self,instance,correctClass):
		return instance.__class__.__name__ == correctClass

	def get_csv_file_as_array(self,path,fileName):
		fullPathCsvFile = ("%s/%s" % (path, fileName))
		csvFile = open(fullPathCsvFile)
		lines = csvFile.readlines()
		counter = 0
		for line in lines:
			lines[counter] = line.rstrip()
			counter += 1
		return lines

	def get_n_random_image_paths(self,path,fileName,n):
		allLines = self.get_csv_file_as_array(path,fileName)
		randomIndeces = sample(range(0, len(allLines)), n)
		result = []
		for i in range(0,len(randomIndeces)):
			result.insert(len(result),allLines[randomIndeces[i]])
		return result

	def get_list_difference(self,list1,list2):
		result = []
		for i,v in enumerate(list1):
			if v in list2:
				continue
			else:
				result.insert(len(result),v)
		return result

	def save_array_contents_as_csv(self,fileNameWrite,array):
		with open(fileNameWrite, 'w') as fileWriter:
			catWriter = csv.writer(fileWriter, delimiter=',', quoting=csv.QUOTE_MINIMAL)
			for i in range(0,len(array)):
				catWriter.writerow([array[i]])




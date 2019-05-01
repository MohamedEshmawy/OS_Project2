
import glob, os
dir_path = os.path.dirname(os.path.realpath(__file__))

for root, dirs, files in os.walk(dir_path):
	for f in files:
		fullpath = os.path.join(root, f)
		if os.path.splitext(fullpath)[1] == '.pyc':
			print (fullpath)
			os.remove(fullpath)

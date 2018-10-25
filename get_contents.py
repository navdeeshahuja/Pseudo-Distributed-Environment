"""

This program expects the user to give a filename, which it will read from the distributed environment.

"""

import os
import sys

if(len(sys.argv) < 2):
	print("Please supply a file name. Run the Program like python3 get_contents.py /path/to/file.ext")
	sys.exit();

filename = sys.argv[1]

if(len(filename) < 1):
	print("Empty Filename. Please run the program like python3 get_contents.py /path/to/file.ext")
	sys.exit();

filename = "distributed_storage/datanode_1/"+filename

if os.path.exists(filename) and os.path.isfile(filename):
	file = open(filename, "r")
	print(file.read())
else:
	print("No such file exists")
"""

This program expects the user to give a file, which it will store in the distributed environment.

"""

import os
import sys
from shutil import copy2

if(len(sys.argv) < 2):
	print("Please supply a file name. Run the Program like python3 save.py /path/to/file.ext")
	sys.exit();

filename = sys.argv[1]

if(len(filename) < 1):
	print("Empty Filename. Please run the program like python3 save.py /path/to/file.ext")
	sys.exit();


if os.path.exists(filename):
	print("Copying the File to Datanode 1")
	copy2(filename, "distributed_storage/datanode_1/")
	print("Replicating the File to Datanode 2")
	copy2(filename, "distributed_storage/datanode_2/")
	print("Replicating the File to Datanode 3")
	copy2(filename, "distributed_storage/datanode_3/")
else:
	print(filename+" no such file exists")
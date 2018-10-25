"""

This program expects the user to give a directory name, which should be listted from the distributed environment.

"""

import os
import sys

if(len(sys.argv) < 2):
	print("Please supply a directory name. Run the Program like python3 ls.py /path/to/directory")
	sys.exit();

directory_name = sys.argv[1]

if(len(directory_name) < 1):
	print("Empty directory name. Please run the program like python3 ls.py /path/to/directory")
	sys.exit();

directory_name = "distributed_storage/datanode_1/"+directory_name

if os.path.exists(directory_name) and os.path.isdir(directory_name):
	for f in os.listdir(directory_name):
		print(f)
else:
	print("No such directory")
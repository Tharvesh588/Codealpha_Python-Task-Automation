# import os
import shutil
print("=====================")
print("Simple File Organiser")
print("=====================")
print("Enter the path of the folder you want to organize") 
path = input("Enter Path:")

files=os.listdir(path)

for file in files:
	filename,extension = os.path.splitext(file)
	extension= extension[1: ]
	
	if os.path.exists(path+'/'+extension):
		shutil.move(path+'/'+file , path+'/'+extension+'/'+file)
		print("File moved successfully")

	else:
		os.mkdir(path+'/'+extension)
		shutil.move(path+'/'+file , path+'/'+extension+'/'+file)
		print("File moved successfully")

print("All files have been organized successfully")


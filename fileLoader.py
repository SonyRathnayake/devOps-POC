from os import walk

directory_path = "/Users/sonal/Desktop/Research/plugin/devOps/files"

# returns empty [] if no file available
filenames = next(walk(directory_path), (None, None, []))[2]
print("Specified Directory Path : ", directory_path)
print(filenames)
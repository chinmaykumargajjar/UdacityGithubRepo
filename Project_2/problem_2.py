import os

# Let us print the files in the directory in which you are running this script
print (os.listdir("./testdir"))

# Let us check if this file is indeed a file!
print (os.path.isfile("./testdir/t1.c"))

# Does the file end with .py?
print ("./testdir/t1.c".endswith(".py"))

def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    paths = list()
    if os.path.isfile(path):
        if path.endswith(suffix):
            paths.append(path)
    else:
        for item in os.listdir(path):
            paths.extend(find_files(suffix, (path+"/"+item)))
    return paths

print(find_files(".c","./testdir"))
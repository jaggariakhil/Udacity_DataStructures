import os
def find_files(suffix, path, files=[]):
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
    
    path1 = suffix
    if path:
        path1 = suffix + '/' + path
    for file in os.listdir(path1):
        path2 = path1 +  '/' + file
        
        if os.path.isdir(path2):
            files = find_files(path1, file, files)
        elif path2.endswith(".c"):
            files.append(path2)
            

        
    return files

print(find_files('.', 'testdir'))   #['./testdir/subdir1/a.c', './testdir/subdir3/subsubdir1/b.c', './testdir/subdir5/a.c', './testdir/t1.c']




print(find_files('.', ''))    #['./testdir/subdir1/a.c', './testdir/subdir3/subsubdir1/b.c', './testdir/subdir5/a.c', './testdir/t1.c', './testdir/subdir1/a.c', './testdir/subdir3/subsubdir1/b.c', './testdir/subdir5/a.c', './testdir/t1.c']


print(find_files('.', 'testdir/subdir3'))   #['./testdir/subdir1/a.c', './testdir/subdir3/subsubdir1/b.c', './testdir/subdir5/a.c', './testdir/t1.c', './testdir/subdir1/a.c', './testdir/subdir3/subsubdir1/b.c', './testdir/subdir5/a.c', './testdir/t1.c', './testdir/subdir3/subsubdir1/b.c']

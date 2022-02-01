
working dir.        index              head
    |.. unstaged files ..|
                      |.. staged files ..|


- unstaged files => diffrent of hash of working dir files and index files
- staged files => diffrent of hash of index files and head files

### see head files
    git ls-tree HEAD

### see index files
    git ls-files --stage


## finding unstaged files
- git index also contains ctime, mtime, inode no, dev, uid, gid, size, flag of each file
- when it compare working dir wrt to index
    - first it compare index of file with file (ctime, mtime, uid ...)
    - if it is same, file not changed
    - if it is changed then, it create a hash of the file and compare with index-hash of file, if it is changed or not

### see index info (ctime, mtime ...)
    git ls-files --debug



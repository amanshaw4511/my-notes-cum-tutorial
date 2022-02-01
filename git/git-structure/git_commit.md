
### git commit is a hash of 
git cat-file commit <commit-hash>
    reference tree
    reference parents (prev. commit)
    author info
    commitor info


### tree structure
git ls-tree <tree-hash>
    reference file1
    reference file2

### file 
git cat-file blob <file-hash>




## commit object, tree object and file object all are stored in
## .git/objects/<first-two-char-of-hash>/<rest-commit-char>

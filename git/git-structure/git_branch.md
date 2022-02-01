## git stroes the branch head reference

.git/refs/heads/
               /master
               /feature1

# creating branch create a file name of brach in ./git/refs/heads/<branch-name>

where file master contains head of master branch ref in graph
where file feature1 contains head of feature1 branch ref in graph



## ./git/HEAD file stores path of the file of the hash of current branch head ref
if we are in feature branch then it contains
    refs/heads/feature1




# Switching branch
    changes the content of ./git/HEAD

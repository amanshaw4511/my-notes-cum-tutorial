## merge feature1 into master
- it goes to the common-ancestor of both branch (m3 commit)
- list the files at common-ancestor from commit-tree
- list the files at feature1 head form commit-tree
- list the files at master head form commit-tree

- In merge commit
- copy file-hash of file common in both branch
- copy file-hash of file changed in master but not in feature1
- copy file-hash of file changed in feature1 but not in master
- if a file is changed in both -> auto-merge
    
    In auto merge
    - copy line common in both version of file
    - copy line changed in master but not in feature1
    - copy line changed in feature1 but not in master
    - if a line is changed in both version of file -> MERGE CONFLICT


### before merge
        - m1 -- m2 -- m3 -- m5(master)
                       |
                       |-- f4 -- f5(feature1)

### after merge
        - m1 -- m2 -- m3 -- m5 -- m6(master)
                       |          |
                       |-- f4 -- f5(feature1)



## fast forward merge
- merge feature1 into master
- if master have no new commits then fast forward merge happens
- it only update the head pointer of master to the head of the feature1

### before merge
        - m1 -- m2 -- m3 (master)
                       |
                       |-- f4 -- f5(feature1)

### after merge
        - m1 -- m2 -- m3
                       |           (master)
                       |-- f4 -- f5(feature1)


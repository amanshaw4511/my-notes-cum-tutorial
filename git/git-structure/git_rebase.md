## rebase feature1 into master
- find common ancenstor (m3 commit)
- apply master commit after (m3) one by one on top of feature1 head.
- move the head pointer of master to the last applied commit

### before rebase 
        - m1 -- m2 -- m3 -- m5(master)
                       |
                       |-- f4 -- f5(feature1)

### after rebase
        - m1 -- m2 -- m3          | -- m5(master)
                       |          |
                       |-- f4 -- f5(feature1)

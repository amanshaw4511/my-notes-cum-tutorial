  1.  VARIABLE ( like a general pointer ) :- it can point to any object

  2.  OBJECT :- it has three parts
            |
            |...    value ( stored in memory )
            |
            |...    type designator ( tell type of object )
            |
            |...    reference counter ( count the no. of variable are refering
                    to the given object

        ## note : when the refernce counter become 0 , the object is deleted by                     garbage collector or memory reclaimed


a = 333
... it create new object of value = 333  ( let name it obj1)
... assign type = int
... create a variable a and reference to object 333
... assign ref. counter = 1

b = 333
... it will create new object of value = 333 ( let name it obj2)
... ans so on


c = a
... create a variable c and reference to object obj1
... increament ref. counter of obj1 = 2

b = 'hello'
... now decrement ref counter of obj2 = 0
... so obj2 is now deleted from memory
... new object of value = 'hello'
... type = str
... ref. counter = 1

del a
... delete var a 
... decrement ref counter = 1

del c
... delete var c
... decrement ref counter = 0
... so obj1 is now removed



## note :
        as an optimization , Python internally caches and reuse certain kinds of        unchangable object such as small int and string.


## NUM
    # bool
    b = True
    b = False

    # int
    i = 4
    i = int(3.2)

    # float
    f = 3.1
    f = float(1)

## STRING
    s = 'hello world'
    s = "hello world"
    s = '''hello
            world'''

## complex
    c = 4 + 3j


## list
    l = list()  # empty list
    l = []      # empty list
    l = [1,2,'hello',3.5]

## dict
    d = dict()  # empty dict
    d = {}      # empty dict
    d = {'a':23, 'b':'alkl'}


## type of varible
    type(var)       -- <class 'int'>

## id of variable
    id(var)

    # every variable is object and it has unique id
    a = 'hello'
    b = 'hello'
    a == b          -- True
    id(a) == id(b)  -- False

    # some integer upto some range (-6 to 257 in my experiment) are constant and they dont create new object
    a = 3
    b = 3
    a == b          -- True
    id(a) == id(b)  -- True



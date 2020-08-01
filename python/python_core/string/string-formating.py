## method 1     ( c type formating )
    
    'i am %s, my age is %d' %('aman',20)
    --- i am aman, my age is 20

    'i am %s, my age is %s' %('aman',20)

    'i am %(name)s, my age is %d(age)' % {'name':'aman','age':20}

## method 2     ( functional formating )
    
    'i am {}, my age is {}'.format('aman',20)

    'i am {0}, my age is {1}'.format('aman',20)     # by position

    'i am {1}, my age is {0}'.format(20,'aman')

    'i am {name}, my age is {age}'.format(name='aman', age=20)      # by keyword

    'i am {name}, my {0} is {age}'format('age',age=20,name='aman')  # by both


## method 3     ( f - string )

    name = aman; age = 20
    f'i am {name}, my age is {age}'


#Code   Meaning
'''
s    String (or any object’s str(X) string)
r    Same as s , but uses repr , not str
c   Character (int or str)
d    Decimal (base-10 integer)
i    Integer
u    Same as d (obsolete: no longer unsigned)
o   Octal integer (base 8)
x    Hex integer (base 16)
X   Same as x , but with uppercase letters
e    Floating point with exponent, lowercase
E   Same as e , but uses uppercase letters
f    Floating-point decimal
F   Same as f , but uses uppercase letters
g   Floating-point e or f
G   Floating-point E or F
%   Literal % (coded as %% )
'''



##  %[(keyname)][flag][width][.precision]typecode

    keyname   : indexing the dictionary
    flag      : 
            +   numeric sign
            0   zerofill
            -   left justification


    width     : width of char to be displayed
    precision : digits after decimal points to display
    typecode  : typee

    # note : we can use * in place of width or precision
            to secify these as parameter
            '... %.*f...'. %(3, 1.12345)
            ... 1.123...


### adding keys,attribute and offsets

    import sys
>>> 'My {1[kind]} runs {0.platform}'.format(sys, {'kind': 'laptop'})
'My laptop runs win32'

>>> 'My {map[kind]} runs {sys.platform}'.format(sys=sys, map={'kind': 'laptop'})
'My laptop runs win32'


## advance formating

#   [[fill]align][sign][#][0][width][,][.precision][typecode]

    align   :
        <   -- left
        >   -- right
        ^   -- center
        =   -- padding after a sign char
        # fill : fill char for alignment

    sign    :
        +   -- 
        -   --
        space   --

    #       :
            
    0       :

    width   :

    ,       : thousand coma separator

    prec    : precision

    typecoe : typecode


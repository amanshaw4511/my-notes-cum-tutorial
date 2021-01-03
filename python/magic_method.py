## repr vs str 
--  myModule.py
    
class Person:
    def __init__(self):
        print('from init')

    def __repr__(self):
        return 'from repl'

    def __str__(self):
        return 'from str'

$ python
>> from myModule import Person
>> p = Person()
from init
>> p
from repl
>> print(p)
from str

##########################
source : https://docs.python.org/3/library/operator.html
## operator overloading
# mathematical operator
+       __add__(self,other)
-       __sub__(self,other)
*       __mul__(self,other)
/       __truediv__(self,other)
//      __floordiv__(self,other)
%       __mod__(self,other)
**      __pow__(self,other)

# assignment operator
+=      __iadd__(self,other)
-=      __isub__(self,other)
*=      __imul__(self,other)
/=      __idiv__(self,other)
%=      __imod__(self,other)
**=     __ipow__(self,other)

# relational operator
<       __lt__(self,other)
>       __gt__(self,other)
==      __eq__(self,other)
!=      __ne__(self,other)
<=      __le__(self,other)
>=      __ge__(self,other)



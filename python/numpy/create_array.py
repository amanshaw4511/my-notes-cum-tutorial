import numpy as np


np.array( object, dtype=None, copy=True, order=None, subok=False, ndmin=0)
    #object :   any sequence object (list)
    #dtype  :   desired data type of array
    #copy   :   object is copied
    #order  :   C (row major : c style), F (column major : fortan, matlab style, any (default)
    #subok  :   returned array forced to be a base class array
    #ndimin :   specify min. dim. of resultant array


# create 1-D array
a = np.array([1,3,5])
--- [1,3,5]

# create 2-D array
a2 = np.array([[1,2,4],[1,3,5]])
--- [[1,2,4]
     [1,3,5]]

# create 2-D array
a3 = np.array([1,2,4], ndimin= 2)
--- [[1,2,4]]

# ceate complex array
a4 = np.array([1,2,4],dtype=complex)
--- [1.+0.j,2.+0.j,4.+0.j]


# create array of any shape ( values will be random )
np.empty(shape, dtype=float, order='c' )
np.zeros( shape, dtype, order)
np.ones( shape, dtype, order)

# array of numerical range
np.arange(start=0, stop, step=1, dtype)

# arry of evenly spaced values in interval
np.linspace(start, stop, num, endpoint=True, retstep, dtype)
    #start  : start limit
    #stop   : end limit
    #num    : no. of points needed
    #endpoint   : stop value is included in seq.
    #retstep    : if true, return sample and stpe b/w two conse. num
    #dtype  : datatype of ndarray

# array of evenly spaced values in log scale
np.logspace(start, stop, num, endpoint=True, base=10, dtype)
    #base   : base of log space



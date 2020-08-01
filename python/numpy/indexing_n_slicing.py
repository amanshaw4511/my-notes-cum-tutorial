# indexing and slicing in 1-D array is same as list
a = np.arange(10)
# array[start: stop: step]
a[2,7,2]
--- [2 4 6]

# for 2-D array
a2 = np.arange(1,10).reshape(3,3)
--- [[ 1 2 3 ]
     [ 4 5 6 ]
     [ 7 8 9 ]]
# array[(for row) start:stop:step, (for column) start:stop:step)
a2[0:1,1:2]
--- [[ 1 2 ]
     [ 4 5 ]]

## advance indexing
-# integer indexing
# array[[row-points],[column-points]]
a2[[0,1,2],[0,1,0]]
--- [ 1 5 7 ]

# combined indexing
a2[1:3,[1,2]]
--- [[ 5 6 ]
     [ 7 8 ]]

# boolean indexing
a2[a2>4]
--- [ 5 6 7 8 9 ]
a2[a2%2 == 0]
--- [ 2 4 6 8 ]
    # removing np.nan numbers
arr[~np.isnan(arr)]
    # selecting complex numbers
arr[np.iscomplex(arr)]



# Rediraction

## Redirect
    awk 'BEGIN { print "file content" > "a.txt" }'

## Redirect Append
    awk 'BEGIN { print "more content" >> "a.txt" }'


## pipe
    awk 'BEGIN { print "hello world !!!" | "tr [a-z] [A-z]" }'


## Two way communication
    ....

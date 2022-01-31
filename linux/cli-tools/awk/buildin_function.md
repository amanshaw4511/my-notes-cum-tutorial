# Buildin Functions


## String functions
printf(format, expr-list)

lenght(string)              => length of string
tolower(string)
toupper(string)

split(string, arr, regex)   => split string to arr

asort(arr [,d [, how]])     => sort arr wrt values
asorti(arr [,d [, how]])    => sort arr wrt keys/index

index(string, sub)          => returns index/pos where substring matched else 0
match(string, regex)        => returns index of longest match of regex else 0

strtonum(string)            => string to num
    strtonum("123")  :  123
    strtonum("0123") :  83
    strtonum("0x123"):  291

sub(regex, sub, string)     => replace first
gsub(regex, sub, string)    => replace all



## Arithmatic functions
int(expr)
sqrt(expr)

sin(expr)       => arg in radians
cos(expr)
atan2(expr)     => returns the arctangent of (y/x) in radians
exp(expr)       => natural exponent
log(exp)        => natural log

rand()          => 0 >= rand() < 1
srand(seed)     => gen random with seed/ when seed not provided uses current time as seed

## Time functions
systime()               => unix epoch time
mktime(datespec)        =>  datespec is string format "YYYY MM DD HH MM SS"
strftime([format [, timestamp [, utc-flag ]]]) => format timestamp
    strftime("Time = %d/%m/%Y %H:%M:%S" , systime())

## Bit manipulation functions
and(num1, num2)
or(num1, num2)
xor(num1, num2)
compl(num)
lshift(num, n)
rshift(num, n)


## Miscellaneous functions
close(file)         => close file of pipe
delete(arr["a"])    => delete array element
exit()              => stop execution
getline()           => read nextline
next()              => stop flow of program
nextfile()          => stop processing current file and start next one
return()            => return in function
system(command)     => similer to os.system(), returns program exit status

        


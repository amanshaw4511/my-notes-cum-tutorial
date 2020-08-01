-- GROUP FUNCTION ( AGGREGATE FUNC )

ABS(m)
MOD(m,n)
POWER(m,n)
SQRT(n)
EXP(n)
LN(n)
LOG(base,n)

ROUND(m[,n])
TRUNC(m[,n])
CEIL(n)
FLOOR(n)
SIGN(n)         :- -1 if n<0, 0 if n=0, +1 if n>0

SIN(n)
COS
TAN
ASIN
ACOS
ATAN
SINH
COSH
TANH


---- SINGLE ROW FUNCTION 

-- CONVERSION FUNCTION
NVL
TO_CHAR
TO_NUMBER
TO_DATE


-- CHAR FUNCTION
INITCAP         -- titlecase
LOWER           -- lowercase
UPPER           -- uppercase

TRIM(char from s1)
LTRIM(char from s1)
RTRIM(char from s1)
LPAD(s1, pad_length[, pad_char])
RPAD(s1, pad_length[, pad_char])

SUBSTR(s1,[-]start[,length])
REPLACE(s1, search, replace )
CONCAT(s1,s2)
INSTR(s1,sub_str[, start_pos[, nth_apperance]])     -- returns index of Nth found substring in s1
LENGTH(s1)


-- DATE FUNCTION



# String

## string initialization
- three ways to initial string
    1. local s = "hello"
    2. local s = 'hello'
    3. local s = [["hello"]]


## string methods

- upper
- lower
- gsub(str, substr, replacestr)
- find(str, substr [, startindex [, endindex]])
- reverse
- format(...)
- len
- rep(str, n)
- char / byte -> convert byte to char / char to byte
    eg.
        string.byte("abc")      -> 97
        string.byte("abc", 3)   -> 99
        string.char(98)         -> b



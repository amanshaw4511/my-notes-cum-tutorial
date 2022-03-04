# meta variable

- item
    an item, like a function, struct, module, etc
- block
    a block (i.e a block of statements and/or an expression, sorrounded by braces )
- stmt
    a statement
- pat
    a pttern
- expr
    an expresssion
- ty
    a type
- ident
    an identifier
- path
    a path (i.e. foo, ::std::mem::replace, transmut::<_,int>, ... )
- tt
    a toke tree ( a single token or tokens in matching delimiters (), [] or {} )
- meta
    a meta item; this tinkgs that go inside #[...] and #![...]
- lifetime
    liftime token
- vis
    a possibly empty visibility qualifier
- literals
    matches literal expression


## Repetitions
    repetition block => $( ... )
    followed by repetition operator, optionally with a seperator token other than rep. operator eg(',', ';')

### repetition operator
- *  -> zero or more repetition
- +  -> one or more repetition
- ?  -> zero or one occurence

    Examples
    $( $i:ident ),*     =>   any number of identifier sep by comman


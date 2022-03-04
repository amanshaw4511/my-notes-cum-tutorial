https://doc.rust-lang.org/std/option/

# methods

## query variant
    is_some() -> bool
    is_none() -> bool

## adapter for working with ref
- as_ref() :        &Option<T> -> Option<&T>
- as_mut() :        &mut Option<T> -> Option<&mut T>

- as_deref() :      &Option<T> -> Option<&T::Target>
- as_deref_mut() :  &mut Option<T> -> Option<&mut T::Target>

- as_pin_ref() :    Pin<&Option<T>> -> Pin<Option<&T>>
- as_pin_ref_mut() :        Pin<&mut Option<T>> -> Pin<Option<&mut T>>


## extracting contained value

- unwrap() :        panic with generic message
- expect(&msg_str) :panic with custom message

- unwrap_or(default_value) : return provided default value
- unwrap_or_default() :     return default value of type
- unwrap_or_else(f):        return defalut value from function f


## transform contained value

### Option => Result
- ok_or(error_value) :
    Some(T) => Ok(T)
    None    => Err(error_value)

- ok_or_else(f) :
    Some(T) => Ok(T)
    None    => Err(f())

- transpose() :     Option<Result<T, E>> -> Result<Option<T>, E>

### Option => Option
- flatten() :       Option<Option<T>> -> Option<T>

- filter(f) :
    None    =>  None
    Some(x) =>  Some(f(x))  , if f(x) == true
                None        , if f(x) == false

- map(f) :
    None    => None
    Some(x) => Some(f(x))

### Option<T> => U
- map_or(default_value, f)
    None    => default_value
    Some(x) => f(x)

- map_or_else(f1, f2)
    None    => f1()
    Some(x) => f2(x)

### Option, Option => Option
- zip(Option)
    Some(x), Some(y)  => Some((x,y))
    _                 => None

- zip_with(Option, f) 
    Some(x), Some(y)  => Some(f(x,y))
    _                 => None


## Boolean Operator
- and(Option)
    Some(x), Some(y)  => Some(y)
    _                 => None

- or(Option)
    Some(x), *        => Some(x)
    None   , Some(y)  => Some(y)
    -                 => None

- xor(Option)
    Some(x), None     => Some(x)
    None   , Some(y)  => Some(y)
    _                 => None


### 
- and_then(f), where f -> Option
    Some(x), f(x)       => f(x)
    _                   => None

- or_else(f),  weher f -> Option
    Some(x), *          => Some(x)
    None   , f(x)       => f(x)
    -                   => None

## Comparision
    Some(x) > None
    None < Some(x)

## Iterating
    eg.
    let nums: Vec<i32> = (0..3).chain(Some(99)).chain(3..5).collect();
        =>  [ 0, 1, 2, 99, 3, 4 ]
    let nums: Vec<i32> = (0..3).chain(None).chain(3..5).collect();
        =>  [ 0, 1, 2, 3, 4 ]

### collecting list of Option
    Iterator<Option<T>> =>  Option<Vec<T>>
    if all element are Some  => Some(list of all the x form Some(x))
    else                     => None

    let v_option = vec![Some(1), None, Some(3)];
    let option_v: Option<Vec<_>> = v.into_iter().collect();
        => None

    let v_option = vec![Some(1), Some(2), Some(3)];
    let option_v: Option<Vec<_>> = v.into_iter().collect();
        => Some(vec[1, 2, 3])
### same as product and sum
    Iterator<Option<T>> => Option<T>
    if all element are Some  => Some( sum/product of all the x from Some(x) )
    else                     => None


## Modify Option in place

## returns mutable ref to the value
- insert(value)
- get_or_insert(value)
- get_or_insert_default()
- get_or_insert_with(f)

## transfer ownership
- take()
    return the value and replace the option with none
- replace(other_value)
    return the value and replace option's value as other_value



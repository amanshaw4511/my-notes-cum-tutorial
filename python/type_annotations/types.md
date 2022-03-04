
### basic types
    int
    float
    str
    bool

    Any
    Tuple[T1, T2, T3, ...]
    List[T]
    Set[T]
    Dict[T, U]
    Optional[T]

    Iterable[T]  # eg. list, set, map, str
    Sequence[T]  # eg. list, str
    Callable[[arg1_type, arg2_type, ...], ret_type]  # for function


## generics
    T = TypeVar('T')

    def get_item(lst: List[T], index: int) -> T :
        return lst[index]


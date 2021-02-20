# premittive Array to boxed Array

    int[] p_arr = { 1, 4, 2, 6, 3 };
    Integer[] b_arr = Arrays.stream(p_arr).boxed().toArray(Integer[]::new);


# boxed Array to premittive Array
    
    Integer[] b_arr = { 1, 4, 2, 6, 3 };
    int[] p_arr = Arrays.stream(b_arr).mapToInt(Integer::intValue).toArray();
    



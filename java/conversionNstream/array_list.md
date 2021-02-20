
# array to list

    // premittive
    int[] p_arr = { 3, 1, 4, 23, 43, 2 };
    List<Integer> list = Arrays.stream(p_arr).boxed().collect(Collectors.toList());

    // boxed
    Integer[] b_arr = {3, 1, 4, 23, 43, 2};
    List<Integer> list = Arrays.stream(b_arr).collect(Collectors.toList());
    LinkedList<Integer> list = Arrays.stream(b_arr).collect(Collectors.toCollection(LinkedList::new));
    List<Integer> immutableList = Arrays.asList(b_arr);


# list to Arrays
    
    List<Integer> list;

    // boxed
    Integer[] b_arr = list.toArray(new Integer[list.size()]);
    Integer[] b_arr = list.toArray(new Integer[0]); // or
    Integer[] b_arr = list.stream().toArray(Integer[]::new) // or java 8
    Integer[] b_arr = list.toArray(Integer[]::new) // or java 11

    // premittive
    int p_arr = list.stream().mapToInt(Integer::intValue).toArray();


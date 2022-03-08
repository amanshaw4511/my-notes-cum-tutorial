# Mokito

```
class NinthElement {
    List<integer> list;
    NinthElement(List<Integer> list) {
        this.list = list;
    }

    int getNinthElement() {
        return list.get(0);
    }
}
```

```
class NinthElementTest {
    @Test
    void test() {
        List<Integer> list = mock(List.class)
        when(list.get(8)).thenReturn(11);

        NinthElement ninthElement = new NinthElement(list);
        assertEqual(ninthElement.getNinthElement(), 11);
    }
}
```

### Using annotation
```
@RunWith(MokitoJUnitRunner.class)
class NinthElementTest {
    @Mock
    List<Integer> list

    @InjectMocks
    NinthElement ninthElement;


    @Test
    void test()  {
        when(list.get(8)).thenReturn(11);
        assertEqual(ninthElement.getNinthElement(), 11);
    }
}
```

## Returning

### Always returning same
List mockList = mock(List.class);
when(mockList.size()).thenReturn(10);

assertEqual(mockList.size(), 10);
assertEqual(mockList.size(), 10);


### Return differnt value each time
List mockList = mock(List.class);
when(mockList.size()).thenReturn(10).thenReturn(20);

assertEqual(mockList.size(), 10);
assertEqual(mockList.size(), 20);
assertEqual(mockList.size(), 20);
assertEqual(mockList.size(), 20);
assertEqual(mockList.size(), 20);

### Mock method with parameter
List mockList = mock(List.class);
when(mockList.get(Mokito.anyInt()).thenReturn("element");

assertEqual(mockList.get(0), "element");
assertEqual(mockList.get(1), "element");
assertEqual(mockList.get(99), "element");

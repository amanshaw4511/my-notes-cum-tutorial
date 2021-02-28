# change title on change component 

    const [count, setCount] = useState(0);
    const incrementCount = () => setCount(prev => prev +1);


## compoenent did mount

    useEffect( () => {
        document.title = `intital count = $count`;
    }, [] );
    // useEffect runs only once when component mount (intital render)


## component did update

    useEffect( () => {
        document.title = `you clicked $count times`;
    }); 
    // useEffect runs on every render of component (mount, update of component)


## compoenent will unmount

    // clean up function
    // the return function (clean up function) will be called
    // when component will unmount

    useEffect( () => {
        document.title = " component did mount";

        return () => {
            document.title = "component will unmount";
        }
    }, [] )


## change in state

    useEffect( () => {
        document.title = `you clicked $count times`;
    }, [count] );
    // useEffect runs only when count value changes

    

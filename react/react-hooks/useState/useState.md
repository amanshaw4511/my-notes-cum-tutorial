
# update boolean value

    const [on, setOn] = useState(false);

    const turnOn = () =>  setOn(true);
    const turnOff = () => setOn(flase);


# update number 

    const [count, setCount] = useState(0);

    const incrementCount = () => setCount(prevCount => prevCount +1);
    const decrementCount = () => setCount(prevCount => prevCount -1);


# update object

    const [student, setStudent] = useState({name : "", roll : null});
    
    const changeStudent = () => setStudent( { name : "new name", roll : 4 } );
    const changeName = () => setStudent(prevStudent => { ...prevStudent, name : "new name" });
    const changeRoll = () => setStudent(prevStudent => { ...prevStudent, roll : 5 }):


# update array

    const [students, setStudents] = useState( [] );

    const newStud = {name : "ram", roll : 21};
    const addStudent = () => setStudent( prevStudents => [ ...prevStudents, newStud ] )

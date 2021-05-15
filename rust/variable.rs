// immutable by defalut
// to make mutable use 'mut' keyword

// statically typed lang

// data types :
//              bool
//              u16
//              i32
//              i64
//              f64
//


fn main() {
    let a; // declaration; without data type
    a = 5; // assignment

    let b: i8 // declaration; with data type
    b = 5;

    let t = true;  // declaration + assignment; without data type
    let t: bool = false; // declaration + assignment; with data type


    let (x,y) = (1,2);  // x = 1 and y = 2

    let mut z = 5;
    z = 7;

    let z = { x + y };  // z = 3

    let z = {
        let x = 1;
        let y = 2;

        x + y
    };      // z = 3


    // constants
    // constants are not allowed to change, they live for entire lifetime of a program but has no fixed address in memeory

    const N: i32 = 5;

    // static
    // static is used to define global variable, there is only one instance of each value, and it's
    // at a fixed memeory location

    static N: i32 = 5;



}

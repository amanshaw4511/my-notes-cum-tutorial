
fn main() {
    let v = vec![3,5,6];
    let a: [i32; 3] = v.iter().map(|e| e*2).collect();
    println!("{:?}", a);
}

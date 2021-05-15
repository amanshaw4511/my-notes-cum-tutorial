
# Crates
A crate is a package, which can be shared via crates.io
a crate can produce an executable bin or a library
IOW it can be **binary** create or a **library** crate.


## produce an executable
    cargo new crate_name --bin
```sh
|_____Cargo.toml
|__ src
    |__ main.rs
```

## produce a library
    cargo new crate_name --lib
```sh
|___Cargo.toml
|__ src
    |__ lib.rs
```

+ **Cargo.toml** is config file, contains all metadata that Cargo need to compile your project
+ **src** dir to store source code
+ **main.rs** and **lib.rs** is the crate root for bin and lib reate



# Project Structure
```sh
.
|__ Cargo.toml
|__ Cargo.lock
|__ src
|   |__ main.rs
|   |__ lib.rs
|   |__ bin
|       |__ example.rs
|
|__ tests
|   |__ some_integration_test.rs
|
|__ benches
|   |__ simple_bench.rs
|
|__ examples
    |__ simple_exampe.rs

```

 

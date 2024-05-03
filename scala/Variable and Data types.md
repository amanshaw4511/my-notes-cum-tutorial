## Build-in data type
```scala
// integer group
val b: Byte = 1
val s: Short = 1
val i: Int = 1 // default in type inference
val l: Long = 1

// floating point group
val f: Float = 1.0
val d: Double = 1.0 // default in type inference

// declaring number type using postfix
val l = 35L  // Long
val f = 3.14F  // Float

// large number
val bi = BigInt(1_500_25)
val bd = BigDecimal(1_500.25)


// char & string
val ch: Char = 'a'
val str: String = "hello"


// string interpolation
val name = "aman"
val age = 20
val intro = s"I am $name. My age is ${age}"

// multipline string
val quote = """The essence of Scala:
               Fusion of functional and object-oriented
               programming in a typed setting."""

```
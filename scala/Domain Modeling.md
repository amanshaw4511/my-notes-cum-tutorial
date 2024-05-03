[domain mooodeling](https://docs.scala-lang.org/scala3/book/domain-modeling-tools.html)
## class
```scala
// declare a class
class Person(var name: String, var age: Int)
class Book(var title: String, var author: String, var year: Int)

// instantiate
val person = Person("aman", 20)

// access fields
println(s"name = ${person.name}, age = ${person.age}")

// modify fields
person.age = 22



//
```
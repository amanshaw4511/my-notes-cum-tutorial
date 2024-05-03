## If-Else
```scala
val age = 20;
if age >= 18 then
	println("adult")
else
	println("not adult")


// if else is an expression :)
val adultStatus = if age >= 18 then "adult" else "not adult"
println(adultStatus)
```

## For loop
```scala
val nums = List(1, 2, 3, 4, 5, 6, 7, 8)

for num <- nums do println(num)


// print even number
for num <- nums
	if num % 2 == 0 // guard
do
	println(num)

// for loop as expression
val squares = for num <- nums yield num * num

// print even number using for yield
val evenNums = for
	num <- nums
	if num % 2 == 0
	yield num

println(evenNums)

```

## Match Expression
```scala
val num = 1
num match
	case 1 => println("one")
	case 2 => println("two")
	case _ => println("other")

// match as expression
val numAsString = num match
	case 1 => "one"
	case 2 => "two"
	case _ => "other"

println(numAsString)

// match class
val person = Person("aman", 20)

val adultStatus = person match
	case Person(name, age) if age >= 18 => s"$name is an adult"
	case Person(name, _) => s"$name is not an adult"

println(adultStatus)


// match types 
def getClassAsString(x: Matchable) : String = x match
	case s: String => s"$s is a String"
	case i: Int => "Int"
	case d: Double => "Double"
	case l: List[?] => "List"
	case _: => "Uknown"

getClassAsString(1)               // Int
getClassAsString("hello")         // 'hello' is a String
getClassAsString(List(1, 2, 3))   // List
//
```


## Try/Catch/Finally
```scala
try
	writeTextToFile(text) 
catch 
	case ioe: IOException => println("Got an IOException.") 
	case nfe: NumberFormatException => println("Got a NumberFormatException.")
finally
	println("Clean up your resources here.")

```



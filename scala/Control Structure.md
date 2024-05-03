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
match num
	case 1 : println("one")
	case 2 : println("two")
	
```
# Neetspeak

Neetspeak is an interpreted programming language with syntax based off mathematical pseudocode. Its purpose is to offer simple, easy to read, and runnable pseudocode found in algorithm papers and textbooks without having to transcribe it into another language. Neetspeak is written in Python using the PLY framework. 

Although the syntax is based off pseudocode, it is very similar to Ruby with the inclusion of the `end` keyword. It should also be noted that due to this, Neetspeak ignores whitespace such as spaces, tabs, and newlines. 

## Requirements

* Python 3.7+
* PLY

On Ubuntu, all dependencies can be installed using apt and pip:
```shell
$ sudo apt install python3 python3-pip
```
```shell
$ pip3 install ply
```

## How to run

To run directly from source, use the `interpreter.py` code file on any text file with neetspeak syntax code.
```shell
$ python3 interpreter.py test.neet
```

Context of `test.neet`:
```ruby
main()
	print('hello there')
end
```

## Data Types

Neetspeak offers all necessary data types to remain simple and barebones without adding too much bloat. Data types are based on those found in Python. Syntax is essentially the same as in Python with the exception of booleans. 

* **Integer**: Identical to Python int type
	```ruby
	4, -7, 324234
	```
* **Real**: Identical to Python float type
	```ruby
	0.5, -3.8, 2e5
	```
* **Boolean**: Lowercase unlike Python bool type
	```ruby
	true, false
	```
* **String**: Identical to Python str type
	```ruby
	"hello", 'there'
	```
* **List**: Identical to Python list type
	```ruby 
	[4,6,3], ['a',5,], [], [[1,3],[1,3]]
	```

## Operations

Operations on data types are essentially the same as operations in Python with slight differences in syntax. Let `x` and `y` be two variables that may represent Integers, Reals, Booleans, Strings, or Lists depending on the context. 

| Operator | Description               |
|----------|---------------------------|
| a + b	   | addition                  |
| a - b    | subtraction               |
| a * b    | multiplication            |
| a / b    | division                  |
| a % b    | modulus                   |
| a ** b   | exponentiation            |
| a := b   | variable assignment       |
| a or b   | boolean OR                |
| a and b  | boolean AND               |
| not a    | boolean NOT               |
| a xor b  | boolean XOR               |
| a = b    | equal to                  |
| a > b    | greater than              |
| a >= b   | greater than or equal to  |
| a < b    | less than                 |
| a <= b   | less than or equal to     |
| a[b]     | list indexing             |
| a()      | function call             |
| a in b   | list or string membership |

## Syntax and Semantics

The syntax and semantics are the same as mathematical psuedocode found in papers and textbooks. The most notable feature is the use of the `end` keyword to close `if` statements, `for` and `while` loops, and function definitions. 

### Print Statement

A simple print statement found in Python. Prints any data type, but only takes a single parameter. Use string concatenation to print multiple statements

```ruby
print('1 + 2 equals ' + (1 + 2))
```

### Main function

Neetspeak requires a main function as an entry point to any program.
```ruby
main()
	print('hello there')
end
```

### Variables

Variables are assigned using the `:=` keyword.
```ruby
x := 5
y := 7
print('x + y = ' + (x + y))

name := "Bob"
age := 18
print('My name is ' + name + ' and I am ' + age + ' years old')
```

### List and String Indexing

Neetspeak is based on mathematical psuedocode so arrays start at 1 instead of 0. List and String indexing is 1 to the length.
```ruby
a := [5, 3, 7]
print(a)
print('[' + a[1] + ', ' + a[2] + ', ' + a[3] + ']')

b := 'word'
print(b)
print("'" + b[1] + b[2] + b[3] + b[4] + "'")
```

Lists and Strings are identical to those in Python and Ruby and can be multidimensional.
```ruby
x := [[1,2],1,3]
print(x[1])
print(x[1][1])

s := "yes i am"
print(s[5])
print(s[2][1][1])
```

### If Statements and Else-If Statements

If statements use the `if` keyword with the boolean condition followed by the `then` keyword. The statement is followed by an `else` keyword for the else statement or ended using the `end` keyword. 

```ruby
x := 5
y := 7

if x = y then
	print('yes')
end

if x = y then
	print('yes')
else 
	print('no')
end
```

Else-if statements are followed by an if statement and use the `elseif` keyword. They are followed by further else-if statements or ended using the `end` keyword. 

```php
x := 2

if x = 1 then
	print('first if statement')
elseif x = 2 then
	print('second if statement')
elseif x = 3 then
	print('third if statement')
else
	print('else statement')
end
```

### While Loops

While loops are the similar to if conditions as they use the `while` keyword with the boolean condition followed by the `then` keyword. They are ended using the `end` keyword. 

```ruby
x := 1
while x < 5 do
	print(x)
	x := x + 1
end

y := 5
while y >= 0 do
	print(y)
	y := y - 1
end
```

### For Loops

For loops are a bit different from most programming languages due to their representation in pseudocode. The actual functionality is similar to C-style for loops. For loops use the `for` keyword and are followed by a variable assignment. Afterwards, there will be a `to` or `downto` keyword to indicate whether to count up or down. A values will then need to be specified to count towards, inclusive. The rest of the syntax is the same as a while loop. 

```ruby
for x := 92 to 97 do
	print(x)
end

for x := 8 downto 4 do
	print(x)
end
```

### Functions

TBA

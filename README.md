# Neetspeak

Neetspeak is an interpreted programming language with syntax based off mathematical pseudocode. Its purpose is to offer simple, easy to read, and runnable pseudocode found in algorithm papers and textbooks without having to transcribe it into another language. Neetspeak is written in Python using the PLY framework. 

Although the syntax is based off pseudocode, it is very similar to Ruby with the inclusion of the `end` keyword. It should also be noted that due to this, Neetspeak ignores whitespace such as spaces, tabs, and newlines. 

## Requirements

* Python 3
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
algorithm main()
    print('hello there')
end
```

## Data Types

Neetspeak offers all necessary data types to remain simple and barebones without adding too much bloat. Data types are based on those found in Python. Syntax is essentially the same as in Python with the exception of booleans. 

* **Integer**: Identical to the Python `int` type
    ```ruby
    4, -7, 324234
    ```
* **Real**: Identical to the Python `float` type
    ```ruby
    0.5, -3.8, 2e5
    ```
* **Boolean**: Similar to the Python `bool` type but lowercase
    ```ruby
    true, false
    ```
* **String**: Identical to the Python `str` type
    ```ruby
    "hello", 'there'
    ```
* **List**: Identical to the Python `list` type
    ```ruby 
    [4,6,3], ['a',5,], [], [[1,3],[1,3]]
    ```
* **Null**: Similar to the Python `None` type
    ```c#
    null
    ```

## Operations

Operations on data types are essentially the same as operations in Python with slight differences in syntax. Let `x` and `y` be two variables that may represent Integers, Reals, Booleans, Strings, or Lists depending on the context. 

| Operator | Description                  |
|----------|------------------------------|
| a + b	   | addition                     |
| a - b    | subtraction                  |
| a * b    | multiplication               |
| a / b    | division                     |
| a % b    | modulus                      |
| a ** b   | exponentiation               |
| a := b   | variable assignment          |
| a or b   | boolean OR                   |
| a and b  | boolean AND                  |
| a xor b  | boolean XOR                  |
| not a    | boolean NOT                  |
| a = b    | equal to                     |
| a != b   | not equal to                 |
| a > b    | greater than                 |
| a >= b   | greater than or equal to     |
| a < b    | less than                    |
| a <= b   | less than or equal to        |
| a | b    | bitwise OR                   |
| a & b    | bitwise AND                  |
| a ^ b    | bitwise XOR                  |
| ~a       | bitwise NOT                  |
| a << b   | bitwise left shift           |
| a >> b   | bitwise right shift          |
| -a       | unary minus                  |
| +a       | unary plus                   |
| a[b]     | list indexing                |
| a()      | function call                |
| a(b)     | function call with parameter |
| a in b   | list or string membership    |

## Syntax and Semantics

The syntax and semantics are the same as mathematical psuedocode found in papers and textbooks. The most notable feature is the use of the `end` keyword to close `if` statements, `for` and `while` loops, and function definitions. 

### Print Statement

A simple print statement found in Python. Prints any data type, but only takes a single parameter. Use string concatenation to print multiple statements

```ruby
print('1 + 2 equals ' + (1 + 2))
```

### Comments

Comments are C-style and will be ignored when running the program. The start with the `/*` keyword and end with the `*/` keyword. Since Neetspeak ignores whitespace, the multiline comment is necessary. 

```c#
/* this will be ignored */
print("hello there")
x := 5 /* good for documentation */
print(x + 1) /* 6 */
```

### Main function

Neetspeak requires a main function as an entry point to any program. Other functions can also created, but the main function is required for the program to run. 
```ruby
algorithm main()
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

All variables are global and can be accessed anywhere regardless of where they are declared. 

```ruby
algorithm main()
    x := 5
    access()
end

algorithm access()
    print(x)
end
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

### Foreach Loops

Foreach loops are the same as the Python style for loops and the C# style foreach loop. Foreach loops begin with the `foreach` keyword and use a variable to represent values of a List or String. The `in` keyword is used to access elements of the variable. THe rest of the syntax is the same as a while or for loop. 

```c#
nums := [4, 7, 3, 8, 1]
foreach x in nums do
    print(x)
end
```

### Functions

Functions declaration syntax is more like Ruby than Python. However, instead of the `def` keyword, the `algorithm` keyword is used instead. Functions behave exactly the same way as in Python and can take parameters. Functions may return any single value using the `return` keyword. 
```ruby
algorithm main()
    x := double(5)
    print(x)
end

algorithm double(x)
    return 2 * x
end
```

Functions that do not return anything using the `return` will return a `null` value. 
```ruby
algorithm main()
    x := hello()
    print(x)
end

algorithm hello()
    print('hello')
end
```

Functions support recursion. Max recursion depth is the default in Python. 
```ruby
algorithm factorial(n)
    if n <= 0 then
        return 1
    else
        return n * factorial(n - 1)
    end
end
```

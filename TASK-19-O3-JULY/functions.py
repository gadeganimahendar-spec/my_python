# atleast 5to10 questions solve in function topic
#1. Function Without Parameters
def greet():
    print("Hello, World!")

greet()

#2. Function With Parameters
def add(a, b):
    print(a + b)

add(10, 20)

#3. Function Returning a Value
def square(n):
    return n * n

result = square(5)
print(result)

#4. Even or Odd Using Function
def even_odd(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(even_odd(8))
print(even_odd(5))

#5. Find the Largest Number
def largest(a, b):
    if a > b:
        return a
    else:
        return b

print(largest(15, 20))

#6. Factorial Using Function
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

print(factorial(5))
#7. Prime Number Using Function
def prime(n):
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True

print(prime(7))
print(prime(8))

#8. Sum of List Elements
def list_sum(numbers):
    return sum(numbers)

nums = [10, 20, 30, 40]
print(list_sum(nums))

#9. Reverse a String
def reverse_string(text):
    return text[::-1]

print(reverse_string("Python"))

#10. Default Arguments
def welcome(name="Guest"):
    print("Welcome", name)

welcome()
welcome("mahi")

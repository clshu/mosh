def fizz_buzz(n):
    if n % 15 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return n


print(fizz_buzz(30))  # FizzBuzz
print(fizz_buzz(3))   # Fizz
print(fizz_buzz(5))   # Buzz
print(fizz_buzz(7))   # 7

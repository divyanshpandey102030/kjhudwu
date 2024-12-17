def fibonacci_in_range(start,end):
    a,b= 0,1
    fibonacci_numbers = []
    while b<= end:
            if b>= start:
             fibonacci_numbers.append(b)
             a,b = b,a + b
    return fibonacci_numbers

print("Fibonacci numbers between", start, "and", end, ":",fibonacci_numbers) 

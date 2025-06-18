ef fibonacci(n):
    fib_series = []
    a, b = 0, 1
    for _ in range(n):
        fib_series.append(a)
        a, b = b, a + b
    return fib_series

def main():
    try:
        n = int(input("Enter the number of Fibonacci terms to generate: "))
        if n <= 0:
            print("Please enter a positive integer.")
            return
    except ValueError:
        print("Invalid input! Please enter an integer.")
        return
    
    result = fibonacci(n)
    print(f"First {n} terms of the Fibonacci series:")
    print(result)

if __name__ == "__main__":
    main()

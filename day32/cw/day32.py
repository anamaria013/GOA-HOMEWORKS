def sum(a, b, c):
    return a + b + c

    def substract(a, b):
        return a - b
    def multiply(a, b):
        return a * b

    def divide(a, b):
        if b != 0:
            return a / b
        else:
            return "Division by zero is not allowed"

    
    print(sum(1, 2, 3))          
    print(substract(10, 5))      
    print(multiply(4, 5))        
    print(divide(10, 2))         
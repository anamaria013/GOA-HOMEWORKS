def find_largest(numbers):

    if not numbers:
        return None

    result = max(numbers)
    return result

numbers = [5, 2, 9, 1, 7, 6, 3]
result = find_largest(numbers)
print(f"The largest number is: {result}") 
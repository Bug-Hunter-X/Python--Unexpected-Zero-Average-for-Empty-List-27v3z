def calculate_average(numbers):
    if not numbers:
        raise ValueError("Cannot calculate the average of an empty list.")
    return sum(numbers) / len(numbers)

# Example usage:
try:
    my_list = []
    average = calculate_average(my_list)
    print(f"The average is: {average}")
except ValueError as e:
    print(f"Error: {e}") #This will print a more informative error message
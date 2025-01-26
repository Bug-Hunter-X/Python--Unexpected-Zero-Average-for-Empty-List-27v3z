def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list
    return sum(numbers) / len(numbers)

# Example usage with potential error:
my_list = []
average = calculate_average(my_list) 
print(f"The average is: {average}") #This will print 0 which is not a desirable output. Consider raising an exception instead
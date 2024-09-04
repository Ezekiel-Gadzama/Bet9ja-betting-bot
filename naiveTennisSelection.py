from collections import Counter
import random

count_percentage = 0.3


def count_every_th(n):
    all_results = []  # List of lists to store results for each i

    for i in range(1, 1000000):
        maximum_count = int(count_percentage * n)  # Target number of elements for this iteration
        result = []
        numbers = list(range(1, n + 1))  # Create a list of all numbers from 1 to n
        index = 0  # Starting index
        percentage = i * 0.1  # Calculate percentage
        target_count = int(percentage * n)
        while len(result) < maximum_count and numbers:
            # Calculate the index for every 70th number
            index = (index + target_count - 1) % len(numbers)  # Adjusted to use len(numbers)

            # Add the selected number to the result
            result.append(numbers[index])

            # Remove the selected number from the list
            numbers.pop(index)

        # Store the sorted result for this percentage
        all_results.append(sorted(result))

    return all_results


def get_most_common_numbers(all_results_now):
    # Flatten the list of lists into a single list
    flattened_list = [num for sublist in all_results_now for num in sublist]

    # Count the frequency of each number
    number_counts = Counter(flattened_list)

    # Sort the numbers based on frequency in descending order

    return sorted(number_counts.items(), key=lambda x: x[1], reverse=True)


# Split the list into t = 5 equal parts
def printResult(final_list_show):
    t = 4
    list_size = len(final_list_show) // t  # Determine the size of each sublist
    split_lists = [final_list_show[i * list_size:(i + 1) * list_size] for i in range(t)]

    # If there are remaining elements, add them to the last sublist
    if len(final_list_show) % t != 0:
        split_lists[-1].extend(final_list_show[t * list_size:])

    # Print each of the 4 sublists
    for i, sublist in enumerate(split_lists, start=1):
        print(f"\nSublist {i}:")
        print(sublist)
    print("\nThe end of the list\n\n")


# Example usage
n = 94  # Replace with any number
all_results = count_every_th(n)
sorted_numbers = get_most_common_numbers(all_results)
print(f"length of sorted_numbers: {len(sorted_numbers)}")
# Print the numbers sorted by highest intersection
# Initialize an empty list to store the first 30 numbers
final_list = []

# Iterate over the sorted numbers and append the first 30 to final_list
for number, count in sorted_numbers[:int(count_percentage * n)]:
    print(f"Number: {number}, Count: {count}")
    final_list.append(number)

# Now final_list will contain the first 30 numbers from the sorted list
print(f"\nFinal List of first {int(count_percentage * n)} numbers:\n{sorted(final_list)}\n\n\n\n")
printResult(final_list)
final_list = sorted(final_list)
printResult(final_list)

# Randomly select 28 unique numbers between 1 and 94
random_numbers = random.sample(range(1, n + 1),  int(count_percentage * n))

# Print the randomly selected numbers
print("Randomly selected numbers:")
print(sorted(random_numbers))

# Find and print the intersection of final_list and random_numbers
intersection = sorted(set(final_list).intersection(random_numbers))
print(f"\nNumbers that intersect between final_list and random_numbers has length: {len(intersection)}")
print(intersection)

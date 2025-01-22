from collections import Counter

# Example list of elements
elements = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']

# Create a Counter object
counter = Counter(elements)

# Display the count of each element
print(counter)

# Access the count of a specific element
print(f"Count of apples: {counter['apple']}")

# Display the most common elements
print("Most common elements:", counter.most_common())

# Update the counter with more elements
more_elements = ['banana', 'orange', 'orange']
counter.update(more_elements)

# Display the updated count of each element
print("Updated counter:", counter)

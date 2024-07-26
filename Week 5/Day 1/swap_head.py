def swap_head_tail(lst):
    n = len(lst)
    if n == 0:
        return lst  # Return the empty list as is
    
    mid_index = n // 2
    if n % 2 == 0:
        head = lst[:mid_index]
        tail = lst[mid_index:]
        return tail + head
    else:
        head = lst[:mid_index]
        middle = lst[mid_index]
        tail = lst[mid_index + 1:]
        return tail + [middle] + head

# Additional tests
test_cases = [
    ([], "Empty list"),  # Edge case: empty list
    ([1], "Single element"),  # Edge case: single element
    ([1, 2], "Two elements"),  # Even number of elements
    ([1, 2, 3], "Three elements"),  # Odd number of elements
    ([1, 2, 3, 4], "Four elements"),  # Even number of elements
    ([1, 2, 3, 4, 5], "Five elements"),  # Odd number of elements
    ([1, 2, 3, 4, 5, 6], "Six elements"),  # Even number of elements
    ([1, 1, 1, 1, 1], "Five identical elements"),  # Odd number of elements, all same
    ([1, 2, 3, 4, 5, 6, 7, 8], "Eight elements"),  # Even number of elements, larger size
]

for lst, description in test_cases:
    result = swap_head_tail(lst)
    print(f"Test case: {description}\nOriginal list: {lst}\nSwapped list: {result}\n")

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

# Example usage
print(swap_head_tail([1, 2, 3, 4, 5]))  # Output: [4, 5, 3, 1, 2]
print(swap_head_tail([1, 2, 3, 4]))     # Output: [3, 4, 1, 2]

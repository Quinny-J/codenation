preset_error_messages = [
    "Error",
    "Success",
    "Warning"
]

# add to end of the list 
preset_error_messages.append("Crash")

print(preset_error_messages)

# remove the item you just added to the end of the list
preset_error_messages.pop()

print(preset_error_messages)

print(f"Number of items in preset_error_messages {len(preset_error_messages)}")
print(f"Number of characters in the first item '{preset_error_messages[0]}' in the list {len(preset_error_messages[0])}")
print(f"Number of characters in the last item '{preset_error_messages[-1]}' in the list {len(preset_error_messages[0])}")


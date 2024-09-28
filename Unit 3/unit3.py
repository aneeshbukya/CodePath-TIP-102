# Post Compare
# U - Understand
# Questions to help understand the problem:
# What happens if the backspace character # is the first character or if there are multiple consecutive backspace characters?
# Should the case of letters (uppercase vs lowercase) be considered when comparing the processed strings?
# P - Plan
# What do I want to do?
# I need to simulate typing out both draft1 and draft2 where each # represents a backspace.
# I will process each string by removing the last character if # is encountered and keep track of the characters that remain.
# Once both drafts are processed, I will compare the final versions of each draft to check if they are equal.
# Pseudocode:
# Create a helper function process(draft) to simulate typing:
# Initialize an empty stack.
# Loop through each character in the draft:
# If the character is # and the stack is not empty, remove the last character.
# If the character is not #, add it to the stack.
# Return the stack joined as a string.
# For draft1 and draft2, apply the process() function.
# Compare the processed results of draft1 and draft2.
# Return True if the processed drafts are equal, otherwise return False.
# I - Implement
def post_compare(draft1, draft2):
    def process(draft):
        # Stack to simulate the text editing with backspaces
        stack = []
        for char in draft:
            if char == '#':
                # Remove last character if stack is not empty
                if stack:
                    stack.pop()
            else:
                # Add the current character to the stack
                stack.append(char)
        # Return the processed string (final result after typing)
        # print(stack)
        # print(''.join(stack))
        return ''.join(stack)
    
    # Compare the processed versions of both drafts
    return process(draft1) == process(draft2)

# Example Usage:
print(post_compare("ab#c", "ad#c"))  # Expected Output: True
print(post_compare("ab##", "c#d#"))  # Expected Output: True
print(post_compare("a#c", "b"))      # Expected Output: False

# Lexicographically Smallest Watchlist
# U - Understand
# Questions to help understand the problem:
# What should happen if the string is already a palindrome? Should we still try to make it lexicographically smaller?
# Can the watchlist string contain only lowercase English letters, or could there be other constraints?
# P - Plan
# What do I want to do?
# I want to make the input string a palindrome with the minimum number of operations. If the characters at symmetric positions (left and right) are different, I should replace the lexicographically larger character with the smaller one.
# The goal is to make the string the lexicographically smallest palindrome possible.
# Pseudocode:
# Convert the input string watchlist to a list (since strings in Python are immutable).
# Initialize two pointers:
# left = 0 (start of the list).
# right = len(watchlist) - 1 (end of the list).
# While left < right:
# If watchlist[left] != watchlist[right]:
# Replace the lexicographically larger character between watchlist[left] and watchlist[right] with the smaller one.
# Move left pointer to the right.
# Move right pointer to the left.
# Convert the list back to a string and return the result.
# I - Implement
def make_smallest_watchlist(watchlist):
    # Convert the watchlist string to a list for easy modification
    watchlist = list(watchlist)
    
    # Initialize two pointers
    left, right = 0, len(watchlist) - 1
    
    # Traverse the list from both ends towards the center
    while left < right:
        # If the characters at left and right are different
        if watchlist[left] != watchlist[right]:
            # Replace the lexicographically larger character with the smaller one
            if watchlist[left] > watchlist[right]:
                watchlist[left] = watchlist[right]
            else:
                watchlist[right] = watchlist[left]
        
        # Move pointers towards the center
        left += 1
        right -= 1
    
    # Convert the list back into a string and return it
    return ''.join(watchlist)

# Example Usage:
print(make_smallest_watchlist("egcfe"))  # Expected Output: "efcfe"
print(make_smallest_watchlist("abcd"))   # Expected Output: "abba"
print(make_smallest_watchlist("seven"))  # Expected Output: "neven"

# Marking the Event Timeline:

# U - Understand
# Questions to help understand the problem:
# Are we allowed to replace the ? with any letter from the event, even if it doesn't exactly match the corresponding letter in timeline?
# What should we do if multiple positions allow us to place the event string? Do we choose the first possible one from the left?
# P - Plan
# What do I want to do?:
# We need to iteratively place the event string into an empty string t (initially filled with ?) such that we gradually transform it into the timeline. We must keep track of where we place event at each turn, and aim to match as much of the timeline as possible each time.
# The problem asks for an efficient approach to minimize the number of moves and ensure that we do not exceed 10 * timeline.length moves.
# Pseudocode:
# Initialize a string t with all ? characters and set up an empty array result to store the indices where we place event.
# Loop up to a maximum of 10 times the length of the timeline.
# For each possible index in t where event can be placed:
# Check if placing event at this index will bring t closer to the timeline.
# If it does, replace the corresponding ? characters in t and update t.
# Append the index of the placement to the result.
# If t matches timeline, return the result array.
# If after 10 * timeline.length turns we can't match the timeline, return an empty array.
# I - Implement
def mark_event_timeline(event, timeline):
    # Initialize the string t with all '?' characters and an empty result list
    current_state = ['?'] * len(timeline)
    placement_indices = []
    
    # Check if placing 'event' at position index brings current_state closer to timeline
    def can_place_event_at(index):
        for i in range(len(event)):
            # Only place event if the characters either match or we have a '?'
            if current_state[index + i] != '?' and current_state[index + i] != event[i]:
                return False
        return True
    
    # Place the 'event' at the given index by replacing '?' in current_state
    def place_event_at(index):
        for i in range(len(event)):
            current_state[index + i] = event[i]
    
    # Maximum number of turns we can take to match the timeline
    max_turns = 10 * len(timeline)
    
    # Try to place the event and match the timeline within the allowed turns
    for _ in range(max_turns):
        # Loop through each valid position where we can place the event
        for start_index in range(len(timeline) - len(event) + 1):
            if can_place_event_at(start_index):
                # Place the event at the valid index
                place_event_at(start_index)
                # Record this index where the event was placed
                placement_indices.append(start_index)
                
                # If current_state matches the timeline, return the result
                if ''.join(current_state) == timeline:
                    return placement_indices
    
    # If we can't match the timeline within the allowed turns, return an empty list
    return []

# Example Usage:
print(mark_event_timeline("abc", "ababc"))  # Expected Output: [0, 2]
print(mark_event_timeline("abca", "aabcaca"))  # Expected Output: [3, 0, 1]

# Validate Animal Sheltering Sequence 
# U - Understand
# Share 2 questions you would ask to help understand the question:
# Can we assume that animals are admitted in the order given in the admitted array?
# Can we adopt an animal only if it was previously admitted and is the most recently admitted (LIFO principle)?
# P - Plan
# Write out in plain English what you want to do:
# This problem can be modeled using a stack, where animals are admitted (pushed to the stack) and adopted (popped from the stack) in a valid sequence. The goal is to simulate the process of admitting animals into the shelter (push) and adopting them out (pop) to verify if the adopted sequence could have happened.
# We push animals onto the stack in the order they are admitted and pop them when the next animal in the adopted sequence matches the top of the stack.
# Translate each sub-problem into pseudocode:
# Initialize an empty stack.
# Iterate over the admitted animals.
# For each animal admitted, push it onto the stack.
# After each push, check if the top of the stack matches the current animal in the adopted sequence:
# If it matches, pop the animal from the stack and move to the next animal in adopted.
# Repeat this process until either all animals are adopted or we cannot match the adopted sequence.
# If the stack is empty at the end and the adopted sequence is fully matched, return True, else return False.
# I - Implement
def validate_shelter_sequence(admitted, adopted):
    # Initialize an empty stack to simulate the shelter process
    stack = []
    # Pointer to track the position in the adopted array
    adopted_index = 0

    # Iterate over all admitted animals
    for animal in admitted:
        # Push the animal onto the stack (admission process)
        stack.append(animal)

        # While stack is not empty and the top of the stack matches the adopted animal
        while stack and stack[-1] == adopted[adopted_index]:
            # Pop the animal from the stack (adoption process)
            stack.pop()
            # Move to the next animal in the adopted sequence
            adopted_index += 1

    # If the stack is empty, all animals were adopted in the correct order
    return not stack

# Example Usage:
print(validate_shelter_sequence([1, 2, 3, 4, 5], [4, 5, 3, 2, 1]))  # True
print(validate_shelter_sequence([1, 2, 3, 4, 5], [4, 3, 5, 1, 2]))  # False


# Sort Performances by Type 
# U - Understand
# Share 2 questions you would ask to help understand the question:
# Can performances contain both zero and negative numbers, and should they be treated as even and odd respectively?
# Are we allowed to change the relative order of the even and odd performances, or should we maintain stability?
# P - Plan
# Write out in plain English what you want to do:
# We want to separate the even and odd performances. All the even-type performances should appear before the odd-type ones. Even numbers are divisible by 2, and odd numbers are not. After separation, we will return the rearranged array.
# Translate each sub-problem into pseudocode:
# Initialize two empty lists: one for even performances and one for odd performances.
# Iterate through the array:
# If a performance is even, append it to the even list.
# If a performance is odd, append it to the odd list.
# Concatenate the even and odd lists to form the final result.
# Return the result.
# I - Implement
def sort_performances_by_type(performances):
    # Step 1: Initialize two lists to store even and odd performances
    even_performances = []
    odd_performances = []

    # Step 2: Iterate through the performances array
    for performance in performances:
        # Check if the performance is even or odd
        if performance % 2 == 0:
            even_performances.append(performance)  # Add to even list
        else:
            odd_performances.append(performance)   # Add to odd list

    # Step 3: Combine the even and odd performances lists
    return even_performances + odd_performances

# Example Usage:
print(sort_performances_by_type([3, 1, 2, 4]))  # Output: [2, 4, 3, 1]
print(sort_performances_by_type([0]))           # Output: [0]

# Check if a Signal Occurs as a Prefix in Any Transmission 
# U - Understand
# Share 2 questions you would ask to help understand the question:
# Does the signal comparison need to be case-sensitive?
# How should we handle empty strings or transmissions that contain no valid signals?
# P - Plan
# Write out in plain English what you want to do:
# First, split the transmission into individual signals using the space character as a delimiter.
# Then, iterate over the list of signals, checking if searchSignal is a prefix of any signal.
# If searchSignal is a prefix, return the 1-based index of the signal.
# If no signal matches, return -1.
# Translate each sub-problem into pseudocode:
# Split the transmission string by spaces to get individual signals.
# Loop through each signal and check if searchSignal is a prefix of the signal using Python's string .startswith() method.
# If a match is found, return the current index (adjusting to 1-based).
# If no match is found after the loop, return -1.
# I - Implement
def is_prefix_of_signal(transmission, searchSignal):
    # Step 1: Split the transmission into a list of signals
    signals = transmission.split(" ")

    # Step 2: Loop through each signal and check if searchSignal is a prefix
    for i, signal in enumerate(signals):
        if signal.startswith(searchSignal):
            # Step 3: Return the 1-indexed position (i+1)
            return i + 1

    # Step 4: If no prefix match is found, return -1
    return -1

# Example Usage:
print(is_prefix_of_signal("i love eating burger", "burg"))  # Output: 4
print(is_prefix_of_signal("this problem is an easy problem", "pro"))  # Output: 2
print(is_prefix_of_signal("i am tired", "you"))  # Output: -1

# Next Greater Element
# U - Understand
# Questions to help understand the problem:
# How should we handle the circular nature of the sequence? Should we loop back to the beginning of the array after reaching the end?
# If there are multiple elements greater than the current element, which one should we choose?
# P - Plan
# Plan in plain English:
# We need to traverse through each element in the list and find the first greater element that comes after it, considering the circular nature of the list.
# If no greater element exists when checking, we will return -1 for that element.
# To handle the circular nature, we can treat the list as if it repeats by iterating through the list twice.
# Use a stack to help track indices where we haven't yet found a next greater element, allowing efficient lookups.
# Pseudocode:
# Initialize an empty stack and an array result filled with -1 (default value for elements with no next greater element).
# Loop over the array twice (circular nature).
# For each element dreams[i]:
# While the stack is not empty and dreams[i] is greater than the element at the index stored at the top of the stack:
# Update result for the index at the top of the stack with the value of dreams[i] (because this is the next greater element for that index).
# Pop the top of the stack.
# If we are in the first loop (not second traversal), push the current index onto the stack.
# Return the result array.
# I - Implement
def next_greater_dream(dreams):
    n = len(dreams)
    result = [-1] * n  # Initialize the result with -1
    stack = []  # Stack to store indices
    
    # Loop through the array twice for circular effect
    for i in range(2 * n):
        while stack and dreams[stack[-1]] < dreams[i % n]:
            result[stack.pop()] = dreams[i % n]
        if i < n:
            stack.append(i)
    
    return result

# Example usage
print(next_greater_dream([1, 2, 1]))  # Output: [2, -1, 2]
print(next_greater_dream([1, 2, 3, 4, 3]))  # Output: [2, 3, 4, -1, 4]

# Market Token Value
# U - Understand
# Questions to help understand the problem:
# How do we differentiate between adjacent tokens and nested tokens when calculating the value?
# Is the input always guaranteed to be a valid mystical token string, or do we need to account for invalid input?
# P - Plan
# Plan in plain English:
# Traverse through the string and use a stack to help track the levels of nesting.
# For every open bracket (, push the current value to the stack, and reset the current value to 0 (indicating we're entering a nested structure).
# For every closing bracket ), pop the last value from the stack and add twice the current value to it. If we encounter a () pair directly, it contributes a value of 1.
# At the end of traversal, return the accumulated value.
# Pseudocode:
# Initialize stack as an empty list and current_value as 0.
# Loop through each character in the string:
# If the character is (:
# Push the current_value onto the stack and reset current_value to 0.
# If the character is ):
# If the last character was ( (i.e., it's ()), set current_value = current_value + 1.
# Otherwise, pop the top value from the stack and add 2 * current_value to it.
# Set current_value to the value at the top of the stack (after popping).
# Return current_value at the end.
# I - Implement
def token_value(token):
    stack = []
    current_value = 0
    
    for i, char in enumerate(token):
        if char == '(':
            # Push current value to the stack and reset current value
            stack.append(current_value)
            current_value = 0
        elif char == ')':
            # Check if it's a direct () pair
            if token[i-1] == '(':
                current_value = 1
            else:
                current_value = 2 * current_value
            
            # Add current value to the top of the stack
            current_value += stack.pop()
    
    return current_value

# Example usage
print(token_value("()"))  # Output: 1
print(token_value("(())"))  # Output: 2
print(token_value("()()"))  # Output: 2

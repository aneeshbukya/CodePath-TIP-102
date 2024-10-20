# 1.) Merging Mission II
# U - Understand
# Share 2 questions you would ask to help understand the question:
# What should the function return if both input linked lists are empty?
# Should the merged list maintain ascending order or any specific order?
# P - Plan
# Write out in plain English what you want to do:
# I need to merge two sorted linked lists into one sorted linked list.
# Start by comparing the first nodes of both linked lists. Attach the smaller node to the result list and move forward in the corresponding list.
# Continue comparing nodes and appending the smaller one until one of the lists is exhausted.
# If any list still has remaining nodes, attach them directly to the merged list since they are already sorted.
# Finally, return the head of the merged linked list.
# Translate each sub-problem into pseudocode:
# Create a temporary node to act as a placeholder for the merged list.
# Use a tail pointer to keep track of the end of the merged list.
# While both lists are non-empty:
# Compare the current nodes from both lists.
# Attach the smaller node to the merged list using the tail pointer.
# Move the corresponding list’s pointer forward.
# Move the tail pointer forward to the newly added node.
# After the loop, if any list still has nodes:
# Attach the remaining nodes to the merged list.
# Return the merged list, starting from the node after the temporary placeholder.
# I - Implement
class Node:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

# Helper function to print linked lists for testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

# Recursive solution to merge two sorted linked lists
def merge_missions_recursive(mission1, mission2):
    # Base cases: if one list is empty, return the other list
    if not mission1:
        return mission2
    if not mission2:
        return mission1

    # Compare the current nodes and recursively merge the rest
    if mission1.value < mission2.value:
        mission1.next = merge_missions_recursive(mission1.next, mission2)
        return mission1
    else:
        mission2.next = merge_missions_recursive(mission1, mission2.next)
        return mission2

# Iterative solution provided in the task for comparison
def merge_missions_iterative(mission1, mission2):
    temp = Node()  # Temporary node to simplify merging
    tail = temp

    while mission1 and mission2:
        if mission1.value < mission2.value:
            tail.next = mission1
            mission1 = mission1.next
        else:
            tail.next = mission2
            mission2 = mission2.next
        tail = tail.next

    # Attach the remaining nodes, if any
    if mission1:
        tail.next = mission1
    elif mission2:
        tail.next = mission2

    return temp.next  # Return the head of the merged linked list

# Test the recursive solution
list1 = Node(1, Node(3, Node(5)))
list2 = Node(2, Node(4, Node(6)))
print("Recursive Solution:")
print_linked_list(merge_missions_recursive(list1, list2))

# Test the iterative solution
list3 = Node(1, Node(3, Node(5)))
list4 = Node(2, Node(4, Node(6)))
print("Iterative Solution:")
print_linked_list(merge_missions_iterative(list3, list4))

# 2.) Weaving Spells I and II
# U - Understand
# Share 2 questions you would ask to help understand the question:
# What should the function return if one of the input linked lists is empty?
# Are the two input linked lists always of the same length, or can one be longer than the other?
# P - Plan
# Write out in plain English what you want to do:
# The goal is to merge two linked lists such that their nodes alternate in this pattern:
# a1 -> b1 -> a2 -> b2 -> a3 -> b3 -> ...
# We will recursively weave the nodes. If one list runs out of nodes, we just return the remaining nodes of the other list.
# For each recursive call:
# Attach the current node from list B after the node from list A.
# Continue weaving by recursively calling the function on the next nodes of both lists.
# The recursion stops when one of the lists is exhausted.
# Translate each sub-problem into pseudocode:
# Base case:
# If one of the lists is None, return the other list.
# Recursive step:
# Store the next pointers of both lists for future recursion.
# Set the next pointer of the current node from list A to the current node from list B.
# Set the next pointer of the current node from list B to the result of the recursive call with the next nodes of both lists.
# Return the head of the merged (woven) list.
# I - Implement

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# Helper function to print linked lists for testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

# Recursive solution to weave two linked lists
def weave_spells(spell_a, spell_b):
    # Base case: If one list is empty, return the other
    if not spell_a:
        return spell_b
    if not spell_b:
        return spell_a

    # Store the next nodes for recursion
    next_a = spell_a.next
    next_b = spell_b.next

    # Weave spell_b after spell_a
    spell_a.next = spell_b

    # Recursively weave the rest of the lists
    spell_b.next = weave_spells(next_a, next_b)

    # Return the head of the woven list
    return spell_a

# Test the recursive solution
spell_a = Node('A', Node('C', Node('E')))
spell_b = Node('B', Node('D', Node('F')))
print("Recursive Solution:")
print_linked_list(weave_spells(spell_a, spell_b))
def weave_spells_iterative(spell_a, spell_b):
    # If either list is empty, return the other
    if not spell_a:
        return spell_b
    if not spell_b:
        return spell_a

    # Start with the first node of spell_a
    head = spell_a
    
    # Loop through both lists until one is exhausted
    while spell_a and spell_b:
        next_a = spell_a.next  # Store next pointers
        next_b = spell_b.next
        
        spell_a.next = spell_b  # Weave spell_b after spell_a
        
        if next_a:  # If there are more nodes in spell_a, weave them
            spell_b.next = next_a
        
        # Move to the next nodes
        spell_a = next_a
        spell_b = next_b

    return head  # Return the head of the woven list
# Which Solution is Better?
# Recursive Solution:
# Easier to read and understand, especially for smaller inputs.
# However, it may cause a stack overflow for very large lists due to deep recursion.
# Iterative Solution:
# More verbose but avoids recursion and stack overflow issues.
# Efficient for large inputs as it only uses a fixed amount of memory.

# 3.) Ternary Expression
# U - Understand
# Share 2 questions you would ask to help understand the question:
# How should nested ternary expressions be evaluated? (Answer: They are grouped right-to-left.)
# What should be the output when encountering multiple levels of nesting in the expression?
# P - Plan
# Write out in plain English what you want to do:
# The task is to evaluate a ternary expression recursively.
# A ternary expression follows the pattern:
# condition ? true_choice : false_choice
# To solve this recursively:
# Evaluate from right to left—if a condition evaluates to T, we return the true part; otherwise, the false part.
# For nested expressions, we continue breaking them down recursively.
# Base case: If the expression is just a single digit or character, return it.
# Translate each sub-problem into pseudocode:
# Base Case: If the expression is a single digit (0 to 9), 'T', or 'F', return it as the result.
# Recursive Step:
# Find the first ternary operator from the end (right to left).
# Identify the condition, true_choice, and false_choice.
# Recursively evaluate the relevant choice based on the condition.
# Keep narrowing down the expression until only one value remains.
# I - Implement
def evaluate_ternary_expression_recursive(expression):
    def helper(i):
        # If the current character is a digit or 'T'/'F', return it as the result.
        if expression[i].isdigit() or expression[i] in 'TF':
            return expression[i], i
        
        # Handle ternary expressions (condition ? true_choice : false_choice)
        condition = expression[i]  # 'T' or 'F'
        i += 2  # Move past '?' to the true choice
        
        # Recursively evaluate the true choice
        true_result, i = helper(i)
        
        i += 1  # Move past ':' to the false choice
        
        # Recursively evaluate the false choice
        false_result, i = helper(i)
        
        # Return the appropriate result based on the condition
        if condition == 'T':
            return true_result, i
        else:
            return false_result, i
    
    # Start evaluating the expression from the first character
    result, _ = helper(0)
    return result

print(evaluate_ternary_expression_recursive("T?2:3")) # Expected output: 2
print(evaluate_ternary_expression_recursive("F?1:T?4:5")) # Expected output: 4
print(evaluate_ternary_expression_recursive("T?T?F:5:3")) # Expected output: F

# 4.) Decoding Ancient Atlantean Scrolls
# U - Understand
# Share 2 questions you would ask to help understand the question:
# Can nested encodings have multiple levels, e.g., 2[3[Sea]Coral]?
# Are there any constraints on the length of the input scroll, or should the solution handle very large inputs?
# P - Plan
# Write out in plain English what you want to do:
# This problem involves decoding nested encodings that follow the pattern k[encoded_message]. The challenge lies in handling nested brackets recursively, expanding each encoded message the correct number of times.
# The recursive approach involves:
# Scanning the scroll from left to right.
# When a digit is found, we parse the full number to know how many times to repeat the next encoded section.
# When encountering an opening bracket [, we recursively decode the substring inside it.
# Once we encounter a closing bracket ], we return the decoded section multiplied by the parsed number.
# The recursion should continue until the entire scroll is decoded.
# Translate each sub-problem into pseudocode:
# 1. Define an empty result string to store the decoded result for the current level.
# 2. While i is within the scroll’s length:
#    a. If the current character is a digit:
#       - Build the complete number (could span multiple digits).
#    b. If the current character is '[':
#       - Recursively decode the substring inside the brackets.
#       - Append the decoded result to the current level’s result string.
#    c. If the current character is ']':
#       - Return the current decoded result string and the current index.
#    d. If the current character is a letter:
#       - Add it to the current result string.
# 3. Return the final decoded string after processing all characters.
# I - Implement
def decode_scroll_recursive(scroll):
    def helper(i):
        current_string = ""
        num = 0

        # Process the scroll starting from index i
        while i < len(scroll):
            char = scroll[i]

            if char.isdigit():
                # Build the number (may have multiple digits)
                num = num * 10 + int(char)

            elif char == '[':
                # Recursively decode the inner message
                decoded_part, i = helper(i + 1)
                # Repeat it 'num' times and append to the current string
                current_string += decoded_part * num
                # Reset the number after processing
                num = 0

            elif char == ']':
                # Return the current decoded string and the next index
                return current_string, i

            else:
                # Regular character, just add it to the current string
                current_string += char

            i += 1

        return current_string, i

    # Start decoding from the first character
    decoded_string, _ = helper(0)
    return decoded_string

# Example Usage
scroll1 = "3[Coral2[Shell]]"
print(decode_scroll_recursive(scroll1))  # Output: CoralShellShellCoralShellShellCoralShellShell

scroll2 = "2[Poseidon3[Sea]]"
print(decode_scroll_recursive(scroll2))  # Output: PoseidonSeaSeaSeaPoseidonSeaSeaSea


# 5.) Cruise Ship Treasure Hunt
# U - Understand
# Share 2 questions you would ask to help understand the question:
# Can the matrix contain duplicate room numbers, or are all values unique?
# What is the expected size of the matrix (m x n)? This helps in analyzing the performance constraints.
# P - Plan
# Write out in plain English what you want to do:
# We need to locate the position of the treasure in a 2D grid where both rows and columns are sorted in ascending order.
# A divide-and-conquer strategy will help us efficiently search the matrix. The idea is to narrow down the search space using the sorted order:
# Start searching from the top-right corner.
# If the current room number is greater than the treasure, move left.
# If the current room number is less than the treasure, move down.
# If the room matches the treasure, return the coordinates (row, col).
# If the search reaches the boundaries without finding the treasure, return (-1, -1).
# 1. Start from the top-right corner of the matrix (row = 0, col = n - 1).
# 2. While the row and column indices are within bounds:
#    - If the current room value matches the treasure:
#        - Return the current (row, col).
#    - If the current room value is greater than the treasure:
#        - Move left (col -= 1).
#    - If the current room value is less than the treasure:
#        - Move down (row += 1).
# 3. If the loop completes without finding the treasure:
#    - Return (-1, -1).

def find_treasure(matrix, treasure):
    # Get the dimensions of the matrix
    if not matrix or not matrix[0]:
        return (-1, -1)  # Handle edge cases where matrix is empty

    rows = len(matrix)
    cols = len(matrix[0])

    # Start from the top-right corner
    row = 0
    col = cols - 1

    # Perform the search
    while row < rows and col >= 0:
        if matrix[row][col] == treasure:
            return (row, col)  # Found the treasure!
        elif matrix[row][col] > treasure:
            col -= 1  # Move left
        else:
            row += 1  # Move down

    # If the loop completes, treasure wasn't found
    return (-1, -1)

# Example Usage
rooms = [
    [1, 4, 7, 11],
    [8, 9, 10, 20],
    [11, 12, 17, 30],
    [18, 21, 23, 40]
]

print(find_treasure(rooms, 17))  # Output: (2, 2)
print(find_treasure(rooms, 5))   # Output: (-1, -1)

# 6.) Merge Sort Playlist
# U - Understand
# Share 2 questions you would ask to help understand the question:
# How should case sensitivity be handled? For example, should "apple" and "Apple" be considered equal or sorted differently?
# Can the input list contain duplicate songs, and should they be preserved in the sorted output?
# P - Plan
# Write out in plain English what you want to do:
# The goal is to sort the playlist alphabetically using merge sort, a divide-and-conquer sorting algorithm.
# Merge sort works by recursively splitting the list into two halves, sorting each half, and merging the sorted halves back together.
# For merging, we use a helper function that compares elements from both halves and builds a sorted result.
# The base case occurs when the playlist has 1 or 0 elements, which is already sorted.
# Translate each sub-problem into pseudocode:
# Function merge_sort_helper(left_arr, right_arr):
# 1. Create an empty list `result` to store the merged sorted list.
# 2. Use two pointers (i, j) for left_arr and right_arr.
# 3. While both pointers are within the bounds of their lists:
#    a. If left_arr[i] is smaller, add it to result and increment i.
#    b. Otherwise, add right_arr[j] to result and increment j.
# 4. Add any remaining elements from left_arr to result.
# 5. Add any remaining elements from right_arr to result.
# 6. Return the merged result.
# Function merge_sort_playlist(playlist):
# 1. Base Case: If playlist has 1 or 0 elements, return the playlist.
# 2. Recursive Case:
#    a. Find the middle index of the playlist.
#    b. Recursively call merge_sort_playlist on the left half.
#    c. Recursively call merge_sort_playlist on the right half.
#    d. Use merge_sort_helper to merge the two sorted halves.
# 3. Return the merged sorted playlist.
# I - Implement
def merge_sort_helper(left_arr, right_arr):
    result = []  # Store the merged sorted list
    i, j = 0, 0  # Pointers for left_arr and right_arr

    # Merge elements from both halves
    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] <= right_arr[j]:
            result.append(left_arr[i])
            i += 1
        else:
            result.append(right_arr[j])
            j += 1

    # Add remaining elements from the left half (if any)
    result.extend(left_arr[i:])
    # Add remaining elements from the right half (if any)
    result.extend(right_arr[j:])

    return result

def merge_sort_playlist(playlist):
    # Base Case: List with 1 or 0 elements is already sorted
    if len(playlist) <= 1:
        return playlist

    # Recursive Case: Divide the list into two halves
    mid = len(playlist) // 2
    left_half = merge_sort_playlist(playlist[:mid])
    right_half = merge_sort_playlist(playlist[mid:])

    # Merge the sorted halves using the helper function
    return merge_sort_helper(left_half, right_half)

# Example Usage
print(merge_sort_playlist(["Formation", "Crazy in Love", "Halo"])) # Output: ['Crazy in Love', 'Formation', 'Halo']
print(merge_sort_playlist(["Single Ladies", "Love on Top", "Irreplaceable"])) # Output: ['Irreplaceable', 'Love on Top', 'Single Ladies']

# 7.) Longest Substring With at Least K Repeating Characters
# U - Understand
# Share 2 questions you would ask to help understand the question:
# Should the entire substring consist only of characters with a frequency ≥ k?
# Are we allowed to consider overlapping substrings, or only disjoint ones?
# P - Plan
# Write out in plain English what you want to do:
# The task is to find the length of the longest substring where each character occurs at least k times.
# We'll use a divide-and-conquer approach by splitting the string at invalid characters (characters with a frequency less than k).
# If a character does not meet the k frequency requirement, no valid substring can span across it, so we recursively search in the segments divided by these invalid characters.
# Base case: If all characters in a substring occur ≥ k times, we return the length of that substring.
# Function longest_substring(s, k):
# 1. Base Case: If the length of s is less than k, return 0 (no valid substring possible).
# 2. Create a frequency dictionary to store the frequency of each character in s.
# 3. Loop through the string:
#    a. If a character has a frequency less than k, split the string at that character.
#    b. Recursively call longest_substring on each substring segment.
#    c. Return the maximum length from all valid recursive calls.
# 4. If all characters in the string have a frequency ≥ k, return the length of the entire string.
# I - Implement
def longest_substring(s, k):
    # Base Case: If the string is too short, no valid substring can exist
    if len(s) < k:
        return 0

    # Create a frequency dictionary to count occurrences of each character
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1

    # Find the first invalid character (with frequency < k)
    for i, char in enumerate(s):
        if freq[char] < k:
            # Split the string at this character and recursively find the longest valid substring
            left = longest_substring(s[:i], k)
            right = longest_substring(s[i + 1:], k)
            return max(left, right)  # Return the maximum of both segments

    # If all characters meet the frequency requirement, return the length of the entire string
    return len(s)

# Example Usage
print(longest_substring("tatooine", 2))  # Output: 2 (longest substring is 'oo')
print(longest_substring("chewbacca", 2))  # Output: 4 (longest substring is 'acca')

# 8.) Longest Harmonious Subsequence
# U - Understand
# Share 2 questions you would ask to help understand the question:
# Should the subsequence be contiguous, or can it be non-contiguous (scattered within the string)?
# If multiple harmonious subsequences of the same length exist, should we return the first one that appears?
# P - Plan
# Write out in plain English what you want to do:
# We need to find the longest contiguous subsequence in which both the lowercase and uppercase versions of every note in the subsequence appear.
# Divide and conquer is an effective approach:
# If we encounter a character whose counterpart (either uppercase or lowercase) is not in the string, we split the string at that character and recursively search for harmonious subsequences in the left and right segments.
# Base Case: If all characters in a substring are harmonious, return the substring itself.
# Function longest_harmonious_subsequence(notes):
# 1. Base Case: If the input string is empty, return an empty string.
# 2. Create a set of all characters in the input string to help check if a character is harmonious.
# 3. Loop through the input string:
#    a. If a characters counterpart (either uppercase or lowercase) is missing, split the string at that character.
#    b. Recursively search for the longest harmonious subsequence in the left and right segments.
#    c. Return the longer of the two results.
# 4. If all characters in the string are harmonious, return the entire string.
# I - Implement
def longest_harmonious_subsequence(notes):
    # Base Case: If the input string is empty, return an empty string
    if not notes:
        return ""

    # Create a set of all characters in the input for quick lookups
    available_chars = set(notes)

    # Iterate through each character in the input string
    for i, char in enumerate(notes):
        # Check if a lowercase character is missing its uppercase counterpart
        if char.islower():
            if char.upper() not in available_chars:
                # Split the string and search both parts recursively
                left_result = longest_harmonious_subsequence(notes[:i])
                right_result = longest_harmonious_subsequence(notes[i + 1:])
                # Return the longer subsequence
                if len(left_result) >= len(right_result):
                    return left_result
                else:
                    return right_result

        # Check if an uppercase character is missing its lowercase counterpart
        elif char.isupper():
            if char.lower() not in available_chars:
                # Split the string and search both parts recursively
                left_result = longest_harmonious_subsequence(notes[:i])
                right_result = longest_harmonious_subsequence(notes[i + 1:])
                # Return the longer subsequence
                if len(left_result) >= len(right_result):
                    return left_result
                else:
                    return right_result

    # If all characters are harmonious, return the entire string
    return notes

# Example Usage
print(longest_harmonious_subsequence("GadaAg"))  # Output: "aAa"
print(longest_harmonious_subsequence("Bb"))      # Output: "Bb"
print(longest_harmonious_subsequence("c"))       # Output: ""


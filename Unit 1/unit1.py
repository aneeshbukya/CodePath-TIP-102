# Locate Thistles Problem
### U - Understand
# Questions to Ask:
# Are we only looking for exact matches of the string "thistle" or any variations (e.g., case-sensitive)?
# What should be returned if no "thistle" is found in the list?
### P - Plan
# Plan in Plain English:
# I want to check each item in the list. If the item is "thistle", I will record the index (position) of that item. If no "thistle" is found, I will return an empty list.
# Pseudocode:
# Start with an empty list called thistle_lst.
# Loop through each item in the items list.
# If the current item is "thistle", append its index to thistle_lst.
# After the loop finishes, return thistle_lst.
### I - Implement
# Final Python Solution:

def locate_thistles(items):
  thistle_lst = [] 
  for i in range(len(items)):
    if items[i] == "thistle":
      thistle_lst.append(i)
  return thistle_lst

items = ["thistle", "stick", "carrot", "thistle", "eeyore's tail"]
print(locate_thistles(items))

items = ["book", "bouncy ball", "leaf", "red balloon"]
print(locate_thistles(items))


# Shuffle Problem
### U - Understand
# Questions to Ask:
# Are the input lists always guaranteed to have an even number of elements?
# Should the function handle any special types of elements, or is it assumed that all elements are of the same type (like integers or strings)?
#### P - Plan
# Plan in Plain English:
# First, split the cards list into two equal halves.
# Then, interleave the two halves, where we take one element from the first half and one from the second half alternately.
# Finally, return the new shuffled list.
# Pseudocode:
# Get the length n of the first half, which is half the length of the entire cards list.
# Split the cards list into first_half and second_half.
# Create an empty list shuffled to store the shuffled elements.
# Loop through the indices of the first half:
# For each index, append the element from the first_half to shuffled.
# Append the corresponding element from the second_half to shuffled.
# Return the shuffled list.
### I - Implement
# Final Python Solution:
def shuffle(cards):
    n = len(cards) // 2
    first_half = cards[:n]
    second_half = cards[n:]
    
    shuffled = []
    for i in range(n):
        shuffled.append(first_half[i])
        shuffled.append(second_half[i])
    
    return shuffled

# Example usage:
cards = ['Joker', 'Queen', 2, 3, 'Ace', 7]
print(shuffle(cards))  # Expected Output: ['Joker', 3, 'Queen', 'Ace', 2, 7]

cards = [9, 2, 3, 'Joker', 'Joker', 3, 2, 9]
print(shuffle(cards))  # Expected Output: [9, 'Joker', 2, 3, 3, 2, 'Joker', 9]

cards = [10, 10, 2, 2]
print(shuffle(cards))  # Expected Output: [10, 2, 10, 2]


# Local Maximum Problem
### U - Understand
# What is the exact definition of a "local maximum" in this context?
# (This question helps clarify whether the problem requires only a local maximum in the given 3x3 sub-grid or a more specific definition.)
# What are the edge cases or constraints for the grid?
# (This question helps determine if there are any constraints such as grid size limitations or special cases like grids smaller than 3x3.)
### P - Plan
# Write out in plain English what you want to do:
# Iterate through each cell in the grid, except for the edges, as the local maximums are defined within the inner cells.
# For each cell, check the 3x3 matrix centered on that cell.
# Compute the maximum value within this 3x3 matrix.
# Collect the maximum values from each cell and construct the resulting grid of local maximums.
# Translate each sub-problem into pseudocode:
# Iterate through inner cells of the grid:
# Loop i from 1 to n-2
# Loop j from 1 to n-2
# Find the maximum in the 3x3 matrix centered at cell (i, j):
# Compute max_val as the maximum of:
# grid[i-1][j-1]
# grid[i-1][j]
# grid[i-1][j+1]
# grid[i][j-1]
# grid[i][j]
# grid[i][j+1]
# grid[i+1][j-1]
# grid[i+1][j]
# grid[i+1][j+1]
# Append the result to local_maxes:
# Append the computed max_val to the current row's list
# After finishing the inner loop, append the row list to local_maxes
### I - Implement
# Translate the pseudocode into Python and share your final answer:
def local_maximums(grid):
    n = len(grid)
    local_maxes = []
    # Iterate over the inner part of the grid, skipping edges
    for i in range(1, n - 1):
        row_maxes = []
        for j in range(1, n - 1):
            # Find the maximum value in the 3x3 matrix centered at grid[i][j]
            max_val = max(
                grid[i-1][j-1], grid[i-1][j], grid[i-1][j+1],
                grid[i][j-1], grid[i][j], grid[i][j+1],
                grid[i+1][j-1], grid[i+1][j], grid[i+1][j+1]
            )
            row_maxes.append(max_val)
        local_maxes.append(row_maxes)
    
    return local_maxes

grid = [
    [9, 9, 8, 1],
    [5, 6, 2, 6],
    [8, 2, 6, 4],
    [6, 2, 2, 2]
]
print(local_maximums(grid))  # Expected Output: [[9, 9], [8, 6]]

grid = [
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 2, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1]
]
print(local_maximums(grid))  # Expected Output: [[2, 2, 2], [2, 2, 2], [2, 2, 2]]


# Defuse the Bomb Problem
### U - Understand
# How do we handle the circular nature of the array when summing elements?
# (This question ensures we correctly manage the wrap-around when calculating sums.)
# What should be the approach when the length of the array is very small or when k has extreme values?
# (This question helps address edge cases like very small arrays or large values of k.)
#### P - Plan
# Write out in plain English what you want to do:
# First, initialize a result array with zeros.
# If k is positive, iterate through each element in the array and replace it with the sum of the next k elements, accounting for circular indexing.
# If k is negative, convert k to a positive number and then replace each element with the sum of the previous |k| elements, also accounting for circular indexing.
# If k is zero, the result remains an array of zeros.
# Translate each sub-problem into pseudocode:
# If k > 0:
# For each index i in the array:
# Initialize sum to 0.
# For each index j from 1 to k:
# Add the element at position (i + j) % n to sum.
# Set result[i] to sum.
# If k < 0:
# Convert k to positive by setting k = -k.
# For each index i in the array:
# Initialize sum to 0.
# For each index j from 1 to k:
# Add the element at position (i - j) % n to sum.
# Set result[i] to sum.
# If k == 0:
# Initialize the result array with zeros.
#### I - Implement
# Translate the pseudocode into Python and share your final answer:
def defuse(code, k):
    # Determine the length of the circular array
    n = len(code)
    # Initialize the result array with zeros of the same length as the input array
    result = [0] * n  
    
    # Case when k > 0: Compute the sum of the next k elements
    if k > 0:
        for i in range(n):
            # Compute the sum of the next k elements for the current index i
            result[i] = sum(code[(i + j) % n] for j in range(1, k + 1))
            
    # Case when k < 0: Compute the sum of the previous |k| elements
    elif k < 0:
        k = -k  # Convert k to positive for easier handling of previous elements
        for i in range(n):
            # Compute the sum of the previous k elements for the current index i
            result[i] = sum(code[(i - j) % n] for j in range(1, k + 1))
    
    # Case when k == 0: The result is already initialized to zeros, so no additional changes needed

    return result

# Example Usage
print(defuse([5, 7, 1, 4], 3))  # Expected Output: [12, 10, 16, 13]
print(defuse([1, 2, 3, 4], 0))  # Expected Output: [0, 0, 0, 0]
print(defuse([2, 4, 9, 3], -2)) # Expected Output: [12, 5, 6, 13]


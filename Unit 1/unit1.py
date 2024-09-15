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
# Translate the pseudocode into Python 
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

# Eeyore's House Problem
### U - Understand
# How should we handle cases where elements in pile2 are zero?
# (Since k is positive, pile2 should not contain zero. This question ensures we handle cases where the multiplication by zero might need special consideration.)
# What is the expected performance for large inputs, and are there any optimizations we need?
# (This question helps understand if the straightforward approach needs any enhancements for better performance.)
#### P - Plan
# Write out in plain English what you want to do:
# Initialize a counter to keep track of the number of good pairs.
# Iterate over each stick in pile1.
# For each stick in pile1, iterate over each stick in pile2.
# Multiply the stick from pile2 by k to get a product.
# Check if the stick from pile1 is divisible by this product.
# If it is, increment the counter.
# Return the final count of good pairs.
# Translate each sub-problem into pseudocode:
# Initialize the count of good pairs:
# Set count to 0.
# Iterate through each stick in pile1:
# For each stick stick1 in pile1, do the following:
# Iterate through each stick in pile2.
# For each stick stick2 in pile2, compute the product product = stick2 * k`.
# Check if stick1 is divisible by product.
# If stick1 % product == 0, increment count.
# Return the count of good pairs:
# Return count.
#### I - Implement
# Translate the pseudocode into Python 
def good_pairs(pile1, pile2, k):
    # Initialize the count of good pairs
    count = 0
    # Iterate through each stick in pile1
    for stick1 in pile1:
        # Iterate through each stick in pile2
        for stick2 in pile2:
            # Compute the product of stick2 and k
            product = stick2 * k
            # Check if stick1 is divisible by the product
            if stick1 % product == 0:
                count += 1
    return count

# Example Usage
pile1 = [1, 3, 4]
pile2 = [1, 3, 4]
k = 1
print(good_pairs(pile1, pile2, k))  # Expected Output: 5

pile1 = [1, 2, 4, 12]
pile2 = [2, 4]
k = 3
print(good_pairs(pile1, pile2, k))  # Expected Output: 2

# Exposing Superman Problem
### U - Understand
# What specific conditions must be met for someone to be Superman?
# Superman must trust no one (i.e., Superman is not in any trust[i][0]).
# Everyone else must trust Superman (i.e., Superman must appear in every trust[i][1] except themselves).
# How do we efficiently check these conditions with the given trust data?
# We need to track the number of people who trust each individual and also ensure that an individual does not trust anyone.
### P - Plan
# Write out in plain English what you want to do:
# Create two lists: one to count the number of people who trust each individual and another to track if someone trusts another.
# Iterate through the trust list to update these counts.
# Identify if there is exactly one person who is trusted by everyone else and does not trust anyone.
# Translate each sub-problem into pseudocode:
# Initialize two lists:
# trust_count to count how many people trust each individual.
# other_trust_count to track if an individual trusts anyone.
# Update counts from the trust list:
# For each pair [a, b] in trust, increment trust_count[b] and mark other_trust_count[a] as True.
# Check for the Superman candidate:
# Iterate through the trust_count and other_trust_count lists.
# Find if there is exactly one person who is trusted by n - 1 people and does not trust anyone (other_trust_count is False for that individual).
### I - Implement
# Translate the pseudocode into Python 
def expose_superman(trust, n):
    # Initialize lists to track the number of trusts and if someone trusts anyone
    trust_count = [0] * (n + 1)  # Index 0 will not be used
    other_trust_count = [False] * (n + 1)
    
    # Process the trust relationships
    for a, b in trust:
        trust_count[b] += 1  # b is trusted by one more person
        other_trust_count[a] = True  # a trusts someone
    
    # Identify the candidate for Superman
    for i in range(1, n + 1):
        if trust_count[i] == n - 1 and not other_trust_count[i]:
            return i  # Found Superman
    
    return -1  # No valid candidate found

# Example Usage
print(expose_superman([[1, 2]], 2))  # Expected Output: 2
print(expose_superman([[1, 3], [2, 3]], 3))  # Expected Output: 3
print(expose_superman([[1, 3], [2, 3], [3, 1]], 3))  # Expected Output: -1

# Merge Intervals Problem
### U - Understand
# How do we determine if two intervals overlap?
# Two intervals [a, b] and [c, d] overlap if a <= d and b >= c.
# How do we efficiently merge overlapping intervals?
# We need to first sort the intervals based on their start times, and then iterate through them to merge any overlapping intervals.
### P - Plan
# Write out in plain English what you want to do:
# Sort the intervals based on their starting times.
# Initialize an empty list to store merged intervals.
# Iterate through the sorted intervals and merge any overlapping intervals.
# Add the merged intervals to the result list.
# Return the result list of merged intervals.
# Translate each sub-problem into pseudocode:
# Sort intervals by their start time:
# Use a sorting algorithm to sort the intervals array based on the start of each interval.
# Initialize the merged intervals list:
# Create an empty list to keep track of merged intervals.
# Iterate through the sorted intervals:
# For each interval, check if it overlaps with the last interval in the merged list.
# If it overlaps, merge the intervals by updating the end time of the last interval in the merged list.
# If it does not overlap, simply add the current interval to the merged list.
# Return the list of merged intervals:
# After processing all intervals, return the merged intervals list.
### I - Implement
# Translate the pseudocode into Python 
def merge_intervals(intervals):
    if not intervals:
        return []
    # Step 1: Sort intervals based on the starting time
    intervals.sort(key=lambda x: x[0])

    # Step 2: Initialize the list to hold merged intervals
    merged_intervals = []

    # Start with the first interval
    current_interval = intervals[0]
    
    # Iterate through the sorted intervals
    for interval in intervals[1:]:
        # Check if the current interval overlaps with the interval to be merged
        if interval[0] <= current_interval[1]:
            # Merge the intervals by extending the end of the current interval
            current_interval[1] = max(current_interval[1], interval[1])
        else:
            # No overlap, add the current interval to the merged list
            merged_intervals.append(current_interval)
            # Update the current interval to the new interval
            current_interval = interval

    # Add the last interval after the loop
    merged_intervals.append(current_interval)

    return merged_intervals

# Example Usage
print(merge_intervals([[1, 3], [2, 6], [8, 10], [15, 18]]))  # Expected Output: [[1, 6], [8, 10], [15, 18]]
print(merge_intervals([[1, 4], [4, 5]]))  # Expected Output: [[1, 5]]

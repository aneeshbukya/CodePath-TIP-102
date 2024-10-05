# Find Closest NFT Values
### U - Understand
# What happens if there are no NFT values either below or above the budget?
# Answer: If the budget is lower than the smallest value or higher than the largest value, we should return None for the missing value (either closest below or closest above).
# What is the expected output if the budget matches an NFT value exactly?
# Answer: If the budget matches an NFT value exactly, the same value should be returned for both the closest below and closest above NFT values.
### P - Plan
# Goal:
# We need to find two NFT values from a sorted list: one that is the closest below or equal to the budget, and one that is the closest above or equal to the budget.

# Initial Setup:
# We'll initialize two pointers, left and right, to the start and end of the list, respectively. We will also track two variables, closest_below and closest_above, both initialized to None.
# Binary Search Approach:
# We use a binary search to quickly narrow down the possible closest values.
# At each step, calculate the middle index (mid).
# If the middle NFT value (nft_values[mid]) is equal to the budget, return it as both the closest below and closest above values.
# If the middle value is less than the budget, it is a candidate for closest_below, and we move the left pointer to mid + 1 to look for higher values.
# If the middle value is greater than the budget, it becomes a candidate for closest_above, and we move the right pointer to mid - 1 to look for lower values.
# Edge Cases:
# If no value is found below the budget, closest_below will remain None.
# If no value is found above the budget, closest_above will remain None.
###### I - Implement
#### Pseudocode:

# Initialize left = 0, right = len(nft_values) - 1.
# Initialize closest_below = None and closest_above = None.
# Use a binary search (while left <= right):
# Calculate mid = (left + right) // 2.
# If nft_values[mid] == budget, return (nft_values[mid], nft_values[mid]).
# If nft_values[mid] < budget, update closest_below = nft_values[mid] and move left = mid + 1.
# If nft_values[mid] > budget, update closest_above = nft_values[mid] and move right = mid - 1.
# Return (closest_below, closest_above) after exiting the loop.
def find_closest_nft_values(nft_values, budget):
    left = 0
    right = len(nft_values) - 1
    closest_below = None
    closest_above = None

    while left <= right:
        mid = (left + right) // 2

        # Exact match case
        if nft_values[mid] == budget:
            return (nft_values[mid], nft_values[mid])

        # If the mid value is less than the budget, it's a candidate for closest_below
        elif nft_values[mid] < budget:
            closest_below = nft_values[mid]
            left = mid + 1  # Look in the right half

        # If the mid value is greater than the budget, it's a candidate for closest_above
        else:
            closest_above = nft_values[mid]
            right = mid - 1  # Look in the left half

    # Return the closest below and above values
    return (closest_below, closest_above)

# Example Usage
nft_values = [3.5, 5.4, 7.2, 9.0, 10.5]
nft_values_2 = [2.0, 4.5, 6.3, 7.8, 12.1]
nft_values_3 = [1.0, 2.5, 4.0, 6.0, 9.0]

print(find_closest_nft_values(nft_values, 8.0))   # Expected output: (7.2, 9.0)
print(find_closest_nft_values(nft_values_2, 6.5))  # Expected output: (6.3, 7.8)
print(find_closest_nft_values(nft_values_3, 3.0))  # Expected output: (2.5, 4.0)

# Analyze Meme Trends
#### U - Understand
# We are tasked with analyzing the trends of various memes based on their repost counts over a specific time range. The goal is to identify the meme that has the highest average repost count over the given time range (start_day to end_day, inclusive).

# What is the input?
# A list of memes, where each meme is represented as a dictionary with keys "name" and "reposts".
# The time range is defined by two integers: start_day and end_day.
# What is the output?
# The name of the meme with the highest average repost count over the specified time range.
# What happens in case of a tie?
# If multiple memes have the same average repost count, return the meme that appears first in the list.
# What is the size of the dataset?
# The list could contain several memes, and each meme has a daily repost count list that may span many days. The start_day and end_day define the time range for which we calculate the average repost count.
###### P - Plan
# Goal:
# For each meme in the list, calculate the average repost count for the given time range (start_day to end_day).
# Return the name of the meme with the highest average repost count.
# Approach:
# Iterate over each meme.
# For each meme, extract the repost counts from the specified time range (start_day to end_day).
# Calculate the average of these repost counts.
# Keep track of the meme with the highest average repost count. If there’s a tie, we will keep the first one encountered.
# Edge cases:
# If the list of memes is empty, return None.
# Ensure that the start_day and end_day are within the valid index range of each meme's repost list.
##### I - Implement
# Pseudocode:

# Initialize variables to keep track of the meme with the highest average repost count (max_average) and the corresponding meme's name (trending_meme).
# For each meme in the list:
# Extract the repost counts for the time range from start_day to end_day.
# Calculate the average repost count.
# If this average is higher than the current max_average, update max_average and set the trending_meme to the current meme’s name.
# Return the trending_meme.
def find_trending_meme(memes, start_day, end_day):
    # Initialize tracking variables for the highest average reposts and trending meme name
    max_average = float('-inf')  # Start with the lowest possible average
    trending_meme = None

    # Iterate over each meme in the list
    for meme in memes:
        name = meme["name"]
        reposts = meme["reposts"]

        # Calculate the average reposts in the range [start_day, end_day]
        reposts_in_range = reposts[start_day:end_day + 1]  # Extract the slice
        average_reposts = sum(reposts_in_range) / len(reposts_in_range)  # Compute the average

        # Update the trending meme if the current average is higher than max_average
        if average_reposts > max_average:
            max_average = average_reposts
            trending_meme = name

    # Return the name of the meme with the highest average repost count
    return trending_meme

# Example Usage
memes = [
    {"name": "Distracted boyfriend", "reposts": [5, 3, 2, 7, 6]},
    {"name": "Dogecoin to the moon!", "reposts": [2, 4, 6, 8, 10]},
    {"name": "One does not simply walk into Mordor", "reposts": [3, 3, 5, 4, 2]}
]

memes_2 = [
    {"name": "Surprised Pikachu", "reposts": [2, 1, 4, 5, 3]},
    {"name": "This is fine", "reposts": [3, 5, 2, 6, 4]},
    {"name": "Expanding brain", "reposts": [4, 2, 1, 4, 2]}
]

memes_3 = [
    {"name": "Y U No?", "reposts": [1, 2, 1, 2, 1]},
    {"name": "Philosoraptor", "reposts": [3, 1, 3, 1, 3]}
]

print(find_trending_meme(memes, 1, 3))   # Output: Dogecoin to the moon!
print(find_trending_meme(memes_2, 0, 2))  # Output: This is fine
print(find_trending_meme(memes_3, 2, 4))  # Output: Philosoraptor


# Fabric Roll Organizer
### U - Understand
# We are tasked with organizing fabric rolls into pairs such that the difference between the lengths of each pair is minimized. If there is an odd number of rolls, one roll will be left out and returned separately.

# What is the input?
# A list of fabric roll lengths (positive integers).
# What is the output?
# A list of pairs of fabric roll lengths with the smallest possible difference between them.
# If there is an odd number of fabric rolls, return the last roll separately.
# What should we consider?
# Minimize the difference between the lengths of each pair.
# Sorting the fabric rolls will likely help in minimizing differences between consecutive lengths.
#### P - Plan
# Approach:
# Sort the fabric rolls in ascending order.
# Pair consecutive rolls after sorting since adjacent rolls in a sorted list will have the smallest difference.
# If there is an odd number of rolls, leave the last one out and return it separately.
# Steps:
# Sort the fabric rolls.
# Initialize an empty list to store the pairs.
# Iterate through the sorted list, pairing adjacent rolls.
# If there is an odd number of rolls, store the last roll separately.
# Edge cases:
# If the list has only one roll, return the roll without pairing.
# Ensure that the solution works for both even and odd numbers of rolls.
##### I - Implement
# Pseudocode:

# Sort the fabric_rolls list.
# Initialize an empty list pairs to store the pairs of rolls.
# Iterate over the sorted fabric rolls:
# For each pair of consecutive elements, add them as a tuple to pairs.
# If there’s an odd roll left, add it separately at the end.
# Return the list of pairs and the remaining roll if any.
def organize_fabric_rolls(fabric_rolls):
    fabric_rolls.sort()  # Sort the fabric rolls by length
    pairs = []

    while len(fabric_rolls) > 1: # Pair consecutive rolls
        smallest = fabric_rolls.pop(0) # Remove the smallest roll
        closest = fabric_rolls.pop(0) # Remove the closest roll to the smallest
        pairs.append((smallest, closest)) # Pair the two rolls

    if fabric_rolls: # If there's a roll left
        return pairs + [fabric_rolls[0]] # Add the remaining roll to the pairs
    else:  # If all rolls are paired
        return pairs # Return the pairs

# Example Usage
fabric_rolls = [15, 10, 25, 30, 22]
fabric_rolls_2 = [5, 8, 10, 7, 12, 14]
fabric_rolls_3 = [40, 10, 25, 15, 30]

print(organize_fabric_rolls(fabric_rolls))   # Output: [(10, 15), (22, 25), 30]
print(organize_fabric_rolls(fabric_rolls_2))  # Output: [(5, 7), (8, 10), (12, 14)]
print(organize_fabric_rolls(fabric_rolls_3))  # Output: [(10, 15), (25, 30), 40]

# Optimizing Break Times
### U - Understand
# Q: What is the structure of the input?

# A: The input is a list of integers representing the duration of each break in minutes and a target time in minutes.
# Q: What is the output?

# A: The output is a tuple containing two integers that represent the pair of break durations whose sum is closest to the target time.
# Q: What should the function return if there are fewer than two breaks?

# A: The function should return an empty tuple.
# Q: What if there are multiple pairs with the same closest sum?

# A: The function should return the pair with the smallest break durations.
### P - Plan
# 1) If `break_times` has fewer than 2 elements, return an empty tuple.
# 2) Sort the `break_times` list in ascending order.
# 3) Initialize two pointers: `left_pointer` at the start of the list and `right_pointer` at the end.
# 4) Initialize variables `closest_sum` to infinity and `best_pair` to an empty tuple.
# 5) While `left_pointer` is less than `right_pointer`:
#    a) Calculate `current_sum` as the sum of the values at `left_pointer` and `right_pointer`.
#    b) If `current_sum` is closer to `target` than `closest_sum`, update `closest_sum` and `best_pair`.
#    c) If `current_sum` equals `closest_sum` but the new pair has smaller values, update `best_pair`.
#    d) If `current_sum` is less than `target`, increment `left_pointer`.
#    e) If `current_sum` is greater than or equal to `target`, decrement `right_pointer`.
# 6) Return `best_pair`.

# Common Mistakes**

# - Forgetting to check if there are fewer than two elements in `break_times`.
# - Not handling ties correctly when multiple pairs have the same closest sum.
def find_best_break_pair(break_times, target):
    if len(break_times) < 2:
        return ()

    break_times.sort()
    left_pointer = 0
    right_pointer = len(break_times) - 1
    closest_sum = float('inf')
    best_pair = ()

    while left_pointer < right_pointer:
        current_sum = break_times[left_pointer] + break_times[right_pointer]

        if abs(target - current_sum) < abs(target - closest_sum):
            closest_sum = current_sum
            best_pair = (break_times[left_pointer], break_times[right_pointer])
        elif abs(target - current_sum) == abs(target - closest_sum):
            # Update if the new pair has smaller values, or if the current sum is closer
            if not best_pair or (break_times[left_pointer] < best_pair[0] or break_times[right_pointer] < best_pair[1]):
                best_pair = (break_times[left_pointer], break_times[right_pointer])

        if current_sum < target:
            left_pointer += 1
        else:
            right_pointer -= 1

    return best_pair
# Example Usage
break_times = [10, 20, 35, 40, 50]
break_times_2 = [5, 10, 25, 30, 45]
break_times_3 = [15, 25, 35, 45]
break_times_4 = [30]

print(find_best_break_pair(break_times, 60))   # Output: (20, 40)
print(find_best_break_pair(break_times_2, 50))  # Output: (5, 45)
print(find_best_break_pair(break_times_3, 70))  # Output: (25, 45)
print(find_best_break_pair(break_times_4, 60))  # Output: ()

# Track Popular Destinations
### U - Understand
# We need to identify the most frequently visited destination from a list of visits, along with the number of times it was visited. If two or more destinations have the same visit count, we will return the one that was visited most recently.

# Input:

# A list of tuples, where each tuple contains a destination (string) and a timestamp (string) in the format "YYYY-MM-DD".
# Output:

# A tuple with the name of the most popular destination and the total number of times it was visited.
# ###P - Plan
# Data Structure: Use a dictionary to count the number of visits for each destination. The keys will be the destination names, and the values will be a tuple containing the visit count and the latest visit date.
# Processing Steps:
# Initialize an empty dictionary to store the counts and latest visit dates.
# Iterate through the list of visits:
# For each destination, update the visit count.
# Compare and update the latest visit date if the current visit is later than the recorded date.
# After processing all visits, determine the destination with the highest visit count. In case of a tie, choose the one with the most recent visit.
# Return the Result: Return a tuple containing the name of the destination and the total number of visits.
##### I - Implement
def most_popular_destination(visits):
    # Dictionary to hold visit counts and latest visit dates
    destination_count = {}
    
    # Process each visit
    for destination, date in visits:
        if destination not in destination_count:
            destination_count[destination] = (0, "")
        
        # Increment visit count
        count, latest_visit = destination_count[destination]
        count += 1
        
        # Update latest visit date if the current one is later
        if date > latest_visit:
            latest_visit = date
            
        # Update the dictionary
        destination_count[destination] = (count, latest_visit)

    # Initialize variables to track the most popular destination
    most_popular = None
    max_count = 0
    latest_visit = ""

    # Determine the most popular destination
    for destination, (count, latest) in destination_count.items():
        if (count > max_count) or (count == max_count and latest > latest_visit):
            most_popular = destination
            max_count = count
            latest_visit = latest
    
    return (most_popular, max_count)

# Example Usage
visits = [
    ("Paris", "2024-07-15"),
    ("Tokyo", "2024-08-01"),
    ("Paris", "2024-08-05"),
    ("New York", "2024-08-10"),
    ("Tokyo", "2024-08-15"),
    ("Paris", "2024-08-20"),
]
print(most_popular_destination(visits))  # Output: ('Paris', 3)

visits_2 = [
    ("London", "2024-06-01"),
    ("Berlin", "2024-06-15"),
    ("London", "2024-07-01"),
    ("Berlin", "2024-07-10"),
    ("London", "2024-07-15"),
]
print(most_popular_destination(visits_2))  # Output: ('London', 3)

visits_3 = [
    ("Sydney", "2024-05-01"),
    ("Dubai", "2024-05-15"),
    ("Sydney", "2024-05-20"),
    ("Dubai", "2024-06-01"),
    ("Dubai", "2024-06-15"),
]
print(most_popular_destination(visits_3))  # Output: ('Dubai', 3)

# Find Longest Consecutive Listen Gaps
### U - Understand
# We need to find the longest gap between consecutive podcast listens. The timestamps are given in minutes since midnight and are sorted in ascending order. The goal is to compute the difference between consecutive timestamps and return the largest difference.
# Input:
# A list of timestamps (integers) representing the minutes since midnight, sorted in ascending order.
# Output:
# The largest gap (difference) between consecutive timestamps.
### P - Plan
# Handle Edge Case: If the list has fewer than two timestamps, return 0 since there's no gap to calculate.
# Compute Gaps:
# Initialize a variable max_gap to keep track of the largest difference between consecutive timestamps.
# Loop through the list, calculate the difference between each consecutive pair of timestamps, and update max_gap if the current difference is larger.
# Return the Largest Gap: After looping through all consecutive pairs, return the value of max_gap.
### I - Implement
def find_longest_gap(timestamps):
    # Initialize variables to keep track of the maximum gap
    max_gap = 0
    n = len(timestamps)

    # Two-pointer approach: start with two pointers
    i, j = 0, 1

    while j < n:
        # Calculate the gap between the current pair of timestamps
        gap = timestamps[j] - timestamps[i]

        # Update max_gap if the current gap is larger
        if gap > max_gap:
            max_gap = gap

        # Move the pointers to the next pair of timestamps
        i += 1
        j += 1

    return max_gap
timestamps1 = [30, 50, 70, 100, 120, 150]
print(find_longest_gap(timestamps1))  # Output: 30

timestamps2 = [10, 20, 30, 50, 60, 90]
print(find_longest_gap(timestamps2))  # Output: 30

timestamps3 = [5, 10, 15, 25, 35, 45]
print(find_longest_gap(timestamps3))  # Output: 10

# Analyze Storyline Continuity
### U - Understand
# We need to verify the chronological order of scenes in a storyline based on their timestamps. The goal is to check whether the timestamps of consecutive scenes are strictly increasing. If they are not, it indicates a gap in the storyline continuity.
# Input:
# A list of scene records, where each record is a dictionary containing a "scene" (string) and a "timestamp" (integer).
# Output:
# Return True if all timestamps are in increasing order, otherwise return False.
# P - Plan
# Handle Edge Case: If the list of scenes has fewer than two records, return True because there can't be any gaps.
# Check Timestamps:
# Initialize a loop that iterates through the list of scenes.
# Compare the timestamp of the current scene with the timestamp of the previous scene.
# If any timestamp is found to be less than or equal to the previous timestamp, return False.
# Return True: If the loop completes without finding any out-of-order timestamps, return True.
### I - Implement
def analyze_storyline_continuity(scenes):
    for i in range(1, len(scenes)): # Start from the second scene
        if scenes[i]['timestamp'] < scenes[i-1]['timestamp']: # Check for decreasing timestamps
            return False # Return False if the timestamps are not strictly increasing
    return True # Return True if all timestamps are in increasing order
scenes1 = [
    {"scene": "The hero enters the dark forest.", "timestamp": 1},
    {"scene": "A mysterious figure appears.", "timestamp": 2},
    {"scene": "The hero faces his fears.", "timestamp": 3},
    {"scene": "The hero finds a hidden treasure.", "timestamp": 4},
    {"scene": "An eerie silence fills the air.", "timestamp": 5}
]

continuity1 = analyze_storyline_continuity(scenes1)
print(continuity1)  # Output: True

scenes2 = [
    {"scene": "The spaceship lands on an alien planet.", "timestamp": 3},
    {"scene": "A strange creature approaches.", "timestamp": 2},
    {"scene": "The crew explores the new world.", "timestamp": 4},
    {"scene": "The crew encounters hostile forces.", "timestamp": 5},
    {"scene": "The crew makes a narrow escape.", "timestamp": 6}
]

continuity2 = analyze_storyline_continuity(scenes2)
print(continuity2)  # Output: False

# Manage Expiration Dates
### U - Understand
# We need to verify whether the food items in a pantry are ordered correctly by their expiration dates. The oldest expiration date should be at the top of the stack, meaning we need to check if the list of expiration dates is in ascending order.

# Input:

# A list of tuples, where each tuple contains a food item (string) and its expiration date (string in the format "YYYY-MM-DD").
# Output:

# Return True if the items are ordered correctly (oldest expiration date at the top of the stack); otherwise, return False.
### P - Plan
# Extract Expiration Dates: Create a list that contains only the expiration dates from the input list of tuples.
# Check Order:
# Iterate through the list of expiration dates.
# Compare each date with the next one to ensure they are in ascending order.
# If any date is found to be later than the next date, return False.
# Return True: If the loop completes without finding any out-of-order dates, return True.
### I - Implement
def check_expiration_order(expiration_dates):
    # Initialize an empty stack
    expiration_stack = []

    # Push all expiry dates onto the stack
    for item, date in expiration_dates:
        expiration_stack.append(date)

    # Initialize previous date with the first element popped from the stack
    previous_date = expiration_stack.pop()

    # Process each date in the stack (reverse order)
    while expiration_stack:
        current_date = expiration_stack.pop()
        # Check if the current date is earlier than or equal to the previous date
        if current_date > previous_date:
            return False
        # Update the previous date for the next comparison
        previous_date = current_date

    return True
expiration_dates_1 = [
    ("Milk", "2024-08-05"),
    ("Bread", "2024-08-10"),
    ("Eggs", "2024-08-12"),
    ("Cheese", "2024-08-15")
]

expiration_dates_2 = [
    ("Milk", "2024-08-05"),
    ("Bread", "2024-08-12"),
    ("Eggs", "2024-08-10"),
    ("Cheese", "2024-08-15")
]

print(check_expiration_order(expiration_dates_1))  # Output: True
print(check_expiration_order(expiration_dates_2))  # Output: False

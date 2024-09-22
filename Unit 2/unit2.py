#  Sort the Performers
### U - Understand
# Two questions to help understand the problem:
# What should happen if two performers have the same performance time? Should their names be returned in a specific order?
# Can performer names repeat, or should all names be unique?
### P - Plan
# In plain English:
# I want to create a dictionary where the keys are performer names, and the values are their performance times. Then, I will sort the dictionary by the performance times in descending order, and return the sorted list of performer names.
# Translate into pseudocode:
# Create a dictionary from the performer names and their performance times.
# Sort the dictionary by values (performance times) in descending order.
# Return the sorted performer names.
### I - Implement
def sort_performers(performer_names, performance_times):
    # Create a dictionary with performer names as keys and performance times as values
    performer_dict = {performer_names[i]: performance_times[i] for i in range(len(performer_names))}
    
    # Sort the dictionary by values (performance times) in descending order
    sorted_performers = sorted(performer_dict, key=performer_dict.get, reverse=True)
    
    return sorted_performers

# Example Usage
performer_names1 = ["Mary", "John", "Emma"]
performance_times1 = [180, 165, 170]

performer_names2 = ["Alice", "Bob", "Bob"]
performance_times2 = [155, 185, 150]

print(sort_performers(performer_names1, performance_times1))  # Output: ["Mary", "Emma", "John"]
print(sort_performers(performer_names2, performance_times2))  # Output: ["Bob", "Alice"]

# Final Communication Hub.
### U - Understand
# Question 1: Is it guaranteed that there is exactly one final hub with no outgoing path?
# Question 2: Can two hubs have the same name, or are all hub names unique?
### P - Plan
# Plan in plain English:
# We want to find the hub that only receives communication (i.e., it only appears as the second element in the path pairs) but doesn't send communication to any other hub (i.e., it does not appear as the first element in any path). This final hub will not have any outgoing paths.
# Pseudocode:
# Step 1: Extract all the hubs that have outgoing paths (the first element in each path).
# Step 2: Extract all the hubs that have incoming paths (the second element in each path).
# Step 3: The final hub will be in the set of hubs with incoming paths but not in the set of hubs with outgoing paths.
# Step 4: Return this hub.
### I - Implement
def find_final_hub(paths):
    # Step 1: Extract hubs with outgoing paths (first element of each path)
    outgoing_hubs = {path[0] for path in paths}
    # print(outgoing_hubs)
    # Step 2: Extract hubs with incoming paths (second element of each path)
    incoming_hubs = {path[1] for path in paths}
    # print(incoming_hubs)
    # Step 3: The final hub will be in incoming_hubs but not in outgoing_hubs
    print(outgoing_hubs), print(incoming_hubs)
    final_hub = incoming_hubs - outgoing_hubs
    # print(final_hub)
    # # Step 4: Return the only element in final_hub
    return final_hub.pop()

### Example Usage:

paths1 = [["Earth", "Mars"], ["Mars", "Titan"], ["Titan", "Europa"]]
paths2 = [["Alpha", "Beta"], ["Gamma", "Alpha"], ["Beta", "Delta"]]
paths3 = [["StationA", "StationZ"]]

print(find_final_hub(paths1)) 
# Expected Output: "Europa"

print(find_final_hub(paths2)) 
# Expected Output: "Delta"

print(find_final_hub(paths3)) 
# Expected Output: "StationZ"


# Counting Pirates' Action Minutes.
### U - Understand
# Question 1: Can a pirate perform multiple actions in the same minute, and should that minute only be counted once for that pirate?
# Question 2: Are all pirate IDs guaranteed to be within the range 0 to k-1?
### P - Plan
# Plan in plain English:
# We want to count how many unique minutes each pirate performed an action in (PAM). Then, we need to create an array where the value at each index j represents how many pirates have exactly j unique action minutes.
# Steps:

# Step 1: Use a dictionary to keep track of each pirate's unique action minutes using a set (to ensure minutes are counted once per pirate).
# Step 2: For each pirate, count their unique action minutes.
# Step 3: Create an answer array of size k, where each element answer[j] holds the number of pirates with exactly j unique action minutes.
# Pseudocode:
# Step 1: Initialize a dictionary to map pirate IDs to sets of unique action minutes.
# Step 2: For each log entry, add the action minute to the corresponding pirate’s set.
# Step 3: Initialize an array answer of size k with all zeros.
# Step 4: Count the unique action minutes for each pirate and increment the corresponding index in answer.
# Step 5: Return the answer array.
### I - Implement
def counting_pirates_action_minutes(logs, k):
    # Step 1: Initialize a dictionary to map pirate IDs to sets of unique action minutes
    pirate_actions = {}

    # Step 2: Add the unique action minutes for each pirate
    for pirate_id, time in logs:
        if pirate_id not in pirate_actions:
            pirate_actions[pirate_id] = set()
        pirate_actions[pirate_id].add(time)

    # Step 3: Initialize the answer array with zeros of size k
    answer = [0] * k

    # Step 4: Count the number of pirates with each unique PAM count
    for unique_minutes in pirate_actions.values():
        pam_count = len(unique_minutes)
        if pam_count <= k:  # Only count if it's within the range
            answer[pam_count - 1] += 1  # Decrement by 1 for 0-based indexing

    # Step 5: Return the answer array
    return answer

### Example Usage:

logs1 = [[0, 5], [1, 2], [0, 2], [0, 5], [1, 3]]
k1 = 5
logs2 = [[1, 1], [2, 2], [2, 3]]
k2 = 4

print(counting_pirates_action_minutes(logs1, k1)) 
# Expected Output: [0, 2, 0, 0, 0]
print(counting_pirates_action_minutes(logs2, k2)) 
# Expected Output: [1, 1, 0, 0]


# Time Portal Usage.
### U - Understand
# Question 1: Are the time_used values guaranteed to be unique across different portals, or can multiple portals have actions at the same time?
# Question 2: Should the portal_number and time_used be sorted numerically and chronologically, respectively, in the output table?
# P - Plan
# Plan in plain English:
# We need to construct a display table that shows how many times each portal was used at each specific time. The table should have a header row containing the sorted unique times, followed by rows for each portal that include how many times the portal was used at each time. The first column should list the portal numbers, and the rest of the columns should list the counts for each time.
# Steps:
# Step 1: Extract all unique times from the usage_records and sort them chronologically.
# Step 2: Extract all portal numbers and sort them numerically.
# Step 3: Initialize a table where each row corresponds to a portal and its usage counts for each time.
# Step 4: For each entry in usage_records, increment the count for the corresponding portal and time.
# Step 5: Return the display table, starting with the header row.
### Pseudocode:
# Step 1: Extract and sort unique times.
# Step 2: Extract and sort unique portal numbers.
# Step 3: Initialize a table with the portal numbers in the first column and zeros in the remaining columns for each unique time.
# Step 4: Loop through each usage_record and increment the usage count for the appropriate portal and time.
# Step 5: Return the table, starting with the header.
### I - Implement
def display_time_portal_usage(usage_records):
    # Step 1: Extract and sort unique times
    times = sorted({record[2] for record in usage_records})
    
    # Step 2: Extract and sort unique portal numbers
    portals = sorted({record[1] for record in usage_records}, key=int)
    
    # Step 3: Initialize the table with the header row
    table = [['Portal'] + times]
    
    # Step 4: Create a dictionary to store counts of portal usages by time
    portal_usage = {portal: {time: 0 for time in times} for portal in portals}
    
    # Step 5: Fill in the usage counts based on usage_records
    for traveler, portal, time in usage_records:
        portal_usage[portal][time] += 1
    
    # Step 6: Construct the table by adding the rows for each portal
    for portal in portals:
        row = [portal] + [str(portal_usage[portal][time]) for time in times]
        table.append(row)
    
    # Step 7: Return the final table
    return table

### Example Usage:

usage_records1 = [["David","3","10:00"],
                  ["Corina","10","10:15"],
                  ["David","3","10:30"],
                  ["Carla","5","11:00"],
                  ["Carla","5","10:00"],
                  ["Rous","3","10:00"]]

usage_records2 = [["James","12","11:00"],
                  ["Ratesh","12","11:00"],
                  ["Amadeus","12","11:00"],
                  ["Adam","1","09:00"],
                  ["Brianna","1","09:00"]]

usage_records3 = [["Laura","2","08:00"],
                  ["Jhon","2","08:15"],
                  ["Melissa","2","08:30"]]

print(display_time_portal_usage(usage_records1))
# Expected Output:
# [['Portal','10:00','10:15','10:30','11:00'],['3','2','0','1','0'],['5','1','0','0','1'],['10','0','1','0','0']]

print(display_time_portal_usage(usage_records2))
# Expected Output:
# [['Portal','09:00','11:00'],['1','2','0'],['12','0','3']]

print(display_time_portal_usage(usage_records3))
# Expected Output:
# [['Portal','08:00','08:15','08:30'],['2','1','1','1']]

# Equivalent Species Pairs.
### U - Understand
# Question 1: How do we treat pairs where the species are the same, such as [a, a]? Are they equivalent to other pairs?
# Question 2: Should we always consider a pair [a, b] equivalent to [b, a], regardless of the order?
### P - Plan
# Plan in plain English:
# We need to count how many species pairs are equivalent to each other. The order of species in a pair does not matter, so [a, b] is the same as [b, a]. To efficiently count equivalent pairs:
# Step 1: Sort each pair so that the smaller species always comes first. This way, [a, b] and [b, a] will always look the same after sorting.
# Step 2: Store the sorted pairs in a dictionary to count how often each unique pair occurs.
# Step 3: For each pair that occurs more than once, compute the number of equivalent pairs using combinations (i.e., if a pair occurs n times, the number of equivalent pairs is n * (n - 1) / 2).
# Step 4: Return the total number of equivalent pairs.
# Pseudocode:
# Step 1: Initialize a dictionary to store the frequency of each sorted pair.
# Step 2: Loop through the species_pairs, sort each pair, and update the count in the dictionary.
# Step 3: Initialize a variable equiv_pairs to store the total number of equivalent pairs.
# Step 4: For each pair in the dictionary with a count greater than 1, calculate the number of equivalent pairs using the formula n * (n - 1) / 2.
# Step 5: Return equiv_pairs.
### I - Implement
def num_equiv_species_pairs(species_pairs):
    # Step 1: Initialize a dictionary to store the frequency of each sorted pair
    pair_count = {}
    
    # Step 2: Loop through the species pairs, sort each one, and update the count in the dictionary
    for pair in species_pairs:
        sorted_pair = tuple(sorted(pair))  # Sort the pair to handle (a, b) and (b, a)
        if sorted_pair in pair_count:
            pair_count[sorted_pair] += 1
        else:
            pair_count[sorted_pair] = 1
    
    # Step 3: Initialize a variable to store the total number of equivalent pairs
    equiv_pairs = 0
    
    # Step 4: For each pair in the dictionary with a count > 1, calculate equivalent pairs
    for count in pair_count.values():
        if count > 1:
            equiv_pairs += count * (count - 1) // 2  # Use the combination formula for n pairs
    
    # Step 5: Return the total number of equivalent pairs
    return equiv_pairs

# Example Usage:

species_pairs1 = [[1, 2], [2, 1], [3, 4], [5, 6]]
species_pairs2 = [[1, 2], [1, 2], [1, 1], [1, 2], [2, 2]]

print(num_equiv_species_pairs(species_pairs1))  # Output: 1
print(num_equiv_species_pairs(species_pairs2))  # Output: 3

# Finding Common Tourist Attractions with Least Travel Time.

# U - Understand
# Question 1: How do we define "travel time" in this context? Is it simply the sum of indices from both lists?
# Question 2: If multiple attractions have the same least travel time, should all of them be included in the result, or is there any preference?
# P - Plan
# Plan in plain English:
# We need to find common tourist attractions from two lists and determine which of these attractions have the minimum total travel time, defined as the sum of their indices from both lists.
# Step 1: Create a set for tourist_list1 to quickly identify common attractions.
# Step 2: Initialize variables to keep track of the minimum travel time and a list to store attractions with that travel time.
# Step 3: Loop through tourist_list2, and for each attraction, check if it exists in tourist_list1.
# Step 4: For each common attraction found, calculate the travel time and update the minimum travel time and results accordingly.
# Step 5: Return the list of attractions with the least total travel time.
# Pseudocode:
# Step 1: Create a set from tourist_list1.
# Step 2: Initialize min_travel_time to infinity and result as an empty list.
# Step 3: Loop through tourist_list2:
# If an attraction is in the set of tourist_list1, calculate the travel time.
# If the travel time is less than min_travel_time, update min_travel_time and reset result.
# If the travel time equals min_travel_time, add the attraction to result.
# Step 4: Return result.
# I - Implement
def find_attractions(tourist_list1, tourist_list2):
    # Step 1: Create a set from tourist_list1 for quick lookup
    attractions_set = set(tourist_list1)
    
    # Step 2: Initialize variables to track minimum travel time and results
    min_travel_time = float('inf')
    result = []
    
    # Step 3: Loop through tourist_list2 to find common attractions
    for j, attraction in enumerate(tourist_list2):
        if attraction in attractions_set:
            # Find the index of the attraction in tourist_list1
            i = tourist_list1.index(attraction)
            travel_time = i + j  # Calculate travel time
            
            # Step 4: Update the result based on travel time
            if travel_time < min_travel_time:
                min_travel_time = travel_time
                result = [attraction]  # Start a new list with this attraction
            elif travel_time == min_travel_time:
                result.append(attraction)  # Add to the existing list
    
    # Step 5: Return the final list of attractions
    return result

# Example Usage:

tourist_list1 = ["Eiffel Tower", "Louvre Museum", "Notre-Dame", "Disneyland"]
tourist_list2 = ["Colosseum", "Trevi Fountain", "Pantheon", "Eiffel Tower"]
print(find_attractions(tourist_list1, tourist_list2))  # Output: ["Eiffel Tower"]

tourist_list1 = ["Eiffel Tower", "Louvre Museum", "Notre-Dame", "Disneyland"]
tourist_list2 = ["Disneyland", "Eiffel Tower", "Notre-Dame"]
print(find_attractions(tourist_list1, tourist_list2))  # Output: ["Eiffel Tower"]

tourist_list1 = ["beach", "mountain", "forest"]
tourist_list2 = ["mountain", "beach", "forest"]
print(find_attractions(tourist_list1, tourist_list2))  # Output: ["mountain", "beach"]


# Counting Divisible Collections in the Gallery.
### U - Understand
# Question 1: How do we define a "subarray," and are we looking for contiguous segments of the original array?
# Question 2: What should be done when the sum of a subarray is negative? Should we still consider it for divisibility by k?
### P - Plan
# Plan in plain English:
# We need to count the number of non-empty contiguous subarrays of collection_sizes whose sum is divisible by k.
# Step 1: Use a prefix sum approach to calculate the cumulative sum of the elements as we iterate through the list.
# Step 2: For each prefix sum, calculate the remainder when divided by k.
# Step 3: Use a dictionary to keep track of how many times each remainder has occurred.
# Step 4: If a remainder has been seen before, it means there are several subarrays that have sums divisible by k.
# Step 5: Update the count of such subarrays and return the total count at the end.
# Pseudocode:
# Step 1: Initialize a variable for count to 0, a variable for current_sum to 0, and a dictionary remainder_count with a default value of 0.
# Step 2: Loop through each size in collection_sizes:
# Update current_sum by adding the current size.
# Calculate remainder as current_sum % k.
# If remainder is negative, adjust it to be positive by adding k.
# Increment the count by the number of times this remainder has been seen.
# Increment the count of this remainder in the dictionary.
# Step 3: Return the total count.
### I - Implement
def count_divisible_collections(collection_sizes, k):
    # Step 1: Initialize count, current_sum, and remainder_count
    count = 0
    current_sum = 0
    remainder_count = {0: 1}  # To handle the case where current_sum itself is divisible by k
    
    # Step 2: Loop through each size in collection_sizes
    for size in collection_sizes:
        current_sum += size  # Update current_sum
        remainder = current_sum % k  # Get the remainder
        
        if remainder < 0:  # Adjust for negative remainders
            remainder += k
        
        # Step 4: Increment count by how many times this remainder has been seen
        count += remainder_count.get(remainder, 0)
        
        # Increment the count of this remainder in the dictionary
        remainder_count[remainder] = remainder_count.get(remainder, 0) + 1
    
    # Step 5: Return the total count
    return count

# Example Usage:
nums1 = [4, 5, 0, -2, -3, 1]
k1 = 5
nums2 = [5]
k2 = 9
print(count_divisible_collections(nums1, k1))  # Output: 7
print(count_divisible_collections(nums2, k2))   # Output: 0

# Pair Contestants
# ### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
#    - How many contestants need to be paired? Is there a specific requirement for the number of contestants?
#    - What happens if the number of contestants is odd? Should we return false if we can't pair everyone?
# ### P - Plan
# 2. Write out in plain English what you want to do:
#    - I want to determine if it's possible to pair contestants based on their scores such that the sum of each pair's scores is divisible by a given number \( k \). To do this, I'll count the occurrences of each possible remainder when the scores are divided by \( k \), and then check if the remainders can be paired correctly.

# 3. Translate each sub-problem into pseudocode:
#    - Initialize a list to count the occurrences of each remainder.
#    - Loop through the scores and update the count of remainders.
#    - Check the pairing conditions:
#      - If the count of remainder 0 is odd, return false.
#      - For each remainder \( r \) from 1 to \( k/2 \):
#        - If \( r \) equals \( k - r \), check if its count is even.
#        - Otherwise, check if the count of remainder \( r \) equals the count of remainder \( k - r \).
# ### I - Implement
def pair_contestants(scores, k):
    # Step 1: Check if the number of contestants is odd
    if len(scores) % 2 != 0:
        return False
    
    # Step 2: Initialize an array to count remainders
    count = [0] * k
    
    # Step 3: Populate the count array with remainders
    for score in scores:
        remainder = score % k
        count[remainder] += 1
    
    # Step 4: Check the conditions for valid pairs
    for r in range(1, (k // 2) + 1):
        if r == k - r:  # Handle special case for k being even
            if count[r] % 2 != 0:
                return False
        else:
            if count[r] != count[k - r]:
                return False
    
    # Step 4: Check for the case where remainder is 0
    if count[0] % 2 != 0:
        return False

    return True

# Example Usage:

scores1 = [1, 2, 3, 4, 5, 10, 6, 7, 8, 9]
k1 = 5
print(pair_contestants(scores1, k1))  # Output: True

scores2 = [1, 2, 3, 4, 5, 6]
k2 = 7
print(pair_contestants(scores2, k2))  # Output: True

scores3 = [1, 2, 3, 4, 5, 6]
k3 = 10
print(pair_contestants(scores3, k3))  # Output: False

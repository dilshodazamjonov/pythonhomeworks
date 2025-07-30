from collections import defaultdict
    
### List Tasks

# 1. Count Occurrences
def count_element(arr, n):
    count = 0
    for element in arr:
        if element == n:
            count += 1
    return count
print(count_element([1, 2, 4, 5, 6, 1, 4], 1))

# 2. Sum of Elements
def sum_elements(arr):
    total = 0
    for num in arr:
        total += num
    return total
print(sum_elements([1, 2, 3]))

# 3. Max Element
def max_element(arr):
    if not arr:
        return None
    maximum = arr[0]
    for num in arr:
        if num > maximum:
            maximum = num
    return maximum
print(max_element([1, 9, 3]))

# 4. Min Element
def min_element(arr):
    if not arr:
        return None
    minimum = arr[0]
    for num in arr:
        if num < minimum:
            minimum = num
    return minimum
print(min_element([2, 0, 5]))

# 5. Check Element
def check_element(arr, n):
    return n in arr
print(check_element([3, 4, 5], 4))

# 6. First Element
def first_element(arr):
    return arr[0] if arr else None
print(first_element([10, 20, 30]))

# 7. Last Element
def last_element(arr):
    return arr[-1] if arr else None
print(last_element([10, 20, 30]))

# 8. Slice List
def slice_list(arr):
    return arr[:3]
print(slice_list([1, 2, 3, 4, 5]))

# 9. Reverse List
def reverse_list(arr):
    return arr[::-1]
print(reverse_list([1, 2, 3]))

# 10. Sort List
def sort_list(arr):
    return sorted(arr)
print(sort_list([3, 1, 2]))

# 11. Remove Duplicates
def remove_duplicates(arr):
    return list(set(arr))
print(remove_duplicates([1, 2, 2, 3, 3]))

# 12. Insert Element
def insert_element(arr, index, value):
    arr.insert(index, value)
    return arr
print(insert_element([1, 2, 3], 1, 99))

# 13. Index of Element
def index_of_element(arr, value):
    if value in arr:
        return arr.index(value)
    return -1
print(index_of_element([5, 7, 9], 7))

# 14. Check for Empty List
def is_empty(arr):
    return len(arr) == 0
print(is_empty([]))

# 15. Count Even Numbers
def count_even(arr):
    return sum(1 for x in arr if x % 2 == 0)
print(count_even([1, 2, 3, 4]))

# 16. Count Odd Numbers
def count_odd(arr):
    return sum(1 for x in arr if x % 2 != 0)
print(count_odd([1, 2, 3, 4]))

# 17. Concatenate Lists
def concatenate_lists(a, b):
    return a + b
print(concatenate_lists([1, 2], [3, 4]))

# 18. Find Sublist
def contains_sublist(lst, sub):
    for i in range(len(lst) - len(sub) + 1):
        if lst[i:i+len(sub)] == sub:
            return True
    return False
print(contains_sublist([1, 2, 3, 4], [2, 3]))

# 19. Replace Element
def replace_first_occurrence(arr, old, new):
    if old in arr:
        idx = arr.index(old)
        arr[idx] = new
    return arr
print(replace_first_occurrence([1, 2, 3, 2], 2, 9))

# 20. Find Second Largest
def second_largest(arr):
    unique = list(set(arr))
    if len(unique) < 2:
        return None
    unique.sort()
    return unique[-2]
print(second_largest([1, 3, 2, 4]))

# 21. Find Second Smallest
def second_smallest(arr):
    unique = list(set(arr))
    if len(unique) < 2:
        return None
    unique.sort()
    return unique[1]
print(second_smallest([5, 1, 3, 2]))

# 22. Filter Even Numbers
def filter_even(arr):
    return [x for x in arr if x % 2 == 0]
print(filter_even([1, 2, 3, 4]))

# 23. Filter Odd Numbers
def filter_odd(arr):
    return [x for x in arr if x % 2 != 0]
print(filter_odd([1, 2, 3, 4]))

# 24. List Length
def list_length(arr):
    return len(arr)
print(list_length([1, 2, 3]))

# 25. Create a Copy
def copy_list(arr):
    return arr[:]
print(copy_list([9, 8, 7]))

# 26. Get Middle Element
def middle_element(arr):
    n = len(arr)
    if n == 0:
        return None
    if n % 2 == 1:
        return arr[n // 2]
    else:
        return arr[n // 2 - 1], arr[n // 2]
print(middle_element([1, 2, 3, 4]))

# 27. Find Maximum of Sublist
def max_of_sublist(arr, start, end):
    return max(arr[start:end])
print(max_of_sublist([1, 5, 2, 9, 3], 1, 4))

# 28. Find Minimum of Sublist
def min_of_sublist(arr, start, end):
    return min(arr[start:end])
print(min_of_sublist([7, 4, 5, 1, 2], 1, 4))

# 29. Remove Element by Index
def remove_by_index(arr, index):
    if 0 <= index < len(arr):
        del arr[index]
    return arr
print(remove_by_index([1, 2, 3], 1))

# 30. Check if List is Sorted
def is_sorted(arr):
    return arr == sorted(arr)
print(is_sorted([1, 2, 3]))

# 31. Repeat Elements
def repeat_elements(arr, n):
    return [x for x in arr for _ in range(n)]
print(repeat_elements([1, 2], 3))

# 32. Merge and Sort
def merge_and_sort(a, b):
    return sorted(a + b)
print(merge_and_sort([4, 1], [3, 2]))

# 33. Find All Indices
def find_all_indices(arr, value):
    return [i for i, x in enumerate(arr) if x == value]
print(find_all_indices([1, 2, 1, 3], 1))

# 34. Rotate List
def rotate_right(arr):
    if not arr:
        return arr
    return [arr[-1]] + arr[:-1]
print(rotate_right([1, 2, 3]))

# 35. Create Range List
def create_range_list(start, end):
    return list(range(start, end + 1))
print(create_range_list(1, 5))

# 36. Sum of Positive Numbers
def sum_positive(arr):
    return sum(x for x in arr if x > 0)
print(sum_positive([-1, 2, 3, -5]))

# 37. Sum of Negative Numbers
def sum_negative(arr):
    return sum(x for x in arr if x < 0)
print(sum_negative([-1, 2, 3, -5]))

# 38. Check Palindrome
def is_palindrome(arr):
    return arr == arr[::-1]
print(is_palindrome([1, 2, 3, 2, 1]))

# 39. Create Nested List
def create_nested_list(arr, size):
    return [arr[i:i+size] for i in range(0, len(arr), size)]
print(create_nested_list([1, 2, 3, 4, 5, 6], 2))

# 40. Get Unique Elements in Order
def unique_in_order(arr):
    seen = set()
    result = []
    for x in arr:
        if x not in seen:
            seen.add(x)
            result.append(x)
    return result
print(unique_in_order([1, 2, 2, 3, 1, 4]))


### Tuple Tasks

# 1. Count Occurrences: Given a tuple and an element, find how many times the element appears in the tuple.
def count_in_tuple(t, val):
    return t.count(val)
print(count_in_tuple((1, 2, 3, 2, 2), 2))

# 2. Max Element: From a given tuple, determine the largest element.
def max_in_tuple(t):
    return max(t) if t else None
print(max_in_tuple((1, 5, 3)))

# 3. Min Element: From a given tuple, determine the smallest element.
def min_in_tuple(t):
    return min(t) if t else None
print(min_in_tuple((4, 2, 7)))

# 4. Check Element: Given a tuple and an element, check if the element is present in the tuple.
def check_element(t, val):
    return val in t
print(check_element((1, 2, 3), 2))

# 5. First Element: Access the first element of a tuple, considering what to return if the tuple is empty.
def first_element(t):
    return t[0] if t else None
print(first_element((5, 6, 7)))

# 6. Last Element: Access the last element of a tuple, considering what to return if the tuple is empty.
def last_element(t):
    return t[-1] if t else None
print(last_element((9, 8, 7)))

# 7. Tuple Length: Determine the number of elements in the tuple.
def tuple_length(t):
    return len(t)
print(tuple_length((1, 2, 3, 4)))

# 8. Slice Tuple: Create a new tuple that contains only the first three elements of the original tuple.
def slice_tuple(t):
    return t[:3]
print(slice_tuple((1, 2, 3, 4, 5)))

# 9. Concatenate Tuples: Given two tuples, create a new tuple that combines both.
def concatenate_tuples(a, b):
    return a + b
print(concatenate_tuples((1, 2), (3, 4)))

# 10. Check if Tuple is Empty: Determine if a tuple has any elements.
def is_tuple_empty(t):
    return len(t) == 0
print(is_tuple_empty(()))

# 11. Get All Indices of Element: Given a tuple and an element, find all the indices of that element in the tuple.
def all_indices(t, val):
    return [i for i, x in enumerate(t) if x == val]
print(all_indices((1, 2, 3, 2, 2), 2))

# 12. Find Second Largest: From a given tuple, find the second largest element.
def second_largest(t):
    unique = sorted(set(t))
    return unique[-2] if len(unique) >= 2 else None
print(second_largest((3, 1, 4, 4, 2)))

# 13. Find Second Smallest: From a given tuple, find the second smallest element.
def second_smallest(t):
    unique = sorted(set(t))
    return unique[1] if len(unique) >= 2 else None
print(second_smallest((5, 2, 2, 1, 3)))

# 14. Create a Single Element Tuple: Create a tuple that contains a single specified element.
def single_element_tuple(x):
    return (x,)
print(single_element_tuple(42))

# 15. Convert List to Tuple: Given a list, create a tuple containing the same elements.
def list_to_tuple(lst):
    return tuple(lst)
print(list_to_tuple([1, 2, 3]))

# 16. Check if Tuple is Sorted: Determine if the tuple is sorted in ascending order and return a boolean.
def is_sorted_tuple(t):
    return t == tuple(sorted(t))
print(is_sorted_tuple((1, 2, 3)))

# 17. Find Maximum of Subtuple: Given a tuple, find the maximum element of a specified subtuple.
def max_of_subtuple(t, start, end):
    return max(t[start:end])
print(max_of_subtuple((1, 5, 3, 7, 2), 1, 4))

# 18. Find Minimum of Subtuple: Given a tuple, find the minimum element of a specified subtuple.
def min_of_subtuple(t, start, end):
    return min(t[start:end])
print(min_of_subtuple((9, 4, 6, 1, 3), 1, 4))

# 19. Remove Element by Value: Given a tuple and an element, create a new tuple that removes the first occurrence of that element.
def remove_first_occurrence(t, val):
    lst = list(t)
    if val in lst:
        lst.remove(val)
    return tuple(lst)
print(remove_first_occurrence((1, 2, 3, 2), 2))

# 20. Create Nested Tuple: Create a new tuple that contains subtuples, where each subtuple contains specified elements from the original tuple.
def create_nested_tuple(t, size):
    return tuple(t[i:i+size] for i in range(0, len(t), size))
print(create_nested_tuple((1, 2, 3, 4, 5, 6), 2))

# 21. Repeat Elements: Given a tuple and a number, create a new tuple where each element is repeated that number of times.
def repeat_elements(t, n):
    return tuple(x for x in t for _ in range(n))
print(repeat_elements((1, 2), 3))

# 22. Create Range Tuple: Create a tuple of numbers in a specified range (e.g., from 1 to 10).
def create_range_tuple(start, end):
    return tuple(range(start, end + 1))
print(create_range_tuple(1, 5))

# 23. Reverse Tuple: Create a new tuple that contains the elements of the original tuple in reverse order.
def reverse_tuple(t):
    return t[::-1]
print(reverse_tuple((1, 2, 3)))

# 24. Check Palindrome: Given a tuple, check if the tuple is a palindrome.
def is_palindrome(t):
    return t == t[::-1]
print(is_palindrome((1, 2, 3, 2, 1)))

# 25. Get Unique Elements: Given a tuple, create a new tuple that contains only the unique elements while maintaining the original order.
def unique_in_order(t):
    seen = set()
    result = []
    for x in t:
        if x not in seen:
            seen.add(x)
            result.append(x)
    return tuple(result)
print(unique_in_order((1, 2, 2, 3, 1, 4)))


### Set Tasks


# 1. Union of Sets
# Given two sets, create a new set that contains all unique elements from both sets.
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1.union(set2)
print("1. Union:", union_set)

# 2. Intersection of Sets
# Given two sets, create a new set that contains elements common to both sets.
set1 = {1, 2, 3}
set2 = {2, 3, 4}
intersection_set = set1.intersection(set2)
print("2. Intersection:", intersection_set)

# 3. Difference of Sets
# Given two sets, create a new set with elements from the first set that are not in the second.
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5}
difference_set = set1.difference(set2)
print("3. Difference:", difference_set)

# 4. Check Subset
# Given two sets, check if one set is a subset of the other.
set1 = {1, 2}
set2 = {1, 2, 3, 4}
is_subset = set1.issubset(set2)
print("4. Is Subset:", is_subset)

# 5. Check Element
# Given a set and an element, check if the element exists in the set.
my_set = {1, 2, 3}
element = 2
exists = element in my_set
print("5. Element Exists:", exists)

# 6. Set Length
# Determine the number of unique elements in a set.
my_set = {1, 2, 3, 4}
length = len(my_set)
print("6. Set Length:", length)

# 7. Convert List to Set
# Given a list, create a new set that contains only the unique elements from that list.
my_list = [1, 2, 2, 3, 4, 4]
unique_set = set(my_list)
print("7. Unique Set:", unique_set)

# 8. Remove Element
# Given a set and an element, remove the element if it exists.
my_set = {1, 2, 3}
my_set.discard(2)
print("8. After Removal:", my_set)

# 9. Clear Set
# Create a new empty set from an existing set.
my_set = {1, 2, 3}
my_set.clear()
print("9. Cleared Set:", my_set)

# 10. Check if Set is Empty
# Determine if a set has any elements.
my_set = set()
is_empty = len(my_set) == 0
print("10. Is Set Empty:", is_empty)

# 11. Symmetric Difference
# Given two sets, create a new set that contains elements in either set but not in both.
set1 = {1, 2, 3}
set2 = {3, 4, 5}
sym_diff = set1.symmetric_difference(set2)
print("11. Symmetric Difference:", sym_diff)

# 12. Add Element
# Add a new element to an existing set.
my_set = {1, 2}
my_set.add(3)
print("12. After Adding:", my_set)

# 13. Copy Set
# Create a copy of a set.
original = {1, 2, 3}
copied = original.copy()
print("13. Copied Set:", copied)

# 14. Frozen Set
# Create an immutable version of a set.
mutable_set = {1, 2, 3}
immutable = frozenset(mutable_set)
print("14. Frozen Set:", immutable)

# 15. Set from String
# Create a set containing unique characters from a string.
text = "hello"
char_set = set(text)
print("15. Character Set:", char_set)

# 16. Set Comprehension
# Use set comprehension to create a set of squares from 1 to 5.
squares = {x**2 for x in range(1, 6)}
print("16. Squares Set:", squares)

# 17. Filter Even Numbers Using Set
# Given a set of numbers, create a new set with only the even numbers.
nums = {1, 2, 3, 4, 5, 6}
evens = {x for x in nums if x % 2 == 0}
print("17. Even Numbers Set:", evens)

# 18. Nested Sets (Not Allowed)
# Demonstrate that sets cannot contain other sets.
try:
    nested_set = {{1, 2}, {3, 4}}  # Invalid
except TypeError as e:
    print("18. Nested Sets Error:", e)

# 19. Convert Set to List
# Convert a set into a list.
my_set = {1, 2, 3}
converted_list = list(my_set)
print("19. Converted List:", converted_list)

# 20. Find Max and Min in Set
# Find the largest and smallest elements in a set.
my_set = {5, 3, 9, 1}
print("20. Max:", max(my_set))
print("20. Min:", min(my_set))

# 21. Set Difference Update
# Remove all elements of another set from this set.
a = {1, 2, 3, 4}
b = {3, 4}
a.difference_update(b)
print("21. After Difference Update:", a)

# 22. Set Intersection Update
# Update a set with only items found in both sets.
a = {1, 2, 3, 4}
b = {2, 4, 6}
a.intersection_update(b)
print("22. After Intersection Update:", a)

# 23. Set Union Update
# Update a set with all elements from another set.
a = {1, 2}
b = {3, 4}
a.update(b)
print("23. After Union Update:", a)


### Dictionary Tasks


# 1. Get Value: Given a dictionary and a key, retrieve the associated value, considering what to return if the key doesn’t exist.
my_dict = {'name': 'Alice', 'age': 25}
key = 'name'
value = my_dict.get(key, 'Not Found')
print("1.", value)

# 2. Check Key: Given a dictionary and a key, check if the key is present in the dictionary.
key = 'name'
exists = key in my_dict
print("2.", exists)

# 3. Count Keys: Determine the number of keys in the dictionary.
print("3.", len(my_dict))

# 4. Get All Keys: Create a list that contains all the keys in the dictionary.
print("4.", list(my_dict.keys()))

# 5. Get All Values: Create a list that contains all the values in the dictionary.
print("5.", list(my_dict.values()))

# 6. Merge Dictionaries: Given two dictionaries, create a new dictionary that combines both.
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
merged = {**dict1, **dict2}
print("6.", merged)

# 7. Remove Key: Given a dictionary and a key, remove the key if it exists, handling the case if it doesn’t.
key_to_remove = 'age'
removed = my_dict.pop(key_to_remove, 'Key not found')
print("7.", removed)

# 8. Clear Dictionary: Create a new empty dictionary.
empty_dict = {}
print("8.", empty_dict)

# 9. Check if Dictionary is Empty: Determine if a dictionary has any elements.
print("9.", len(empty_dict) == 0)

# 10. Get Key-Value Pair: Given a dictionary and a key, retrieve the key-value pair if the key exists.
key = 'name'
if key in my_dict:
    print("10.", (key, my_dict[key]))
else:
    print("10.", "Key not found")

# 11. Update Value: Given a dictionary, update the value for a specified key.
my_dict['name'] = 'Bob'
print("11.", my_dict)

# 12. Count Value Occurrences: Given a dictionary, count how many times a specific value appears across the keys.
value_to_count = 'Bob'
count = list(my_dict.values()).count(value_to_count)
print("12.", count)

# 13. Invert Dictionary: Given a dictionary, create a new dictionary that swaps keys and values.
inverted = {v: k for k, v in my_dict.items()}
print("13.", inverted)

# 14. Find Keys with Value: Given a dictionary and a value, create a list of all keys that have that value.
value = 'Bob'
matching_keys = [k for k, v in my_dict.items() if v == value]
print("14.", matching_keys)

# 15. Create a Dictionary from Lists: Given two lists (one of keys and one of values), create a dictionary that pairs them.
keys = ['x', 'y', 'z']
values = [1, 2, 3]
zipped_dict = dict(zip(keys, values))
print("15.", zipped_dict)

# 16. Check for Nested Dictionaries: Given a dictionary, check if any values are also dictionaries.
nested_dict = {'a': 1, 'b': {'x': 10}, 'c': 3}
has_nested = any(isinstance(v, dict) for v in nested_dict.values())
print("16.", has_nested)

# 17. Get Nested Value: Given a nested dictionary, retrieve a value from within one of the inner dictionaries.
nested_value = nested_dict.get('b', {}).get('x', 'Not found')
print("17.", nested_value)

# 18. Create Default Dictionary: Create a dictionary that provides a default value for missing keys.

default_dict = defaultdict(lambda: 'N/A')
default_dict['existing'] = 'yes'
print("18.", default_dict['missing'])

# 19. Count Unique Values: Given a dictionary, determine the number of unique values it contains.
sample_dict = {'a': 1, 'b': 2, 'c': 1}
unique_values = len(set(sample_dict.values()))
print("19.", unique_values)

# 20. Sort Dictionary by Key: Create a new dictionary sorted by keys.
sorted_by_key = dict(sorted(sample_dict.items()))
print("20.", sorted_by_key)

# 21. Sort Dictionary by Value: Create a new dictionary sorted by values.
sorted_by_value = dict(sorted(sample_dict.items(), key=lambda item: item[1]))
print("21.", sorted_by_value)

# 22. Filter by Value: Given a dictionary, create a new dictionary that only includes items with values that meet a certain condition.
filtered = {k: v for k, v in sample_dict.items() if v > 1}
print("22.", filtered)

# 23. Check for Common Keys: Given two dictionaries, check if they have any keys in common.
dict3 = {'a': 5, 'x': 9}
common_keys = set(sample_dict.keys()) & set(dict3.keys())
print("23.", len(common_keys) > 0)

# 24. Create Dictionary from Tuple: Given a tuple of key-value pairs, create a dictionary from it.
pair_tuple = (('a', 1), ('b', 2))
tuple_dict = dict(pair_tuple)
print("24.", tuple_dict)

# 25. Get the First Key-Value Pair: Retrieve the first key-value pair from a dictionary.
first_item = next(iter(sample_dict.items()))
print("25.", first_item)


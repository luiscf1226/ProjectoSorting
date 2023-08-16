import random
#method to check if its sorted
def is_sorted(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True
#run bogo sort while its not sorted
def bogosort(random_numbers):
    while not is_sorted(random_numbers):
        random.shuffle(random_numbers)
    return random_numbers
random_numbers= [23, 56, 12,3,6, 89, 45, 67, 34, 90, 10, 78,100]
print("Before sort: "+"\n")
print(random_numbers)
print("after sort: "+"\n")
sorted_numbers = bogosort(random_numbers)
print(sorted_numbers)

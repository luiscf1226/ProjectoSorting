#quicksort function
def quicksort(random_numbers):
    #check if its less than 2 it cant be sorted
    if len(random_numbers) < 2:
        return random_numbers
    
    #get pivot element to be first
    pivot = random_numbers[0]
    #left and right array to be used
    leftArray = []
    rightArray = []
    #check if each number is less or more than pivot
    for i in range(1, len(random_numbers)):
        if random_numbers[i] < pivot:
            leftArray.append(random_numbers[i])
        else:
            rightArray.append(random_numbers[i])
    #recursively call each left and right to quick sort array
    leftSort = quicksort(leftArray)
    rightSort = quicksort(rightArray)
    #return left array + pivot middle + right recursively
    return leftSort + [pivot] + rightSort
random_numbers= [23, 56, 12,3,6, 89, 45, 67, 34, 90, 10, 78,100]
print("Before sort: "+"\n")
print(random_numbers)
print("after sort: "+"\n")
sorted_numbers = quicksort(random_numbers)
print(sorted_numbers)
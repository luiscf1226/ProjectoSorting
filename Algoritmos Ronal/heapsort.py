def heapify(random_numbers, n, i):
    #position of the greatest number
    greatest = i
    #position of left child
    left = 2*i+1
    #position of right child
    right = 2*i+2
    #if left child is greatest than number alocated on greatest position
    if left < n and random_numbers[i] < random_numbers[left]:
        #then the greatest number is alocated in left child
        greatest = left

    #if right child is greatest than number alocated on greatest position
    if right < n and random_numbers[greatest] < random_numbers[right]:
        #then the greatest number is alocated in right child
        greatest = right

    #if greatest position has changed
    if greatest != i:
        #then we change the original greatest with the child that has the greatest number
        random_numbers[i], random_numbers[greatest] = random_numbers[greatest], random_numbers[i]
        #recall the function to continue evaluating
        heapify(random_numbers,n,greatest)

def heapsort(random_numbers):
    n=len(random_numbers)
    #iterates the array from the end to the begining
    for i in range(n,-1,-1):
        #calls heapify to generates the max heap
        heapify(random_numbers,n,i)

    #iterates the array from the end to the second element
    for i in range(n-1,0,-1):
        #changes the max with the last position
        random_numbers[i], random_numbers[0] = random_numbers[0], random_numbers[i]
        #calls the heapify function with a reduced len of the array
        heapify(random_numbers, i, 0)
    return random_numbers

random_numbers= [23, 56, 12,3,6, 89, 45, 67, 34, 90, 10, 78,100]
print("Before sort: "+"\n")
print(random_numbers)
print("after sort: "+"\n")
sorted_numbers = heapsort(random_numbers)
print(sorted_numbers)
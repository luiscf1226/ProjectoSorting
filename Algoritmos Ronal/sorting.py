#imports necessary
import threading

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
    print("HeapSort: ", random_numbers)   
    return random_numbers

def bubblesort(random_numbers):
    n = len(random_numbers)
    for i in range(n):
        #is n-i-1 because, in each iteration, the greatest number is getting at last, so it is not necessary to compare all the numbers
        for j in range(0,n-i-1):
            if random_numbers[j] > random_numbers[j+1]:
                random_numbers[j], random_numbers[j+1] = random_numbers[j+1], random_numbers[j] 
        
    print("BubbleSort: ", random_numbers)      
    return random_numbers

#array with numbers
random_numbers= [23, 56, 12,3,6, 89, 100, 67, 34, 90, 10, 78,45]
print("Before sort:")
print(random_numbers)
#create threads with target and argumments to the function called
thread1 = threading.Thread(target=heapsort, args=(random_numbers,))
thread2 = threading.Thread(target=bubblesort, args=(random_numbers.copy(),))
#starts threads
thread1.start()
thread2.start()
#join means thread finished
thread1.join()
#join means thread finished
thread2.join()


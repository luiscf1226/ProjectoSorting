def bubblesort(random_numbers):
    n = len(random_numbers)
    for i in range(n):
        #is n-i-1 because, in each iteration, the greatest number is getting at last, so it is not necessary to compare all the numbers
        for j in range(0,n-i-1):
            if random_numbers[j] > random_numbers[j+1]:
                random_numbers[j], random_numbers[j+1] = random_numbers[j+1], random_numbers[j]       
    return random_numbers

random_numbers= [23, 56, 12,3,6, 89, 45, 67, 34, 90, 10, 78,100]
print("Before sort: "+"\n")
print(random_numbers)
print("after sort: "+"\n")
sorted_numbers = bubblesort(random_numbers)
print(sorted_numbers)
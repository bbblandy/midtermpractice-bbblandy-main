import random


def selection_sort(L):
    # i indicates how many items were sorted
    for i in range(len(L)-1):
        # To find the minimum value of the unsorted segment
        # We first assume that the first element is the lowest
        min_index = i
        # We then use j to loop through the remaining elements
        for j in range(i+1, len(L)-1):
            # Update the min_index if the element at j is lower than it
            if L[j] < L[min_index]:
                min_index = j
        # After finding the lowest item of the unsorted regions, swap with the first unsorted item
        L[i], L[min_index] = L[min_index], L[i]

def main():
    # L = [3, 1, 41, 59, 26, 53, 59]
    L = []
    for i in range(0, 5):
        n = random.randint(1, 30)
        L.append(n)
    print(L)
    selection_sort(L)
    print(L)

if __name__ == '__main__':
    main()

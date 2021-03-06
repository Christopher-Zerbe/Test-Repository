# This is the main file of this test repository.
# It is used to test the functionality of the GitHub.

# import the necessary packages
import random
import time


def main():
    print("Hello World! It is currently: " + time.strftime("%H:%M:%S"))
    print("We recommend the following lotto numbers: " + str(bubble_sort(generate_lotto_numbers())))
    print('rubbls privat branch is no longer private')
    print('rubbls privat branch')
    print('rubbls privat branch')

def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def generate_lotto_numbers():
    lotto_numbers = []
    for i in range(6):
        lotto_numbers.append(random.randint(1, 45))
    return lotto_numbers


test_array = [1, 8, 3, 8, 32, 98, 3, 9, 212, 68, 3, 1, 5]
print('ich gewinne im Lotto, komm in die Gruppe')

if __name__ == "__main__":
    main()

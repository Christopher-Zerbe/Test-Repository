# This is the main file of this test repository.
# It is used to test the functionality of the GitHub.

# import the necessary packages
import random
import time


def main():
<<<<<<< HEAD
    print('Hallo Rubbl Branch')
=======
    print("Hello World! It is currently: " + time.strftime("%H:%M:%S"))
    print("We recommend the following lotto numbers: " + str(bubble_sort(generate_lotto_numbers())))


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


test_array = [1, 8, 3, 8, 32, 98, 3, 9, 212, 68, 3, 1]

if __name__ == "__main__":
    main()
>>>>>>> bb7b25ac7757ce07f8b6587a648ab5c589351470

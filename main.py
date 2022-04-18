# This is the main file of this test repository.
# It is used to test the functionality of the GitHub.

def main():
    print("Hello World!")
    print("Hello World!!")
    print("Hello World!")
    print("Hello World!!")
    print("Hello World!")
    print("Hello World!!")
    print("TestTestTest")

def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def generate_lotto_numbers():
    import random
    lotto_numbers = []
    for i in range(6):
        lotto_numbers.append(random.randint(1, 45))
    return lotto_numbers

# Happy Comment

test_array = [1, 8, 3, 8, 32, 98, 3, 9, 212, 68, 3, 1]

if __name__ == "__main__":
    main()
    print(bubble_sort(test_array))
    print(generate_lotto_numbers())
"Hallo, Ich hab einen PUUUSHHH"
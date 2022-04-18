# This is the main file of this test repository.
# It is used to test the functionality of the GitHub.

def main():
    print("Hello World!")


def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


test_array = [1, 8, 3, 8, 32, 98, 3, 9, 212, 68, 3, 1]

if __name__ == "__main__":
    main()
    print(bubble_sort(test_array))

"Hallo, Ich hab einen PUUUSHHH"
def bubbleSort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def largest_sum(arr, k):
    sum = 0
    for i in range(0, len(arr)):
        for j in range(i + 1, len(arr)):
            if (arr[i] + arr[j] < k) and (arr[i] + arr[j] > sum):
                sum = arr[i] + arr[j]
                a = arr[i]
                b = arr[j]
                return a, b


def main():
    arr = [5, 20, 110, 100, 10]
    arr2 = [30, 20, 50]
    arr3 = [34, 23, 1, 24, 75, 33, 54, 8]
    arr4 = [10, 20, 30]
    k = 85
    k2 = 70
    k3 = 60
    k4 = 15
    print(largest_sum(arr, k))
    print(largest_sum(arr2, k2))
    print(largest_sum(arr3, k3))
    print(largest_sum(arr4, k4))


if __name__ == "__main__":
    main()

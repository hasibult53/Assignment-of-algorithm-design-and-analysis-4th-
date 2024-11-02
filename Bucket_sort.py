def bucketSort(arr):
    n = len(arr)

    # Find minimum and maximum values
    min_val = min(arr)
    max_val = max(arr)

    # Calculate the size of each bucket
    bucket_size = (max_val - min_val + 1) / n

    # Create buckets
    buckets = [[] for _ in range(n)]

    # Insert elements into buckets
    for i in range(n):
        index = int((arr[i] - min_val) / bucket_size)
        buckets[index].append(arr[i])

    # Sort each bucket (using insertion sort for simplicity)
    for bucket in buckets:
        insertionSort(bucket)

    # Concatenate the sorted buckets
    k = 0
    for i in range(n):
        for j in range(len(buckets[i])):
            arr[k] = buckets[i][j]
            k += 1

def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Example usage:
arr = [170, 45, 75, 90, 802, 24, 2, 66]
bucketSort(arr)

print("Sorted array is")
for i in range(len(arr)):
    print(arr[i], end=" ")

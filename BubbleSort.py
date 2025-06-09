arr = [5, 10, 11, 2, 3]

while True:
    a = True
    for i in range(0, len(arr) - 1):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
            a = False
    if a:
        break  

print(arr)

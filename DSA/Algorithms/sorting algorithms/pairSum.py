def pair_sum(arr, target):
    """
    :param: arr - input array
    :param: target - target value
    Return the two numbers in the form of a sorted list
    """

    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == target:
                if arr[i] > arr[j]:
                    return [arr[j], arr[i]]
                else:
                    return [arr[i], arr[j]]

    return [None, None]


cList = [5,2,3,9,4,1]
target = 8
check = pair_sum(cList, target)
print(check)
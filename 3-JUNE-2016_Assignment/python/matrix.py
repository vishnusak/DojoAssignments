def arr_size(arr):
    size = []

    if len(arr):
        size.append(len(arr))

    if len(size):
        # check that all elements in the array passed are also arrays
        has_arrays = reduce((lambda x, y: ([] if type(x) is list and type(y) is list else 0)), arr, arr[0])

        if type(has_arrays) is list:
            # check that all element arrays have the same length
            cols = reduce((lambda x, y: (x if x == len(y) else None)), arr, len(arr[0]))

            if cols:
                size.append(cols)

    return size if len(size) == 2 else []


def validate(size1, size2):
    valid = {
        'status': None,
        'msg': ''
    }
    if (size1[0] >= size2[0]) and (size1[1] >= size2[1]):
        valid['status'] = True
    elif (size1[0] >= size2[0]) and (size1[1] < size2[1]):
        valid['status'] = False
    elif (size1[0] < size2[0]) and (size1[1] >= size2[1]):
        valid['status'] = False
    else:
        valid['status'] = True
        valid['msg'] = 'switch'

    return valid


def compare(arr1, arr2, arr1_start, size2):
    result = True
    x = 0
    y = 0

    for i in range(arr1_start[0], arr1_start[0]+size2[0]):
        if i < len(arr1):
            for j in range(arr1_start[1], arr1_start[1]+size2[1]):
                if j < len(arr1[i]):
                    if arr1[i][j] != arr2[x][y]:
                        result = False
                        break
                    y += 1
            if not result:
                break
            x += 1
            y = 0

    return result


def search(arr1, arr2):
    result = {}
    comparison = False

    arr1_size = arr_size(arr1)
    arr2_size = arr_size(arr2)

    if arr1_size and arr2_size:
        result = validate(arr1_size, arr2_size)
        if result['status'] and result['msg'] == 'switch':
            arr1, arr2 = arr2, arr1
    else:
        result['status'] = False
        result['msg'] = "The arrays are not valid matrices"

    if result['status']:
        for i in range(arr1_size[0]):
            for j in range(arr1_size[1]):
                if arr1[i][j] == arr2[0][0]:
                    if compare(arr1, arr2, [i, j], arr2_size):
                        comparison = True
                        result['msg'] = ''
                        break
                    else:
                        result['status'] = False
                        result['msg'] = "Matrix2 not in Matrix1"
            if comparison:
                break

    return result

# ==================================================================
matrix1 = [
    [12,34,45,56],
    [98,87,76,65],
    [56,67,78,89],
    [54,43,32,21]
]

matrix2 = [
    [76,65],
    [78,89],
    [32,21]
]

myResult = search(matrix1, matrix2)
if myResult['status']:
    print "It is there"
else:
    print myResult['msg']
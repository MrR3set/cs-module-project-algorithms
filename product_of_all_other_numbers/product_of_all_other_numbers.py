'''
Input: a List of integers
Returns: a List of integers
'''
def product_of_all_other_numbers(arr):
    # Your code here
    newArr = [0]*len(arr)

    print(len(arr),len(newArr))

    for i in range(0,len(newArr)):
        total = 1
        for j in range(0,len(arr)):
            if i != j:
                total = total * arr[j]
        newArr[i] = total
    return newArr


if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    # arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]
    arr = [7, 9, 1, 8, 6, 7, 8, 8, 7, 10]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")

'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # Your code here
    print("Initial array",arr)
    i,end = 0,len(arr)
    while i < end:
        if arr[i] == 0:
            arr.append(arr.pop(i))
            print(" Removed the element at index ", i)
            print(" New array", arr)
            print("-"*50)
            end-=1
        else:
            i+=1
    print("Zeroes moved array",arr)
    print("#"*50)
    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]
    arr = [0, 0, 0, 0, 3, 2, 1]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")
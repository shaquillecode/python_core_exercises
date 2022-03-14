'''Binary Search'''
def binary_search(lst, x ):
    '''Binary Search'''
    # search by index
    left = 0
    right = len(lst) - 1

    while left <= right:

        # find the index of middle element: len() / 2
        middle = (left + right) // 2
        if lst[middle] < x:
            # Middle element is smaller
            # if it's less than , look at only the elements to the left of the middle
            left = middle + 1

        elif lst[middle] > x:
            # Mid element is larger
            # if it's greater than, look at only the elements to the right of the middle
            right = middle - 1
        else:

            return f"{x} was found at the {middle} index"
    return -1


def binary_search_recursive(lst, target):
    '''Binary Search recursive'''
    middle = int(len(lst) / 2)

    if len(lst) == 0:
        return f'{target} not found!'

    elif lst[middle] == target:
        return f'{lst[middle]} was found!'

    else:
        if target > lst[middle]:
            return binary_search_recursive(lst[middle + 1:], target)

        elif target < lst[middle]:
            return binary_search_recursive(lst[:middle], target)

if __name__ == '__main__':
    x = 3
    lst = [1,3,6,7,8,10,12,16]
    print(binary_search(lst,x))
    print(binary_search_recursive(lst,x))

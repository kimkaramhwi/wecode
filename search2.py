def binary_search_recursion(target, start, end, data):
    if start > end:
        return None

    mid = (start + end) // 2

    if data[mid] == target:
        return mid
    elif data[mid] > target:
        end = mid - 1
    else:
        start = mid + 1

    return binary_search_recursion(target, start, end, data)

if __name__ == '__main__': # 메인 함수 선언
    my_list = [i*3 for i in range(11)]
    target = 9
    my_index = binary_search_recursion(target, 0, 10, my_list)

    print(my_list)
    print(my_index)
# print(binary_search_recursion(target=9, start=0, end=5, data=[-1,0,3,5,9,12]))
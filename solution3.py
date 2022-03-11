def solution(N):
    binary_list = ""

    while N != 0:
        binary_list += str(N%2)
        N //= 2

    binary_list = (binary_list[::-1].split('1'))[:-1]

    return len(max(binary_list))


print(solution(32))
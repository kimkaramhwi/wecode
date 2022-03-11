def solution(N):
    binary_list = list(format(N, 'b'))

    count = 0
    max = 0

    for i in binary_list:
        if i == '0':
            count += 1
        elif i == '1':
            if count > max:
                max = count
            count = 0
    return max

print(solution(1))
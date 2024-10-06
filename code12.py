def solution(arr, queries):
    answer = []
    for q in queries:
        number = []
        for i in range(q[0], q[1] + 1):
            if arr[i] > q[2]:
                number.append(arr[i])
        if number:
            answer.append(min(number))
        else:
            answer.append(-1)
    return answer


answer = solution([0, 1, 2, 4, 3], [[0, 4, 2], [0, 3, 2], [0, 2, 2]])
print(answer)

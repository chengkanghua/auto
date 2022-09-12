def solution(string):
    data_list = []
    for i in string:
        data_list.append(i)
    data_list = data_list[::-1]
    ret = ''.join(data_list)
    return ret


ret = solution("world")
print(ret)
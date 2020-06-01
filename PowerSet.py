import copy
def powerset(List,result):
    if len(List) == 0:
        return [[]]
    else:
        value = List.pop()
        result = powerset(List,result)
        clone = copy.deepcopy(result) #Have to do the deep copy in order to have a perfect copy without any problem
        for i in result:
            i.append(value)
        result.extend(clone)
    return result

List = [1,2,3]
empty = []

result = powerset(List,empty)
print(result)
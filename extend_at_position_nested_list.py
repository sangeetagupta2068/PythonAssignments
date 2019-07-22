list_val = []
def extend_multi_to_one_dim(parent_list):
    for i in parent_list:
        if(type(i) == list):
            extend_multi_to_one_dim(i)
        else:
            list_val.append(i)
    return list_val

extend_multi_to_one_dim([1,[2,3],[4,[5]]])
print(list_val)




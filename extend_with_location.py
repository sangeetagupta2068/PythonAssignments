def extend_at_position(parent_list,child_list,position):
    parent_list = parent_list[ :position] + child_list + parent_list[position: ]
    return parent_list

if __name__ == '__main__':
    list1 = [1,2,3,4]
    list2 = [7,8,9]
    print(extend_at_position(list1,list2,2))
    print(list1)



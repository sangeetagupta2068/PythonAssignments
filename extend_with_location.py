def extend_at_position(parent_list,child_list,position):
    # for i in range(len(child_list)):
    #     parent_list.insert(position,child_list[i])
    #     position = position + 1
    parent_list = parent_list[ :position] + child_list + parent_list[position: ]
    return parent_list

def main():
    list1 = [1,2,3,4]
    list2 = [7,8,9]
    print(extend_at_position(list1,list2,2))
    print(list1)

main()

'''
    created by: Sangeeta Gupta
    created on: 15.07.19
    objective: replace a substring provided by user at all even places in a given string
            ( String, String) -> (String)
'''
def replace_sub_string(value,substring):
    value = value.split(substring)

    for i in range(2,len(value),2):
        value[i] = substring + value[i]

    for i in range(1,len(value)-1,2):
        value[i] = value[i]+value[i+1]
        value[i+1] = ','

    if(value[len(value)-1] == ','):
        value[len(value)-1] = ''

    value.insert(1,',')
    value = ''.join(value)
    return value

if __name__ == '__main__':
    value = "abc123def123ejg123kjh123lmn123qrs123"
    value = value.replace("123"," ",6)
    print(value)

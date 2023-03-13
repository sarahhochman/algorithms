def split_in_half(string):
    length = len(string)
    if length % 2 != 0:
        half_string2 = string[round(length/2)+1:]
        half_string1 = string[:round(length/2)+1]
    else:
        half_string1 = string[:round(len(string)/2)]
        half_string2 = string[round(len(string)/2):]
    return half_string2 + half_string1


def unique_char(string):
    for x in range(len(string)):
        if string[x] == string[x+1]:
            return False
        return True


print(split_in_half('Sarah'))  #rahSa
print(split_in_half('Rachel'))  #helRa
print(unique_char('aabb'))  #False
print(unique_char('abcd'))  #True
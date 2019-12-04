MIN, MAX = (145852, 616942)

def char_array(i):
    return [ch for ch in str(i)]

def is_sorted(list):
    for i in range(1, len(list)):
        if list[i] < list[i-1]:
            return False
    return True

def has_doubles_part_two(list):
    i,j = 0,1
    while j < len(list):
        if list[i] == list[j]:
            j +=1
        elif j-i == 2:
            return True
        else:
            i,j = j, j+1
    return j-i == 2

def has_doubles_part_one(list):
    if len(list) > 1:
        for i in range(1, len(list)):
            if list[i] == list[i-1]:
                return True
    return False

def next_number_without_decreasing_pair(sec):
    for i in range(1, len(seq)):
        if seq[i] < seq[i-1]:
            for j in range(i, len(seq)):
                seq[j] = seq[i-1]
            break
    return int("".join(seq))

if __name__ == "__main__":
    for has_doubles in (has_doubles_part_one, has_doubles_part_two):
        num = MIN
        found = 0
        while num <= MAX:
            seq = char_array(num)
            if not is_sorted(seq):
                num = next_number_without_decreasing_pair(seq)
                continue
            elif has_doubles(seq):
                found += 1
            num +=1
        print(found)
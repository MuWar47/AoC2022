import string
alphabets = string.ascii_letters
priority = {}
for i in range(1, 53):
    priority[alphabets[i - 1]] = i

with open("adventofcode.com_2022_day_3_input.txt") as f:
    add = 0
    raw = f.readlines()
    lines = [line.strip() for line in raw]
    length = len(lines)
    for i in range(0, length, 3):
        #PART 1
        # fst_half, sec_half = set(i[:len(i) // 2]), set(i[len(i) // 2:])
        # new_set = fst_half.intersection(sec_half)

        # PART 2
        fst, sec, third = set(lines[i]), set(lines[i + 1]), set(lines[i + 2])

        new_set = fst.intersection(sec, third)
        for j in new_set:
            add += priority[j]
            # could use builtin ord() ftn to get alphabets ascii value but would need to do some hocus pocus to get
            # that value in our given range
    print(add)

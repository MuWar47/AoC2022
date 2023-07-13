with open("adventofcode.com_2022_day_6_input.txt") as f:
    string = f.read()


# PART 1
def subroutine():
    start = 0
    stop = 4
    for i in range(len(string)):
        sub_str = string[start: stop]
        if len(set(sub_str)) == len(sub_str):
            return stop
        else:
            start += 1
            stop += 1


# PART 2
def msg_subroutine():
    start = 0
    stop = 14
    for i in range(len(string)):
        sub_str = string[start: stop]
        if len(set(sub_str)) == len(sub_str):
            return stop
        else:
            start += 1
            stop += 1


print(subroutine())
print(msg_subroutine())

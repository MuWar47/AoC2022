with open("adventofcode.com_2022_day_4_input.txt") as f:
    raw = f.readlines()
    lines = [line.strip() for line in raw]
    counter = 0
    for i in lines:
        comma_sep1, comma_sep2 = i.split(",")
        range_a_start, range_a_end = map(int, comma_sep1.split("-"))
        range_b_start, range_b_end = map(int, comma_sep2.split("-"))

        fst_range = range(range_a_start, range_a_end + 1)
        sec_range = range(range_b_start, range_b_end + 1)
        #PART 1
        # if set(fst_range).issubset(sec_range) or set(sec_range).issubset(fst_range):
        #     counter += 1

        #PART 2
        if set(fst_range).isdisjoint(sec_range) is False or set(sec_range).isdisjoint(fst_range) is False:
            counter += 1
    print(counter)

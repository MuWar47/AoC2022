# they are just vertical lists
# like a punch card

with open("adventofcode.com_2022_day_5_input.txt") as f:
    #PARSE INPUT
    grid, instructions = f.read().split("\n\n")
    stacks = {int(positions): [] for positions in grid.splitlines()[-1] if positions.isdigit()}
    index_lst = [index for index, char in enumerate(grid.splitlines()[-1]) if char.isdigit()]

    for line in grid.splitlines()[:-1]:
        stack_number = 1
        for i in index_lst:
            if line[i].isalpha():
                stacks[stack_number].insert(0, line[i])
            stack_number += 1
    print(stacks)
    #SOLVE PART 1
    for step in instructions.splitlines():
        quantity = int(step.split()[1])
        start = int(step.split()[3])
        stop = int(step.split()[5])
    #     for q in range(1, quantity + 1):
    #         crate = stacks[start].pop()
    #         stacks[stop].append(crate)
    #
    # answer = [values[-1] for values in stacks.values()]
    # print("".join(answer))

    #SOLVE PART 2
        stacks[stop] = stacks[stop] + stacks[start][-quantity:]
        del stacks[start][-quantity:]
    answer = [values[-1] for values in stacks.values()]
    print("".join(answer))

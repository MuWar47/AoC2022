hands = {
    "A": "Rock",
    "B": "Paper",
    "C": "Scissors",
    # "X": "Rock",
    # "Y": "Paper",
    # "Z": "Scissors"
}
points = {
    "Rock": 1,
    "Paper": 2,
    "Scissors": 3
}
new_hand = {
    "X": "lose",
    "Y": "draw",
    "Z": "win"
}
me_lose = {
    "Rock": "Scissors",
    "Paper": "Rock",
    "Scissors": "Paper"
}
me_wins = {
    "Rock": "Paper",
    "Paper": "Scissors",
    "Scissors": "Rock"
}

with open("adventofcode.com_2022_day_2_input.txt") as f:
    counter = 0
    for i in f.readlines():
        x = i.strip().split(" ")
        first = x[0]
        second = x[1]
        #Part 1
    #     if hands[first] == hands[second]:
    #         counter += 3 + points[hands[second]]
    #     elif (hands[first], hands[second]) in [('Paper', 'Rock'), ('Rock', 'Scissors'), ('Scissors', 'Paper')]:
    #         counter += 0 + points[hands[second]]
    #     else:
    #         counter += 6 + points[hands[second]]
    # print(counter)

        #PART 2
        if new_hand[second] == "draw":
            counter += 3 + points[hands[first]]
        elif new_hand[second] == "lose":
            counter += 0 + points[me_lose[hands[first]]]
        else:
            counter += 6 + points[me_wins[hands[first]]]
    print(counter)



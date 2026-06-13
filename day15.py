# Rambunctious Recitation
def part1(starting_numbers, target_turn):
    last_spoken = {}
    for i, num in enumerate(starting_numbers[:-1]):
        last_spoken[num] = i + 1

    last_num = starting_numbers[-1]
    for turn in range(len(starting_numbers) + 1, target_turn + 1):
        if last_num in last_spoken:
            next_num = turn - 1 - last_spoken[last_num]
        else:
            next_num = 0
        last_spoken[last_num] = turn - 1
        last_num = next_num

    return last_num
part1(starting_numbers=[0, 3, 6], target_turn=2020)  # Example input
def part2(starting_numbers, target_turn):
    return part1(starting_numbers, target_turn)
part2(starting_numbers=[0, 3, 6], target_turn=30000000)  # Example input

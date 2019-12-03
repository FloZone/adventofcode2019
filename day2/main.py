#!/usr/bin/python3


def read_init_value():
    f = open("input.txt", "r")
    value = [int(x) for x in f.readline().split(",")]
    f.close()
    return value


def compute_day2(value):
    instruction_pointer = 0

    while instruction_pointer < len(value):
        opcode = value[instruction_pointer]

        if opcode in [1, 2]:
            param1 = value[instruction_pointer + 1]
            param2 = value[instruction_pointer + 2]
            adress = value[instruction_pointer + 3]
            if opcode == 1:
                res = value[param1] + value[param2]
            else:
                res = value[param1] * value[param2]
            value[adress] = res

        elif opcode == 99:
            return value

        else:
            raise ValueError(f"Wrong opcode '{opcode}' read as position '{instruction_pointer}'")
        instruction_pointer += 4

    return value


def prepare_day2(value, noun, verb):
    if len(value) < 2:
        raise ValueError(f"Input length should be at least 2. Current is {len(value)}")
    value[1] = noun
    value[2] = verb
    return value


def test_compute_day2():
    init_value = [1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50]
    res = [3500, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50]
    assert compute_day2(init_value) == res
    assert compute_day2([1, 0, 0, 0, 99]) == [2, 0, 0, 0, 99]
    assert compute_day2([2, 3, 0, 3, 99]) == [2, 3, 0, 6, 99]
    assert compute_day2([2, 4, 4, 5, 99, 0]) == [2, 4, 4, 5, 99, 9801]
    assert compute_day2([1, 1, 1, 4, 99, 5, 6, 0, 99]) == [30, 1, 1, 4, 2, 5, 6, 0, 99]


def day2():
    print("--- Day 2 ---")

    test_compute_day2()

    init_value = read_init_value()
    init_value = prepare_day2(init_value, 12, 2)
    output = compute_day2(init_value)

    print(f"Result: {output[0]}\n")


def compute_part2(value):
    return 0


def test_compute_part2():
    assert compute_part2(14) == 0
    assert compute_part2(1969) == 0
    assert compute_part2(100756) == 0


def part2():
    print("--- Part 2 ---")

    init_value = read_init_value()

    done = False
    for noun in range(0, 99):
        for verb in range(0, 99):
            value = init_value.copy()
            value = prepare_day2(value, noun, verb)
            output = compute_day2(value)
            if output[0] == 19690720:
                done = True
                break
        if done:
            break

    res = 100 * noun + verb
    print(f"Result: noun={noun}, verb={verb}, result={res}\n")


def main():
    day2()
    part2()


main()

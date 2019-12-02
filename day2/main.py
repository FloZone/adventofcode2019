#!/usr/bin/python3


def compute_day2(value):
    index = 0

    while index < len(value):
        opcode = value[index]

        if opcode in [1, 2]:
            pos1 = value[index + 1]
            pos2 = value[index + 2]
            dest = value[index + 3]
            if opcode == 1:
                res = value[pos1] + value[pos2]
            else:
                res = value[pos1] * value[pos2]
            value[dest] = res

        elif opcode == 99:
            return value

        else:
            raise ValueError(f"Wrong opcode '{opcode}' read as position '{index}'")
        index += 4

    return value


def prepare_day2(value):
    if len(value) < 2:
        raise ValueError(f"Input length should be at least 2. Current is {len(value)}")
    value[1] = 12
    value[2] = 2
    return value


def test_compute_day2():
    val = [1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50]
    res = [3500, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50]
    assert compute_day2(val) == res
    assert compute_day2([1, 0, 0, 0, 99]) == [2, 0, 0, 0, 99]
    assert compute_day2([2, 3, 0, 3, 99]) == [2, 3, 0, 6, 99]
    assert compute_day2([2, 4, 4, 5, 99, 0]) == [2, 4, 4, 5, 99, 9801]
    assert compute_day2([1, 1, 1, 4, 99, 5, 6, 0, 99]) == [30, 1, 1, 4, 2, 5, 6, 0, 99]


def day2():
    print("--- Day 2 ---")

    test_compute_day2()

    f = open("input.txt", "r")
    value = [int(x) for x in f.readline().split(",")]
    f.close()

    value = prepare_day2(value)
    compute_day2(value)

    print(f"Result: {value[0]}\n")


def main():
    day2()


main()

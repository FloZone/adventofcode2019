#!/usr/bin/python3


def compute_day1(value):
    return int(value / 3) - 2


def test_compute_day1():
    assert compute_day1(12) == 2
    assert compute_day1(14) == 2
    assert compute_day1(1969) == 654
    assert compute_day1(100756) == 33583


def day1():
    print("--- Day 1 ---")

    test_compute_day1()

    res = 0
    f = open("input.txt", "r")
    for value in f:
        tmp = int(value.strip())
        res += compute_day1(tmp)
    f.close()

    print(f"Result: {res}\n")


def compute_part2(value):
    res = compute_day1(value)
    if res <= 0:
        return 0
    else:
        return res + compute_part2(res)


def test_compute_part2():
    assert compute_part2(14) == 2
    assert compute_part2(1969) == 966
    assert compute_part2(100756) == 50346


def part2():
    print("--- Part 2 ---")

    test_compute_part2()

    res = 0
    f = open("input.txt", "r")
    for value in f:
        tmp = int(value.strip())
        res += compute_part2(tmp)
    f.close()

    print(f"Result: {res}\n")


def main():
    day1()
    part2()


main()

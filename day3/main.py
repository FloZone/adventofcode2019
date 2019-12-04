#!/usr/bin/python3


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x},{self.y})"

    def get_distance(self, other):
        return abs(other.x - self.x) + abs(other.y - self.x)


class Segment:
    def __init__(self, p1=None, p2=None):
        self.p1 = p1
        self.p2 = p2

    def __str__(self):
        return f"[{self.p1} - {self.p2}]"

    def det(self, a, b):
        return a.x * b.y - a.y * b.x

    def intersects(self, other):
        d = (other.p2.y - other.p1.y) * (self.p2.x - self.p1.x) - (
            other.p2.x - other.p1.x
        ) * (self.p2.y - self.p1.y)
        n_a = (other.p2.x - other.p1.x) * (self.p1.y - other.p1.y) - (
            other.p2.y - other.p1.y
        ) * (self.p1.x - other.p1.x)
        n_b = (self.p2.x - self.p1.x) * (self.p1.y - other.p1.y) - (
            self.p2.y - self.p1.y
        ) * (self.p1.x - other.p1.x)
        if d == 0:
            return None

        ua = float(n_a / d)
        ub = float(n_b / d)

        if ua >= 0.0 and ua <= 1.0 and ub >= 0.0 and ub <= 1.0:
            x = int(self.p1.x + float(ua * (self.p2.x - self.p1.x)))
            y = int(self.p1.y + float(ua * (self.p2.y - self.p1.y)))
            if x != 0 or y != 0:  # Do not get the origin point
                return Point(x, y)
        return None


class Wire:
    def __init__(self):
        self.segments = []

    def __str__(self):
        res = ""
        for s in self.segments:
            res += f"{s}\n"
        return res

    def add_seg(self, segment):
        self.segments.append(segment)


def read_init_value():
    f = open("input.txt", "r")
    value = []
    for line in f:
        value.append(line)
    f.close()
    return value


def compute_day3(value):
    # construct the list of all wires
    wires = build_wires(value)
    print("Wires")
    for wire in wires:
        print(wire)

    # For each wire, check if it intersects other wires
    intersections = get_intersections_points(wires)
    print("Intersections")
    for point in intersections:
        print(f"{point}")

    if len(intersections) > 1:
        point, distance = get_closest_point(intersections)
    elif len(intersections) == 1:
        point = intersections[0]
        distance = Point(0, 0).get_distance(point)
    else:
        point = None
        distance = None
    print(f"\nClosest intersection: {point} - {distance}\n")
    return distance


def build_wires(value):
    # construct the list of all wires
    wires = []

    # value = list of wires / str path ["R8,U5,L5,D3", "U7,R6,D4,L4", ...]
    for wire_str in value:
        # list of segments for one wire
        wire = Wire()
        path = wire_str.split(",")
        orig = Point(0, 0)
        # path = list of movements for one wire "R8,U5,L5,D3"
        for m in path:
            d = m[0]
            v = int(m[1:])
            if d == "R":
                dest = Point(orig.x + v, orig.y)
            elif d == "U":
                dest = Point(orig.x, orig.y + v)
            elif d == "L":
                dest = Point(orig.x - v, orig.y)
            elif d == "D":
                dest = Point(orig.x, orig.y - v)

            seg = Segment(orig, dest)

            wire.add_seg(seg)
            orig = dest

        wires.append(wire)
    return wires


def get_intersections_points(wires):
    intersections = []
    for i in range(0, len(wires) - 1):
        for j in range(i + 1, len(wires)):
            # Get intersections points between this two wires
            points = get_intersections_for_wires(wires[i], wires[j])
            if(points):
                intersections += points
    return intersections


def get_intersections_for_wires(w1, w2):
    intersections = []
    for s1 in w1.segments:
        for s2 in w2.segments:
            intersection_point = s1.intersects(s2)
            if(intersection_point):
                intersections.append(intersection_point)
    return intersections


def get_closest_point(points):
    orig = Point(0, 0)
    closest_point = points[0]
    closest_dist = orig.get_distance(closest_point)

    for i in range(1, len(points)):
        d = orig.get_distance(points[i])
        if d < closest_dist:
            closest_dist = d
            closest_point = points[i]

    return closest_point, closest_dist


def test_compute_day3():
    init_value = ["R8,U5,L5,D3", "U7,R6,D4,L4"]
    assert compute_day3(init_value) == 6
    init_value = [
        "R75,D30,R83,U83,L12,D49,R71,U7,L72",
        "U62,R66,U55,R34,D71,R55,D58,R83",
    ]
    assert compute_day3(init_value) == 159
    init_value = [
        "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51",
        "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7",
    ]
    assert compute_day3(init_value) == 135


def day3():
    print("--- Day 3 ---")

    test_compute_day3()

    init_value = read_init_value()
    output = compute_day3(init_value)

    print(f"Result: {output}\n")


def main():
    day3()
    # compute_day3(["R8,U5,L5,D3", "U7,R6,D4,L4"])
    # test_compute_day3()


main()

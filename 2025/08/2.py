import math

from collections import namedtuple


def read_from_file(file: str) -> str:
    data = None
    with open(file) as f:
        data = f.read()
    return data


Box = namedtuple('Box', ['name', 'x', 'y', 'z'])

type Circuit = list[Box]


def get_distance_between_boxes(b1: Box, b2: Box) -> float:
    return math.sqrt((b1.x - b2.x)**2 + (b1.y - b2.y)**2 + (b1.z - b2.z)**2)


def join_circuits(c1: Circuit, c2: Circuit) -> Circuit:
    return c1 + c2


def find_circuit_containing_box(box: Box, circuits: list[Circuit]):
    for circuit in circuits:
        if box in circuit:
            return circuit

    return None


def solve(file_path) -> None:
    file_contents = read_from_file(file_path)

    boxes = [Box('box#' + str(i), *list(map(int, row.split(','))))
             for i, row in enumerate(file_contents.split('\n'))]

    distances = []
    for i in range(len(boxes)):
        for j in range(i + 1, len(boxes)):
            b1, b2 = boxes[i], boxes[j]
            distance = get_distance_between_boxes(b1, b2)
            distances.append({"b1": b1, "b2": b2, "distance": distance})

    sorted_distances = sorted(distances, key=lambda d: d['distance'])

    circuits: list[Circuit] = []

    limit = 10 if file_path == 'sample.txt' else 1000 if file_path == 'input.txt' else None

    if limit == None:
        raise Exception('invalid limit')

    for sorted_distance in sorted_distances:
        b1 = sorted_distance['b1']
        b2 = sorted_distance['b2']

        c1 = find_circuit_containing_box(b1, circuits)
        c2 = find_circuit_containing_box(b2, circuits)

        circuit: Circuit = []
        if c1 and c2 == None:
            circuits.remove(c1)
            circuit = c1
            circuit.append(b2)
        elif c2 and c1 == None:
            circuits.remove(c2)
            circuit = c2
            circuit.append(b1)
        elif c1 == None and c2 == None:
            circuit.append(b1)
            circuit.append(b2)
        elif c1 == c2:
            continue
        elif c1 != None and c2 != None:
            circuits.remove(c1)
            circuits.remove(c2)
            circuit = join_circuits(c1, c2)
        else:
            print(c2)
            print(c1)
            raise Exception("unknown scenario")

        circuits.append(circuit)

        if len(circuits) == 1 and len(circuits[0]) == len(boxes):
            print(b1.x * b2.x)


solve('sample.txt')
solve('input.txt')

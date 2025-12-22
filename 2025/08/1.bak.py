import math

from collections import namedtuple


def read_from_file(file: str) -> str:
    data = None
    with open(file) as f:
        data = f.read()
    return data


Box = namedtuple('Box', ['x', 'y', 'z'])

type Circuit = list[Box]


def get_distance_between_boxes(b1: Box, b2: Box) -> float:
    return math.sqrt((b1.x - b2.x)**2 + (b1.y - b2.y)**2 + (b1.z - b2.z)**2)


def are_boxes_in_same_circuit(b1: Box, b2: Box, circuits: list[Circuit]) -> bool:
    in_same_circuit = False

    for circuit in circuits:
        if b1 in circuit and b2 in circuit:
            in_same_circuit = True
            break

    return in_same_circuit


def join_circuits(c1: Circuit, c2: Circuit) -> Circuit:
    return c1 + c2


def find_circuit_containing_box(box: Box, circuits: list[Circuit]):
    for circuit in circuits:
        if box in circuit:
            return circuit

    return None


def find_boxes_with_shortest_distance(circuits: list[Circuit]):
    distances = []
    for i in range(len(circuits)):
        for j in range(i+1, len(circuits)):
            c1, c2 = circuits[i], circuits[j]
            for b1 in c1:
                for b2 in c2:
                    distance = get_distance_between_boxes(b1, b2)
                    distances.append({"b1": b1, "b2": b2, "distance": distance})

    closest_boxes = min(distances, key=lambda d: d['distance'])

    return [closest_boxes['b1'], closest_boxes['b2']]

def next_step(circuits: list[Circuit]) -> list[Circuit]:
    return circuits


def solve(file_path) -> None:
    file_contents = read_from_file(file_path)

    boxes = [Box(*list(map(int, row.split(','))))
             for row in file_contents.split('\n')]

    circuits: list[Circuit] = [[box] for box in boxes]

    for i in range(999):
      b1, b2 = find_boxes_with_shortest_distance(circuits)
      
      if i % 100 == 0:
        print("Doing pass #", i)

      c1 = find_circuit_containing_box(b1, circuits)
      c2 = find_circuit_containing_box(b2, circuits)

      if not c1 or not c2:
          raise Exception('lol')
      
      if c1 == c2:
          raise Exception('same lol')
      
      circuits.remove(c1)
      circuits.remove(c2)

      circuits.append(join_circuits(c1, c2))

    sorated_circuit_lengths = sorted([len(circuit) for circuit in circuits], reverse=True)

    print(sorated_circuit_lengths[0] * sorated_circuit_lengths[1] * sorated_circuit_lengths[2])


solve('input.txt')

from collections import namedtuple


def read_from_file(file: str) -> str:
    data = None
    with open(file) as f:
        data = f.read()
    return data


def ranges_have_overlap(r1: Range, r2: Range) -> bool:
    return not (r1.end < r2.start or r1.start > r2.end)


Range = namedtuple('Range', ['start', 'end'])


def merge_ranges(r1: Range, r2: Range) -> Range:
    if not ranges_have_overlap(r1, r2):
        raise Exception("ranges don't overlap", r1, r2)
    start = min(r1.start, r2.start)
    end = max(r1.end, r2.end)
    return Range(start, end)


def solve(file_path: str) -> None:
    file_contents = read_from_file(file_path)

    id_ranges_str, _ingredient_ids_str = file_contents.split('\n\n')

    id_ranges_with_duplicates = [Range(*list(map(int, id_range.split('-'))))
                                 for id_range in id_ranges_str.split('\n')]

    id_ranges: list[Range] = []
    for id_range in id_ranges_with_duplicates:
        if not id_range in id_ranges:
            id_ranges.append(id_range)

    some_ranges_overlap = True
    while (some_ranges_overlap):
        overlap = False
        unique_id_ranges = id_ranges.copy()
        for i in range(len(id_ranges)):
            for j in range(i + 1, len(id_ranges)):
                r1 = id_ranges[i]
                r2 = id_ranges[j]
                if ranges_have_overlap(r1, r2):
                    overlap = True
                    if r1 in unique_id_ranges:
                        unique_id_ranges.remove(r1)
                    if r2 in unique_id_ranges:
                        unique_id_ranges.remove(r2)
                    if merge_ranges(r1, r2) not in unique_id_ranges:
                        unique_id_ranges.append(merge_ranges(r1, r2))

        id_ranges = unique_id_ranges.copy()
        if not overlap:
            some_ranges_overlap = False

    total = 0
    for id_range in id_ranges:
        total = total + (id_range.end - id_range.start) + 1

    print(total)


solve('input.txt')

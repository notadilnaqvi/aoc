def read_from_file(file):
    data = None
    with open(file) as f:
        data = f.read()
    return data

def determine_forest_dimensions(forest):
    no_of_rows = len(forest.splitlines())
    no_of_cols = len(forest.splitlines()[0])
    return [no_of_rows, no_of_cols]


def find_position_of_tallest_trees(rows, cols):
    positions = []
    for row_idx, row in enumerate(rows):
        idx_of_tallest_trees = [col_idx for col_idx, tree in enumerate(row) if tree == max(row)]
        only_one_tallest_tree = len(idx_of_tallest_trees) == 1
        if(only_one_tallest_tree):
            col_idx = idx_of_tallest_trees[0]
            positions.append(f'{row_idx + 1},{col_idx + 1}')
        else:
            col_idx_1 = sorted(idx_of_tallest_trees)[0]
            positions.append(f'{row_idx + 1},{col_idx_1 + 1}')
            col_idx_2 = sorted(idx_of_tallest_trees)[1]
            positions.append(f'{row_idx + 1},{col_idx_2 + 1}')
    
    for col_idx, col in enumerate(cols):
        idx_of_tallest_trees = [row_idx for row_idx, tree in enumerate(row) if tree == max(row)]
        only_one_tallest_tree = len(idx_of_tallest_trees) == 1
        if(only_one_tallest_tree):
            row_idx = idx_of_tallest_trees[0]
            positions.append(f'{col_idx + 1},{row_idx + 1}')
        else:
            row_idx_1 = sorted(idx_of_tallest_trees)[0]
            positions.append(f'{col_idx + 1},{row_idx_1 + 1}')
            row_idx_2 = sorted(idx_of_tallest_trees)[1]
            positions.append(f'{col_idx + 1},{row_idx_2 + 1}')
        
        return positions

def divide_into_rows_and_cols(forest):
    rows = forest.splitlines()
    cols = [''] * len(rows[0])
    for row_idx, row in enumerate(rows):
        for col_idx, tree in enumerate(row):
            cols[col_idx] += tree

    return [rows, cols]

def solve(file):
    forest = read_from_file(file)
    print(forest)
    print('\n=====\n')
    [rows, cols] = divide_into_rows_and_cols(forest)
    print(find_position_of_tallest_trees(rows, cols))
    





solve('sample.txt')
# solve('input.txt')

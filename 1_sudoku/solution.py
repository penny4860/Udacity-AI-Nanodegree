# -*- coding: utf-8 -*-

assignments = []

def assign_value(values, box, value):
    """
    Please use this function to update your values dictionary!
    Assigns a value to a given box. If it updates the board record it.
    """

    # Don't waste memory appending actions that don't actually change any values
    if values[box] == value:
        return values

    values[box] = value
    if len(value) == 1:
        assignments.append(values.copy())
    return values

def naked_twins(values):
    """Eliminate values using the naked twins strategy.
    Args:
        values(dict): a dictionary of the form {'box_name': '123456789', ...}

    Returns:
        the values dictionary with the naked twins eliminated from peers.
    """
    def get_twin_digits(unit, values):
        """Get twin digit from the unit."""
        unit_values = [values[box] for box in unit if len(values[box]) == 2]
        
        twin_digits = [x for i, x in enumerate(unit_values) if unit_values.count(x) > 1]
        if twin_digits == []:
            return False
        else:
            return list(set(twin_digits))
    
    for unit in unitlist:
        list_twin_digits = get_twin_digits(unit, values)
        if list_twin_digits:
            # Remove twin digits from the boxes which contain the digit
            for box in unit:
                for twin_digits in list_twin_digits:
                    for d in twin_digits:
                        if values[box] != twin_digits and d in values[box]:
                            values = assign_value(values, box, values[box].replace(d, ""))    
    return values

def cross(A, B):
    """Cross product of elements in A and elements in B.
    Args:
        A(string)
        B(string)
    Returns:
        cross product string
    """
    return [a+b for a in A for b in B]

def grid_values(grid):
    """
    Convert grid into a dict of {square: char} with '123456789' for empties.
    Args:
        grid(string) - A grid in string form.
    Returns:
        A grid in dictionary form
            Keys: The boxes, e.g., 'A1'
            Values: The value in each box, e.g., '8'. If the box has no value, then the value will be '123456789'.
    """
    assert len(grid) == 81, "Input grid must be a string of length 81 (9x9)"
    keys = boxes
    values = grid
    dict_ = {}
    for k, v in zip(keys, values):
        if v == ".":
            v_filled = "123456789"
        else:
            v_filled = v
        dict_[k] = v_filled
    return dict_    

def display(values):
    """
    Display the values as a 2-D grid.
    Args:
        values(dict): The sudoku in dictionary form
    """
    width = 1+max(len(values[s]) for s in boxes)
    line = '+'.join(['-'*(width*3)]*3)
    for r in rows:
        print(''.join(values[r+c].center(width)+('|' if c in '36' else '')
                      for c in cols))
        if r in 'CF': print(line)

def eliminate(values):
    """Eliminate values from peers of each box with a single value.

    Go through all the boxes, and whenever there is a box with a single value,
    eliminate this value from the set of values of all its peers.

    Args:
        values: Sudoku in dictionary form.
    Returns:
        Resulting Sudoku in dictionary form after eliminating values.
    """
    
    for k, v in zip(values.keys(), values.values()):
        if len(v) > 1:
            # Get Peer boxes
            k_peer_boxes = peers[k]
            eliminated_v = v
            
            for peer_key in k_peer_boxes:
                if len(values[peer_key]) == 1 and values[peer_key] in eliminated_v:
                    eliminated_v = eliminated_v.replace(values[peer_key], "")
            values = assign_value(values, k, eliminated_v)
        else:
            values = assign_value(values, k, v)
    return values


def only_choice(values):
    """Finalize all values that are the only choice for a unit.

    Go through all the units, and whenever there is a unit with a value
    that only fits in one box, assign the value to this box.

    Input: Sudoku in dictionary form.
    Output: Resulting Sudoku in dictionary form after filling in only choices.
    """
    def get_boxes_contain_digit(unit, digit):
        """Get boxes containing the digit from the unit
        # Args:
            unit : list of strs
            digit : str
        # Returns:
            dplaces : list of strs (boxes location : e.g.) 'A1')
        """
        dplaces = []
        for box in unit:
            if digit in values[box]:
                dplaces.append(box)
        return dplaces        
    
    # for each unit
    for unit in unitlist:
        # for each digit
        for digit in '123456789':
            # get boxes containing the digit
            dplaces = get_boxes_contain_digit(unit, digit)
            if len(dplaces) == 1:
                values = assign_value(values, dplaces[0], digit)
    return values
        
def reduce_puzzle(values):
    stalled = False
    while not stalled:
        # Check how many boxes have a determined value
        solved_values_before = len([box for box in values.keys() if len(values[box]) == 1])

        # Eliminate Strategy
        values = eliminate(values)

        # Only Choice Strategy
        values = only_choice(values)

        # Naked_twins Strategy
        values = naked_twins(values)

        # Check how many boxes have a determined value, to compare
        solved_values_after = len([box for box in values.keys() if len(values[box]) == 1])
        # If no new values were added, stop the loop.
        stalled = solved_values_before == solved_values_after
        # Sanity check, return False if there is a box with zero available values:
        if len([box for box in values.keys() if len(values[box]) == 0]):
            return False
    return values

def search(values):
    "Using depth-first search and propagation, try all possible values."
    # First, reduce the puzzle using the previous function
    values = reduce_puzzle(values)
    if values is False:
        return False ## Failed earlier
    if all(len(values[s]) == 1 for s in boxes): 
        return values ## Solved!
    # Choose one of the unfilled squares with the fewest possibilities
    n,s = min((len(values[s]), s) for s in boxes if len(values[s]) > 1)
    # Now use recurrence to solve each one of the resulting sudokus, and 
    for value in values[s]:
        new_sudoku = values.copy()
        new_sudoku[s] = value
        attempt = search(new_sudoku)
        if attempt:
            return attempt

def solve(grid):
    """
    Find the solution to a Sudoku grid.
    Args:
        grid(string): a string representing a sudoku grid.
            Example: '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    Returns:
        The dictionary representation of the final sudoku grid. False if no solution exists.
    """
    values = grid_values(grid)
    values = search(values)
    return values


rows = 'ABCDEFGHI'
cols = '123456789'

boxes = cross(rows, cols)

row_units = [cross(r, cols) for r in rows]
column_units = [cross(rows, c) for c in cols]
square_units = [cross(rs, cs) for rs in ('ABC','DEF','GHI') for cs in ('123','456','789')]

diag_units_from_left_most = [r+c for r, c in zip(rows, cols)]
diag_units_from_right_most = [r+c for r, c in zip(rows, cols[::-1])]
diag_units = [diag_units_from_left_most, diag_units_from_right_most]

unitlist = row_units + column_units + square_units + diag_units

units = dict((s, [u for u in unitlist if s in u]) for s in boxes)
peers = dict((s, set(sum(units[s],[]))-set([s])) for s in boxes)


if __name__ == '__main__':
    
    diag_sudoku_grid = '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    display(solve(diag_sudoku_grid))

    try:
        from visualize import visualize_assignments
        visualize_assignments(assignments)

    except SystemExit:
        pass
    except:
        print('We could not visualize your board due to a pygame issue. Not a problem! It is not a requirement.')
    
    


import math
import os

def make_substrings(s, L):
    """ splits `s` into substrings of length L """
    i = 0
    pieces = []
    while i < len(s):
        pieces.append(s[i:i+L])
        i += L
    return pieces
    
def print_side_by_side(output1, output2, print_line_numbers=False, col_padding=2, delimiter=''):
    if len(delimiter) > col_padding:
        raise ValueError('Delimiter cannot be longer than padding')
    # Get terminal size
    rows, columns = map(int, os.popen('stty size', 'r').read().split())
    # Split files into lines
    lines1 = output1.split('\n')
    lines2 = output2.split('\n')
    # Get number of digits in line numbers
    max_num_lines = max(len(lines1), len(lines2))
    if print_line_numbers:
        max_num_digits_in_line_num = math.ceil(math.log(max_num_lines))
        col_width = (columns - (max_num_digits_in_line_num) - col_padding) // 2
        line_fmt = ('{:<' + str(max_num_digits_in_line_num) + '}' )
    else:
        col_width = (columns - col_padding) // 2
        max_num_digits_in_line_num = False
        line_fmt = ''
    # Print lines side by side
    line_fmt += ('{:<' + str(col_width) + '}' 
               + (' ' * math.floor((col_padding-len(delimiter))/2.)) 
               + delimiter
               + (' ' * math.ceil((col_padding-len(delimiter))/2.))
               + '{:<' + str(col_width) + '}')
    for i in range(max_num_lines):
        # Get rows for this line for file 1.
        l1 = ''
        if i < len(lines1):
            l1 = lines1[i]
        rows1 = make_substrings(l1, col_width)
        # Get rows for this line for file 2.
        l2 = ''
        if i < len(lines2):
            l2 = lines2[i]
        rows2 = make_substrings(l2, col_width)
        # Print rows.
        max_num_rows = max(len(rows1), len(rows2))
        j = 0
        while j < max_num_rows:
            token1 = rows1[j] if j < len(rows1) else ''
            token2 = rows2[j] if j < len(rows2) else ''
            if print_line_numbers:
                row_num = i if j == 0 else ''
                print(line_fmt.format(row_num, token1, token2))
            else:
                print(line_fmt.format(token1, token2))
            j += 1
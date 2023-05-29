import math
import shutil
from IPython import get_ipython
from IPython.display import display

def make_substrings(s, L):
    """splits `s` into substrings of length L"""
    i = 0
    pieces = []
    while i < len(s):
        pieces.append(s[i:i+L])
        i += L
    return pieces

# optimized
def print_side_by_side(output1, output2, print_line_numbers=False, col_padding=2, delimiter='', terminal_width=None):
    # sourcery skip: low-code-quality
    if len(delimiter) > col_padding:
        raise ValueError('Delimiter cannot be longer than padding')
    
    # Determine terminal width
    if terminal_width is None:
        ipython = get_ipython()
        if ipython is not None and ('ipykernel' in str(ipython) or 'google.colab' in str(ipython)):
            # Running in IPython
            terminal_width = 180
        else:
            terminal_width = shutil.get_terminal_size().columns
    
    # Split files into lines
    lines1 = output1.splitlines()
    lines2 = output2.splitlines()
    
    # Get number of digits in line numbers
    max_num_lines = max(len(lines1), len(lines2))
    
    if print_line_numbers:
        max_num_digits_in_line_num = math.ceil(math.log(max_num_lines))
        col_width = (terminal_width - max_num_digits_in_line_num - col_padding) // 2
        line_fmt = '{:<{}}'
    else:
        col_width = (terminal_width - col_padding) // 2
        max_num_digits_in_line_num = False
        line_fmt = ''
    
    # Print lines side by side
    line_fmt += ('{:<' + str(col_width) + '}'
               + (' ' * math.floor((col_padding - len(delimiter)) / 2.))
               + delimiter
               + (' ' * math.ceil((col_padding - len(delimiter)) / 2.))
               + '{:<' + str(col_width) + '}')
    
    for i in range(max_num_lines):
        # Get rows for this line for file 1.
        l1 = lines1[i] if i < len(lines1) else ''
        rows1 = make_substrings(l1, col_width)
        
        # Get rows for this line for file 2.
        l2 = lines2[i] if i < len(lines2) else ''
        rows2 = make_substrings(l2, col_width)
        
        # Print rows.
        max_num_rows = max(len(rows1), len(rows2))
        for j in range(max_num_rows):
            token1 = rows1[j] if j < len(rows1) else ''
            token2 = rows2[j] if j < len(rows2) else ''
            
            if print_line_numbers:
                row_num = i if j == 0 else ''
                display(line_fmt.format(row_num, max_num_digits_in_line_num, token1, token2))
            else:
                display(line_fmt.format(token1, token2))
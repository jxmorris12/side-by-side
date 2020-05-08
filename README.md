# Print two outputs side-by-side, in Python 

`side_by_side` allows users to print two multi-line outputs side-by-side. This produces an effect similar to running `diff -y file1 file2` in a Unix system.

## Usage

This library provides a single function, `side_by_side.print_side_by_side`. To print two_strings side-by-side with default settings:

```
from side_by_side import print_side_by_side

print_side_by_side(s1, s2)
```
![lorem ipsum output with typical usage](https://raw.githubusercontent.com/jxmorris12/side-by-side/master/imgs/test.png)

## Optional parameters

* `print_line_numbers (bool)`: If True, prints line-numbers along the left column.
* `col_padding (int)`: the number of spaces to leave between the two columns (and between the text and line number, if applicable)
* `delimiter (str)`: a delimiter to separate the columns


## Fancy usage

Here's an example of a print format that uses all of the parameters:

```
from side_by_side import print_side_by_side

print_side_by_side(lorem_ipsum, lorem_ipsum, print_line_numbers=True, col_padding=24, delimiter='|++++|')
```
![lorem ipsum output with typical usage](https://raw.githubusercontent.com/jxmorris12/side-by-side/master/imgs/test_fancy.png)

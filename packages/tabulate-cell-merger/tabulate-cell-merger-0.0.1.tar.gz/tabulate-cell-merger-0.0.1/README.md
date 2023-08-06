# Tabulate Cell Merger

This is a package to merge cells when tabulating table. A table is a list of lists which can be represented into rows and columns.
It is inspired in the already existing tabulate package.

### How to import the module
Module's name for importing:
```
import tabulate_cell_merger.tabulate_cell_merger
```

### How to use
The module contains one function for you to use:
tabulate()
This function accepts three arguments as following:
tabulate(table, colspan, rowspan)
The colspan and rowspan are optional arguments. The table argument is required.

To merge cells horizontally, use the colspan argument.
To merge cells vertically, use the rowspan argument.
These arguments are **dictionaries**.
They allow you to stretch cells over others.
Syntax:
```
colspan = {(y, x): value}
rowspan = {(y, x): value}
```
For each cell you want to stretch, you have to associate its coordinates, having then a tuple as key, to a stretching value: 1 generates no stretching, 2 stretches over one other cell (to the right or to downwards), etc.")
Here, `y` is the cell row, `x` the cell column, and `value` the stretching value.

#### An example
Input:
```
table = [['a1', 'b1'], ['a2', 'b2']]
colspan = {(0, 0): 2}
rowspan = {(0, 1): 2}
```
Output:
```
+----+----+
| a1      |
+----+    +
| a2 |    |
+----+----+
```

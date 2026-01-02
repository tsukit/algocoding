# PROBLEM STATEMENT
# Given a Binary Matrix mat[][] of order m*n. A cell with a value of zero 
# is a Dead Cell, while a cell with a value of one is a Live Cell. The 
# state of cells in a matrix mat[][] is known as Generation. The task is 
# to find the next generation of cells based on the following rules:
# 
# Any live cell with fewer than two live (< 2) neighbours dies as if caused 
# by underpopulation.
#
# Any live cell with two or three live (= 2 or 3) neighbours lives on to the 
# next generation.
# 
# Any live cell with more than three live (> 3) neighbours dies, as if by 
# overpopulation.
#
# Any dead cell with exactly three live ( = 3) neighbours becomes a live 
# cell, as if by reproduction.


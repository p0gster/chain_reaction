# chain_reaction
An implementation of the game chain reaction in python.

In this game, there is a grid of cells with a number of atoms in each. 
If the amount in each cell is greater than a certain amount, the atom "explodes", releasing all atoms into neighbouring cells.
In the centre of the grid, this limit is 3. In the edges, but not the very corners, this limit is 2. In the corners, this limit is 1.

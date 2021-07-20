def find_next_empty(puzzle) :
  #finds the next row, col on the puzzle which is empty(empty spaces are represented with -1)
  #return row,col tuple(or (None,None) if there is no empty space)
  for r in range(9):
    for c in range(9):
      if puzzle[r][c] == -1:
        return r, c
  return None,None #if there is no empty space

def is_valid(puzzle,guess,row,col): 
  #function to check the guess is valid or not
  #returns True if it is valid,False otherwise
  
  #checks if the guess is in the row:
  row_vals = puzzle[row]
  if guess in row_vals:
    return False
  
  #checks if the guess is in the column
  col_vals = []
  for i in range(9):
    col_vals.append(puzzle[i][col])
  if guess in col_vals:
    return False
  
  #checks if the guess is in the 3 x 3 square
  row_start = (row // 3) * 3 #(1 // 3)= 0,(4 // 3)=0,..
  col_start = (col // 3) * 3
  for r in range(row_start,row_start+3):
    for c in range(col_start,col_start+3):
      if puzzle[r][c] == guess:
        return False
      
  #if we reach here all the possible checks for checking whether our guess is valid or not
  return True

def solve_sudoku(puzzle):
  #solve sudoku using backtracking technique
  #our puzzle is a lists of lists where the rows of the puzzles are inner lists of our column
  #mutates the puzzle(if solution exists) and return if a solution exists
  
  #step 1: choose somewhere on the puzzle to make guess
  row, col = find_next_empty(puzzle)
  if row is None:  #if there are no empty spaces then the puzzle is already solved
    return True
  
  #step 2: we have to guess the number between 1 to 9 to put in the empty space
  for guess in range(1,10):      #if there are empty spaces we have to guess the number between 1 to 9
    #step 3:To check whether our guess is valid or not
    if is_valid(puzzle,guess,row,col):  
      puzzle[row][col] = guess   #place the guess on the puzzle
      #Now we have to recursively call our function to fill the all other empty spaces
      #step 4:Recursively call the function
      if solve_sudoku(puzzle):
        return True
    #step 5:if guess does not solve the puzzle then we have to backtrack and try a new number
    puzzle[row][col] = -1 #reset the guess
  #step 6: if none of the numbers we try work then the puzzle is UNSOLVABLE!!
  return False
if __name__ == '__main__':
   board = [ ]
    for i in range(0, 9):
     vals = [int(input()), int(input()), int(input()), int(input()),int(input()),int(input()),int(input()),int(input()),int(input())]
     board.append(vals)
print(solve_sudoku(board))
print(board)
      
      
      
    
  

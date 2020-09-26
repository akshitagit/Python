rows = 3
columns = 3

matrix = [ [3,30,38], [44,52,54], [57,60,69] ]
value = 5


def get_row_index( value ):
  row_index = -1
  
  for row in matrix:
    first_number_row = row[0]
    if first_number_row <= value:
      row_index += 1
      
  return row_index
  
def search_value_on_sorted_matrix(matrix, value):
  row_index = get_row_index(value)
  if row_index == -1:
    return 0
  
  row = matrix[ row_index ]
  print(row)
  
  if value in row:
    return 1
    
  
  return 0

 
  

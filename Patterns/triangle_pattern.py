rows = int(input( "please put the number of rows: "))

total_columns = rows + (rows-1) 
spaces = rows-1

def get_numerical_patron_row( row ):
  text = ""
  for i in range(row, 2*row ):
    text += str(i) + ' '

  right_side = text[0:(row-1)*2]
  right_side = right_side[::-1]
  right_side = right_side[1:]
  
  text += right_side
  
  return text


for y in range(0, rows):
  strip_spaces = "  "*spaces
  
  text = get_numerical_patron_row( (y + 1) )
  
  row = strip_spaces + text
  print(row)
  
  spaces -=  1
    

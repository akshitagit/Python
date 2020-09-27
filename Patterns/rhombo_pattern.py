
def draw_rhombo_pattern(num_rows):
  spaces = 0
  characters = int(num_rows/2) +1 

  middle_row_index = int(num_rows/2)

  for y in range(num_rows):
    left_part = '* '*characters
    center_left = '  '*spaces
    center_right = center_left[2:]
    
    if y == 0 or y == num_rows-1:
      right_part = left_part[2:]
    else:
      right_part = left_part[:]
      
    print(left_part + center_left + center_right + right_part)
    
    if y < middle_row_index:
      characters -= 1
      spaces += 1  
    else:
      characters += 1
      spaces -= 1

num_rows = int( input('please put a odd number between 1 and 9: ') )

if num_rows < 1 or num_rows > 9:
  print(" Error: number out of the range ")
else:
  if num_rows % 2 == 1:
    draw_rhombo_pattern(num_rows)
  else:
    print(" Error: this program only accept odd numbers")

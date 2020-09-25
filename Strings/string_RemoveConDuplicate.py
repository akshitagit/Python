string = input()
# Function to remove same consecutive characters from the string
def removeC(string):
    temp_Str = ""
    for i in range(len(string)-1):
        if string[i]  != string[i+1]:
            temp_Str = temp_Str + string[i]    # Copying Unique elements to the string temp_Str
    return temp_Str
string = removeC(string)
print(string)
    

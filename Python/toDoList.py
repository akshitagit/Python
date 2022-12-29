# Ask user number of inputs it does wants to have.
# Ask user after completing the input whether it wants to shows the list, enter another input or just exit the whole thing.
# Add, if yes then how much?
# Show?
# Exit?
# 
def userInput():
    taskList = {}
    askList = ["add", "show", "remove", "exit", "clear all the list", "clear all", "clear", "all","clear the list", "exit()"]
    while True:
        ask = input("Do you want to\nAdd\nShow\nRemove\nExit\nClear all the list.\nEnter the Input:- ")
        if ask.lower() in askList:
            break
        else:
            continue
    askLower = ask.lower()
    match askLower:
        case "add":
            howMuch = input("Amount of input you want to do")
            i = 0
            while i < howMuch:
                appendVar = input("Input the task you want to add to the list.")
                taskList.append(appendVar)
                i ++
            break
        case "show":
            for count, ele in enumerate(taskList):
                print("{0}. {1}".format(count, ele))
            break
        case "remove":
            # remove method can be used but with only try and except and else method.
            # pop method can be used but with only enumeration thing it can be done.
            # del method can also be used but with only # it doesn't return anything so...hm ...all of them will have to be used by try and except method.
        case "exit":
        case "exit()":
            break # Should be able to break the bigger loop, I must say so.
        
userInput()
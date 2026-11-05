#christmas tree

#and then user input for how big the tree will be
tree_size = (int(input("how big is your christmas tree? (please say 10): ")) * 3)#times 3 because user may inpuyt a less impressive tree size
#so first variable for how much spaces is needed at the top, spaces need to minus tree size - 1
#i realize spaces need to be behind tree_size
spaces = int(tree_size)
#THIS BLOCK BELOW IS FOR AESTHETIC TEMPORARILY (because i cant figure out the spaces yet)
ok = False
if tree_size / 3 == 10:
    spaces -= 16
    ok = True
#for loop with ifs to minus spaces by 1 each time i iterates
for i in range(1, tree_size, 2):
    
    print((spaces * " "), (i * "*"))
    spaces -= 1
#and then the tree stump, 
#if user input 15, there are 43 asterisks and 25 spaces in the last line, and idk why
#ill just add a if for the tree stump, chceking i for if it becomes tree size
    # if i == i / 2 - 1:
    #     print("crazy")
    # print(i)
#i dont know whats going on
if ok == True:
    print("            |||||||")
    print("            |||||||")
    print("            |||||||")
    print("")
print("HAPPY CHRISTMAS!!!")
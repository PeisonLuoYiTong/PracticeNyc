#christmas tree

#and then user input for how big the tree will be
tree_size = (int(input("how big is your christmas tree?: ")) * 3)#times 3 because user may inpuyt a less impressive tree size
#so first variable for how much spaces is needed at the top, spaces need to minus tree size - 1
spaces = (tree_size - 1) // 2
#for loop with ifs to minus spaces by 1 each time i iterates
for i in range(1, tree_size, 2):
    #concatenate instead of doing print((),()) because that adds a space
    print(spaces * " " + i * "*")
    spaces -= 1
#and then the tree stump
print("HAPPY CHRISTMAS!!!")
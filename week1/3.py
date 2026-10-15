#Ask for the width and the height of a rectangle, then calculate the perimeter and the area of the rectangle (search to find the formulas)

#formulas:
    #perimeter: 
        #P = 2 × (height + width) or P = 2 × height + 2 × width
    #area: 
        #multiply its width by its height

#ask user width and height
w = float(input("input width: "))
h = float(input("input height: "))

#calculate
p = 2 * (h + w)
a = w*h 

#print
print(f"Perimeter of your rectangle: {p}\nArea of your rectangle: {a}")
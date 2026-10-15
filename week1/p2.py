#ask user weight
weight = float(input("type your weight: "))
#ask user kg or lb
kg_or_lb = input("kg or lbs?: ")
weight_unit = ""
#check is user input is kg or lb then run calculations
if kg_or_lb == "kg":
    weight *= 2.20462
    weight_unit = "lbs"
else:
    weight *= 0.453592
    weight_unit = "kg"

#print weight message
print(f"your weight in {weight_unit} is {weight}")
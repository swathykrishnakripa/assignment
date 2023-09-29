def calculate_area(length, width):
    if length == width:
        return "This is a squire!"
    else:
        return length*width

length = float(input("Enter the value of length:"))
width = float(input("Enter the value of width:"))

result = calculate_area(length, width)
print(result)
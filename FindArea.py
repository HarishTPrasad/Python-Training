def area_circle(r):
    if r < 0:
        raise ValueError("radius cannot be negative")
        # print("Value cannot be nagative")
    return 3.14 * r**2

def area_square(s):
    if s < 0:
        raise ValueError("side cannot be negative")
        # print("Value cannot be nagative")
    return s**2


def main():

    a = int(input("Enter any value 1 or 2 : "))

    if a == 1:
        r = float(input("Enter the radius of circle here : "))
        area = area_circle(r)
        print(f"The area of the circle {r} is : {area}")

    elif a == 2 :
        s = float(input("enter the side of the square here : "))
        area = area_square(s)
        print(f"the area of the square {s} is : {area}")

    else :
        print("You have to select on of the Availabe options ")
        # raise ValueError("You have to select on of the Availabe options")


    # try:
    #     r = float(input("enter the radius : "))
    #     area = area_circle(r)
    #     print(f"the area of the {r} is: {area:.2f}")
    # except ValueError as e:
    #     print(f"Error: {e}")



if __name__ == "__main__":
    main()
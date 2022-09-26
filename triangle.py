import triangleUtils

triangle = "start"

while triangle != "exit":
    triangle = input("To continue, press any key or 'exit' to quit: ")

    if triangle != "exit":
        while True:
            try:
                a = int(input("What is first Side: "))
                b = int(input("What is second Side: "))
                c = int(input("What is third Side: "))
                print(triangleUtils.length_of_triangle(a,b,c))
                break

            except Exception:
                print("Please write the valid input")

    else:
        print("Thank you for using the app")
        break
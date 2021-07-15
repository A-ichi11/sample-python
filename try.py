while True:
    try:
        x= int(input("please enter a number"))
        print(x)
    except ValueError:
        print("Oops! That")
    finally:
        print("exec")

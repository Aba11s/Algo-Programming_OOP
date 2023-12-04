from setting import Shopping_List

def create_list():
    food_list = []
    print("How many items would you like to order? ",end="")
    while True:
        try:
            user_input = int(input(""))
            if user_input < 1:
                print("Number of items must be at least 1. Please re-enter: ",end="")
            else:
                break

        except (ValueError,NameError,TypeError):
            print("Invalid input. Please re-enter: ",end="")

    for i in range(user_input):
        print(f"#item {i+1}-")
        food_input = str(input("Enter food: "))
        print("Enter amount of pounds: ",end="")
        nested = True
        while nested:
            try:
                amt_input = float(input(""))
                if amt_input <= 0:
                    print("Amount must be greater than 0. Please re-enter: ",end="")
                else:
                    nested = False

            except (ValueError,NameError,TypeError):
                print("Invalid inpur. Please re-enter: ",end="")
        
        food_list.append(Shopping_List(food_input,amt_input))
    return food_list

def show_items(list):
    for item in list:
        print(item.__str__())

list1 = create_list()
show_items(list1)

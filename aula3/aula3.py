print("Initializing program...")

def show_welcome_message(name, world,message= "This is so amazing"):
    print("Hello, " + name )
    print("Welcome to the amazing world of " + world)
    print(message)


def calculate_bmi(weight, height):
    bmi = weight / height ** 2 
    return bmi


def calculate(order_total, has_tip=True):
    if not has_tip:
        return order_total
    
    total = order_total * 1.10
    return total


show_welcome_message("Leonardo", "Saturn")
print("Finished")




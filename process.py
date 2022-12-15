def printing_report(dic, money):
    print("----Report----")
    print("Water :", dic["water"], "ml")
    print("Milk :", dic["milk"], "ml")
    print("Coffee :", dic["coffee"], "ml")
    print("Money: $", money)


def money_read():
    # quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
    quarters = int(input("quarters"))
    dimes = int(input("dimes"))
    nickles = int(input("nickles"))
    pennies = int(input("pennies"))
    return quarters,dimes,nickles,pennies

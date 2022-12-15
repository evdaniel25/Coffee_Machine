import data as da                                           #Contains data on resources needed and available resources
import process as pr                                        #Contains method to print report and read money

res = da.resources
money = 0
choice = input("What would you like? (espresso/latte/cappuccino):")
while choice != "off":
    if choice == 'report':
        pr.printing_report(res, money)
    elif choice == 'espresso':
        if res["water"] < da.MENU["espresso"]["ingredients"]["water"] or res["coffee"] < da.MENU["espresso"]['ingredients']["coffee"]:
            if res["water"] < da.MENU["espresso"]["ingredients"]["water"]:
                print("Sorry there is not enough water")
            if res["coffee"] < da.MENU["espresso"]['ingredients']["coffee"]:
                print("Sorry there is not enough coffee")
        else:
            q, d, n, p = pr.money_read()
            money_inserted = round((q * .25) + (d * .10) + (n * .05) + (p * .01), 2)
            if money_inserted < da.MENU["espresso"]["cost"]:
                print("Sorry that's not enough money. Money refunded.")
            else:
                if money_inserted > da.MENU["espresso"]["cost"]:
                    money_to_give = round(money_inserted - da.MENU["espresso"]["cost"], 2)
                    money = money + da.MENU["espresso"]["cost"]
                    print(f'Here is {money_to_give} dollars in change.')
                else:
                    money = money + da.MENU["espresso"]["cost"]
                res["water"] = res["water"] - da.MENU["espresso"]["ingredients"]["water"]
                res["coffee"] = res["coffee"] - da.MENU["espresso"]["ingredients"]["coffee"]
    elif choice == 'latte':
        if res["water"] < da.MENU["latte"]["ingredients"]["water"] or res["milk"] < da.MENU["latte"]["ingredients"][
            "milk"] or res["coffee"] < da.MENU["latte"]["ingredients"]["coffee"]:
            if res["water"] < da.MENU["latte"]["ingredients"]["water"]:
                print("Sorry there is not enough water")
            if res["water"] < da.MENU["latte"]["ingredients"]["water"]:
                print("Sorry there is not enough water")
            if res["coffee"] < da.MENU["latte"]['ingredients']["coffee"]:
                print("Sorry there is not enough coffee")
        else:
            q, d, n, p = pr.money_read()
            money_inserted = round((q * .25) + (d * .10) + (n * .05) + (p * .01), 2)
            if money_inserted < da.MENU["latte"]["cost"]:
                print("Sorry that's not enough money. Money refunded.")
            else:
                res["water"] = res["water"] - da.MENU["latte"]["ingredients"]["water"]
                res["milk"] = res["milk"] - da.MENU["latte"]["ingredients"]["milk"]
                res["coffee"] = res["coffee"] - da.MENU["latte"]["ingredients"]["coffee"]
                if money_inserted > da.MENU["latte"]["cost"]:
                    money_to_give = round(money_inserted - da.MENU["latte"]["cost"], 2)
                    money = money + da.MENU["latte"]["cost"]
                    print(f'Here is {money_to_give} dollars in change.')
                else:
                    money = money + da.MENU["latte"]["cost"]
    elif choice == 'cappuccino':
        if res["water"] < da.MENU["cappuccino"]["ingredients"]["water"] or res["milk"] < \
                da.MENU["cappuccino"]["ingredients"]["milk"] or res["coffee"] < da.MENU["cappuccino"]["ingredients"][
            "coffee"]:
            if res["water"] < da.MENU["cappuccino"]["ingredients"]["water"]:
                print("Sorry there is not enough water")
            if res["water"] < da.MENU["cappuccino"]["ingredients"]["water"]:
                print("Sorry there is not enough water")
            if res["coffee"] < da.MENU["cappuccino"]['ingredients']["coffee"]:
                print("Sorry there is not enough coffee")
        else:
            q, d, n, p = pr.money_read()
            money_inserted = round((q * .25) + (d * .10) + (n * .05) + (p * .01), 2)
            if money_inserted < da.MENU["cappuccino"]["cost"]:
                print("Sorry that's not enough money. Money refunded.")
            else:
                res["water"] = res["water"] - da.MENU["cappuccino"]["ingredients"]["water"]
                res["milk"] = res["milk"] - da.MENU["cappuccino"]["ingredients"]["milk"]
                res["coffee"] = res["coffee"] - da.MENU["cappuccino"]["ingredients"]["coffee"]
                if money_inserted > da.MENU["cappuccino"]["cost"]:
                    money_to_give = round(money_inserted - da.MENU["cappuccino"]["cost"], 2)
                    money = money + da.MENU["cappuccino"]["cost"]
                    print(f'Here is {money_to_give} dollars in change.')
                else:
                    money = money + da.MENU["cappuccino"]["cost"]
    choice = input("What would you like? (espresso/latte/cappuccino):")

def menu():
    print("Welcome to Bethesda Restaurant")
    print("1. Breakfast")
    print("2.Lunch")

###
def handle_selection (selected_value):
    if "selected_value" ==1:
        print("You have selected breakfast.")
        print("Pancakes is shs20,000.")
        print("Omelette and toast is shs20,000.")
        print("cake is shs20,000.")
        print("All come with Black tea or milk teaprint.")
    elif "selected_value" == 2:
        print("You have selected Lunch.")
        print("Beans is shs20,000.")
        print("Chicken is shs20,000.")
        print("Fish is shs25,000.")
        print("All dises come with a side of rice, chips or matooke and a cold drink.")
    else:
        print("Please enter correct selection.")

    def main():
        menu()
        selected_value = int(input("Please make a choice:"))
        #handle_selection(selected_value):

if __name__ ==  "__main__":
    main()

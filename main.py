import mytheater as mt #THEATER MODULE IS TAKEN
import mycolor   #COLOR MODULE IS IMPORT TO CHANGE THE COLOR OF THE OUTPUT

color = mycolor.color() #REFRENCE OBJECT OF COLOR MODULE
print(color.BOLD + color.PURPLE + color.UNDERLINE + "WELCOME TO PYTHON THEATER\n" + color.END)
print(color.BOLD + "To Start Operating Create The Auditorium" + color.END)
row = int(input("Enter The Number Of Rows For Seating\n"))
col = int(input("Enter The Number Of Column For Seating\n"))
theater = mt.Theater(row, col)
theater.price()
print(color.DARKCYAN + color.BOLD + "="*40,"" + color.END)
print("\nWhat Action Would You Like To Perform")
theater.menu()
while (True):
    choice = int(input("Enter Your Chice Here: "))
    if choice == 1:
        print()
        print(color.BOLD + color.PURPLE + "Avilable seats:" + color.END)
        theater.showseats()
        print(color.DARKCYAN + color.BOLD + "=" * 40, "" + color.END)
        print(color.BOLD + color.GREEN + "Would You Like To Do Anything Else" + color.END)
        theater.menu()
    elif choice == 2:
        print()
        print(color.BOLD + color.YELLOW + "Enter The Row And Column Number You Would Like To seat" + color.END)
        buy_row, buy_col = input().split()
        theater.buyticket(buy_row, buy_col)
        theater.showseats()
        print(color.DARKCYAN + color.BOLD + "=" * 40, "" + color.END)
        print(color.BOLD + color.GREEN + "Would You Like To Do Anything Else" + color.END)
        theater.menu()
    elif choice == 3:
        print()
        print(color.BOLD + color.PURPLE + "Here Are The Statistics" + color.END)
        theater.showseats()
        theater.getstats()
        print(color.DARKCYAN + color.BOLD + "=" * 40, "" + color.END)
        print(color.BOLD + color.GREEN + "Would You Like To Do Anything Else" + color.END)
        theater.menu()
    elif choice == 4:
        print()
        print(color.BOLD + color.YELLOW + "Enter Booked Seat Number To Get Booked Ticket User Info" + color.END)
        get_row, get_col = input().split()
        print(color.BOLD + color.PURPLE + "Here Are The Booked Ticket User Info" + color.END)
        theater.user_info(get_row, get_col)
        print(color.DARKCYAN + color.BOLD + "=" * 40, "" + color.END)
        print(color.BOLD + color.GREEN + "Would You Like To Do Anything Else" + color.END)
        theater.menu()
    elif choice == 0:
        print(color.DARKCYAN + color.BOLD + "=" * 40, "" + color.END)
        print()
        print(color.BOLD + color.BLUE + "Thank You, Have A Great Day!!" + color.END)
        exit()
    else:
        print(color.BOLD + color.RED + "Enter Valid Input" + color.END)

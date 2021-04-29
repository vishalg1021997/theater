##Aaj apun banaeyga apna personal theater

import mycolor #COLOR MODULE IS IMPORT TO CHANGE THE COLOR OF THE OUTPUT
color = mycolor.color()

class Theater: #CLASS THEATER IS CREATED
    def menu(self):    #MENU IS CREATED SO USER CAN SEE THE OPTION AVILABE SO USER CAN PERFORM THE ACTION
        print("1 Show The Seats")  # done
        print("2 Buy A Ticket")  # done
        print("3 Get Statistics")  # done
        print("4 Show Booked Ticket User Info")  # done
        print("0 Exit")  # done

    def __init__(self, row, col): #TO CREATE THE AUDITORIUM OF THE THEATER
        print("Total Seats:")
        self.row = row      #TAKE THE NUMBER OF ROW
        self.col = col      #TAKE THE NUMBER OF COLUMN
        self.details = {}   #TO STORE THE DETAILS OF USER AFTER BOOKING THE TICKET SEAT NUMBER WILL BE THE KEY
        self.matrix = []    #TO STORE THE TOTAL SEATS WHICH IS CREATED IN LIST IN LIST FORMAT (MATRIX FORMAT)
        self.pricing = {}   #TO STORE THE PRICE FOR EACH SEAT
        for i in range(self.row): #LOOP WILL ITERATE TO THE NUMBER OF ROWS GIVEN BY USER
            a = [] # EMPTY LIST WHERE THE SEATS WILL BE STORE i.e"S IT WILL BE EMPTY AFTER EACH COMPLETION OF LOOP"
            for j in range(self.col): #NESTED LOOP WILL ITERATE TO THE NUMBER OF COLUMN GIVEN BY USER
                a.append("S")#S DENOTES AS NUMBER OF VACANT SEATS AVILABLE WHICH WILL BE DISBLAYED TO USER
                             #S WILL BE STORE IN LIST a SO WE WILL HAVE NUMBER OF VACANT SEAT IN LIST
            self.matrix.append(a)#THE LIST a WILL BE APPEND IN MATRIX AS SUB LIST
        print(end="  ") #TO DISPLAY IN SPACE SEPRATED
        for j in range(self.col):#LOOP WILL ITERATE TO THE COLUMN GIEN BY USER
            print(j + 1, end=" ")#INCREMENT OF NUMBER OF COLUMN DISPLAY
        print()#TO GO TO NEXT LINE
        for i in range(self.row):#LOOP WILL ITERATE TO THE ROW NUMBER GIVEN BY USER
            print(i + 1, end=" ")#THIS WILL DISPLAY THE ROW NUMBER
            for j in range(col):#LOOP WILL ITERATE TO THE COLUMN NUMBER GIVEN BY USER
                print(self.matrix[i][j], end=" ")#SUBLIST STORE IN MATRIX WILL BE DISPLAYED
            print()#TO GO TO NEXT LINE

    def showseats(self):#TO DSIPAY UPDATED THE SEATS STORE IN MATRIX
        a = 0
        b = 0
        print(end="  ")
        for j in range(1, self.col + 1):#LOOP WILL ITREATE TO THE COLUMN GIVEN BYS USER TO SHOW THE COLUMN NUMBER
            b = b + 1 #INCREMENT BY 1
            print(b, end=" ")
        print()
        for i in self.matrix: #LOOP WILL ITREATE TO THE ROW GIVEN BYS USER TO SHOW THE ROW NUMBER
            a = a + 1 #INCREMENT BY 1
            print(a, end=" ")
            print(" ".join(i), sep=",") #JOIN AND SEPRATER USED TO DISPLAY THE SEATS WITHOUTH BRACKET AND COMA

    def price(self):#TO CALCULATE THE PRICE
        if self.row * self.col <= 60:              #IF THE SEATS ARE LESS THAN 60 THE PRICE OF EACH SEAT
            for i in range(1, self.row + 1):       #WILL BE 10
                for j in range(1, self.col + 1):
                    a = {}    #THE PRICE WILL BE STORE IN DICTIONARY EACH SEAT WILL HAVE ITS OWN PRICE
                    a[i, j] = 10
                    self.pricing.update(a) #THE PRICE AND VALUE WILL BE ADDED IN PRICING DICTIONARY TO USE LATER
        elif self.row * self.col > 60:  #IF THE TOTAL SEAT IS MORE THAN 60 THEN THE FRONT HALF SEAT PRICE WILL BE 9
                                        #AND THE OTHER HALF PRICE WILL BE 10
            c = self.row // 2           #TO GET THE HALF VALUE OF ROW
            b = self.col // 2           #TO GET THE HALF VALUE OF COLUMN
            for i in range(1, self.row + 1):  #LOOP IS CREATED TO ITERATE TO THE ROW AND NESTED LOOP FOR COLUMN
                for j in range(1, self.col + 1):#SO WE CAN GET SEAT NUMBER OF EACH ROW AND COLUMN
                    a = {}     #EMPTY DICTIONAR TO STORE THE PRICE OF EACH UNIQUE SEAT
                    a[i, j] = 8             #SEAT ALONG WITH PRICE IS STORE
                    self.pricing.update(a) # IN PRICING HERE THE PRICE OF ALL SEAT IS 9
            for i in range((c + 1), self.row + 1):#TO CHANGE THE PRICE OF FRONT HALF SEAT TO 10 IN THE AUDI
                for j in range(1, self.col + 1):
                    a = {}
                    a[i, j] = 10            #SEAT ALONG WITH PRICE FOR FRONT HALF IS STORE
                    self.pricing.update(a)  #FRONT HALF SEAT PRICE WILL BE UPDATED TO 10

    def getstats(self):  #TO GET THE STATISTICS OF THE THEATER
        count1 = 0   #TO COUNT THE NUMBER OF BOOKED SEAT
        count2 = 0   #TO COUNT THE NUMBER OF VACANT SEAT
        current_income = 0  #TO CALCULATE THE BOOKED SEAT INCOME
        total_income = 0    #TO CALCULATE THE TOTAL INCOME OF THE THEATER COULD BE GENERATED
        for i in self.details.items(): #THE BOOKED SEAT DETAILS ARE STROE IN detail DICT LOOP WILL ITERATE
            a = i[1]                   #AND FOR EACH BOOKED SEAT IT WILL GET THE PRICE
            b = a[4]
            current_income = current_income + b #INCOME BY BOOKED SEAT WILL BE STORE HERE
        for i in self.pricing.items():  #THE PRICE FOR ALL THE SEATS ARE STORE IN pricing DICT LOOP WILL ITERATE
            total_income = total_income + i[1] #IT WILL CALCULATE THE PRICE FOR ALL SEAT IN THE THEATER
        for i in self.matrix: #LOOP WILL ITERATE TO THE MATRIX LIST
            for j in i:        #NESTED LOPP WILL ITTERATE TO THE SUB_LIST STROE IN MATRIX LIST
                if j == 'B':  #IF THE VALUE OF SEAT IS B IT WILL INCREMENT THE VALUE OF BOOKED SEAT
                    count1 = count1 + 1
                elif j == 'S':  #IF THE VALUE OF SEAT IS S IT WILL INCREMENT THE VALUE OF VACANT SEAT
                    count2 = count2 + 1
        print(color.BOLD + "Number Of Purchased Tickets: ", count1) #NUMBER OF BOKKED TICKET WILL BE DISPLAYED
        print("Percentage Of Booked Tickets: ", (count1 / (count2 + count1)) * 100) #PERCENTAGE OF BOOKING DONE
        print("Current Income: ", current_income)  #TO DISPLAY THE CURRENT INCOME GENNERATED
        print("Total Income: ", total_income, " " + color.END) #TO DISPLAY THE INCOME COULD BE GENERATED

    def user_info(self, row, col):#TO GET THE BOOKED TICKET USER INFO
        self.getrow = row  #GET THE ROW AND COLUMN FROM THE USER WHICH IS THE SEAT NUMBER OF THE USER AND IT WILL
        self.getcol = col #SEARCH THE DETAILS IN THE details DICT AND THE DETAILS OF THE CUST WILL BE DISPLAYED
        if (int(self.getrow),int(self.getcol)) not in self.details:
            print(color.RED + color.BOLD + "\nPlease Enter The Correct Booked Seat Number\n" + color.END)
        else:
            print(color.BOLD + "Name: ", self.details[int(self.getrow), int(self.getcol)][0])
            print("Gender: ", self.details[int(self.getrow), int(self.getcol)][1])
            print("Age: ", self.details[int(self.getrow), int(self.getcol)][2])
            print("Phone Number: ", self.details[int(self.getrow), int(self.getcol)][3])
            print("Ticket Price: ", self.details[int(self.getrow), int(self.getcol)][4], "\n " + color.END)

    def buyticket(self, row, col): #TO BOOK THE SEAT
        self.buyrow = row #TO TAKE THE SEAT NUMBER FROM THE USER WHERE HE WILL LIKE TO BOOK
        self.buycol = col # i.e ROW AND COLUM NUMBER
        if (int(self.buyrow),int(self.buycol)) not in self.pricing:
            print(color.RED + color.BOLD + "Please Enter The Correct Seat Number" + color.END)
        else:
            if self.matrix[int(self.buyrow)][int(self.buycol)] == "B": #IF THE SEAT IS ALREAYD BOOKED
                print("Seat Already Booked Book Another Seat" + color.END)#IT WILL DSPLAY ALREADY BOOKED
            else: #IF THE SEAT IS VACANT IT WILL DISPLAY THE PRICE OF TICKET AND ASK FOR CONFIRMATION
                print("Price Of The Ticket: ", self.pricing[(int(self.buyrow), int(self.buycol))])
                confirm = input("To Confirm Your Booking Click Y\n")
                if confirm == "Y":
                    a = {} #EMPTY DICT  IS CREATED TO STORE THE VALUE GIVEN BY USER LIKE NAME AGE NUMBER
                    customer_name, customer_gender, customer_age, customer_phone = input("Enter Your Name Gender Age Phone Number: \n").split()
                    if int(customer_age) > 17 and len(customer_phone) == 10:
                        #THE VALUE IS GETTING STORED IN GIVEN SEAT NUMBER BY USER WITH HIS DETAILS IN a DICT
                        a[int(self.buyrow), int(self.buycol)] = list((customer_name, customer_gender, int(customer_age),int(customer_phone),self.pricing[(int(self.buyrow), int(self.buycol))]))
                        self.details.update(a)#VALUE OF A WILL BE UPDATED IN details DICT
                        self.matrix[int(self.buyrow)][int(self.buycol)] = "B" #THE SEAT NUMBER VALUE IN THE LIST WILL BE CHANGE TO B
                        print(color.BOLD + color.PURPLE + "Your Booking Is Done" + color.END) #SHOWING AS BOOKED
                    else:
                        print(color.RED + "\nPeople Between Age 18 and 60 Are Allowed and Check If The Phone Number Enter Is COrrect \n" + color.END)
                else:#IF THE USER CLICK ANOTHER BUTTON EXCEPT Y THE BOOKING WILL BE CANCELLED
                    print(color.BOLD + color.RED + "Your Current Booking Was Tarminated" + color.END)

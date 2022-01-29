import json
class Food:

    dict_food_items = {}
    list_food_names = []
    list_foodid = set()
    user_profile = {}
    c = 0

    def __init__(self):
        pass

    def def_main(self):
        while True:                                            #Repeat Menu until stops.
            print("\t(A) Admin Login \n",
                  "\t(U) User Login \n"
                  "\t(R) Register New User \n",
                  "\t(E) Exit \n")

            input_1 = str(input("Please Select Your Operation: ")).upper()
            if len(input_1) == 1:
                if input_1 == 'A':
                    self.def_Admin()
                    break
                elif input_1 == 'U':
                    self.def_User()
                    break
                elif input_1 == 'R':
                    self.def_Register()
                elif input_1 == 'E':
                    print('Thankyou!!!')
                    exit()
                else:
                    print("ERROR: Invalid Input (" + str(input_1) + "). Try again!")
            else:                                                                                     #If input length not equal to 1...
                print("ERROR: Invalid Input (" + str(input_1) + "). Try again!")

    def def_Admin(self):
        username = str(input("Enter Login UserName: "))
        password = str(input("Enter Login Password: "))
        print('Hello '+username)
        while True:
            print("\t (A) Add Food Items \n",
                  "\t (M) Modify/Edit Food Items \n"
                  "\t (V) View Food Items \n",
                  "\t (B) Back to Main Menu \n"
                  "\t (E) Exit \n")
            input_1 = str(input("Please Select your Option: ")).upper()
            if len(input_1) == 1:
                if input_1 == 'A':
                    self.add_food_items()
                elif input_1 == 'M':
                    print(json.dumps(Food.dict_food_items, sort_keys=False, indent=4))
                    self.edit_food_items()
                elif input_1 == 'V':
                    self.view_food_items()
                elif input_1 == 'B':
                    self.def_main()
                elif input_1 == 'E':
                    print('Thankyou!!!')
                    exit()
                else:
                    print("ERROR: Invalid Input (" + str(input_1) + "). Try again!")
            else:
                print("ERROR: Invalid Input (" + str(input_1) + "). Try again!")

    def def_User(self):
        username = str(input("\nEnter Login UserName: "))
        password = str(input("Enter Login Password: "))
        print('Hello '+username)
        while True:
            print("\t (O) Place New Order \n",
                  "\t (H) Order History \n",
                  "\t (U) Update Profile \n"
                  "\t (M) Main Menu \n",
                  "\t (E) Exit \n")
            input_1 = str(input("Please Select your Option: ")).upper()
            if len(input_1) == 1:
                if input_1 == 'O':
                    self.take_user_order()
                elif input_1 == 'H':
                    self.order_history()
                elif input_1 == 'U':
                    self.update_profile()
                elif input_1 == 'M':
                    self.def_main()
                elif input_1 == 'E':
                    print('Thankyou!!!')
                    exit()
                else:
                    print("ERROR: Invalid Input (" + str(input_1) + "). Try again!")
            else:
                print("ERROR: Invalid Input (" + str(input_1) + "). Try again!")

    def def_Register(self):
        try:
            uname = str(input("Enter Full Name: "))
            uphn = int(input("Enter Phone Number: "))
            uemail = str(input("Enter Email: "))
            uaddress = str(input("Enter Address: "))
            upassword = str(input("Enter Password: "))
            Food.user_profile[uname] = {"Phone": uphn, "Email": uemail, "Address" : uaddress, "Password": upassword}
            print("\nYou are registered successfully!!!\n")
        except Exception as e:
            print("Please enter valid value or user", uname, "already exists")
            self.def_Register()
        self.def_User()

    def add_food_items(self):
        while True:
            try:
                Total_Items = int(input("Enter Total Items in menu: "))
                break
            except Exception as e:
                print("Please enter valid value")
        for foodid in range(1, Total_Items+1):
            while True:
                try:
                    self.fname = str(input("Enter Food Item Name: ").upper())
                    self.fqty = int(input("Enter Food Quantity: "))
                    self.fprice = int(input("Enter Food Price: "))
                    self.fstock = int(input("Enter Stock: "))
                    self.fdiscount = int(input("Enter Discount Percent: "))
                    assert self.fdiscount <= 100, "Discount Percent cannot be greater than 100"
                    break
                except Exception as e:
                    print("Please enter valid value")
            if (foodid not in Food.dict_food_items) and (self.fname not in Food.list_food_names):
                Food.dict_food_items[foodid] = {'Name': self.fname, 'Quantity': self.fqty, 'Price': self.fprice, 'Discount': self.fdiscount, 'Stock': self.fstock}
                print("\n"+self.fname+" added Successfully in Menu!!! \n")
                Food.list_food_names.append(self.fname)
                Food.list_foodid.add(foodid)
            else:
                print(self.fname+' already present in the menu')

    def view_food_items(self):
        print("List of Food Items Present in Menu\n", Food.list_food_names)
        print("\n****************Food Items in Menu*******************\n")
        '''
        vals = []
        for k, v in Food.dict_food_items.items():
            for ki, vi in v.items():
                vals.append(vi)
        print("Name\tQuantity(gm/ml)\tPrice(Rs.)\tDiscount\tStock")
        for value in vals:
            print(value, end="\t\t")
        '''
        print(json.dumps(Food.dict_food_items, sort_keys=False, indent=4))

    def edit_food_items(self):
        while True:
            try:
                fid = int(input("\nEnter FoodID of Item to edit:"))
            except Exception as e:
                print("\nPlease enter valid value")
            if fid in Food.list_foodid:
                try:
                    Food.dict_food_items[fid]["Quantity"] = int(input("Enter Food Quantity: "))
                    Food.dict_food_items[fid]["Price"] = int(input("Enter Food Price: "))
                    Food.dict_food_items[fid]["Discount"] = int(input("Enter Stock: "))
                    Food.dict_food_items[fid]["Stock"] =  int(input("Enter Discount Percent: "))
                    assert Food.dict_food_items[fid]["Stock"] <= 100, "Discount Percent cannot be greater than 100"
                    break
                except Exception as e:
                    print("\nPlease enter valid value\n")
            else:
                print("\nFoodID does not exist in Menu\n")
                break

            print(json.dumps(Food.dict_food_items, sort_keys=False, indent=4))


    def take_user_order(self):
        if len(Food.dict_food_items) == 0:
            print("No Menu Defined")
            return
        else:
            print("****************Menu*********************")
            print(json.dumps(Food.dict_food_items, sort_keys=False, indent=4))
        while True:
            try:
                self.user_items = list(map(int, input("\nEnter space separeted FoodId: ").split()))
                break
            except Exception as e:
                print("Please enter valid value")

        print("\nFood Cart:", self.user_items)
        Food.c = input("\nPlace order y/n: ")
        if Food.c:
            payment = 0
            for item in self.user_items:
                payment = payment + (Food.dict_food_items[item]["Price"] * (1 - Food.dict_food_items[item]["Discount"]/100)) * Food.dict_food_items[item]["Quantity"]
            print("\n\n Order Placed Successfully!! \n\n Total Amount is: Rs.", payment, "\n")
        else:
            print("\nHistory not found!!\n")
            return

    def order_history(self):
        if Food.c:
            print("\n******Order History********\n")
            for i in self.user_items:
                print(Food.dict_food_items[i]["Name"])

    def update_profile(self):
        try:
            Food.user_profile["Phone"] = int(input("Enter Phone Number: "))
            Food.user_profile["Email"] = str(input("Enter Email: "))
            Food.user_profile["Address"] = str(input("Enter Address: "))
            Food.user_profile["Password"] = str(input("Enter Password: "))
            print("\nChanges done successfully!!!\n")
            return
        except Exception as e:
            print("\nPlease enter valid value")
            update_profile()



print("\n******************Welcome*******************\n")
obj = Food()
obj.def_main()

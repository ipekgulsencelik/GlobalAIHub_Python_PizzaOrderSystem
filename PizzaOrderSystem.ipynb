import csv
from datetime import  datetime
import re

with open("Menu.txt", mode = "w") as f:
    f.write("* Please Choose a Pizza Base:\n1: Classic \n2: Margherita \n3: TurkPizza \n4: PlainPizza \n* and sauce of your choice: \n11: Olives \n12: Mushrooms \n13: GoatCheese \n14: Meat \n15: Onions \n16: Corn \n* Thank you!")

class Pizza:
  def __init__(self):
    self.description = "Unknown Pizza"
    self.cost = 0.0

  def get_description(self):
    return self.description

  def get_cost(self):
    return self.cost

class ClassicPizza(Pizza):
  def __init__(self):
    self.description = "A classic pizza with tomato sauce and cheese"
    self.cost = 100.0

class MargheritaPizza(Pizza):
  def __init__(self):
    self.description = "A Margherita pizza with tomato sauce, cheese, and basil"
    self.cost = 154.99

class TurkPizza(Pizza):
  def __init__(self):
    self.description = "A Turkish pizza with minced meat, peppers, onions, and tomato sauce"
    self.cost = 150.0

class DominosPizza(Pizza):
  def __init__(self):
    self.description = "A Dominos pizza with pepperoni, mushrooms, onions, and cheese"
    self.cost = 180.0

# Define the Pizza and Decorator classes as described earlier
class Decorator(Pizza):
  def __init__(self, component):
    self.component = component

  def get_cost(self):
    return self.component.get_cost() + Pizza.get_cost(self)

  def get_description(self):
    return self.component.get_description() + ' ' + Pizza.get_description(self)

# Define the sauces as Decorator subclasses
class Olives(Decorator):
  def __init__(self, pizza):
    super().__init__(pizza)
    self.cost = 5.0
    self.description = "A sauce with olives and olive oil"
        
class Mushrooms(Decorator):
  def __init__(self, pizza):
    super().__init__(pizza)
    self.cost = 7.5
    self.description = "A sauce with mushrooms, cream, and garlic"
        
class GoatCheese(Decorator):
  def __init__(self, pizza):
    super().__init__(pizza)
    self.cost = 9.0
    self.description = "A sauce with goat cheese, basil, and tomato"
        
class Meat(Decorator):
  def __init__(self, pizza):
    super().__init__(pizza)
    self.cost = 12.5
    self.description = "A sauce with ground beef, tomato, and spices"
        
class Onions(Decorator):
  def __init__(self, pizza):
    super().__init__(pizza)
    self.cost = 6.0
    self.description = "A sauce with caramelized onions and balsamic vinegar"
        
class Corn(Decorator):
  def __init__(self, pizza):
    super().__init__(pizza)
    self.cost = 8.0
    self.description = "A spicy sauce with tomato, onion, and chili pepper"

def get_tc_number():
  while True:
    # Get user input for TC number
    tc_number = input("TC number: ")

    if len(tc_number) != 11:
      print("Lütfen 11 haneli bir TC numarası giriniz.")
      continue
    elif not tc_number.isdigit():
      print("TC numarası sadece sayılardan oluşmalıdır.")
      continue
    elif int(tc_number[0]) == 0:
      print("TC numarasının ilk hanesi sıfır olamaz.")
      continue
    else:
      return tc_number

def credit_card_info():
  while True:
    # Get user input for credit card number
    credit_card_number = input("Credit card number: ")

    # Validate credit card number using regex
    if not re.match(r'^[0-9]{16}$', credit_card_number):
      print("Invalid credit card number. Please enter a valid 16-digit number.")
      continue

    # Get user input for credit card password
    credit_card_password = input("Credit card password: ")

    # Validate credit card password using regex
    credit_card_password_regex = r"^[0-9]{3}$"
    if not re.match(credit_card_password_regex, credit_card_password):
        print("Invalid credit card password. Please enter a valid 3-digit password.")
        continue

    # Return valid credit card number and password
    return credit_card_number, credit_card_password

# Define the main function
def main():
  # Display the menu
  print("Pizza Menu")
  print("----------")
  print("1. Classic Pizza - 100.00 TL")
  print("2. Margherita Pizza - 154.99")
  print("3. Turk Pizza - 150.00 TL")
  print("4. Dominos Pizza - 180.00 TL")
  print("")

  # Get user's pizza choice
  pizza_choice = input("Please enter the number of the pizza you'd like to order: ")

  # Create the pizza object based on the user's choice
  if pizza_choice == "1":
     pizza = ClassicPizza()
  elif pizza_choice == "2":
     pizza = MargheritaPizza()
  elif pizza_choice == "3":
     pizza = TurkPizza()
  elif pizza_choice == "4":
     pizza = DominosPizza()
  else:
     print("Invalid input. Please try again.")
     return

  # Display the sauce
  print("Sauce choice(s)")
  print("----------")
  print("1. Olive - 5.00 TL")
  print("2. Mushrooms Pizza - 7.50 TL")
  print("3. Goat Cheese - 9.00 TL")
  print("4. Meat - 12.50 TL")
  print("5. Onion - 6.00 TL")
  print("6. Corn - 8 TL")
  print("")

  # Get user's sauce choice(s)
  sauce_choices = []
  sauce_number = []
  while True:
     sauce_choice = input("Please enter the number of the sauce you'd like to add or 'e' if you're finished: ")
     if sauce_choice == "e":
       break
     elif sauce_choice == "1":
       sauce = Olives(pizza)
     elif sauce_choice == "2":
       sauce = Mushrooms(pizza)
     elif sauce_choice == "3":
       sauce = GoatCheese(pizza)
     elif sauce_choice == "4":
       sauce = Meat(pizza)
     elif sauce_choice == "5":
       sauce = Onions(pizza)
     elif sauce_choice == "6":
       sauce = Corn(pizza)
     else:
       print("Invalid input. Please try again.")
       continue
     if sauce_number.count(sauce_choice) >= 1:
       print(sauce.description + " is already exist. Please enter the another number of the sauce you'd like or exit") 
     else:
        sauce_number.append(sauce_choice)
        sauce_choices.append(sauce)
    
     print(sauce_choice)

  # Calculate the total cost of the order
  total_cost = pizza.get_cost()
  print(total_cost)
  order_description = pizza.get_description()
  print(order_description)
  for sauce in sauce_choices:
    total_cost += sauce.cost
    order_description = order_description + ",\n" + sauce.description
    print(total_cost)
    print(order_description)

  print(total_cost)
  print(order_description)
    
  # Get user's payment information
  fullname = input("Please enter your name: ")
  print(f'{fullname} have to pay {total_cost}')

  order_confirm = input("do you confirm your order ? Y/N")
  if order_confirm == "y":
    # Call the get_tc_number function and handle the returned value
    tc_number = get_tc_number()
    print("TC number validated successfully:", tc_number)

    # Call the get_credit_card_info function and handle the returned value
    card_number, card_password = credit_card_info()
    print("Credit card info validated successfully.")
  
    # order time
    order_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # file name
    file_name = "Orders_Database.csv"

    with open(file_name, mode="a", newline="") as file:
      writer = csv.writer(file)

      # Dosya boşsa, başlık satırını yazdır
      if file.tell() == 0:
        writer.writerow(["Name", "User ID", "Credit Card Number", "Total Cost", "Order Description", "Order Time", "Credit Card Password"])

      # Kullanıcı bilgileri, sipariş bilgileri ve ödeme bilgilerini dosyaya yazdır
      writer.writerow([fullname, tc_number, card_number, total_cost, order_description, order_time, card_password])

    # Dosyayı kapat
    file.close()

if __name__ == "__main__":
  main()

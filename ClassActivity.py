class Milk:
    def __init_(self, k: int = 0):
        self.__k_milk = k

        @property
        def k_milk(self):
            return self.__k_milk

        @k_milk.setter
        def set_k_milks(self, k_milk):
            self.__k.milk = k_milk


class Sugar:
    def __init_(self, k: int = 0):
        self.__k_sugar = k

        @property
        def k_sugar(self):
            return self.__k_sugar

        @k_sugar.setter
        def set_k_sugar(self, k_sugar):
            self.__k.sugar = k_sugar



class Beverage:
    def __init_(self):
        self._milk = 0
        self._sugar = 0

        @property
        def milk(self):
            return self.__milk

        @milk.setter
        def set_milk(self, milk: Milk):
            self.__milk = milk

        @property
        def sugar(self):
            return self.__sugar

        @sugar.setter

        def set_sugar(self, sugar: Sugar):
            self.__sugar = sugar



    def Condiments(self):
        while True:
            k_milk = int(input("How many milk(s) would you have? "))
            k_sugar = int(input("How many sugar(s) would you have? "))

            if (k_milk + k_sugar) > 4:
                print("You can't choose more than 3 condiments. Try again.")

            else:
                self.set_milk = Milk(k_milk)
                self.set_sugar = Sugar(k_sugar)


class Espresso(Beverage):
    def __init__(self):
        super().__init__()
        self.name = "Espresso"



class Americano(Beverage):
    def __init__(self):
        super().__init__()
        self.name = "Espresso"


class Espresso(Beverage):
    def __init__(self):
        super().__init__()
        self.name = "Americano"

class Latte(Beverage):
    def __init__(self):
        super().__init__()
        self.name = "Latte Machiato"

class BlackTea(Beverage):
    def __init__(self):
        super().__init__()
        self.name = "Black Tea"

class GreenTea(Beverage):
    def __init__(self):
        super().__init__()
        self.name = "Green Tea"

class YellowTea(Beverage):
    def __init__(self):
        super().__init__()
        self.name = "Yellow Tea"



class VendingMachine:
    def __action_loop(self, dialog: str, error: str, inputs: list):
        done = False

        while not done:
            looperPrompt = str(input(dialog)).lower().replace(" " , " ")
            if looperPrompt in inputs:
                done = True
                return looperPrompt
            else:
                print(error)

    def __init__(self):
        while True:
            orders = self.__action_loop( dialog = "Choose from the following options:\n 1. Espresso\n 2. Americano\n, 3. Latte Macchiato\n 4. Black Tea\n  5. Green Tea\n 6. Yellow Tea\n>>> ", error = "Sorry I didn't get that. Try again\n", inputs = ['1', '2', '3', '4', '5', '6', "Latte Macchiato", "Americano", "Black Tea", "Green Tea", "Yellow Tea", "latte macchiato", "americano", "black tea", "green tea", "yellow tea", "espresso", "Espresso", "Latte macchiato",  "Black tea", "Green tea", "Yellow tea"])


            if orders == '1' or orders == "Espresso" or orders =="espresso":
                drink = Espresso()

            elif orders == '2' or orders =="Americano" or orders == "americano":
                drink = Americano()

            elif orders == '3' or orders == "Latte Macchiato" or orders == "Latte macchiato" or orders == "latte macchiato":
                drink = Latte()

            elif orders == '4' or orders == "Black Tea" or orders == "Black tea" or orders == "black tea":
                drink = BlackTea()
                                       
            elif orders == '5' or orders == "Green Tea" or orders == "Green tea" or orders == "green tea":
                drink = GreenTea()
                                                                        
            elif orders == '6' or orders == "Yellow Tea" or orders == "yellow tea" or orders == "yellow tea":
                drink = YellowTea()


                drink.Condiments()

                print("One", {drink.name}, "with", { str(drink.milk.k_milk) }, "milk(s) and ", { str(drink.sugar.k_sugar)}, "coming up!")



if __name__ == "__main__":
    vendingMachine = VendingMachine()
                               


            

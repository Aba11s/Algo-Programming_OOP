class Shopping_List:
    def __init__(self,food_name,food_amt):
        self.__name = food_name
        self.__amount = food_amt
        self.__unit_price = 0
        self.__total_price = 0

        self.__dict = {"Dry Cured Iberian Ham":177.80,
                       "Wagyu Steaks":450.00,
                       "Matsutake Mushrooms":272.00,
                       "Kopi Luwak Coffee":306.50,
                       "Moose Cheese": 487.20,
                       "White Truffles": 3600.00,
                       "Blue Fin Tuna":3603.00,
                       "Le Bonnotte Potato":270.81
                       }
        
    def __str__(self):
        return str(self.__name)

    def __PriceList(self):
        self.__unit_price = self.__dict[self.__name]
        return self.__unit_price
        
    def calculate(self):
        self.__total_price = self.__PriceList() * self.__amount


    
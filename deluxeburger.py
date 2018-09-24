#Name: Whitt Hyde
#HW no. and Name: HW 9 Diner - New System
#Due Date: 11/13/2017
#Program Description: Deluxe Burger Sub-Class

#DEFINING CONSTANTS
SMALL = 6
MEDIUM = 8
LARGE = 10
SMALL_PRICE = 5.99
MEDIUM_PRICE = 7.99
LARGE_PRICE = 9.99
CHEESE = .99
BACON = 1.79
AVOCADO = 1.99

#import the entree Super Class
import plainburger

#defining subclass Pizza Slice
class DeluxeBurger(plainburger.PlainBurger):

    #defining the init method
    def __init__(self, name, qty, size):
        super().__init__(name,qty, size)
        self.__cheese = True
        self.__bacon = True
        self.__avocado = True
        
    #defining accessors
    def get_cheese(self):
        return self.__cheese

    def get_bacon(self):
        return self.__bacon

    def get_avocado(self):
        return self.__avocado


    #defining remove functions to remove some toppings on the deluxe burger
    def remove_cheese(self):
        #using decision structure to check if topping was already taken off
        if self.get_cheese():
            self.__cheese = False
        
    def remove_bacon(self):
        #using decision structure to check if topping was already taken off
        if self.get_bacon():
            self.__bacon = False
            
    def remove_avocado(self):
        #using decision structure to check if topping was already taken off
        if self.get_avocado():
            self.__avocado = False
            
    #defining calculate cost
    def calc_cost(self):
        #getting variables to calculate cose
        extras = 0
        quantity = self.get_qty()
        price = self.get_price()
        #decision tree for extra toppings
        if self.get_cheese():
            extras += CHEESE
        if self.get_bacon():
            extras += BACON
        if self.get_avocado():
            extras += AVOCADO
        #final calculation with variables
        cost = (quantity * price) + extras
        return cost
        
        

    #defining str method
    def __str__(self):
        if self.get_cheese():
            cheddar = 'cheese '
        else:
            cheddar = ""
        if self.get_bacon():
            pig = 'bacon '
        else:
            pig = ''
        if self.get_avocado():
            pico = 'avocado '
        else:
            pico = ""
        var = str(self.get_qty()) +" "+ "Deluxe Burger " + str(self.get_size()) +'oz Toppings: '+ str(cheddar) + str(pig) + str(pico) +"$" + format(self.calc_cost(),'.2f')
        return var       


#Name: Whitt Hyde
#HW no. and Name: HW 9 Diner - New System
#Due Date: 11/13/2017
#Program Description:Plain Burger Sub-Class

#DEFINING CONSTANTS
SMALL = 6
MEDIUM = 8
LARGE = 10
SMALL_PRICE = 5.99
MEDIUM_PRICE = 7.99
LARGE_PRICE = 9.99

#import the entree Super Class
import entree

#defining subclass Pizza Slice
class PlainBurger(entree.Entree):

    #defining the init method
    def __init__(self, name, qty, size):
        super().__init__(name,qty)
        self.__size = size
        self.__price = 1
        
    #defining accessors
    def get_size(self):
        return self.__size

    def get_price(self):
        return self.__price

    #defining mutators
    def set_price(self):
        if self.get_size() == SMALL:
            self.__price = SMALL_PRICE
        elif self.get_size() == MEDIUM:
            self.__price = MEDIUM_PRICE
        elif self.get_size() == LARGE:
            self.__price = LARGE_PRICE
        

    
    #defining the calculate cost method
    def calc_cost(self):
        #establishing variables for use in calculation
        quantity = self.get_qty()
        price = self.get_price()

        cost = (quantity * price)
        
        return cost
        
        

    #defining str method
    def __str__(self):
        var = str(self.get_qty()) + " Plain Burger " + str(self.__size) + "oz $" + str(self.calc_cost())
        return var    

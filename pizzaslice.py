#Name: Whitt Hyde
#HW no. and Name: HW 9 Diner - New System
#Due Date: 11/13/2017
#Program Description: Pizza Slice Sub-Class

#DEFINING CONSTANTS
SLICE_COST = 1.99
PER_TOPPING_COST = .99

#import the entree Super Class
import entree

#defining subclass Pizza Slice
class PizzaSlice(entree.Entree):

    #defining the init method
    def __init__(self, name, qty, toppings):
        super().__init__(name,qty)
        self.__toppings = toppings
        
    #defining accessors
    def get_toppings(self):
        return self.__toppings

    #defining method for calculating cost
    def calc_cost(self):
        quantity = self.get_qty()
        toppings = self.get_toppings()

        cost = (quantity * SLICE_COST) + (quantity * toppings * PER_TOPPING_COST)
        return cost
        
        

    #defining str method
    def __str__(self):
        var = str(self.get_qty()) + " Pizza Slice " + str(self.__toppings) + " Toppings $" + str(self.calc_cost())
        return var    


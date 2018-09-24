#Name: Whitt Hyde
#HW no. and Name: HW 9 Diner - New System
#Due Date: 11/13/2017
#Program Description: Defines Superclass Entree for our system

#defining our super class
class Entree:
    
    #defining the init method
    def __init__(self, start_name, start_qty):
        self.__name = start_name
        self.__quantity = start_qty

    #defining accessors
    def get_name(self):
        return self.__name

    def get_qty(self):
        return self.__quantity

    #defining str method
    def __str__(self):
        var = str(self.__quantity) + " " +str(self.__name)
        return var

    

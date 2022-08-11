# Inheritance - P.o.o

# This code is a simple way of explaining how inheritance works on python
# In this case a Superclass has the abbilite to determinate the surface of a rectangle
# then a subclass is created in order to use some of the code of the superclass which leads to
# determinate the surface of a square just giving one side meassure.

class rectangle:
    def __init__(self, measure1, measure2):
        self.measure1=measure1 
        self.measure2=measure2
    
    def area(self):
        return self.measure1 * self.measure2

class square(rectangle):
    def __init__(self,lado):
        super().__init__(lado,lado)

if __name__=="__main__":
    print("Determinate the area of a : \n1) Rectangle\n2) Square\n")
    choice= int(input( "Select please: "))
    if choice == 1 :
        print("You've choosen RECTANGLE, first enter the Width:")
        width= int(input(""))
        lenght= int(input("Now please enter the lenght: "))
        choice = rectangle(width,lenght)
        print(f'The area of the rectangle is {choice.area()}')
    elif choice == 2:
        print("You've choosen Square, enter the side lenght: ")
        side = int(input(""))
        choice = square(side)
        print(f'The area of the square is {choice.area()}')
    else:
        print("invalid option.")


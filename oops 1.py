# class Phone:
#     def make_call(self):
#         print("making phone call")
#     def play_game(self):
#         print("playing game")
#
# p1=Phone()
# p1.make_call()
# p1.play_game()
#
# class Phone:
#     def set_color(self,color):
#         self.color=color
#     def set_cost(self,cost):
#         self.cost=cost
#     def show_color(self):
#         print(self.color)
#     def show_cost(self):
#         print(self.cost)
#
#     def make_call(self):
#         print("make a call")
#     def play_game(self):
#         print("playing game")
#
#
# p1=Phone()
# p1.set_color('blue')
# p1.set_cost("19000")
# p1.show_color()
# p1.show_cost()
# p1.make_call()
# p1.play_game()

#----------------this is constructor method in python------------------

# class Employee:
#     def __init__(self,name,age,salary,gender):
#         self.name=name
#         self.age=age
#         self.salary=salary
#         self.gender=gender
#     def emp_show(self):
#         print("Name of employee is ",self.name)
#         print("Age of employee is ",self.age ,"years")
#         print("Salary of Employee is  ",self.salary,"Rs")
#         print("Gender of employee is ",self.gender)
#
# #----------------invoking values--------------
# e1=Employee("praveen",23,10000,"male")
# e1.emp_show()

#------------inheritance in python---------
class Vehicle:
    def __init__(self,milage,cost):
        self.milage=milage
        self.cost=cost
    def show_vehicle(self):
        print("vehicle milage is",self.milage)
        print("the cost of vehicle",self.cost)
        print("i am a vehicle")

v1=Vehicle(500,500)
v1.show_vehicle()
#
class Car(Vehicle):
    def car_detail(self):
        print("I am car")
c1=Car(200,1200)
c1.show_vehicle()
c1.car_detail()
#list1=[["happy", 1],["marry", 3],["harry", 5],["narry", 2]]
#dict1=dict(list1)
#for item,lollypop in dict1.items():
 #   print(item,"and lollypop is",lollypop)

 #CREATE LIST AND PRINT ONLY NUMBERS IS GREATER THAN 6

list=[1,2,3,4,5,6,7,8,9,10,"harry","marry","carry"]
for item in list:
    if str(item).isnumeric() and item>6:
        print(item)
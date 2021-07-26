def argsfunc(normal,*pavy,**pavi):
    print(normal)
    for item in pavy:
        print(item)
    print("...!dinner details!....")
    for key, value in pavi.items():
        print(f"{key} eat a {value}")

har=["pavi","adi","prateek","dhiraj","manohar","omkar"]
p="This is a args info"


a={har[0]:"eggrice",har[1]:"chicken",har[2]:"vimal",har[3]:"biriyani",har[4]:"kabab",har[5]:"roti"}
argsfunc(p,*har,**a)

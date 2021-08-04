import time
initial=time.time()
k=0
while(k<10):
    print("this is praveen")
    time.sleep(2)
    k+=1
# print(f"while loop ran in {time.time()}-{initial} seconds")
#
# initial2=time.time()
# for i in range(10):
#     print("this is praveen")
# print(f"for loop ran in {time.time()}-{initial2}

print(time.asctime(time.localtime()))

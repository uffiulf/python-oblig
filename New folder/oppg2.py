import random



def rando():
    rei = random.randrange(0,101)
    return(rei)



for i in range(3):
    print("*********")
    print("***"+str(rando())+"***")
    print("*********")
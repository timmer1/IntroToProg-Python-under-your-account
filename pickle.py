
#Show pickling
#Dev: Eric Timm (I feel a little awkward calling myself a dev)
#5/13/2019
# I am having problems, i get errors with the line import pickle, i'm not sure why, but I can't get the code to work.

# creating dictionary called EMP
emp = {1:"A",2:"B",3:"C",4:"D",5:"E"}

import pickle # I undersand this is supposed to call code, this 
pickling_on = open("Emp.pickle","wb")
pickle.dump(emp, pickling_on)
pickling_on.close()


pickle_off = open("Emp.pickle","rb")
emp = pickle.load(pickle_off)
print(emp)

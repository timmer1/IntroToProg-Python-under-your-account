#Open a file, read the data, and save into dictionary, give user
#options to interact with dictionary close and save.
#Dev: Eric Timm (I feel a little awkward calling myself a dev)
#4/29/2019

# "f" is a function I am asking(calling?) Python to open the todo.txt file and "r" read it.
fob = open("todo.txt","r") #opens file with name of "todo.txt"
D ={} #creates an empty dictionary

#For loop to read the lines and put into dictionary.
for line in fob:
    x = line.split (",") #splits the line at the comma e.g. Clean house(,) Low
    a = x[0] #a is a variable which is saving the first word in the line e.g. Clean House
    b = x[1] #b is a variable which is saving the first word in the line e.g. Low
    c = len(b)-1 #c = new variable, len = argument? which tells the variable c to use variable b, but remove the last character (/n = 1
    b = b[0:c] # this assigns c (which is b - one char) back to b. I understand the concept, but do not understand the syntax (from youtube)
    D[a] = b #creates dictionary relationship e.g. (Word: Definition)
#setting up functions; I had trouble with the looping logic, this was my method to keep the loop logic clean.
def f1(): #f1 prints what is in the dictionary
    print(D)
def f2(): #f2 allows the input of new values in the dictionary
    newtaskvar = input('What is the Task you would like to add: ') #creates var, and asks user for task name
    taskurgvar = input('What is the urgency for the task: ') #creates var, and asks user for task urgency
    D[newtaskvar] = taskurgvar
    print("new values")
    print(D)
def f3(): #f3 allows the user to delete values in dictionary
    print(D) #Giving list to user to figure out which task they want to delete
    delvar = input('Which task would you like to delete: ')
    #create variable to capture user input that will guide the delet "delvar"
    del D[delvar] #deletes the task
    print('New values')
    print(D)
def f4(): #f4 allows user to write and save into .txt file.  I am sure that my solution isn't what you want, but! No requirements listed and it writes!
    tupledata1 = (D)
    print(tupledata1)
    fob = open("todo.txt", "a")
    fob.write(str(tupledata1))
    fob.close()
    print('Data saved to file!')
def main(): #this is how I got the program to loop
    routvalue = int(input('''
        Menu of Options
            1) Show current data
            2) Add a new item.
            3) Remove an existing item.
            4) Save Data to File
            5) Exit Program
        lease input your selection:
        '''))
    if(routvalue == 1):
        f1()
        main()
    if(routvalue == 2):
        f2()
        main()
    if(routvalue == 3):
        f3()
        main()
    if(routvalue ==4):
        f4()
        main()
    if(routvalue == 5): 
        print('goodbye')
        quit()
main() # this is necssary, as everyting else is funtion, main() tells python to run from here.
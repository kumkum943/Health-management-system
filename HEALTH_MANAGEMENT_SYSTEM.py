def func1():
    print("Welcome to Piyush's File")
    print("---------------------------")
    print("Press 1 for adding exercise.")
    print("Press 2 for adding diet.")
    print("Press 3 to see all exercises.")
    print("Press 4 to see diet.")
def func2():
    print("Welcome to Sandesh's's File")
    print("---------------------------")
    print("Press 1 for adding exercise.")
    print("Press 2 for adding diet.")
    print("Press 3 to see all exercises.")
    print("Press 4 to see diet.")
def piyush_diet():
        f=open("piyush_diet.txt", "a")
        print("Enter the Piyush's Diet name: ")
        f.write(input())
        f.close()
        print("Your diet is successfully added to the file.")
        print("Thankyou!!")
def piyush_diet_display():
    f=open("piyush_diet.txt")
    d=f.read()
    print(d)
    f.close()
def piyush_exercise():
    g=open("piyush_exercise.txt","a")
    print("Enter the Piyush's Exercise name: ")
    g.write(input())
    g.close()
    print("Your exercise is successfully added to the file.")
    print("Thankyou!!")
def piyush_exercise_display():
    g=open("piyush_exercise.txt")
    a=g.read()
    print(a)
    g.close()
def sandesh_diet():
    h=open("sandesh_diet.txt")
    b=h.read()
    print(b)
    h.close()
def sandesh_diet_display():
    h=open("sandesh_diet.txt", "a")
    print("Enter the Sandesh's Diet name: ")
    h.write( input())
    h.close()
    print("Your diet is successfully added to the file.")
    print("Thankyou!!")
def sandesh_exercise():
    i=open("sandesh_exercise.txt", "a")
    print("Enter the Sandesh's Exercise name: ")
    i.write( input())
    i.close()
    print("Your exercise is successfully added to the file.")
    print("Thankyou!!")
def sandesh_exercise_display():
    i=open("sandesh_exercise.txt")
    c=i.read()
    print(c)
    i.close()

print("Welcome to Aryan's Health Management System!!")
print("Press 1 to go in Piyush's File")
print("Press 2 to go in Sandesh's File")

inp=int(input())
if inp==1:
    func1()
    inp1=int(input())
    if inp1==1:
        piyush_exercise()
    elif inp1==2:
        piyush_diet()
    elif inp1==3:
        piyush_exercise_display()
    elif inp1==4:
        piyush_diet_display()
    else:
        print("Enter a Valid input.")
elif inp==2:
    func2()
    inp1 = int(input())
    if inp1 == 1:
        sandesh_exercise()
    elif inp1 == 2:
        sandesh_diet()
    elif inp1 == 3:
        sandesh_exercise_display()
    elif inp1 == 4:
        sandesh_diet_display()
    else:
        print("Enter a Valid input.")
else:
    print("Enter a Valid input.")
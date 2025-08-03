

# data file
def print_task():
    try:
        with open("data.txt") as datafile:
            print("____________TODO____________")
            for i, item in enumerate(datafile):
                print(i, "-", item.strip())
    except Exception as err:
        print(f"cannot read file :", err)



# add task
def addtask():
    try:
        while True:
            task = input("Enter your task : ")
            with open("data.txt", "a") as datafile:
                datafile.write(task + "\n")
            check = input("add more task ? (Y/N) : ").lower()
            if check == "n":
                break
    except Exception as err:
        print(f"An unexpected error occurred:")
    finally:
        print(" adeddd sucess ✅ ")
    print_task()


# # remove tassk
def remove_task():
    while True:
        with open("data.txt") as datafile:
            taskdata = datafile.readlines()
            print_task()
            userinpput = int(input("which tassk do you want to remove ? "))
            del taskdata[
                userinpput
            ]  # here task data is te list and useriput yha index hai
            with open("data.txt", "w") as datafile:
                datafile.writelines(taskdata)
            print_task()
            print(" removed sucess ")
            check = input("removed more task ? (Y/N) : ").lower()
            if check == "n":
                break


# update task
def update_task():
    with open("data.txt") as datafile:
        taskdata = datafile.readlines()
        print_task()
        userinput = int(input("which task you want to update ? : "))
        newtask = input("enter new task : ")
        taskdata[userinput] = newtask + "\n"
        with open("data.txt", "w") as datafile:
            datafile.writelines(taskdata)
        print_task()


# user imputs
def useriputs():

    print("1: print all tasks")
    print("2: add neww task")
    print("3: remove  task")
    print("4: update task")
    user_input = input(f"what do you want to do ? : ")
    if user_input == "1":
        print_task()
    if user_input == "2":
        addtask()
    if user_input == "3":
        remove_task()
    if user_input == "4":
        update_task()

while True:
    useriputs()
    check= input("couninue ? (Y/N)").lower()
    if check=='n':
        break

# UI 
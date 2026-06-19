Tasks=[]
while True:
    print("-----------TO-DO LIST-------------")
    print("1-Add Task")
    print("2-View Task")
    print("3-Delete Task")
    print("4-Exiting Task")

    choice=int(input("Enter user choice"))
    if(choice==1):
        Task=input("Enter your Task: ")
        Task2=input("Enter your task: ")
        Task3=input("Enter your task: ")
        Tasks.append(Task)
        Tasks.append(Task2)
        Tasks.append(Task3)
        print("----------Task added successfully----------")
    elif(choice==2):
        if len(Tasks)==0:
            print("No Task Found")   
        else:
            print("your tasks")
            for task in Tasks:
                print("Task=",task)
    elif(choice==3):
            if len(Tasks)==0:
                print("No Task to delete :")
            else:
                print("Your Tasks")
                for i in range(len(Tasks)):
                    print(i+1,"-",Tasks[i])                 
            num=int(input("Enter an number you want to delete"))
            if(1<=num<=len(Tasks)):
                removed=Tasks.pop(num-1)
                print("Task Deleted Successfully")
            else:
                print("Invalid Task number")            
    elif(choice==4):
        print("Exiting.....")
        break        


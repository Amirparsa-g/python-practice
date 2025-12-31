from task import Task
from ToDoList import ToDoList

menu = """
1)add task
2)remove task
3)show tasks
4)clear
5)exit
6) show menu"""

todo = ToDoList()

print(f"Hello werlcome to your personal ToDoList select any items from menu!\n{menu}")
UserInput = input()
while True:
    if UserInput == "1" or UserInput == "add task":
        task = input("task name:")
        explanation = input("explanation:")
        priority = input("priority(High, Medium, Low):")
        while priority !="High" and priority !="high" and priority !="Medium" and priority !="medium" and priority !="Low" and priority !="low":
            print("the priority should be High or Medium or Low")
            priority = input("priority(High, Medium, Low):")


        todo.AddTask(task, explanation, priority)
    elif UserInput == "2" or UserInput == "remove task":
        task = input("task name:")
        todo.RemoveTask(task)

    elif UserInput == "3" or UserInput == "show tasks":
        todo.ShowAll()

    elif UserInput == "4" or UserInput == "clear":
        todo.ClearToDoList()

    elif UserInput == "5" or UserInput == "exit":
        break
    elif UserInput == "6" or UserInput == "show_menu":
        print(menu)

    else:
        print("select a topic from the menu")
    UserInput = input()
print("see you later!")

from task import Task
import csv
from colorama import Fore, Style, init

class ToDoList():
    input_file="ToDoList.csv"
    FieldNames=["task","explanation","priority"]
    def SortTasks(self):
        p_high=[]
        p_medium=[]
        p_low=[]
        total=[]
        with open(self.input_file, mode="r") as file:
            csv_reader=csv.DictReader(file)
            for line in csv_reader:
                if line["priority"]== "High" or line["priority"]=="high" :
                    p_high.append(line)
                elif line["priority"]== "Medium" or line["priority"]=="medium" :
                    p_medium.append(line)
                elif line["priority"]== "Low" or line["priority"]=="low" :
                    p_low.append(line)
            total=p_high+p_medium+p_low
        with open(self.input_file, mode="w", newline="", encoding="utf-8") as file:
            csv_writer = csv.DictWriter(file, fieldnames=self.FieldNames)
            csv_writer.writeheader()
            csv_writer.writerows(total)
            

    def AddTask(self,name,explanation,priority):
        with open(self.input_file,mode="a",encoding="utf-8") as file:
            csv_writer=csv.DictWriter(file, fieldnames=self.FieldNames)
            csv_writer.writerow({
                "task":name,
                "explanation":explanation,
                "priority": priority
            })
        self.SortTasks()
        print("the task has been added!\nif ypu want to see the menu type 6")
    def RemoveTask(self,name):

        tasks=[]
        found=False
        with open(self.input_file, mode="r",encoding="utf-8") as file:
            csv_reader=csv.DictReader(file)
            for line in csv_reader:
                if line["task"]!=name:
                    tasks.append(line)
                else:
                    found=True
            if found:
                with open(self.input_file, mode="w",encoding="utf-8") as file:
                    csv_writer=csv.DictWriter(file,fieldnames=self.FieldNames)
                    csv_writer.writeheader()
                    csv_writer.writerows(tasks)
                print("the task has been deleted!\nif ypu want to see the menu type 6")
            else:
                print("there is no such task!!\nif ypu want to see the menu type 6")
    def ShowAll(self):
        with open(self.input_file, mode="r", encoding="utf-8") as file:
            csv_reader = csv.DictReader(file, delimiter=",")
            print("\nTo-Do List:")
            for line in csv_reader:
                if line["priority"] == "High" or line["priority"]=="high":
                    print(Fore.RED + f"task : {line['task']} ({line['priority']}): {line['explanation']}")
                elif line["priority"] == "Medium" or line["priority"]=="medium":
                    print(Fore.LIGHTYELLOW_EX + f"task : {line['task']} ({line['priority']}): {line['explanation']}")
                elif line["priority"] == "Low" or line["priority"]=="low":
                    print(Fore.GREEN + f"task : {line['task']} ({line['priority']}): {line['explanation']}")

        print(Fore.WHITE+"if ypu want to see the menu type 6")    
    def ClearToDoList(self):
        with open(self.input_file, mode="w",encoding="utf-8") as file:
                csv_writer=csv.DictWriter(file,fieldnames=self.FieldNames)
                csv_writer.writeheader()
        print("the List Has been cleared!!\nif ypu want to see the menu type 6")
        
        
    
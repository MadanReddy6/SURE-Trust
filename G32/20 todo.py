
class Todo_Item:
    priority_options = ["High", "Medium", "Low"]

    def __init__(self,task:str,priority:str = None,done:bool = False):
        if type(task) == str:
            if task:
                self.task = task
            else:
                raise Exception("Task should not be empty")
        else:
            raise Exception("Task needs to be a string")

        if type(done) == bool:
            self.done = done
        else:
            raise Exception("Done argument needs to be a boolean")

        if priority:
            if priority in Todo_Item.priority_options:
                self.priority = priority
            else:
                raise Exception(f"priority setting should be one of {Todo_Item.priority_options}")
        else:
            self.priority = None

    def __str__(self):
        return f'[{"x" if self.done else "o"}] - {self.priority if self.priority else "None"} : {self.task}'

    def finish(self):
        self.done = True

    def raise_priority(self):
        if not self.priority:
            return

        if self.priority == "Low":
            self.priority = "Medium"
        if self.priority == "Medium":
            self.priority = "High"


class Todo_List:
    def __init__(self,owner:str, todo_list:list = []):

        for item in todo_list:
            if type(item) != Todo_Item:
                raise Exception(f"Expected Todo Item got {type(item)}")

        self.todo_items = todo_list

        if type(owner) == str:
            if owner:
                self.owner = owner
            else:
                raise Exception("Owner name should not be empty")
        else:
            raise Exception("Owner name needs to be a string")

    def __str__(self):
        # write code so the output is like the following
        output = f"{self.owner}'s ToDo List\n"

        for item in self.todo_items:
            output += str(item) + "\n"

        return output

    def info(self):
        pending_tasks = {"High": 0, "Medium": 0, "Low": 0}
        finished_tasks = 0

        for item in self.todo_items:
            if item.done:
                finished_tasks += 1
            else:
                if item.priority:
                    pending_tasks[item.priority] += 1

        pending_summary = ", ".join([f"{priority} - {count}" for priority, count in pending_tasks.items()])

        print(f"{self.owner}'s Todo list\n\nPending Tasks: {len(self.todo_items) - finished_tasks} \n{pending_summary}\nFinished Tasks: {finished_tasks}\n------------")

    def add_todo_item(self, todo_item):
        if type(todo_item) == Todo_Item:
            self.todo_items.append(todo_item)
        else:
            raise Exception(f"ToDo item must be of datatype Todo_Item not {type(todo_item)}")

    def create_todo_item(self,task:str,priority:str = None,done:bool = False):
        item = Todo_Item(task, priority,done)
        self.todo_items.append(item)

    def search_todo_item(self, query):
        output = []


        return [item1, item3]




a = Todo_Item("Wash my dishes")
b = Todo_Item("Buy groceries",priority="High")
c = Todo_Item("Call mom",priority="Low")
d = Todo_Item("Do homework",priority="Medium")
e = Todo_Item("Go to the gym")

my_list = Todo_List("Ashwani",[a,b,c,d,e])

# print(my_list)
my_list.info()

b.finish()
c.finish()

my_list.info()



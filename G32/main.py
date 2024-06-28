from Modules.todo import Todo_Item, Todo_List, sample_todo

output = sample_todo.list_todo_items(sort=True)
for item in output:
    print(item)
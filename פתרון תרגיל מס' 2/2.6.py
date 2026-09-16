def task_manager():
    # Dictionary inside the closure representing the tasks
    tasks = {}

    def add_task(task, status="incomplete"):
        # Add a new task with a default status
        tasks[task] = status

    def get_tasks():
        # Return the dictionary of current tasks
        return tasks

    def complete_task(task):
        # Change a task's status to 'complete'
        if task in tasks:
            tasks[task] = "complete"

    # Return a dictionary granting access to the functions
    return {
        'add_task': add_task,
        'get_tasks': get_tasks,
        'complete_task': complete_task
    }

# Create a new task manager and test according to instructions
tasks_manager = task_manager()
tasks_manager['add_task']("Write email")
tasks_manager['add_task']("Shopping", "in progress")
tasks_manager['add_task']("Homework")

current_tasks = tasks_manager['get_tasks']()
print(current_tasks)

tasks_manager['complete_task']("Write email")
current_tasks = tasks_manager['get_tasks']()
print(current_tasks)
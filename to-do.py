tasks = []

def add_task(task):
    tasks.append(task)

def show_tasks():
    for i, t in enumerate(tasks, 1):
        print(i, t)

if __name__ == "__main__":
    add_task("Finish DevOps assignment")
    add_task("Push code to GitHub")
    show_tasks()

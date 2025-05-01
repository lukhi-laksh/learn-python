class Task:
    def __init__(self, title):
        self.title = title
        self.completed = False

    def mark_complete(self):
        self.completed = True

    def display(self, indent=0):
        status = "[x]" if self.completed else "[ ]"
        print("  " * indent + f"{status} {self.title}")


class CompositeTask(Task):
    def __init__(self, title):
        super().__init__(title)
        self.subtasks = []

    def add_subtask(self, task):
        self.subtasks.append(task)

    def mark_complete(self):
        self.completed = True
        for task in self.subtasks:  
            task.mark_complete()    

    def display(self, indent=0):
        super().display(indent)
        for task in self.subtasks:  
            task.display(indent + 1)

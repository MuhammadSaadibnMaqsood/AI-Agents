class Task:
    def __init__(self, name, priority, deadline):
        self.name = name
        self.priority = priority
        self.deadline = deadline
        self.completed = False


class ProjectManagement:
    def __init__(self):
        self.tasks = [] 
        

    def add_task(self, task):
        self.tasks.append(task)

    def chooseNextTask(self):
        
        self.tasks.sort(key=lambda x: (-x.priority, x.deadline))

        for task in self.tasks:
            if not task.completed:
                return task
        return None

    def completeTask(self, task):
        task.completed = True
        print(f" Task '{task.name}' marked as completed.")

    def run(self):
        while True:
            task = self.chooseNextTask()
            if task:
                print(f"Next task is: {task.name}")
                self.completeTask(task)
            else:
                print(" All tasks are completed!")
                break


if __name__ == "__main__":
    agent = ProjectManagement()

    # Adding tasks
    agent.add_task(Task("Design goal-based agent", priority=2, deadline="2024-10-20"))
    agent.add_task(Task("Develop model for goal-based agent", priority=1, deadline="2024-10-25"))
    agent.add_task(Task("Create project management system", priority=3, deadline="2024-10-30"))

    agent.run()

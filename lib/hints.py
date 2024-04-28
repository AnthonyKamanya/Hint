class Hint:
    def __init__(self,name):
        self.name = name
        self.task_list = []
        

    def remind_me_to(self,task):
        self.task_list.append(task)

    def remind(self):
        if self.task_list == []:
            raise Exception("No task set.")
        for assignment in self.task_list:
            return f"{assignment}, {self.name}!"
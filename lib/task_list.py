class Task():
    def __init__(self):
        self._task_list = []

    def add_task(self,todo):
        if todo == "":
            raise Exception("Cannot add empty todo")
        self._task_list.append(todo)

    def extract_task(self):
        return self._task_list
    
    def completed_task(self,index):
        if index < 0 or index >= len(self._task_list):
            raise Exception("No such task to mark complete")
        del self._task_list[index]
        
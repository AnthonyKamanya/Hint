from lib.task_list import Task
import pytest

"""Given an empty todo
#add_task should raise an error message "Cannot add empty todo"
"""
def test_empty_todo():
    task = Task()
    with pytest.raises(Exception) as err:
        task.add_task("") 
    error_message = str(err.value)
    assert error_message == "Cannot add empty todo"

"""Given  a todo
#extract_task should show task to the todo list 
"""
def test_one_todo():
    task = Task()
    task.add_task("Please get up and study") 
    results = task.extract_task()
    assert results == ["Please get up and study"]

"""Given multiple todo
#extract_task should show task list to the todo list 
"""
def test_multiple_task_entries():
    task = Task()
    task.add_task("Please get up and study") 
    task.add_task("Pray for family") 
    task.add_task("Apply for software engineering roles") 
    results= task.extract_task()
    assert results ==["Please get up and study","Pray for family","Apply for software engineering roles"]


"""Given a list of task
#completed_task if we try to mark a track complete that does not exist (too high)
it raises an error
"""
def test_mark_task_that_is_low_complete():
    task = Task()
    task.add_task("Please get up and study") 
    task.add_task("Pray for family") 
    task.add_task("Apply for software engineering roles") 
    with pytest.raises(Exception) as err:
        task.completed_task(-1)
    error_message = str(err.value)
    task_list = task.extract_task()
    assert error_message == "No such task to mark complete"
    assert task_list == ["Please get up and study","Pray for family","Apply for software engineering roles"]



"""Given a list of task
#completed_task if we try to mark a track complete that does not exist (too low)
it raises an error
"""
def test_mark_task_that_is_high_complete():
    task = Task()
    task.add_task("Please get up and study") 
    task.add_task("Pray for family") 
    task.add_task("Apply for software engineering roles") 
    with pytest.raises(Exception) as err:
        task.completed_task(3)
    error_message = str(err.value)
    task_list = task.extract_task()
    assert error_message == "No such task to mark complete"
    assert task_list == ["Please get up and study","Pray for family","Apply for software engineering roles"]


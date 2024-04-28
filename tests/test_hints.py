from lib.hints import Hint
import pytest


"""
Given a name and a task
#remind reminds the user to do the task
"""
def test_user_given_a_name_and_task():
    reminder = Hint("Edem")
    reminder.remind_me_to("Walk the dog")
    result = reminder.remind() # => 
    assert result == "Walk the dog, Edem!"

"""
Given a name and no task
#remind raises an exception
"""
def test_user_given_a_name_and_no_task():
    reminder = Hint("Edem")
    with pytest.raises(Exception) as err:
        reminder.remind() # raises an error with the message "No task set."
    error_message = str(err.value)
    assert error_message == "No task set."

"""
Given a name and an empty task
#remind still reminds the user to do the task, even though it looks odd
"""
def test_user_given_a_name_and_an_empty_task():
    reminder = Hint("Edem")
    reminder.remind_me_to("")
    result = reminder.remind() 
    assert result == ", Edem!"


   
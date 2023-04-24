from lib.reminder import *

def test_reminds_the_user_to_do_a_task():
    reminder = Reminder("Afzaa")
    reminder.remind_me_to("Play with the cat")
    result = reminder.remind()
    assert result == "Play with the cat, Afzaa!"
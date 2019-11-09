# -*- coding: utf-8 -*-
# try something like
def index(): return dict(message="hello from reports.py")

@auth.requires_login()
def report_data():
    my_tasks_grid = SQLFORM.grid(db.tasks.task_owner==auth.user_id, showbuttontext = True, create=False, exportclasses = dict(xml=False, html=False, tsv_with_hidden_cols = False, tsv = False, csv_with_hidden_cols=False ) )

#create a list of the users who have the current logged-in user as their supervisor
    my_employees = db(db.auth_user.supervisor_id == auth.user_id).select()

# creates a rows object to hold a junction table of all tasks and their owners for later sorting in the view
    all_tasks = db(db.tasks.task_owner == db.auth_user.id).select(db.tasks.task_owner, db.tasks.task_name, db.tasks.task_description, db.auth_user.id, db.auth_user.first_name, db.auth_user.last_name, db.auth_user.supervisor_id)

    return locals()

# -*- coding: utf-8 -*-

import datetime

@auth.requires_login()
def index():
    current_time = datetime.datetime.now()
    tasks_form = SQLFORM(db.tasks).process()
    my_tasks = db(db.tasks.task_owner==auth.user_id).select(orderby= ~(db.tasks.id) )
    tasks_tags_rows = db(db.tasks_tags.tag==db.tags.id).select()
    tags = db(db.tags).select()

# the following code handles creating a tasks_tags record to associate a tag with a task
    add_form=FORM('my_tag_form:',
              INPUT(_task='task', requires=IS_IN_DB(db, db.tasks.id)),
              INPUT(_tag='tag', requires=IS_IN_DB(db, db.tags.id)),
              INPUT(_type='submit'),
              _formname='add_task_tag_form')
    if add_form.accepts(request, session, formname='add_task_tag_form'):
        db.tasks_tags.insert(task=request.vars.task, tag=request.vars.tag) # the actual creation of a record
        response.flash = 'form accepted'
    elif add_form.errors:
        response.flash = 'form has errors'
    else:
        response.flash = 'please fill the form'

# the following form handles tags_tasks record deletion
    ttremoval=FORM('my_task_tag_form:',
                   INPUT(_id='id', requires=IS_NOT_EMPTY()),
                   INPUT(_type='submit'),
                   _formname='del_task_tag_form')
    if ttremoval.accepts(request, session, formname='del_task_tag_form'):
        del db.tasks_tags[request.vars.id] #the actual deletion
        #db(db.tasks_tags.id == request.vars.id).delete()
        response.flash = 'Tag Removed'


    return locals()

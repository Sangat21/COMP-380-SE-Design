# -*- coding: utf-8 -*-
# try something like
@auth.requires_login()
def index():
    # TAGS FORM
    form = SQLFORM(db.tags).process()
    
    # SHOW TAG GRID
    grid = SQLFORM.grid( db.tags, create=False, exportclasses = dict(xml=False, html=False, tsv_with_hidden_cols = False, tsv = False, csv_with_hidden_cols=False) ) 
    employees = db(db.auth_user.supervisor_id==auth.user_id).select(db.auth_user.first_name, db.auth_user.last_name , db.auth_user.id, orderby=(db.auth_user.last_name) )
    return locals()

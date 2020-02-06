# -*- coding: utf-8 -*-
# try something like
def index(): return dict(message="hello from home.py")

@auth.requires_login()
def login_page():
    form = SQLFORM(db.account_login).process()
    return locals()

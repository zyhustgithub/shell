#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Models for user, blog, comment.
'''

__author__ = 'M.r Zeng'

import time, uuid

from mysql.orm import Model, StringField, BooleanField, FloatField, TextField

def next_id():
    return '%015d%s000' % (int(time.time() * 1000), uuid.uuid4().hex)

class User(Model):
    __table__ = 'users'

    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    name = StringField(ddl='varchar(50)')
    passwd = StringField(ddl='varchar(50)')
    admin = BooleanField()
    created_at = FloatField(default=time.time)

class Product(Model):
    __table__ = 'products'

    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    user_id = StringField(ddl='varchar(50)')
    user_name = StringField(ddl='varchar(50)')
    cpmc = StringField(ddl='varchar(50)')
    cplb = StringField(ddl='varchar(20)') 
    xwdm = StringField(ddl='varchar(20)')
    zqzh = StringField(ddl='varchar(20)')
    zjzh = StringField(ddl='varchar(20)', default=0)
    qzmm = BooleanField()
    created_at = FloatField(default=time.time)

class File(Model):
    __table__ = 'files'
    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    wjlb = StringField(ddl='varchar(20)')
    wjlj = StringField(ddl='varchar(50)')
    created_at = FloatField(default=time.time)
# -*- coding:utf-8 -*-
from app import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, index=True)
    password_hash = db.Column(db.String(64))
    full_name = db.Column(db.String(20))
    group_id = db.Column(db.String(20))
    role_id = db.String(db.Column(10))

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)


class Role(db.Model):
    __tabelname__ = 'role'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True)
    default = db.Column(db.Boolean, default=False, index=True)
    permissions = db.Column(db.Integer)
    users = db.relationship('User', backref='role', lazy='dynamic')

    @staticmethod
    def insert_roles():
        roles = {
            'user': (Permission.READ_FILE),
            'author': (Permission.READ_FILE |
                      Permission.UPLOAD_FILE |
                      Permission.MODIFICATION_FILE |
                      Permission.DELETE_FILE
                      ),
            'Adminstrator': (0xff, False)
        }


class Permission:
    """
    权限表
        操作              位值
        阅读项目文件      0X01
        上传项目文件      0x02
        修改项目文件      0x04
        删除项目文件      0x08
        新建项目          0x80
    """
    READ_FILE = 0x01
    UPLOAD_FILE = 0x02
    MODIFICATION_FILE = 0x04
    DELETE_FILE = 0x08
    NEW_PROJECT = 0x80

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    p_id = db.Column(db.Integer)
    desc = db.Column(db.String(60))
    creat_time = db.Column(db.)

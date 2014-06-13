#-*- coding:utf-8 -*-

from flask import Flask

app = Flask(__name__, static_folder='assets', template_folder='views')

from . import routes


#-- EOF --

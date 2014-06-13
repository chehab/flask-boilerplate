#-*- coding:utf-8 -*-

from flask import render_template, flash, redirect, session, url_for, request, g


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Some attributes could be attached to customize behavior the view function,        #
#  in the Example below the `method` attr. is attached to the `index` view func.    #
#  Read more about this at flask's documentation at the link below.                 #
#                                                                                   #
# Documentation:                                                                    #
#   http://flask.pocoo.org/docs/api/?highlight=add_url_rule#view-function-options   #
#                                                                                   #
# Example:                                                                          #
#                                                                                   #
#   def index():                                                                    #
#       if request.method == 'OPTIONS':                                             #
#           # custom options handling here                                          #
#           ...                                                                     #
#       return 'Hello World!'                                                       #
#   index.provide_automatic_options = False                                         #
#   index.methods = ['GET', 'OPTIONS']                                              #
#                                                                                   #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def view(foo=None):
    bar = "Welcome "+str(foo) if foo else False
    return render_template("helloworld.html", page_title=bar)
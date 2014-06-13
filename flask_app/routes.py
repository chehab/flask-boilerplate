#-*- coding:utf-8 -*-

import os

from flask import send_from_directory

from . import app

# Controllers
from .controllers import helloworld


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#  flask.Flask.add_url_rule(*args, **kwargs)                                            #
#                                                                                       #
#  Parameters:                                                                          #
#    rule      – the URL rule as string                                                 #
#    endpoint  – the endpoint for the registered URL rule.                              #
#                 Flask itself assumes the name of the view function as endpoint.       #
#    view_func – the function to call when serving a request to the provided endpoint.  #
#    options   – the options to be forwarded to the underlying Rule object.             #
#                 A list of methods this rule should be limited to (GET, POST etc.).    #
#                  By default a rule just listens for GET (and implicitly HEAD).        #
#                                                                                       #
# http://flask.pocoo.org/docs/api/?highlight=add_url_rule#url-route-registrations       #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


app.add_url_rule('/', view_func=helloworld.view)
app.add_url_rule('/<foo>', view_func=helloworld.view)



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#  Serving favicons                                                                     #
#                                                                                       #

@app.route('/favicon.ico')
def favicon_ico():
    return send_from_directory(os.path.join(app.root_path, 'assets/favicons'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')
#
@app.route('/browserconfig.xml')
def favicon_browserconfig():
    return send_from_directory(os.path.join(app.root_path, 'assets/favicons'),
                               'browserconfig.xml', mimetype='application/xml')

#                                                                                       #
# http://flask.pocoo.org/docs/patterns/favicon/                                         #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#!/usr/bin/env python3
#-*- coding:utf-8 -*-

import subprocess

from docopt import docopt
from flask_app import app

# default port number
PORT  = 3000
# force debug mode
DEBUG = False
# CLI help message
DOC   = """ run - version 0.0.0-dev

Usage:
    run [options]
    run rename (<new-name>) [<app-name>]
    run -h | --help
    run --version

Options:
  -p <number> --port <number>
    Start on Port Number [default: {PORT}].

  -d --debug
    Start in debug mode.

  rename
    Change the flask_app name.

  <new-name>
    New name to change the app's name to.

  <app-name>
    Current app name if changed from the initial name "flask_app".

  -h --help
    Show this screen.

  -v --version
    Show version.
""".format(PORT=PORT)


def rename_app(new_name, old_name='flask_app'):
    try:
        run_file = None
        # read this file to change 'import' at line 7
        with open('run.py', 'r') as f:
            run_file = f.read()
        # Create import string for Replacement.
        old_import_str = "from {} import app".format(old_name)
        new_import_str = "from {} import app".format(new_name)
        # Replace the import string.
        run_file = run_file.replace(old_import_str, new_import_str)
        # Rewrite this file.
        with open('run.py', 'w') as f:
            f.write(run_file)
        # Change App directory name.
        subprocess.call(["mv", old_name, new_name])
        # Print Success Message
        print("App Name is now changed.")
    except:
        # Print Error Message
        print('<!> Error Occurred. \n \t Process terminated.')
        exit(1)
#end:rename_app

if __name__ == '__main__':

    args = docopt(DOC, version=DOC.splitlines()[0])

    if args['rename']:
        print("\n* This will only change the flask app director name and the `import` directive at 'run.py' on line 7")
        confirmation = input("  <!> This could break the app, would you like to continue? [Yes|No]: ")
        if confirmation.upper()== 'YES':
            if args['<app-name>']:
                rename_app(new_name=args['<new-name>'], old_name=args['<app-name>'])
            else:
                rename_app(new_name=args['<new-name>'])
            exit(0)
        elif confirmation.upper() != 'NO' or len(confirmation) == 1:
            print("\a\n<!> Process Canceled.")
            print("Next time please type 'yes' or 'no'.\n")
            exit(1)
    else:
        args['--debug'] = True if DEBUG else args['--debug']
        app.run(port=int(args['--port']), debug=args['--debug'])

#-- EOF --

import os
import sys
import site

# sys.path.append(os.path.dirname(__file__))
# os.environ['DJANGO_SETTINGS_MODULE'] = 'settings.board'

# Add the site-packages of the chosen virtualenv to work with
site.addsitedir('/home/igor_bolotin/.virtualenvs/whisker/local/lib/python2.7/site-packages')

# Add the app's directory to the PYTHONPATH
sys.path.append('/opt/whiskerboard')
sys.path.append('/opt/whiskerboard/board')
#sys.path.append(os.path.dirname(__file__))

os.environ['DJANGO_SETTINGS_MODULE'] = 'board.settings'

# Activate your virtual env
activate_env=os.path.expanduser("/home/igor_bolotin/.virtualenvs/whisker/bin/activate_this.py")
execfile(activate_env, dict(__file__=activate_env))

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
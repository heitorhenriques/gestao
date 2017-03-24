import os, sys, site

# Activate your virtual env
activate_env=os.path.expanduser("/home/virtualenvs/gestao/bin/activate_this.py")
execfile(activate_env, dict(__file__=activate_env))


# Add the site-packages of the chosen virtualenv to work with
#site.addsitedir('/home/virtualenvs/gestao/local/lib/python2.7/site-packages')

# Add the apps directory to the PYTHONPATH
sys.path.append('/var/www/gestao/')

#to set enviroment settings for Django apps
os.environ["DJANGO_SETTINGS_MODULE"] = "gestao.settings"

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()


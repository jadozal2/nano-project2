from os import environ

#--------- Flask settings
#SERVER_HOST = '0.0.0.0' # Update this for the appropriate front-end website when up
SERVER_HOST = environ.get('SERVER_HOST', 'localhost')
SERVER_PORT = 5000
#SERVER_PORT = int(environ.get('SERVER_PORT', '5000'))

FLASK_DEBUG = False # Do not use debug mode in prod

# Flask-Restplus settings
SWAGGER_UI_DOC_EXPANSION = 'list'
RESTPLUS_VALIDATE = True
RESTPLUS_MASK_SWAGGER = False
RESTPLUS_404_HELP = True
API_VERSION = 'v1'

#-------- Azure constants

# API_URL format: "https://[FUNCTION_APP_NAME_GOES_HERE].azurewebsites.net"
#API_URL = " https://neighborlyapi.azurewebsites.net/api/"

# for local host if Azure functions served locally
API_URL = "https://nano-project2-func-app.azurewebsites.net/api"

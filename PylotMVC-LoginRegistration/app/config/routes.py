"""
    Routes Configuration File

    Put Routing rules here
"""
from system.core.router import routes

routes['default_controller'] = 'Logins'
routes['POST']['/login'] = 'Logins#login'
routes['POST']['/register'] = 'Logins#register'

"""
    Routes Configuration File

    Put Routing rules here
"""
from system.core.router import routes

routes['default_controller'] = 'Courses'
routes['POST']['/courses/add'] = 'Courses#add'
routes['GET']['/courses/load'] = 'Courses#load'
routes['GET']['/courses/destroy/<id>'] = 'Courses#show'
routes['GET']['/courses/remove/<id>'] = 'Courses#remove'

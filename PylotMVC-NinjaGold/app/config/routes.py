"""
    Routes Configuration File

    Put Routing rules here
"""
from system.core.router import routes

routes['default_controller'] = 'Ninja'
routes['POST']['/process_money/<building>'] = 'Ninja#process'
routes['GET']['/process_money'] = 'Ninja#show'
routes['GET']['/reset'] = 'Ninja#reset'

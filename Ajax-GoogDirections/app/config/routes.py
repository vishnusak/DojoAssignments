from system.core.router import routes

routes['default_controller'] = 'Directions'
routes['POST']['/directions'] = 'Directions#get_directions'

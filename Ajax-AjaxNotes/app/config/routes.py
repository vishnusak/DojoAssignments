from system.core.router import routes

routes['default_controller'] = 'Notes'
routes['/notes/del/<id>'] = 'Notes#delete'
routes['POST']['/notes/add'] = 'Notes#add'
routes['POST']['/notes/update/<id>'] = 'Notes#update'

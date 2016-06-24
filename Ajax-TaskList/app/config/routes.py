from system.core.router import routes

routes['default_controller'] = 'Tasks'
routes['POST']['/tasks/add'] = 'Tasks#add'
routes['POST']['/tasks/update/<id>'] = 'Tasks#update'
routes['POST']['/tasks/delete/<id>'] = 'Tasks#delete'

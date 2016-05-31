"""
    Routes Configuration File

    Put Routing rules here
"""
from system.core.router import routes

routes['default_controller'] = 'Products'
routes['GET']['/products/edit/<id>'] = 'Products#edit'
routes['GET']['/products/show/<id>'] = 'Products#show'
routes['GET']['/products/new'] = 'Products#new'
routes['POST']['/products/create'] = 'Products#create'
routes['POST']['/products/update/<id>'] = 'Products#update'
routes['GET']['/products/remove/<id>'] = 'Products#destroy'

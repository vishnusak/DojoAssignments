from system.core.router import routes

routes['default_controller'] = 'Tunes'
routes['POST']['/tunes/<artist>'] = 'Tunes#get_video'

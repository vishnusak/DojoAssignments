from system.core.router import routes

routes['default_controller'] = 'Leads'
routes['POST']['/leads/<int:page_num>'] = 'Leads#another_page'
routes['POST']['/leads/filter'] = 'Leads#filter_page'

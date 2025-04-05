# -*- coding: utf-8 -*-
# from odoo import http


# class ExampleModule(http.Controller):
#     @http.route('/example_module/example_module', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/example_module/example_module/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('example_module.listing', {
#             'root': '/example_module/example_module',
#             'objects': http.request.env['example_module.example_module'].search([]),
#         })

#     @http.route('/example_module/example_module/objects/<model("example_module.example_module"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('example_module.object', {
#             'object': obj
#         })


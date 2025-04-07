# -*- coding: utf-8 -*-
# from odoo import http


# class ModuleRequester(http.Controller):
#     @http.route('/module_requester/module_requester', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module_requester/module_requester/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('module_requester.listing', {
#             'root': '/module_requester/module_requester',
#             'objects': http.request.env['module_requester.module_requester'].search([]),
#         })

#     @http.route('/module_requester/module_requester/objects/<model("module_requester.module_requester"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module_requester.object', {
#             'object': obj
#         })


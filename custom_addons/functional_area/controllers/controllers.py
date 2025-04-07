# -*- coding: utf-8 -*-
# from odoo import http


# class FunctionalArea(http.Controller):
#     @http.route('/functional_area/functional_area', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/functional_area/functional_area/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('functional_area.listing', {
#             'root': '/functional_area/functional_area',
#             'objects': http.request.env['functional_area.functional_area'].search([]),
#         })

#     @http.route('/functional_area/functional_area/objects/<model("functional_area.functional_area"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('functional_area.object', {
#             'object': obj
#         })


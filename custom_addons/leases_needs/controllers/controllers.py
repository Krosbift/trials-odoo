# -*- coding: utf-8 -*-
# from odoo import http


# class LeasesNeeds(http.Controller):
#     @http.route('/leases_needs/leases_needs', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/leases_needs/leases_needs/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('leases_needs.listing', {
#             'root': '/leases_needs/leases_needs',
#             'objects': http.request.env['leases_needs.leases_needs'].search([]),
#         })

#     @http.route('/leases_needs/leases_needs/objects/<model("leases_needs.leases_needs"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('leases_needs.object', {
#             'object': obj
#         })


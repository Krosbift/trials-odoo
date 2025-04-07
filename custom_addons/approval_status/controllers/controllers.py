# -*- coding: utf-8 -*-
# from odoo import http


# class ApprovalStatus(http.Controller):
#     @http.route('/approval_status/approval_status', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/approval_status/approval_status/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('approval_status.listing', {
#             'root': '/approval_status/approval_status',
#             'objects': http.request.env['approval_status.approval_status'].search([]),
#         })

#     @http.route('/approval_status/approval_status/objects/<model("approval_status.approval_status"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('approval_status.object', {
#             'object': obj
#         })


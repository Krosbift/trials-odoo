# -*- coding: utf-8 -*-
# from odoo import http


# class EquipementNeeds(http.Controller):
#     @http.route('/equipement_needs/equipement_needs', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/equipement_needs/equipement_needs/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('equipement_needs.listing', {
#             'root': '/equipement_needs/equipement_needs',
#             'objects': http.request.env['equipement_needs.equipement_needs'].search([]),
#         })

#     @http.route('/equipement_needs/equipement_needs/objects/<model("equipement_needs.equipement_needs"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('equipement_needs.object', {
#             'object': obj
#         })


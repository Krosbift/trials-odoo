from odoo import models, fields


class module_requester(models.Model):
    _name = 'module_requester.module_requester'
    _description = 'module_requester.module_requester'

    name = fields.Char(string="Module Name", required=True)
    description = fields.Text(string="Description")

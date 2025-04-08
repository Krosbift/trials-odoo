from odoo import models, fields, api
from odoo.exceptions import ValidationError


class leases_needs(models.Model):
    _name = "leases.needs"
    _description = "Leases Description"

    place = fields.Char(string="Place", required=True)
    annual_amount = fields.Integer(string="Annual Amount", required=True)
    cost = fields.Integer(string="Cost", required=True)

    @api.constrains("annual_amount")
    def _check_positive_annual_amount(self):
        for record in self:
            if record.annual_amount < 0:
                raise ValidationError("Annual Amount must be a positive integer")

    @api.constrains("cost")
    def _check_positive_cost(self):
        for record in self:
            if record.cost < 0:
                raise ValidationError("Cost must be a positive float")

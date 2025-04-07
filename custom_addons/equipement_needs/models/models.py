from odoo import models, fields, api
from odoo.exceptions import ValidationError


class equipement_needs(models.Model):
    _name = "equipement_needs.equipement_needs"
    _description = "Description test"

    equipement = fields.Char(string="Equipement", required=True)
    quantity = fields.Integer(string="Quantity", required=True)
    unit_cost = fields.Float(string="Unit Cost", required=True)

    # description = fields.Text()
    @api.constrains("quantity")
    def _check_positive_quantity(self):
        for record in self:
            if record.quantity <= 0:
                raise ValidationError("Quantity must be a positive integer")

    @api.constrains("unit_cost")
    def _check_positive_unit_cost(self):
        for record in self:
            if record.unit_cost <= 0:
                raise ValidationError("Unit Cost must be a positive float")

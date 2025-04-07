from odoo import models, fields, api
from odoo.exceptions import ValidationError


class equipment_needs(models.Model):
    _name = "equipment.needs"
    _description = "Equipment Needs Request"

    equipement = fields.Char(string="Equipment", required=True)
    quantity = fields.Integer(string="Quantity", required=True)
    unit_cost = fields.Float(string="Unit Cost", required=True)
    total_cost = fields.Float(
        string="Total Cost", compute="_compute_total_cost", store=True
    )

    @api.depends("quantity", "unit_cost")
    def _compute_total_cost(self):
        for record in self:
            record.total_cost = record.quantity * record.unit_cost

    @api.constrains("quantity")
    def _check_positive_quantity(self):
        for record in self:
            if record.quantity < 0:
                raise ValidationError("Quantity must be a positive integer")

    @api.constrains("unit_cost")
    def _check_positive_unit_cost(self):
        for record in self:
            if record.unit_cost < 0:
                raise ValidationError("Unit Cost must be a positive float")

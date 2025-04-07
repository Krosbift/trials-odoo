from odoo import models, fields, api
from odoo.exceptions import ValidationError


class equipement_needs(models.Model):
    _name = "equipement_needs.equipement_needs"
    _description = "Equipment Needs Request"
    _inherit = ["mail.thread", "mail.activity.mixin"]

    equipement = fields.Char(string="Equipment", required=True, tracking=True)
    quantity = fields.Integer(string="Quantity", required=True, tracking=True)
    unit_cost = fields.Float(string="Unit Cost", required=True, tracking=True)

    # total_cost = fields.Float(
    #     string="Total Cost", compute="_compute_total_cost", store=True
    # )
    #
    # priority = fields.Selection(
    #     [("0", "Low"), ("1", "Normal"), ("2", "High"), ("3", "Very High")],
    #     string="Priority",
    #     default="1",
    #     tracking=True,
    # )
    # request_date = fields.Date(
    #     string="Request Date", default=fields.Date.today, tracking=True
    # )
    # notes = fields.Text(string="Notes")
    #
    # @api.depends("quantity", "unit_cost")
    # def _compute_total_cost(self):
    #     for record in self:
    #         record.total_cost = record.quantity * record.unit_cost

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

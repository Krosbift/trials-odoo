from odoo import models, fields, api
from odoo.exceptions import ValidationError


class leases_needs(models.Model):
    _name = "leases.needs"
    _description = "Leases Description"
    _inherit = ["approval.status.mixin"]
    module_id = 4

    place = fields.Char(string="Place", required=True)
    annual_amount = fields.Integer(string="Annual Amount", required=True)
    cost = fields.Integer(string="Cost", required=True)
    total_cost = fields.Float(
        string="Total Cost", compute="_compute_total_cost", store=True
    )

    approval_status_id = fields.Many2one(
        "approval_status_type.approval_status_type", string="Approval Status"
    )
    functional_area_id = fields.Many2one(
        "functional_area.functional_area", string="Functional Area"
    )

    @api.depends("annual_amount", "cost")
    def _compute_total_cost(self):
        for record in self:
            record.total_cost = record.annual_amount * record.cost

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

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class leases_needs(models.Model):
    _name = "leases.needs"
    _description = "Leases Description"

    place = fields.Char(string="Place", required=True)
    annual_amount = fields.Integer(string="Annual Amount", required=True)
    cost = fields.Integer(string="Cost", required=True)

    approval_status_id = fields.Integer(string="Approval Status")
    # approval_status_id = fields.Many2one(
    #     "approval_status_type.approval_status_type", string="Approval Status"
    # )
    functional_area_id = fields.Many2one(
        "functional_area.functional_area", string="Functional Area"
    )

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

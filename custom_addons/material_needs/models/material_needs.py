from odoo import models, fields, api


class material_needs(models.Model):
    _name = "material_needs.material_needs"
    _description = "Material Requirements"
    _inherit = ["approval.status.mixin"]
<<<<<<< HEAD
    module_id = 2
=======
    module_id = 1
>>>>>>> eacb265e372ef6bd48ffb19e2e1237fe6935f8f6

    material_name = fields.Char(string="Material Name", required=True)
    quantity = fields.Integer(string="Quantity", default=1)
    unit_cost = fields.Float(string="Unit Cost")
    approval_status_id = fields.Many2one(
        "approval_status_type.approval_status_type", string="Approval Status"
    )
    functional_area_id = fields.Many2one(
        "functional_area.functional_area", string="Functional Area"
    )
    total_cost = fields.Float(
        string="Total Cost", compute="_compute_total_cost", store=True
    )

    @api.depends("quantity", "unit_cost")
    def _compute_total_cost(self):
        for record in self:
            record.total_cost = record.quantity * record.unit_cost

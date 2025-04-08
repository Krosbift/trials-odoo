from odoo import models, fields, api


class material_needs(models.Model):
    _name = "material_needs.material_needs"
    _description = "Material Requirements"

    module_id = 2

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

    def _create_approval_status_log(self, record, new_status_id):
        """Create a log entry for approval status changes."""
        log_model = self.env["approval_status_log.approval_status_log"]

        existing_log = log_model.search(
            [
                ("module_id", "=", self.module_id),
                ("request_id", "=", record.id),
                ("user_id", "=", self.env.uid),
            ],
            limit=1,
        )

        log_vals = {
            "module_id": self.module_id,
            "request_id": record.id,
            "user_id": self.env.uid,
            "approval_status_id": new_status_id,
            "secuence": (existing_log.secuence + 1) if existing_log else 1,
        }

        return log_model.create(log_vals)

    def write(self, vals):
        for record in self:
            old_status = record.approval_status_id
            res = super(material_needs, record).write(vals)

            new_status_id = vals.get("approval_status_id")
            if new_status_id and new_status_id != (
                old_status.id if old_status else None
            ):
                self._create_approval_status_log(record, new_status_id)

        return res

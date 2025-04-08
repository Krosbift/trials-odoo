from odoo import models, fields


class approval_status_type(models.Model):
    _name = "approval_status_type.approval_status_type"
    _description = "approval_status_type.approval_status_type"

    name = fields.Char(string="Status", required=True)
    description = fields.Text(string="Description")


class approval_status_log(models.Model):
    _name = "approval_status_log.approval_status_log"
    _description = "approval_status_log.approval_status_log"

    module_id = fields.Integer(string="Module ID", required=True)


    old_status_id = fields.Many2one("approval_status_type.approval_status_type", string="Previous Status")
    new_status_id = fields.Many2one("approval_status_type.approval_status_type", string="New Status")
    # user_id = fields.Many2one("res.users", string="Changed By", default=lambda self: self.env.user)

    user_id = fields.Integer(string="Changed By")

from odoo import models, fields


class user_access(models.Model):
    _inherit = "res.users"

    functional_area_ids = fields.Many2many(
        "functional_area.functional_area", string="Functional Area"
    )

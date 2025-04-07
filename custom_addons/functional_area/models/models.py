from odoo import models, fields


class functional_area(models.Model):
    _name = "functional_area.functional_area"
    _description = "functional_area.functional_area"

    name = fields.Char(string="Functional Area", required=True)
    description = fields.Text(string="Description")

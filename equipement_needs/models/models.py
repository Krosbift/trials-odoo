from odoo import models, fields


class equipement_needs(models.Model):
    _name = "equipement_needs.equipement_needs"
    _description = "Description test"

    equipement = fields.Char(string="Equipement", required=True)
    quantity = fields.Integer(string="Quantity", required=True)
    unit_cost = fields.Float(string="Unit Cost", required=True)
    # description = fields.Text()

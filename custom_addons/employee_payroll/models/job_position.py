from odoo import models, fields


class job_position(models.Model):
    _name = "job.position"
    _description = "Employee Position"
    _rec_name = "position"

    position = fields.Selection(
        [  # type: ignore
            ("administrative", "Administrative"),
            ("worker", "Worker"),
        ],
        required=True,
    )

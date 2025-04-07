from odoo import models, fields


class job_position(models.Model):
    """
    Model: job_position
    This model represents a job position within the organization. It includes the following fields:
    Fields:
        - position (Selection): Specifies the type of job position. It is a required field with the following options:
            * "administrative" - Administrative
            * "worker" - Worker
    """

    _name = "job_position"
    _description = "Employee Position"
    _rec_name = "position"

    position = fields.Selection(
        [
            ("administrative", "Administrative"),
            ("worker", "Worker"),
        ],
        required=True,
        readonly=True,
    )

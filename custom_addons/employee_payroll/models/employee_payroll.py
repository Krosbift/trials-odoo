from odoo import models, fields, api


class employee_payroll(models.Model):
    _name = "employee.payroll"
    _description = "Employee Payroll Request"

    _inherit = ["approval.status.mixin"]
    module_id = 2

    fullName = fields.Char(string="Full Name", size=32, required=True, trim=True)
    document = fields.Char(string="Document Number", size=32, required=True)
    monthly_salary = fields.Float(string="Monthly Salary", required=True)
    job_position_id = fields.Many2one(
        comodel_name="job.position", string="Job Position", required=True
    )

    approval_status_id = fields.Many2one(
        "approval_status_type.approval_status_type", string="Approval Status"
    )

    functional_area_id = fields.Many2one(
        "functional_area.functional_area", string="Functional Area"
    )

    annual_salary = fields.Float(
        string="Annual Salary", compute="_compute_annual_salary", store=True
    )

    @api.depends("monthly_salary")
    def _compute_annual_salary(self):
        for record in self:
            record.annual_salary = record.monthly_salary * 12

    @api.constrains("document")
    def _check_document(self):
        for record in self:
            if not record.document.isdigit():
                raise models.ValidationError(
                    "The document number must contain only digits."
                )

    @api.constrains("fullName", "document")
    def _check_immutable_fields(self):
        for record in self:
            if record.id:
                original = self.browse(record.id)
                if record.fullName != original.fullName:
                    raise models.ValidationError(
                        "The Full Name field cannot be updated."
                    )
                if record.document != original.document:
                    raise models.ValidationError(
                        "The Document field cannot be updated."
                    )

    @api.constrains("monthly_salary")
    def _check_monthly_salary(self):
        for record in self:
            if record.monthly_salary < 0:
                raise models.ValidationError("Monthly Salary cannot be less than zero.")

    @api.onchange("monthly_salary")
    def _onchange_monthly_salary(self):
        if self.monthly_salary < 0:
            return {
                "warning": {
                    "title": "Invalid Monthly Salary",
                    "message": "The monthly salary must be greater than zero.",
                }
            }

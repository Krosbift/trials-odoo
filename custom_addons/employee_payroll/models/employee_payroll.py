from odoo import models, fields, api


class employee_payroll(models.Model):
    """
    Module: employee_payroll

    This module defines the `employee_payroll` model, which represents employee payroll information.

    Classes:
        - employee_payroll: A model to manage employee payroll details, including full name, document number,
          monthly salary, job position, and computed annual salary.

    Fields:
        - fullName (Char): The full name of the employee. Required field with a maximum size of 32 characters.
        - document (Char): The document number of the employee. Required field with a maximum size of 32 characters.
        - monthly_salary (Float): The monthly salary of the employee. Required field.
        - job_position_id (Many2one): A reference to the job position of the employee. Required field.
        - annual_salary (Float): The computed annual salary of the employee, calculated as `monthly_salary * 12`.

    Methods:
        - _compute_annual_salary: Computes the annual salary based on the monthly salary.
        - _check_monthly_salary: Ensures that the monthly salary is greater than zero. Raises a ValidationError if not.

    Dependencies:
        - Depends on the `monthly_salary` field for computing the `annual_salary`.
        - Constrains the `monthly_salary` field to ensure it is a positive value.
    """

    _name = "employee_payroll.employee_payroll"
    _description = "employee_payroll.employee_payroll"

    fullName = fields.Char(string="Full Name", size=32, required=True, trim=True)
    document = fields.Char(string="Document Number", size=32, required=True)
    monthly_salary = fields.Float(string="Monthly Salary", required=True)
    job_position_id = fields.Many2one(
        comodel_name="job_position.job_position", string="Job Position", required=True
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

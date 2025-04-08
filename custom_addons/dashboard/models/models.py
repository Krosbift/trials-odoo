from odoo import models, fields, api


class dashboard(models.Model):
    _name = "dashboard"
    _description = "Dashboard"

    # name = fields.Char(string="Categoría")
    # value = fields.Float(string="Valor")

    total_cost_leases = fields.Float(
        string="Total de costos de Arrendamientos", compute="_compute_total_cost_leases"
    )
    total_cost_employee = fields.Float(
        string="Total de costos de Empleados", compute="_compute_total_cost_employee"
    )
    total_cost_equipment = fields.Float(
        string="Total de costos de Equipos", compute="_compute_total_cost_equipment"
    )
    total_cost_material = fields.Float(
        string="Total de costos de Materiales", compute="_compute_total_cost_material"
    )

    @api.depends()
    def _compute_total_cost_leases(self):
        for record in self:
            leases = self.env["leases.needs"].search([])
            record.total_cost_leases = sum(leases.mapped("total_cost")) if leases else 0

    @api.depends()
    def _compute_total_cost_employee(self):
        for record in self:
            employees = self.env["employee.payroll"].search([])
            record.total_cost_employee = (
                sum(employees.mapped("annual_salary")) if employees else 0
            )

    @api.depends()
    def _compute_total_cost_equipment(self):
        for record in self:
            equipment = self.env["equipment.needs"].search([])
            record.total_cost_equipment = (
                sum(equipment.mapped("total_cost")) if equipment else 0
            )

    @api.depends()
    def _compute_total_cost_material(self):
        for record in self:
            materials = self.env["material_needs.material_needs"].search([])
            record.total_cost_material = (
                sum(materials.mapped("total_cost")) if materials else 0
            )

    # @api.model
    # def update_chart_data(self):
    #     self.env["dashboard.chart.line"].search([]).unlink()
    #     self.env["dashboard.chart.line"].create(
    #         [
    #             {
    #                 "name": "Arrendamientos",
    #                 "value": self._get_total_cost("leases.needs", "total_cost"),
    #             },
    #             {
    #                 "name": "Empleados",
    #                 "value": self._get_total_cost("employee.payroll", "annual_salary"),
    #             },
    #             {
    #                 "name": "Equipos",
    #                 "value": self._get_total_cost("equipment.needs", "total_cost"),
    #             },
    #             {
    #                 "name": "Materiales",
    #                 "value": self._get_total_cost(
    #                     "material_needs.material_needs", "total_cost"
    #                 ),
    #             },
    #         ]
    #     )
    #
    # def _get_total_cost(self, model_name, field_name):
    #     records = self.env[model_name].search([])
    #     return sum(records.mapped(field_name)) if records else 0

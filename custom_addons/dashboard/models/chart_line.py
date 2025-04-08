from odoo import models, fields, api


class DashboardChartLine(models.Model):
    _name = "dashboard.chart.line"
    _description = "Líneas del gráfico de Dashboard"

    name = fields.Char(string="Categoría")
    value = fields.Float(string="Valor")

    @api.model
    def update_chart_data(self):
        self.env["dashboard.chart.line"].search([]).unlink()
        self.env["dashboard.chart.line"].create(
            [
                {
                    "name": "Arrendamientos",
                    "value": self._get_total_cost("leases.needs", "total_cost"),
                },
                {
                    "name": "Empleados",
                    "value": self._get_total_cost("employee.payroll", "annual_salary"),
                },
                {
                    "name": "Equipos",
                    "value": self._get_total_cost("equipment.needs", "total_cost"),
                },
                {
                    "name": "Materiales",
                    "value": self._get_total_cost(
                        "material_needs.material_needs", "total_cost"
                    ),
                },
            ]
        )

# from odoo import http


# class EmployeePayroll(http.Controller):
#     @http.route('/employee_payroll/employee_payroll', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/employee_payroll/employee_payroll/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('employee_payroll.listing', {
#             'root': '/employee_payroll/employee_payroll',
#             'objects': http.request.env['employee_payroll.employee_payroll'].search([]),
#         })

#     @http.route('/employee_payroll/employee_payroll/objects/<model("employee_payroll.employee_payroll"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('employee_payroll.object', {
#             'object': obj
#         })

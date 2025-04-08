{
    "name": "Nómina de empleados",
    "category": "Data",
    "version": "1.0",
    "depends": ["base", "functional_area"],
    "data": [
        "security/ir.model.access.csv",
        "data/employee_position_data.xml",
        "views/employee_payroll_views.xml",
        "views/employee_payroll_menus.xml",
        "views/employee_payroll_list.xml",
        "views/employee_payroll_form.xml",
    ],
    "demo": [
        "demo/employee_position_demo.xml",
    ],
    "installable": True,
    "application": True,
    "license": "LGPL-3",
}

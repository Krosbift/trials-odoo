{  # type: ignore
    "name": "dasboard",
    "category": "Data",
    "depends": [
        "base",
        "leases_needs",
        "employee_payroll",
        "equipment_needs",
        "material_needs",
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/dashboard_views.xml",
        "views/dashboard_menu.xml",
        "views/dashboard_list.xml",
        "views/dashboard_graph.xml",
    ],
    "installable": True,
    "application": True,
    "license": "LGPL-3",
}

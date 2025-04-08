{  # type: ignore
    "name": "Solicitudes de equipo",
    "category": "Data",
    "version": "0.0.1",
    "depends": ["base", "functional_area", "approval_status"],
    "data": [
        "security/ir.model.access.csv",
        "views/equipment_needs_views.xml",
        "views/equipment_needs_menu.xml",
        "views/equipment_needs_form.xml",
        "views/equipment_needs_list.xml",
    ],
    "installable": True,
    "application": True,
    "license": "LGPL-3",
}

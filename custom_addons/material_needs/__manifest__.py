{  # type: ignore
    "name": "Necesidades de Material",
    "category": "Data",
    "version": "0.1",
    "depends": ["base", "functional_area", "approval_status"],
    "author": "NePinFe",
    "data": [
        "security/ir.model.access.csv",
        "views/material_needs_views.xml",
        "views/material_needs_menu.xml",
        "views/material_needs_list.xml",
        "views/material_needs_form.xml",
    ],
    "installable": True,
    "application": True,
    "license": "LGPL-3",
}

{  # type: ignore
    "name": "Arrendamientos",
    "category": "data",
    "depends": ["base", "functional_area"],
    "data": [
        "security/ir.model.access.csv",
        "views/leases_needs_list.xml",
        "views/leases_needs_form.xml",
        "views/leases_needs_views.xml",  # Acción que usa las vistas anteriores
        "views/leases_needs_menu.xml",  # Menú que usa la acción
    ],
    # "demo": [
    #     "demo/demo.xml",
    # ],
    "installable": True,
    "application": True,
    "license": "LGPL-3",
}

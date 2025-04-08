{
    "name": "Estados de Aprobación",
    "version": "0.1",
    "depends": ["base"],
    "author": "NePinFe",
    "data": [
        "security/ir.model.access.csv",
        "views/type_views/approval_status_type_views.xml",
        "views/type_views/approval_status_type_menu.xml",
        "views/type_views/approval_status_type_list.xml",
        "views/type_views/approval_status_type_form.xml",
        # Log
        "views/log_views/approval_status_log_views.xml",
        "views/log_views/approval_status_log_menu.xml",
        "views/log_views/approval_status_log_form.xml",
        "views/log_views/approval_status_log_list.xml",
    ],
    "installable": True,
    "application": True,
    "license": "LGPL-3",
}

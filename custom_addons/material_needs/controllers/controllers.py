from odoo import http


class MaterialNeeds(http.Controller):
    @http.route("/material_needs/material_needs", auth="public")
    def index(self, **kw):
        return "Hello, world"

    @http.route("/material_needs/material_needs/objects", auth="public")
    def list(self, **kw):
        return http.request.render(
            "material_needs.listing",
            {
                "root": "/material_needs/material_needs",
                "objects": http.request.env["material_needs.material_needs"].search([]),
            },
        )

    @http.route(
        '/material_needs/material_needs/objects/<model("material_needs.material_needs"):obj>',
        auth="public",
    )
    def object(self, obj, **kw):
        return http.request.render("material_needs.object", {"object": obj})

from odoo import models

class ApprovalStatusMixin(models.AbstractModel):
    _name = "approval.status.mixin"
    _description = "Mixin for approval status logging"

    def _create_approval_status_log(self, record, new_status_id):
        log_model = self.env["approval_status_log.approval_status_log"]

        existing_log = log_model.search(
            [
                ("module_id", "=", self.module_id),
                ("request_id", "=", record.id),
                ("user_id", "=", self.env.uid),
            ],
            limit=1,
        )

        log_vals = {
            "module_id": self.module_id,
            "request_id": record.id,
            "user_id": self.env.uid,
            "approval_status_id": new_status_id,
            "secuence": (existing_log.secuence + 1) if existing_log else 1,
        }

        return log_model.create(log_vals)

    def write(self, vals):
        for record in self:
            old_status = record.approval_status_id
            res = super().write(vals)

            new_status_id = vals.get("approval_status_id")
            if new_status_id and new_status_id != (
                old_status.id if old_status else None
            ):
                self._create_approval_status_log(record, new_status_id)

        return res

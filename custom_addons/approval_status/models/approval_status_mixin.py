from odoo import models


class ApprovalStatusMixin(models.AbstractModel):
    _name = "approval.status.mixin"
    _description = "Mixin for approval status logging"

    def _create_approval_status_log(self, record, new_status_id):
        log_model = self.env["approval_status_log.approval_status_log"]

        # Buscar todos los logs del request actual
        logs = log_model.search(
            [("request_id", "=", record.id)],
            order="secuence desc",
            limit=1,
        )

        last_secuence = logs.secuence if logs else 0

        log_vals = {
            "module_id": self.module_id,
            "request_id": record.id,
            "user_id": self.env.uid,
            "approval_status_id": new_status_id,
            "secuence": last_secuence + 1,
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

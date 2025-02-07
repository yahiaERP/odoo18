# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).

from odoo import fields, models


class ResCompany(models.Model):
    _inherit = "res.company"

    use_stamp = fields.Boolean(
        string="Timbre fiscale", store=True, default=True, readonly=True
    )
    auto_compute = fields.Boolean(string="Auto-compute", store=True, readonly=True)


class AccountConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    use_stamp = fields.Boolean(
        string="Timbre fiscale",
        related="company_id.use_stamp",
        store=True,
        default=True,
        readonly=True,
    )
    auto_compute = fields.Boolean(
        string="Auto-compute",
        related="company_id.auto_compute",
        store=True,
        readonly=True,
    )

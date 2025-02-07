# -*- coding: utf-8 -*-

from odoo import models, fields, api
import logging
from odoo.exceptions import UserError
import json

_logger = logging.getLogger(__name__)


class AccountInvoice(models.Model):
    _inherit = 'account.move'

    withholding_id = fields.Many2one('account.withholding', string='Withholding Tax', copy=False)


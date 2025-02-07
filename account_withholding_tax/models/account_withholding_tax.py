# -*- coding: utf-8 -*-

from odoo import models, fields, api
import odoo.addons.decimal_precision as dp


class AccountWithholdingTax(models.Model):
    _name = 'account.withholding.tax'

    name = fields.Char(string='Tax Name', required=True)

    rate = fields.Float(string='Rate', required=True, digits=dp.get_precision('Discount'))

    account_id = fields.Many2one('account.account', domain=[('deprecated', '=', False)], string='Tax Account',
                                 ondelete='restrict', required=True)
    refund_account_id = fields.Many2one('account.account', domain=[('deprecated', '=', False)],
                                        string='Tax Account on Refunds', ondelete='restrict', required=True)

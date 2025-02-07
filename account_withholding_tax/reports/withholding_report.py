# -*- coding: utf-8 -*-

from odoo import api, models,_
from datetime import datetime
from odoo.exceptions import ValidationError
import logging

_logger = logging.getLogger(__name__)

class withholding(models.AbstractModel):
    _name = 'report.account_withholding_tax.withholding_report'
    _wrapped_report_class = None

    @api.model
    def _get_report_values(self, docids, data=None):
        docs = self.env['account.withholding'].browse(docids)
        data = {}
        withholding_tab = {}
        withholding_ids = []
        amount_total = 0.0
        withholding_total = 0.0
        net_amount_total = 0.0
        if len(docs) == 1:
            amount_total = 0.0
            for line in docs.account_invoice_ids:
                amount_total += line.amount_total
            date_stop = docs.date
            if docs.type == 'in_withholding':
                data['company_id'] = docs.company_id.partner_id
                data['partner_id'] = docs.partner_id
            else:
                data['company_id'] = docs.partner_id
                data['partner_id'] = docs.company_id.partner_id

            for w in docs.account_withholding_tax_ids:
                if w.name not in withholding_tab:
                    withholding_tab[w.name] = {
                        'amount': amount_total,
                        'withholding': self.compute_withholdin_amount(docs, w),
                        'net_amount': amount_total - self.compute_withholdin_amount(docs, w)
                    }
                    withholding_ids.append(w.id)
                else:
                    withholding_tab[w.name]['withholding'] += docs.amount
                    withholding_tab[w.name]['net_amount'] -= docs.amount
                withholding_total += self.compute_withholdin_amount(docs, w)

            net_amount_total += amount_total - withholding_total

        withholding_ids = self.env['account.withholding.tax'].search([('id', 'not in', withholding_ids)])

        withholdings = []
        for w in withholding_ids:
            withholdings.append(w.name)

        data['date'] = datetime.strptime(str(date_stop), '%Y-%m-%d').date()
        data['withholding_tab'] = withholding_tab
        data['withholdings'] = withholdings
        data['net_amount'] = net_amount_total
        data['withholding'] = withholding_total
        data['amount'] = amount_total
        data['invoice'] = " , ".join(invoice.name for invoice in docs.account_invoice_ids)
        # data['ref'] = " , ".join(invoice.ref for invoice in docs.account_invoice_ids)
        # data['invoice'] = docs.type == 'in_withholding' and ', '.join(
        #     map(lambda x: x.ref, docs.account_invoice_ids)) or ', '.join(
        #     map(lambda x: x.move_name, docs.account_invoice_ids))

        if not data['company_id'].vat:
            raise ValidationError(_("You must define the vat number for your company"))
        # if not data['partner_id'].vat and not data['partner_id'].ref:
        #     raise ValidationError(_("You must define the vat or the cin number for your partner"))
        return {
            'doc_ids': docids,
            'data': data,
            'docs': docs,
            'tax_id': self.tax_id,
            'tva_code': self.tva_code,
            'categ_code': self.categ_code,
            'etb_num': self.etb_num
        }

    def tax_id(self, vat):
        if not vat:
            return ''
        vat_number = vat.replace('/', '').replace(' ', '')[:8]
        return vat_number.upper()

    def tva_code(self, vat):
        if not vat:
            return ''
        vat_number = ' '
        vat = vat.replace('/', '').replace(' ', '')
        if len(vat) > 8:
            vat_number = vat[8:9]
        return vat_number.upper()

    def categ_code(self, vat):
        if not vat:
            return ''
        vat_number = ' '
        vat = vat.replace('/', '').replace(' ', '')
        if len(vat) > 9:
            vat_number = vat[9:10]
        return vat_number.upper()

    def etb_num(self, vat):
        if not vat:
            return ''
        vat_number = ' '
        vat = vat.replace('/', '').replace(' ', '')
        if len(vat) > 10:
            vat_number = vat[10:]
        return vat_number.upper()

    def compute_withholdin_amount(self,obj,w):
        invoice_sum = 0.0
        for invoice in obj.account_invoice_ids:
            invoice_sum += invoice.amount_total
        return round(invoice_sum * 0.01 * w.rate, 3)



# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

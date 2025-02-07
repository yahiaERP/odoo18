# -*- coding: utf-8 -*-
{
    'name': "account_withholding_tax",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Whitecape",
    'website': "http://www.whitecapetech.com.com",

    'category': 'Accounting',
    'version': '0.1',

    'depends': ['account'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/account_withholding_views.xml',
        'views/account_withholding_tax_views.xml',
        'reports/withholding_report.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

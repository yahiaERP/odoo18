# -*- coding: utf-8 -*-
{
    'name': "account_withholding_tax",

    'summary': """
         Module retenue a la source en Tunisie selon les derniers lois de la ministére de
        la finance en 2025 
        """,

    'description': """
        Module retenue a la source en Tunisie selon les derniers lois de la ministére de
        la finance en 2025 
    """,

    'author': "yahia chehaidar",
    'category': 'Accounting',
    'version': '1.0',

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

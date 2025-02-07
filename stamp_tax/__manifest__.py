##############################################################################
{
    "name": "Fiscal stamp",
    # "version": "16.0.1.0.3",
    # "category": "Localization/Italy",
    "summary": """""
                Fiscal stamp
               """
    "",
    "author": "Shazler ERP",
    "website": "https://shazler.com",
    "license": "LGPL-3",
    "depends": [
        "base",
        "product",
        "account",
    ],
    "data": [
        # "data/data.xml",
        "views/account_move_view.xml",
        "views/company_view.xml",
        "views/account_move_report.xml",
    ],
    "installable": True,
}

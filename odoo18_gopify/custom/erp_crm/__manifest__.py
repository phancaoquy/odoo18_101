# -*- coding: utf-8 -*-
# CRM

{
    'name': 'CRM0.1',
    'version': '0.1',
    'category': 'Sales/CRM',
    'depends': [
        'base',
        'crm',
    ],
    'data': [
        'security/ir.model.access.csv',
        # 'security/crm_security.xml',

        'views/crm_lead_source_views.xml',
        'views/crm_lead_source_menu_views.xml',


    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3'
}

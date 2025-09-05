# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    "name": "Real Estate",
    "version": "16.0",
    "summary": "Real Estate Module",
    "category": "Uncategorized",
    "depends": ["base_setup"],
    "data": [
        "security/ir.model.access.csv",
        "views/estate_property_views.xml",
    ],  # no views or data files
    "installable": True,
    "application": True,
    'license': 'LGPL-3'
}

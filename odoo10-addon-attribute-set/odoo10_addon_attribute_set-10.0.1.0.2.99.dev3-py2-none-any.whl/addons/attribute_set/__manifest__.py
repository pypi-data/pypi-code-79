# -*- coding: utf-8 -*-
{
    "name": "Attribute Set",
    "version": "10.0.1.0.2",
    "category": "Generic Modules/Others",
    "license": "AGPL-3",
    "author": "Akretion",
    "website": "https://github.com/shopinvader/odoo-pim",
    "depends": ["base", "base_sparse_field_list_support"],
    "data": [
        "security/ir.model.access.csv",
        "security/attribute_security.xml",
        "views/menu_view.xml",
        "views/attribute_attribute_view.xml",
        "views/attribute_group_view.xml",
        "views/attribute_option_view.xml",
        "views/attribute_set_view.xml",
        "wizard/attribute_option_wizard_view.xml",
    ],
    "external_dependencies": {"python": ["unidecode"]},
}

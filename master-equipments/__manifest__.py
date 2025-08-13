# -*- coding: utf-8 -*-
{
    "name": "Master Equipments",
    "version": "1.0",
    "summary": "Manage master equipment records",
    "sequence": 20,
    "description": """
This module allows you to manage master equipment records, including their details and associated information.
    """,

    "category": "Inventory/Equipment Management",

    'installable': True,
    'application': True,

    "depends": ["base","stock","purchase"],
    "data": [
        "security/ir.model.access.csv",
        "security/master_equipment_category_rules.xml",
        "views/master_equipment_category_views.xml",
		"views/product_template_view.xml",
		"views/purchase_order_view.xml",
        "views/master_equipment_menus.xml",

    ]
}
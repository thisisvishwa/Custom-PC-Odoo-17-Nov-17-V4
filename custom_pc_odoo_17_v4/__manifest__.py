{
    'name': 'Custom PC Builder',
    'version': '1.0',
    'category': 'Sales',
    'summary': 'Custom PC Building Module for Odoo 17 Community Edition',
    'sequence': 10,
    'author': 'Your Company',
    'website': 'https://www.yourcompany.com',
    'depends': ['base', 'sale', 'stock'],
    'data': [
        'security/ir.model.access.csv',
        'data/pc_component_data.xml',
        'views/pc_component_view.xml',
        'views/pc_build_view.xml',
        'views/customer_view.xml',
        'views/templates.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'description': """
Custom PC Building Module for Odoo 17 Community Edition
=======================================================

This module enables users to custom-build PCs through a comprehensive, user-friendly interface.

Key features include:
--------------------
* Custom PC Configuration Interface
* Component Management
* Price Estimation and Compatibility Check
* Integration with Inventory and Sales Modules
* Customer Profiles and Order History
    """,
}
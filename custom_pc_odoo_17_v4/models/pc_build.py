```python
from odoo import models, fields, api

class PcBuild(models.Model):
    _name = 'custom_pc_odoo_17_v4.pc_build'
    _description = 'PC Build'

    name = fields.Char(string='Build Name', required=True)
    customer_id = fields.Many2one('custom_pc_odoo_17_v4.customer', string='Customer')
    component_ids = fields.Many2many('custom_pc_odoo_17_v4.pc_component', string='Components')
    total_price = fields.Float(string='Total Price', compute='_compute_total_price')
    is_compatible = fields.Boolean(string='Is Compatible', compute='_check_compatibility')

    @api.depends('component_ids')
    def _compute_total_price(self):
        for record in self:
            record.total_price = sum(component.price for component in record.component_ids)

    @api.depends('component_ids')
    def _check_compatibility(self):
        for record in self:
            # Placeholder for compatibility check logic
            record.is_compatible = True

    def create_sales_order(self):
        # Placeholder for sales order creation logic
        pass
```
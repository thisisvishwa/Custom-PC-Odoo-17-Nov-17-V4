```python
from odoo import models, fields

class Customer(models.Model):
    _name = 'custom_pc_odoo_17_v4.customer'
    _description = 'Customer'

    name = fields.Char(string='Name', required=True)
    email = fields.Char(string='Email')
    phone = fields.Char(string='Phone')
    pc_build_ids = fields.One2many('custom_pc_odoo_17_v4.pc_build', 'customer_id', string='PC Builds')

    def save_build(self, pc_build_id):
        self.ensure_one()
        self.write({'pc_build_ids': [(4, pc_build_id)]})

    def view_past_orders(self):
        self.ensure_one()
        return {
            'name': 'Past Orders',
            'type': 'ir.actions.act_window',
            'view_mode': 'tree,form',
            'res_model': 'custom_pc_odoo_17_v4.pc_build',
            'domain': [('customer_id', '=', self.id)],
        }
```
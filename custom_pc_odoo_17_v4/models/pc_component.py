```python
from odoo import models, fields, api, exceptions

class PcComponent(models.Model):
    _name = 'custom_pc_odoo_17_v4.pc_component'
    _description = 'PC Component'

    name = fields.Char(string='Component Name', required=True)
    specifications = fields.Text(string='Specifications')
    price = fields.Float(string='Price', required=True)
    compatibility = fields.Many2many('custom_pc_odoo_17_v4.pc_component', 'pc_component_compatibility_rel', 'component_id', 'compatible_id', string='Compatible Components')
    supplier_info = fields.Many2one('res.partner', string='Supplier')

    @api.constrains('price')
    def _check_price(self):
        for record in self:
            if record.price <= 0:
                raise exceptions.ValidationError("Price must be greater than 0")

    @api.constrains('compatibility')
    def _check_compatibility(self):
        for record in self:
            if record.id in record.compatibility.ids:
                raise exceptions.ValidationError("A component cannot be compatible with itself")
```
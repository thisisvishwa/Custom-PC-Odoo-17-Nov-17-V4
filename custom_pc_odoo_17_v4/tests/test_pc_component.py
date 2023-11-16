```python
from odoo.tests import common

class TestPcComponent(common.TransactionCase):

    def setUp(self):
        super(TestPcComponent, self).setUp()
        self.PcComponent = self.env['pc_component']

    def test_crud_operations(self):
        # Create a new PC component
        pc_component = self.PcComponent.create({
            'name': 'Test Component',
            'specifications': 'Test Specifications',
            'price': 100.0,
            'compatibility': 'Test Compatibility',
            'supplier_info': 'Test Supplier'
        })

        # Read the created PC component
        pc_component = self.PcComponent.search([('name', '=', 'Test Component')])
        self.assertEqual(pc_component.name, 'Test Component')

        # Update the created PC component
        pc_component.write({
            'name': 'Updated Test Component'
        })
        self.assertEqual(pc_component.name, 'Updated Test Component')

        # Delete the created PC component
        pc_component.unlink()
        pc_component = self.PcComponent.search([('name', '=', 'Updated Test Component')])
        self.assertEqual(len(pc_component), 0)

    def test_price_estimation_and_compatibility_check(self):
        # Create a new PC component
        pc_component = self.PcComponent.create({
            'name': 'Test Component',
            'specifications': 'Test Specifications',
            'price': 100.0,
            'compatibility': 'Test Compatibility',
            'supplier_info': 'Test Supplier'
        })

        # Check price estimation
        self.assertEqual(pc_component.price, 100.0)

        # Check compatibility
        self.assertEqual(pc_component.compatibility, 'Test Compatibility')
```
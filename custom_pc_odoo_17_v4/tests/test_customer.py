```python
from odoo.tests import common

class TestCustomer(common.TransactionCase):

    def setUp(self):
        super(TestCustomer, self).setUp()
        self.Customer = self.env['custom_pc_odoo_17_v4.customer']

    def test_create_customer(self):
        """
        Test the creation of a customer and check if the fields are correctly set
        """
        customer = self.Customer.create({
            'name': 'Test Customer',
            'email': 'test@customer.com',
        })

        self.assertEqual(customer.name, 'Test Customer')
        self.assertEqual(customer.email, 'test@customer.com')

    def test_customer_order_history(self):
        """
        Test the order history of a customer
        """
        customer = self.Customer.create({
            'name': 'Test Customer',
            'email': 'test@customer.com',
        })

        # Create a PC build for the customer
        pc_build = self.env['custom_pc_odoo_17_v4.pc_build'].create({
            'name': 'Test Build',
            'customer_id': customer.id,
        })

        # Check if the PC build is in the customer's order history
        self.assertIn(pc_build, customer.order_history)

    def test_customer_saved_builds(self):
        """
        Test the saved builds of a customer
        """
        customer = self.Customer.create({
            'name': 'Test Customer',
            'email': 'test@customer.com',
        })

        # Create a PC build for the customer
        pc_build = self.env['custom_pc_odoo_17_v4.pc_build'].create({
            'name': 'Test Build',
            'customer_id': customer.id,
        })

        # Save the PC build
        customer.saved_builds = [(4, pc_build.id)]

        # Check if the PC build is in the customer's saved builds
        self.assertIn(pc_build, customer.saved_builds)
```
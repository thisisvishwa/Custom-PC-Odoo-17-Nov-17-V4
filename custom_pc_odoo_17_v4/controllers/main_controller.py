```python
from odoo import http
from odoo.http import request

class MainController(http.Controller):

    @http.route('/custom_pc_odoo_17_v4/configure', type='http', auth='user')
    def configure_pc(self, **kwargs):
        pc_components = request.env['pc_component'].search([])
        return request.render('custom_pc_odoo_17_v4.configure_pc', {'pc_components': pc_components})

    @http.route('/custom_pc_odoo_17_v4/save_build', type='json', auth='user')
    def save_build(self, **kwargs):
        try:
            pc_build = request.env['pc_build'].create(kwargs)
            return {'status': 'success', 'message': 'PC Build saved successfully', 'pc_build_id': pc_build.id}
        except Exception as e:
            return {'status': 'error', 'message': str(e)}

    @http.route('/custom_pc_odoo_17_v4/view_build/<int:build_id>', type='http', auth='user')
    def view_build(self, build_id):
        pc_build = request.env['pc_build'].browse(build_id)
        if not pc_build.exists():
            return request.not_found()
        return request.render('custom_pc_odoo_17_v4.view_build', {'pc_build': pc_build})
```
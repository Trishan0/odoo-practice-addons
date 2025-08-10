from odoo import api, fields, models

class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    master_equipment_category_id = fields.Many2one('master.equipment.category')

    @api.onchange('product_id')
    def onchange_product_for_equipment_category(self):
        for line in self:
            if line.product_id and line.product_id.master_equipment_category_id:
                line.master_equipment_category_id = line.product_id.master_equipment_category_id
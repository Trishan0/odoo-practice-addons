from odoo import fields, models

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    master_equipment_category_id = fields.Many2one('master.equipment.category')
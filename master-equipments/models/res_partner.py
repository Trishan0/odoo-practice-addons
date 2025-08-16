from email.policy import default

from odoo import fields, models

class ResPartner(models.Model):
    _inherit = 'res.partner'

    is_filter_po_products_category = fields.Boolean(string="Filter Products in PO based on Category",default=False)
    product_list_ids = fields.Many2many('product.product')
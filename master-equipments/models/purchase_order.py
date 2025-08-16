# -*- coding: utf-8 -*-
from odoo import api, fields, models


class PurchaseOrder(models.Model):
    """ This model represents purchase.order."""
    _inherit = 'purchase.order'

    product_list_ids = fields.Many2many('product.product', compute="_get_products_from_vendor")

    @api.depends('partner_id')
    def _get_products_from_vendor(self):
        for po in self:
            if po.partner_id and po.partner_id.is_filter_po_products_category and po.partner_id.product_list_ids:
                po.product_list_ids = po.partner_id.product_list_ids
            else:
                po.product_list_ids = self.env['product.product'].search([('purchase_ok', '=', True)])

import re
import typing

from odoo import api, fields, models
from odoo.api import ValuesType, Self
from odoo.exceptions import ValidationError


class ResPartner(models.Model):
    _inherit = 'res.partner'

    is_filter_po_products_category = fields.Boolean(string="Filter Products in PO based on Category",default=False)
    product_list_ids = fields.Many2many('product.product')
    vendor_priority = fields.Selection([('low',"Low"),("medium","Medium"),("high","High"),("critical","Critical"),("strategic","Strategic")],default="medium")

    @api.constrains('mobile')
    def _check_mobile_number(self):
        for record in self:
            if record.mobile:
                cleaned_mobile = record.mobile.replace(" ","").replace("-","").replace("+","")
                if not cleaned_mobile.isdigit() or len(cleaned_mobile) != 10:
                    raise ValidationError("Mobile number should be 10 digits long and contain only numbers.")


    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if 'mobile' in vals and vals_list['mobile']:
                vals_list['mobile'] = self._format_mobile_number(vals_list['mobile'])
        return super().create(vals_list)

    def write(self, vals_list):
        for vals in vals_list:
            if 'mobile' in vals and vals_list['mobile']:
                vals_list['mobile'] = self._format_mobile_number(vals_list['mobile'])
                print(f"Formatted mobile number: {vals_list['mobile']}")
        return super().write(vals_list)


    def _format_mobile_number(self, mobile):
            if mobile:
                mobile_number = re.sub(r'[^\d]','',mobile)
                if len(mobile_number) == 10:
                    return f"+{mobile}"
            return mobile

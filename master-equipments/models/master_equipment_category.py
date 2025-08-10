# -*- coding: utf-8 -*-
from odoo import api, fields, models


class MasterEquipmentCategory(models.Model):
    _name = 'master.equipment.category'
    _description = 'Master Equipment Category'

    name = fields.Char(string='Title', required=True)
    reference = fields.Char(string='Reference', required=True)

    _sql_constraints = [
        ('reference_uniq', 'unique(reference)', 'The reference must be unique.'),
    ]

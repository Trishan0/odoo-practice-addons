# -*- coding: utf-8 -*-
from odoo import api, fields, models


class MasterEquipmentCategory(models.Model):
    _name = 'master.equipment.category'
    _description = 'Master Equipment Category'

    name = fields.Char(string='Reference', required=True)
    title = fields.Char(string='Title', required=True)

    _sql_constraints = [
        ('name_uniq', 'unique(name)', 'The reference must be unique.'),
    ]

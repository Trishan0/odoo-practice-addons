from odoo import fields, models

class ProcManagerReportWizard(models.TransientModel):
    _name = 'proc.manager.report.wizard'
    _description = 'Procurement Manager Report Wizard'

    name = fields.Many2many(comodel_name='res.users', string='Procurement Manager', domain="[('share', '=', False)]")

    def filter_po_by_proc_manager(self):
        record = self.env['purchase.order'].search([("user_id",'in', self.name.ids)])
        return {
            'name': 'Purchase Order',
            'view_mode': 'list,form',
            'res_model': 'purchase.order',
            "domain": [('id','in', record.ids)],
            "type": "ir.actions.act_window",
        }
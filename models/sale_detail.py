from odoo import models,fields,api,_

class Student(models.Model):
    _inherit="sale.order"
    


    def open_so_detail(self):
        return {
            'type': 'ir.actions.act_window',
            'name': _('So Report'),
            'res_model': 'sodata.wizard',
            'view_mode': 'form',
            'target':'new',
        }
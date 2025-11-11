from odoo import models,fields,api,_

class Student(models.Model):
    _inherit="stock.picking"
    
    def open_delevery(self):
        return {
            'type': 'ir.actions.act_window',
            'name': _('Delevery'),
            'res_model': 'delivery.wizard',
            'view_mode': 'form',
            'target':'new',
        } 
        
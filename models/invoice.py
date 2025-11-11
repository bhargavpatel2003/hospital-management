from odoo import models,fields,api,_

class Student(models.Model):
    _inherit="account.move"
    


    # def open_invoice(self):
    #     return {
    #         'type': 'ir.actions.act_window',
    #         'name': _('Invoice Wizard'),
    #         'res_model': 'invoice.wizard',
    #         'view_mode': 'form',
    #         'target':'new',
    #     }
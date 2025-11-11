from odoo import models, fields, api


class DelveryWizard(models.TransientModel):
    _name = "delivery.wizard"
    _description = "delivery Wizard"

    partner_id = fields.Many2one("res.partner", string="Del Address", required=True)
    line_ids = fields.One2many("delivery.line.wizard", "wizard_id", string="Invoice Lines")



    @api.model
    def default_get(self, fields_list):

        res=super(DelveryWizard,self).default_get(fields_list)
        active_id=self.env.context.get('active_id')

        if active_id:
            delivery_data=self.env['stock.picking'].browse(active_id)
            res['partner_id']=delivery_data.partner_id

            lines=[]

            for line in delivery_data.move_ids_without_package:

                lines.append((0,0,{
                    'product_id':line.product_id, 
                    'date':line.date, 
                    'deadline_date':line.date_deadline, 
                    'demand_qty':line.product_uom_qty, 
                    'reserve_qty':line.forecast_availability,
                    'done_qty':line.quantity_done
                    
                }))

            res['line_ids']=lines

        return res

class DelverylineWizard(models.TransientModel):
    _name = "delivery.line.wizard"
    _description = "delivery Wizard"

    wizard_id = fields.Many2one("delivery.wizard", string="Wizard", ondelete="cascade")
    product_id = fields.Many2one("product.product", string="Product", required=True)
    demand_qty=fields.Float(string="Demand")
    reserve_qty=fields.Float(string="Reserve")
    done_qty=fields.Float(string="Done")
    date=fields.Datetime(string="Date")
    deadline_date=fields.Datetime(string="Deadline")


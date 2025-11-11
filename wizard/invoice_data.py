from odoo import models, fields, api


class InvoiceWizard(models.TransientModel):
    _name = "invoice.wizard"
    _description = "Invoice Wizard"

    partner_id = fields.Many2one("res.partner", string="Customer", required=True)
    inv_line_ids = fields.One2many("invoice.wizard.line", "wizard_id", string="Invoice Lines")

    @api.model
    def default_get(self, fields_list):

        print("fieldssssssssssss",fields_list)

        res=super(InvoiceWizard,self).default_get(fields_list)
        print('ressssssssssss',res)

        active_id=self.env.context.get('active_id')
        
        if active_id:
            invoice=self.env['account.move'].browse(active_id)
            res['partner_id']=invoice.partner_id.id

            lines=[]

            for line in invoice.invoice_line_ids:
                lines.append((0,0,{
                    'product_id':line.product_id,
                    'description':line.name, 
                    'product_qty':line.quantity, 
                    'price_unit' :line.price_unit, 
                    'tax_ids':[(6,0,line.tax_ids.ids)],
                    'subtotal':line.price_subtotal,
                }))
                
            res['inv_line_ids']=lines
        print('updateeeee...............',res)
        return res


    def get_inv_sum(self):
        invs=self.env['account.move'].search([])
        inv_sum=0

        for inv in invs:
            inv_sum+=sum(inv.invoice_line_ids.filtered(lambda line: line.partner_id.name == "Bhargav").mapped('price_subtotal'))

        print('inv summmmmmmm',inv_sum)

        return inv_sum


class InvoiceWizardLine(models.TransientModel):
    _name = "invoice.wizard.line"
    _description = "Invoice Wizard Line"

    wizard_id = fields.Many2one("invoice.wizard", string="Wizard", ondelete="cascade")
    product_id = fields.Many2one("product.product", string="Product", required=True)
    description = fields.Char(string="Description")
    product_qty = fields.Float(string="Ordered Qty")
    price_unit = fields.Float(string="Unit Price")
    tax_ids = fields.Many2many("account.tax", string="Taxes")
    subtotal = fields.Monetary(string="Subtotal", store=True)
    currency_id = fields.Many2one("res.currency", default=lambda self: self.env.company.currency_id)

    
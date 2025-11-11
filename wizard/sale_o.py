from odoo import models, fields,_,api

class LrReportWizard(models.TransientModel):
    _name = 'sodata.wizard'
    _description = 'sales Wizard'

    # start_date = fields.Date("Start Date", required=True)
    # end_date = fields.Date("End Date", required=True)

    # def action_download_excel(self):
    #     return self.env['lr.trip.details']._generate_excel(self.start_date, self.end_date)
    partner_id=fields.Many2one('res.partner',string="Customer")
    sale_order_line=fields.One2many('sodata.wizard.line','sales_ord_id',string="sale line")


    @api.model
    def default_get(self, fields_list):
        res= super(LrReportWizard,self).default_get(fields_list)

        print("fildsssss",fields_list)
        print("???????",res)

        active_id=self.env.context.get('active_id')

        print('?????????????',self.env.context)

        if active_id:
            sale_order=self.env['sale.order'].browse(active_id)
            
            res['partner_id']=sale_order.partner_id.id

            lines=[]
            for line in sale_order.order_line:
                lines.append((0,0,{

                    'product_id':line.product_id.id,
                    'discription':line.name,
                    'product_qty':line.product_uom_qty,
                    'qty_dilv': line.qty_delivered,
                    'qty_invoice':line.qty_invoiced,
                    'price_unit':line.price_unit,
                    'tax_ids':[(6,0,line.tax_id.ids)],
                    'subtotal':line.price_subtotal,
                    'currency_id':line.currency_id.id
                
                }))
            print("?????????",lines)

        res['sale_order_line']=lines

        return res  
    
    def confirm_so(self):
        activ_id=self.env.context.get('active_id')

        if activ_id:
            sale_or=self.env['sale.order'].browse(activ_id)

            sale_or.order_line.unlink()

            lines=[]

            for line in self.sale_order_line:
                    lines.append((0,0,{

                            'product_id':line.product_id.id,
                            'name':line.discription,
                            'product_uom_qty':line.product_qty,
                            'qty_delivered':line.qty_dilv,
                            'qty_invoiced':line.qty_invoice, 
                            'price_unit':line.price_unit

                    }))

            sale_or.order_line=lines



class Saleorderwix(models.TransientModel):
    _name = 'sodata.wizard.line'
    _description = 'sales Wizard line'


    sales_ord_id=fields.Many2one('sodata.wizard')
    product_id = fields.Many2one(
        'product.product',
        string="Products",
    ) 
    discription=fields.Text(string="Discription")
    product_qty=fields.Float(string="Qty")
    qty_dilv=fields.Float(string="deliverd")
    qty_invoice=fields.Float(string="Invoice qty")
    price_unit=fields.Float(string="Unit Price")
    tax_ids = fields.Many2many(
        'account.tax',
        string="Taxes",

    )
    subtotal=fields.Monetary(string="Subtotal",currency_field="currency_id")

    currency_id = fields.Many2one(
        'res.currency',
        string="Currency",
        required=True,
        default=lambda self: self.env.company.currency_id.id
    )
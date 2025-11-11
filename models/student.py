from odoo import models,fields,api


class Student(models.Model):
    _name="school.student"
    _description="studeng"
    _inherit = ["mail.thread", "mail.activity.mixin"]


    name=fields.Char(string="Name")
    firstname=fields.Char(string="firstname",compute="compute_name")
    partner_id=fields.Many2one('res.partner','Student')
    age=fields.Integer(string="age",compute="compute_age")
    dob=fields.Date(string="Date Of Birth")
    std=fields.Integer(string="Standard",tracking=True)
    image = fields.Image(string="",max_width=1920, max_height=1920)
    email=fields.Char(string="Email")
    gendor=fields.Selection([("male","Male"),("female","Female")],string="Gender",default='male')
    teacher_id = fields.Many2one("school.teacher", string="Class Teacher")
    father_name=fields.Char(string="fathername")
    
    # child=fields.Boolean(string="Child",compute="get_genration")
    # adult=fields.Boolean(string="Adult",compute="get_genration")
    age_group=fields.Selection([("chld","Child"),('adlt',"Adult")],compute="get_genration",default=False)

    def send_mail_template(self):
        for rec in self:
            if rec.name:
                mail_template = self.env.ref('school_management.mail_template_send_student')
                mail_template.send_mail(rec.id, force_send=True)

    @api.model_create_multi
    def create(self, vals_list):
        
        res=super().create(vals_list)
        print(">>>>>>>>>>>>>>>>>>>>>>>>.",res)
        for rec in res:
            rec.email=rec.partner_id.email
         
        return res

    @api.onchange('partner_id')
    def get_email(self):
        if self.partner_id: 
            self.email=self.partner_id.email


    @api.depends('partner_id')
    def compute_name(self):
        if self.partner_id:
            self.firstname=self.partner_id.name
        else:
            self.firstname=''
    
    @api.depends('dob')
    def compute_age(self):
        for rec in self:
            today=fields.Date.today()
            rec.age=(today.year-rec.dob.year) if rec.dob else 0


    @api.depends('age')
    def get_genration(self):
        for rec in self:
            if rec.age < 15:
                rec.age_group='chld'
            elif rec.age > 15:
                rec.age_group='adlt'
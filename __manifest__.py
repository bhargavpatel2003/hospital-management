{
    "name": "School Management",
    "version": "1.0",
    "category": "Education",
    "depends": ["base",'mail','account','sale','stock'],
    "data": [
        'security/ir.model.access.csv',
        'data/mail_template.xml',
        'views/student.xml',
        'views/teacher.xml',
        'views/sale_orders_views.xml',
        'wizard/new_wizard.xml',
        'views/invoce_view.xml',
        'wizard/invoice_wizard.xml',
        'views/delivery_view.xml',
        'wizard/delivery.xml',
        'report/student_idcard_template.xml',
        'report/ir_actions_report.xml',
        

    ],
    "installable": True,
    "application": True,
}

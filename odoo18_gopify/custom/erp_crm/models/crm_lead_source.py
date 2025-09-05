from odoo import fields, models
import secrets


class CrmLeadSource(models.Model):
    _name = 'crm.lead.source'
    _description = 'CRM Lead Source'

    # Description
    name = fields.Char(string='Opportunity Source', default='Unknown')
    description = fields.Text(string='Description', default='Description')
    company_id = fields.Many2one('res.partner')
    api_key = fields.Char(string='API key')
    active = fields.Boolean('Active', default=True)
    currency_id = fields.Many2one(
        'res.currency',
        string='Currency',
        required=True,
        default=lambda self: self.env.company.currency_id
    )
    estimated_total = fields.Float(
        string='Estimated Totals',
        currency_field='currency_id'
    )
    crm_lead_ids = fields.One2many(
        "crm.lead",
        "source_company_id",
        string="Leads"
    )

    def generate_api_key(self):
        for record in self:
            record.write({'api_key': secrets.token_hex(16)})

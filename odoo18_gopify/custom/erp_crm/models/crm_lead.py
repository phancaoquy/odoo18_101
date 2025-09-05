from odoo import fields, models


class CrmLead(models.Model):
    _inherit = "crm.lead"

    # Description
    source_company_id = fields.Many2one(
        "crm.lead.source",
        string="Source Company",
    )

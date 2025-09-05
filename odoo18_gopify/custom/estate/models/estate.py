from odoo import fields, models
from datetime import date
from dateutil.relativedelta import relativedelta


class RealEstate(models.Model):
    _name = "estate.property"
    _description = "Real Estate Model"

    def _default_date_available(self):
        return date.today() + relativedelta(months=3)

    name = fields.Char("Estate Name", required=True, default="Unknown")
    description = fields.Text("Description")
    postcode = fields.Char("Postcode")
    date_available = fields.Date(
        "Date Available", copy=False, default=_default_date_available
    )
    active = fields.Boolean("Active", default=True)
    state = fields.Selection(
        string="Status",
        selection=[
            ("new", "New"),
            ("offer_received", "Offer Received"),
            ("offer_accepted", "Offer Accepted"),
            ("sold", "Sold"),
            ("canceled", "Canceled"),
        ],
        default="new",
        copy=False,
    )
    last_seen = fields.Datetime("Last Seen", copy=False, default=fields.Datetime.now)
    expected_price = fields.Float("Expected Price", required=True)
    selling_price = fields.Float("Selling Price", copy=False)
    bedrooms = fields.Integer("Bedrooms", default=2)
    living_area = fields.Integer("Living Area")
    facades = fields.Integer("Facades")
    garage = fields.Boolean("Garage")
    garden = fields.Boolean("Garden")
    garden_area = fields.Integer("Garden Area")
    garden_orientation = fields.Selection(
        string="Garden Orientation",
        selection=[
            ("north", "North"),
            ("south", "South"),
            ("east", "East"),
            ("west", "West"),
        ],
    )

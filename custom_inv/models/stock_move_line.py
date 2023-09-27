from odoo import api, fields, models, _
from pprint import pprint
from odoo.exceptions import UserError, ValidationError
from datetime import datetime,date


class MyStockMoveLine(models.Model):
    _inherit = 'stock.move.line'


    transferred_qty = fields.Float()

    def unlink(self):

        for rec in self:
            if rec.picking_id:
                move_line= self.env["stock.picking"].search([("id", "=", rec.picking_id.id)])
                move_line= self.env["stock.move.line"].search([("picking_id", "=", move_line.parent_id.id),("product_id", "=", rec.product_id.id)])
                move_line.write({"transferred_qty": 0})

        result = super(MyStockMoveLine, self).unlink()

        # if self.picking_id:
        #     move_line= self.env["stock.picking"].search([("id", "=", self.picking_id.id)])
        #     move_line= self.env["stock.move.line"].search([("picking_id", "=", move_line.parent_id.id),("product_id", "=", self.product_id.id)])
        #     move_line.write({"transferred_qty": 0})
        # result = super(MyStockMoveLine, self).unlink()

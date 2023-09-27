# -*- coding: utf-8 -*-

from odoo import models, fields, api




class stockCardViewInherit(models.TransientModel):
    _inherit='stock.card.view'
    department_id= fields.Many2one(comodel_name='hr.department')






















class stockCardReportInherit(models.TransientModel):
    _inherit='report.stock.card.report'
    custome_test_field = fields.Char()
#
    @api.model
    def _compute_results(self):
        self.ensure_one()
        date_from = self.date_from or "0001-01-01"
        self.date_to = self.date_to or fields.Date.context_today(self)
        locations = self.env["stock.location"].search(
            [("id", "child_of", [self.location_id.id])]
        )
        print(locations.ids)
        self._cr.execute(
            """
            SELECT move.date, move.product_id, move.product_qty,
                move.product_uom_qty, move.product_uom, move.reference,
                move.location_id, move.location_dest_id,
                case when move.location_dest_id in %s
                    then move.product_qty end as product_in,
                case when move.location_id in %s
                    then move.product_qty end as product_out,
                case when move.date < %s then True else False end as is_initial,
                move.picking_id
            FROM stock_move move
            WHERE (move.location_id in %s or move.location_dest_id in %s)
                and move.state = 'done' and move.product_id in %s
                and CAST(move.date AS date) <= %s
            ORDER BY move.date, move.reference
        """,
            (
                tuple(locations.ids),
                tuple(locations.ids),
                date_from,
                tuple(locations.ids),
                tuple(locations.ids),
                tuple(self.product_ids.ids),
                self.date_to,
            ),
        )
        stock_card_results = self._cr.dictfetchall()
        # abdallah custome code
        stockepicking = self.env["stock.picking"]

        for line in stock_card_results:
            pick = stockepicking.browse(line['picking_id'])
            line['department_id']=pick.department_id.id
        print(stock_card_results)

        print("pick department", pick.department_id.name)
        print(line)
        #

        ReportLine = self.env["stock.card.view"]
        self.results = [ReportLine.new(line).id for line in stock_card_results]


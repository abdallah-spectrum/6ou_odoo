from odoo import api, fields, models, _
from pprint import pprint
from odoo.exceptions import UserError, ValidationError
from datetime import datetime,date


class StockPicking(models.Model):
    _inherit = 'stock.picking'


    department_id = fields.Many2one('hr.department', 'Department',)
    parent_id = fields.Many2one(
        comodel_name="stock.picking",
        required=False,
        string='checking receipt number',
        translatable=True,
    )
    product_template_id = fields.Many2one(
        comodel_name="product.template",
        required=False,
        string='Car number',
        translatable=True,
    )
    hide_fields = fields.Boolean(compute='compute_hide_fields')
    transferred = fields.Boolean()

    def button_validate(self):
        result = super(StockPicking, self).button_validate()
        base_lines = self.env["stock.move.line"].search([("picking_id", "=", self.parent_id.id),("transferred_qty", "!=", 0)],order="id asc")
        move_lines = self.env["stock.move.line"].search([("picking_id", "=", self.parent_id.id)],order="id asc")
        
        if len(move_lines) ==len(base_lines):
            self.parent_id.transferred = 't'
        return result 

    @api.onchange('picking_type_id')
    def compute_hide_fields(self):
        if self.picking_type_id.code !='outgoing':
            self.hide_fields = True
        else:
            self.hide_fields = False

    @api.onchange('parent_id')
    def create_lines(self):
        if bool(self.parent_id) != False:
            admin_id = 2
            now = datetime.now()
            now_str=now.strftime('%Y-%m-%d %H:%M:%S')
            today = datetime.today()
            parent_id = self.parent_id
            location_id = self.location_id
            location_dest_id = self.location_dest_id
            last_hour_str=today.replace(hour=int(now.hour)-1).strftime('%Y-%m-%d %H:%M:%S')
            move_ids=[]
            move_line_ids=[]
            user_category_ids=[]
            user_id = self.env.user.id
            banned_group_ids = self.env["res.users"].search([("id", "=", user_id)])
            if bool(banned_group_ids) != False:
                user_category_ids=banned_group_ids.user_category_ids
                user_product_ids=banned_group_ids.user_product_ids.ids

            move = self.env["stock.move"].search([
                    ("picking_id", "=", parent_id.id),
                ],order="id asc")
            base_move_line2 = self.env["stock.move.line"].search([
                ('state','=','draft'),
                ('location_id','=',self.location_id.id),
                ('location_dest_id','=',self.location_dest_id.id),
                ('create_date','>',last_hour_str),
                ('create_date','<',now_str),
                ],order="move_id asc")
            move_lines = self.env["stock.move.line"].search([
                ("picking_id", "=", parent_id.id),
                ],order="move_id asc")
            if bool(base_move_line2) != False:
                for line in base_move_line2:
                    line.unlink()
            for line in move:
                try:
                    product_id = line['product_id'].product_tmpl_id.id
                    category_id = line['product_id'].product_tmpl_id.categ_id
                    if category_id  in user_category_ids or user_id==admin_id or product_id in user_product_ids:    
                        vals = {
                        'picking_id': self.id,
                        'product_id': line['product_id'].id,
                        'description_picking': line['description_picking'],
                        'product_uom': line['product_uom'].id,
                        'product_uom_qty': line['product_uom_qty'],
                        'name': line['name'],
                        'state': 'draft',
                        'location_id': self.location_id.id,
                        'location_dest_id': self.location_dest_id.id,
                    }
                        move_id= self.env['stock.move'].create(vals)
                        move_ids.append(move_id)
                except  (UserError,ValidationError) as e:
                    ...
            for i,line in enumerate(move_lines):
                try:
                    product_id = line['product_id'].product_tmpl_id.id
                    category_id = line['product_id'].product_tmpl_id.categ_id
                    if int(line['transferred_qty']) != line['qty_done'] and (category_id  in user_category_ids or user_id==admin_id or product_id in user_product_ids) : 
                        vals={
                        'picking_id': self.id,
                        'company_id': line['company_id'].id,
                        'product_id': line['product_id'].id,
                        'product_uom_id': line['product_uom_id'].id,
                        'product_uom_qty': line['product_uom_qty'],
                        'qty_done': line['qty_done'],
                        'package_id': line['package_id'].id,
                        'package_level_id': line['package_level_id'].id,
                        'lot_id': line['lot_id'].id,
                        'lot_name': line['lot_name'],
                        'result_package_id': line['result_package_id'].id,
                        'date': line['date'],
                        'owner_id': line['owner_id'].id,
                        'location_id': self.location_id.id,
                        'location_dest_id': self.location_dest_id.id,
                        'state': 'draft',
                        'reference': line['reference'],
                        'description_picking': line['description_picking'],
                        }
                        move_line_id = self.env['stock.move.line'].create(vals)
                        move_line_ids.append(move_line_id)
                        created = line.write({"transferred_qty": line['qty_done']})
                except  (UserError,ValidationError) as e:
                    ...
            for i in range(len(move_line_ids)):
                move_line = self.env["stock.move.line"].search([
                    ("id", "=", move_line_ids[i].id),
                ])
                updated = move_line.write({"move_id": move_ids[i].id})

            self.parent_id=parent_id
            self.location_id=location_id
            self.location_dest_id=location_dest_id
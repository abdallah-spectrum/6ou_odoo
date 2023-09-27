


from odoo import fields , api,models

class purchaseRequisition(models.Model):
  _inherit='purchase.requisition'
  # custome_products = fields.One2many('product.product', 'inverse_field_name', string='custome_products')

  def state_convert(self, state):
    if state == 'draft':
      return 'مسودة'
    elif state == 'ongoing':
      return 'جاري'
    elif state == 'open':
      return 'طريقة الاختيار'
    elif state == 'done':
      return 'مغلق'
    elif state == 'cancel':
      return 'ملغي'
    elif state == 'in_progress':
      return 'موكد'

  def print_report(self):
    # self.ensure_one()
    # pass
    agrement={}
    products=[]
    agrement['ref']=str(self.name)
    if self.date_end:
      agrement['date_end']=self.date_end.strftime('%B %d, %Y')
    else:
     agrement['date_end']=self.date_end
    agrement['type']=self.type_id.name
    agrement['state']=self.state_convert(self.state)
    



    for po in self.purchase_ids :
      for order_line in po.order_line:
        print(order_line.product_id.name)
        products.append({
          "code":order_line.product_id.code,
          'name':order_line.product_id.name,
          'qty':order_line.product_qty,
          'vendor':order_line.partner_id.name,
          'rfq':order_line.order_id.name,
          'price':order_line.price_subtotal,
        })
    
  
    products.sort(key=lambda x:( x['name'] , x['price']))
   
    return self.env.ref('purchase_aggrement_report.action_print_purchase_aggremt2').report_action(self,{"products":products,'agrement':agrement})



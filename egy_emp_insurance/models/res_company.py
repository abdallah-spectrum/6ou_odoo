from odoo import api, fields, models, _
from pprint import pprint

class ParticularReport(models.AbstractModel):
    _name = 'report.egy_emp_insurance.report_form_view'

    def _get_report_values(self, docids, data=None,ctx=None):
        from_date=data['form']['from_date']
        to_date=data['form']['to_date']
        draft=data['form']['draft']
        posted=data['form']['posted']
        report_type=data['form']['report_type']
        partner_id=data['form']['partner_id'][1]
        status_list = []
        if draft ==True:
            status_list.append('draft')
        if posted ==True:
            status_list.append('posted')
        account_account=data['form']['account_account']
        debit_total=0
        report = self.env['ir.actions.report']._get_report_from_name('egy_emp_insurance.report_form_view')
        if report_type =='debit': 
           report.name='debit note'
        elif report_type =='credit': 
           report.name='credit note'
        obj = self.env[report.model].browse(data['context']['allowed_company_ids'])
        account_move_lines=self.env["account.move.line"].search(['&',('account_id', 'in', account_account),('partner_id', '=', partner_id),('debit', '!=', 0),('date', '>=', from_date),('date', '<=', to_date),('parent_state', 'in', status_list)],order="date asc")
        account_move_lines_grouped=self.env["account.move.line"].read_group(['&',('account_id', 'in', account_account),('partner_id', '=', partner_id),('debit', '!=', 0),('date', '>=', from_date),('date', '<=', to_date),('parent_state', 'in', status_list)],orderby="account_id,date asc",groupby=["date","account_id"],fields=['id','date','debit','credit','account_id'],lazy=False)

        if report_type =='debit': 
            account_move_lines=self.env["account.move.line"].search(['&',('account_id', 'in', account_account),('partner_id', '=', partner_id),('debit', '!=', 0),('date', '>=', from_date),('date', '<=', to_date),('parent_state', 'in', status_list)],order="date asc")
            account_move_lines_grouped=self.env["account.move.line"].read_group(['&',('account_id', 'in', account_account),('partner_id', '=', partner_id),('debit', '!=', 0),('date', '>=', from_date),('date', '<=', to_date),('parent_state', 'in', status_list)],orderby="account_id,date asc",groupby=["date","account_id"],fields=['id','date','debit','credit','account_id'],lazy=False)
            for account_move_line in account_move_lines:
                debit_total+=account_move_line['debit']
        elif report_type =='credit': 
            account_move_lines=self.env["account.move.line"].search(['&',('account_id', 'in', account_account),('partner_id', '=', partner_id),('credit', '!=', 0),('date', '>=', from_date),('date', '<=', to_date),('parent_state', 'in', status_list)],order="date asc")
            account_move_lines_grouped=self.env["account.move.line"].read_group(['&',('account_id', 'in', account_account),('partner_id', '=', partner_id),('credit', '!=', 0),('date', '>=', from_date),('date', '<=', to_date),('parent_state', 'in', status_list)],orderby="account_id,date asc",groupby=["date","account_id"],fields=['id','date','debit','credit','account_id'],lazy=False)
            for account_move_line in account_move_lines:
                debit_total+=account_move_line['credit']

        for line in account_move_lines_grouped:
            base_account_name = str(line['account_id'][1]).split()[1:]
            account_name = ' '.join(base_account_name)
            line['account_name'] =account_name

        return {
            'docs': obj,
            'debit_total':debit_total,
            'from_date':from_date,
            'to_date':to_date,
            'report_name':report_type,
            'partner_id':partner_id,
            'account_move_lines': account_move_lines,
            'account_move_lines_grouped': account_move_lines_grouped,
            "account_account":account_account,
        }


class ResCompany(models.Model):
    _inherit = 'res.company'

    authority_logo = fields.Binary()
    entity_number = fields.Char('رقم المنشأة')
    enterprise_legal_form = fields.Char('الشكل القانونى للمنشأة')
    insurance_area = fields.Char('المنطقة التأمينية')
    insurance_office = fields.Char('المكتب التأميني')
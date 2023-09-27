# -*- coding: utf-8 -*-
{
    'name': "base_fix",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends':['sale', 'account_online_synchronization', 'account_bank_statement_import_camt', 'account_bank_statement_import_csv', 'account_bank_statement_import_ofx', 'account_followup', 'account_reports_tax_reminder', 'snailmail_account_followup', 'user_product_restriction', 'account', 'analytic', 'studio_customization', 'web_studio', 'analytic_required', 'custome_partner_ledger', 'accounting_partner_required', 'barcodes', 'account_bank_statement_import', 'web', 'base_setup', 'sale_purchase', 'stock_account', 'auth_signup', 'hr_custody', 'purchase', 'stock_sms', 'purchase_request_to_requisition', 'partner_autocomplete', 'hr_skills', 'mail_bot_hr', 'base_automation_hr_contract', 'sms', 'hr_contract_reports', 'hr_work_entry_contract', 'hr_payroll', 'hr_work_entry', 'stock_report_custome', 'hr_holidays_gantt', 'hr_payroll_account', 'hr_payroll_holidays', 'iap', 'employee_check_list', 'account_accountant_check_printing', 'purchase_requisition', 'product_expiry', 'bi_print_journal_entries', 'hide_menu_user', 'product_hide_sale_cost_price', 'l10n_eg', 'calendar_sms', 'stock_no_negative', 'purchase_history', 'web_unsplash', 'stock', 'payment_transfer', 'sale_account_accountant', 'account_edi', 'account_invoice_extract', 'account_edi_facturx', 'currency_rate_live', 'analytic_enterprise', 'sale_enterprise', 'auth_totp', 'sale_sms', 'account_asset_ndt', 'account_predictive_bills', 'account_reports', 'account_accountant', 'mail_bot', 'account_auto_transfer', 'mail_enterprise', 'base_automation', 'calendar', 'purchase_stock_enterprise', 'contacts', 'mail', 'snailmail', 'phone_validation', 'uom', 'stock_account_enterprise', 'stock_card_report', 'digest', 'purchase_enterprise', 'purchase_request', 'auth_totp_mail', 'hr_attendance_mobile', 'sale_purchase_stock', 'contacts_enterprise', 'purchase_requisition_stock', 'account_3way_match', 'stock_enterprise', 'hr_mobile', 'account_invoice_extract_purchase', 'product', 'report_xlsx_helper', 'hr_work_entry_holidays_enterprise', 'stock_landed_costs', 'web_kanban_gauge', 'account_asset', 'purchase_stock', 'stock_accountant', 'account_check_printing', 'iap_mail', 'web_dashboard', 'deltatech_invoice_product_filter', 'base_import', 'resource', 'spectrum_attendance', 'oi_hr_employee_no', 'up_working_time_attendence', 'custom_inv', 'date_range', 'report_xlsx', 'hr_gantt', 'portal', 'web_tour', 'web_mobile', 'hr', 'web_enterprise', 'fetchmail', 'hr_attendance', 'snailmail_account', 'hr_contract', 'payment', 'gamification', 'web_grid', 'hr_gamification', 'hr_holidays', 'hr_holidays_attendance', 'hr_work_entry_contract_enterprise', 'web_gantt', 'hr_work_entry_holidays', 'web_editor', 'warehouse_stock_restrictions', 'bus', 'sales_team', 'employee_documents_expiry', 'my_hr', 'barcodes_mobile', 'http_routing', 'mail_mobile', 'auth_totp_portal', 'web_map', 'sale_stock', 'web_cohort', 'l10n_multilang', 'hr_org_chart', 'base_import_module', 'base', 'utm', 'digest_enterprise']
,

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

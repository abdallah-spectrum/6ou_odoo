
from odoo import http
class Books(http.Controller):
    @http.route("/library/books")
    def list(self, **kwargs):
        books = http.request.env['libray.book'].search([])
        return http.request.render('library.book_list_template',{'books':books})


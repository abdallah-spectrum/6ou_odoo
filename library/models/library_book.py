


from odoo import fields , api  , models
from odoo.exceptions import ValidationError



class Book(models.Model):
    _name = 'libray.book'
    _description ='book model '
    active=fields.Boolean('active', default=True)
    name = fields.Char('book name', max_length= 50)
    isbn = fields.Integer('ISBN')
    date_published = fields.Date()
    image  = fields.Binary('book cover ')
    author_ids = fields.Many2one('res.partner', 'author')
    publisher_id = fields.Many2one('res.partner','publishers')

    def _check_isbn(self):
        self.ensure_one()
        digits = [int(x) for x in self.isbn if x.isdigit()]
        if len(digits) == 13:
            ponderations = [1, 3] * 6
            terms = [a * b for a, b in zip(digits[:12],
                                           ponderations)]
            remain = sum(terms) % 10
            check = 10 - remain if remain != 0 else 0
            return digits[-1] == check


    def check_isbn_button(self):
        print(self,"self here ")
        if not self.isbn:
            raise ValidationError('ISBN is required')
        if self.isbn  and not self._check_isbn():
            raise ValidationError('ISBN is invalid')



# kjnkjnjkn
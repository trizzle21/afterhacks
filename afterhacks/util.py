""" Utility file containing functions that don't belong anywhere else"""
from wtforms.validators import ValidationError

class Unique(object):
    def __init__(self, model, field, message=u"This Element already exists"):
        self.model = model
        self.field = field
        self.message = message

    def __call__(self, form, field):
        check = self.model.query.filter(self.field == field.data).first()
        if check:
            raise ValidationError(self.message)

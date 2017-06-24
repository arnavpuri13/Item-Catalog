"""Form for creating and editing items."""

from catalog.forms import CSRFForm, ImageFileValidator
from wtforms import Form, TextField, TextAreaField, SelectField, FileField
from wtforms import validators, ValidationError

class ItemForm(CSRFForm):
    
    name = TextField("Name", [validators.Required(), validators.Length(min = 5, max = 120)])

    description = TextAreaField("Description", [validators.Required(), validators.Length(min = 10)])

    category_id = SelectField("Category", coerce = int)

    image = FileField("Image", [ImageFileValidator()])

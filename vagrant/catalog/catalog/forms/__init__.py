from catalog import app

from flask import request
from flask import session

from wtforms import Form, ValidationError
from wtforms.csrf.session import SessionCSRF


class BaseForm(Form):
    """Base form for the application."""
    pass

class CSRFForm(BaseForm):
    """Base form with cross site request forgery (CSRF) configuration."""
    class Meta:
        csrf = True
        csrf_class = SessionCSRF
        csrf_secret = app.config['CSRF_SECRET_KEY']

        @property
        def csrf_context(self):
            return session


class ImageFileValidator(object):
    """Validates that a form file, if present, is an image file.
    This only does a basic check of the file extension.
    It does not check the actual content of the file."""

    def __init__(self, valid_extensions = app.config['ALLOWED_IMAGE_EXTENSIONS'], message = None):
        self.valid_extensions = valid_extensions
        if not message:
            message = 'Invalid file extension.'
        self.message = message

    def __call__(self, form, field):
        form_file = request.files[field.name]
        if form_file and not self.allowed_file(form_file):
            raise ValidationError(self.message)

    def allowed_file(self, file):
        filename = file.filename
        return '.' in filename and \
                filename.rsplit('.', 1)[1] in self.valid_extensions

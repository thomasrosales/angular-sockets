from marshmallow import Schema, fields, validates, ValidationError
from utils.serializer_validations import must_not_be_blank, must_be_in_allowed_extension
import os


class ResponseSchema(Schema):
    status = fields.Int(dump_only=True)
    offset = fields.Int(dump_only=True)
    totalResults = fields.Int(dump_only=True)
    results = fields.Dict(dump_only=True)


class BaseSchema(Schema):
    id = fields.Int(dump_only=True)
    created = fields.DateTime(dump_only=True, format='%Y-%m-%d')
    modified = fields.DateTime(dump_only=True, format='%Y-%m-%d')
    is_active = fields.Boolean(dump_only=True)


class SuccessResponseSchema(Schema):
    message = fields.Str()
    status = fields.Int()


class EntityIDSchema(Schema):
    id = fields.Int(
        required=True,
        allow_none=False,
        validate=must_not_be_blank
    )


class ImageSchema(Schema):
    thumbnail = fields.Str(
        required=True,
        validate=must_not_be_blank,
        allow_none=False
    )
    extension = fields.Str(
        required=True,
        validate=must_not_be_blank,
        allow_none=False
    )

    @validates("extension")
    def validate_extension(self, value):
        if not must_be_in_allowed_extension(value):
            raise ValidationError(
                f"Extension must be one of the followings types: { os.environ.get('ALLOWED_EXTENSIONS')} ")


class YesOrNotResponseSchema(Schema):
    valid = fields.Boolean(required=True,  allow_none=False)

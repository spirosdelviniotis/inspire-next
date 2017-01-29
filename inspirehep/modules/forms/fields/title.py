# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2012, 2013, 2014, 2015 CERN.
#
# Invenio is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; either version 2 of the
# License, or (at your option) any later version.
#
# Invenio is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Invenio; if not, write to the Free Software Foundation, Inc.,
# 59 Temple Place, Suite 330, Boston, MA 02111-1307, USA.
"""Deprecated."""

from __future__ import absolute_import, division, print_function

from wtforms import StringField, ValidationError

from ..field_base import INSPIREField

__all__ = ['TitleField']


def validate_title(form, field):
    """Deprecated."""
    import warnings
    warnings.warn("Validator has been deprecated", PendingDeprecationWarning)

    value = field.data or ''
    if value == "" or value.isspace():
        return

    if len(value) <= 4:
        raise ValidationError("This field must have at least 4 characters")


class TitleField(INSPIREField, StringField):
    """Deprecated."""

    def __init__(self, **kwargs):
        """Deprecated."""
        import warnings
        warnings.warn("Field has been deprecated", PendingDeprecationWarning)
        defaults = dict(
            icon='book',
            export_key='title.title',
            widget_classes="form-control"
            # FIXMEvalidators=[validate_title]
        )
        defaults.update(kwargs)
        super(TitleField, self).__init__(**defaults)

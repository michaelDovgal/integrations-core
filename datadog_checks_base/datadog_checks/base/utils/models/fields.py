# (C) Datadog, Inc. 2021-present
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)
import typing
from collections.abc import Mapping, Sequence


def get_default_field_value(field, value):
    for arg in typing.get_args(field.annotation):
        origin = typing.get_origin(arg) or arg
        if origin in (float, int, str):
            return origin()
        elif origin in (Sequence, list):
            return []
        elif origin in (Mapping, dict):
            return {}

    return value

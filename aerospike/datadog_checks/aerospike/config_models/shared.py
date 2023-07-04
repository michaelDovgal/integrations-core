# (C) Datadog, Inc. 2021-present
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)

# This file is autogenerated.
# To change this file you should edit assets/configuration/spec.yaml and then run the following commands:
#     ddev -x validate config -s <INTEGRATION_NAME>
#     ddev -x validate models -s <INTEGRATION_NAME>

from __future__ import annotations

from typing import Optional, Sequence

from pydantic import BaseModel, ConfigDict, field_validator, model_validator

from datadog_checks.base.utils.functions import identity
from datadog_checks.base.utils.models import validation

from . import defaults, validators


class Proxy(BaseModel):
    model_config = ConfigDict(
        frozen=True,
    )
    http: Optional[str] = None
    https: Optional[str] = None
    no_proxy: Optional[Sequence[str]] = None


class SharedConfig(BaseModel):
    model_config = ConfigDict(
        validate_default=True,
        frozen=True,
    )
    mappings: Optional[Sequence[str]] = None
    proxy: Optional[Proxy] = None
    service: Optional[str] = None
    skip_proxy: Optional[bool] = None
    timeout: Optional[float] = None

    @model_validator(mode='before')
    def _initial_validation(cls, values):
        return validation.core.initialize_config(getattr(validators, 'initialize_shared', identity)(values))

    @field_validator('*', mode='before')
    def _ensure_defaults(cls, value, info):
        if info.field_name in info.context['configured_fields']:
            return value

        field = cls.model_fields[info.field_name]
        return getattr(defaults, f'shared_{info.field_name}')(field, value)

    @field_validator('*')
    def _run_validations(cls, value, info):
        if info.field_name not in info.context['configured_fields']:
            return value

        field = cls.model_fields[info.field_name]
        return getattr(validators, f'shared_{info.field_name}', identity)(value, field=field)

    @field_validator('*', mode='after')
    def _make_immutable(cls, value):
        return validation.utils.make_immutable(value)

    @model_validator(mode='after')
    def _final_validation(cls, model):
        return validation.core.check_model(getattr(validators, 'check_shared', identity)(model))

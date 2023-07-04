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


class MetricPatterns(BaseModel):
    model_config = ConfigDict(
        frozen=True,
    )
    exclude: Optional[Sequence[str]] = None
    include: Optional[Sequence[str]] = None


class InstanceConfig(BaseModel):
    model_config = ConfigDict(
        validate_default=True,
        frozen=True,
    )
    disable_generic_tags: Optional[bool] = None
    empty_default_hostname: Optional[bool] = None
    host: Optional[str] = None
    keyspaces: Sequence[str]
    metric_patterns: Optional[MetricPatterns] = None
    min_collection_interval: Optional[float] = None
    nodetool: Optional[str] = None
    password: Optional[str] = None
    port: Optional[int] = None
    service: Optional[str] = None
    ssl: Optional[bool] = None
    tags: Optional[Sequence[str]] = None
    username: Optional[str] = None

    @model_validator(mode='before')
    def _initial_validation(cls, values):
        return validation.core.initialize_config(getattr(validators, 'initialize_instance', identity)(values))

    @field_validator('*', mode='before')
    def _ensure_defaults(cls, value, info):
        if info.field_name in info.context['configured_fields']:
            return value

        field = cls.model_fields[info.field_name]
        return getattr(defaults, f'instance_{info.field_name}')(field, value)

    @field_validator('*')
    def _run_validations(cls, value, info):
        if info.field_name not in info.context['configured_fields']:
            return value

        field = cls.model_fields[info.field_name]
        return getattr(validators, f'instance_{info.field_name}', identity)(value, field=field)

    @field_validator('*', mode='after')
    def _make_immutable(cls, value):
        return validation.utils.make_immutable(value)

    @model_validator(mode='after')
    def _final_validation(cls, model):
        return validation.core.check_model(getattr(validators, 'check_instance', identity)(model))

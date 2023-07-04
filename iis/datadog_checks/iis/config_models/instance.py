# (C) Datadog, Inc. 2021-present
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)

# This file is autogenerated.
# To change this file you should edit assets/configuration/spec.yaml and then run the following commands:
#     ddev -x validate config -s <INTEGRATION_NAME>
#     ddev -x validate models -s <INTEGRATION_NAME>

from __future__ import annotations

from typing import Mapping, Optional, Sequence, Union

from pydantic import BaseModel, ConfigDict, Field, field_validator, model_validator
from typing_extensions import Literal

from datadog_checks.base.utils.functions import identity
from datadog_checks.base.utils.models import validation

from . import defaults, validators


class AppPool(BaseModel):
    model_config = ConfigDict(
        frozen=True,
    )
    exclude: Optional[Sequence[str]] = None
    include: Optional[Sequence[str]] = None


class Counter(BaseModel):
    model_config = ConfigDict(
        extra='allow',
        frozen=True,
    )
    aggregate: Optional[Union[bool, Literal['only']]] = None
    average: Optional[bool] = None
    metric_name: Optional[str] = None
    name: Optional[str] = None
    type: Optional[str] = None


class InstanceCounts(BaseModel):
    model_config = ConfigDict(
        frozen=True,
    )
    monitored: Optional[str] = None
    total: Optional[str] = None
    unique: Optional[str] = None


class ExtraMetrics(BaseModel):
    model_config = ConfigDict(
        frozen=True,
    )
    counters: Sequence[Mapping[str, Union[str, Counter]]]
    exclude: Optional[Sequence[str]] = None
    include: Optional[Sequence[str]] = None
    instance_counts: Optional[InstanceCounts] = None
    name: str
    tag_name: Optional[str] = None
    use_localized_counters: Optional[bool] = None


class MetricPatterns(BaseModel):
    model_config = ConfigDict(
        frozen=True,
    )
    exclude: Optional[Sequence[str]] = None
    include: Optional[Sequence[str]] = None


class Metrics(BaseModel):
    model_config = ConfigDict(
        frozen=True,
    )
    counters: Sequence[Mapping[str, Union[str, Counter]]]
    exclude: Optional[Sequence[str]] = None
    include: Optional[Sequence[str]] = None
    instance_counts: Optional[InstanceCounts] = None
    name: str
    tag_name: Optional[str] = None
    use_localized_counters: Optional[bool] = None


class Site(BaseModel):
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
    additional_metrics: Optional[Sequence[Sequence[str]]] = None
    app_pools: Optional[Union[Sequence[str], AppPool]] = None
    counter_data_types: Optional[Sequence[str]] = None
    disable_generic_tags: Optional[bool] = None
    empty_default_hostname: Optional[bool] = None
    enable_health_service_check: Optional[bool] = None
    extra_metrics: Optional[Mapping[str, ExtraMetrics]] = None
    host: Optional[str] = None
    metric_patterns: Optional[MetricPatterns] = None
    metrics: Optional[Mapping[str, Metrics]] = None
    min_collection_interval: Optional[float] = None
    namespace: Optional[str] = Field(None, pattern='\\w*')
    password: Optional[str] = None
    server: Optional[str] = None
    server_tag: Optional[str] = None
    service: Optional[str] = None
    sites: Optional[Union[Sequence[str], Site]] = None
    tags: Optional[Sequence[str]] = None
    use_legacy_check_version: Optional[bool] = None
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

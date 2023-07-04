# (C) Datadog, Inc. 2021-present
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)

# This file is autogenerated.
# To change this file you should edit assets/configuration/spec.yaml and then run the following commands:
#     ddev -x validate config -s <INTEGRATION_NAME>
#     ddev -x validate models -s <INTEGRATION_NAME>

from __future__ import annotations

from typing import Any, Mapping, Optional, Sequence

from pydantic import BaseModel, ConfigDict, field_validator, model_validator

from datadog_checks.base.utils.functions import identity
from datadog_checks.base.utils.models import validation

from . import defaults, validators


class AuthToken(BaseModel):
    model_config = ConfigDict(
        frozen=True,
    )
    reader: Optional[Mapping[str, Any]] = None
    writer: Optional[Mapping[str, Any]] = None


class MetricPatterns(BaseModel):
    model_config = ConfigDict(
        frozen=True,
    )
    exclude: Optional[Sequence[str]] = None
    include: Optional[Sequence[str]] = None


class Proxy(BaseModel):
    model_config = ConfigDict(
        frozen=True,
    )
    http: Optional[str] = None
    https: Optional[str] = None
    no_proxy: Optional[Sequence[str]] = None


class InstanceConfig(BaseModel):
    model_config = ConfigDict(
        validate_default=True,
        frozen=True,
    )
    allow_redirects: Optional[bool] = None
    auth_token: Optional[AuthToken] = None
    auth_type: Optional[str] = None
    aws_host: Optional[str] = None
    aws_region: Optional[str] = None
    aws_service: Optional[str] = None
    connect_timeout: Optional[float] = None
    disable_generic_tags: Optional[bool] = None
    empty_default_hostname: Optional[bool] = None
    extra_headers: Optional[Mapping[str, Any]] = None
    headers: Optional[Mapping[str, Any]] = None
    kerberos_auth: Optional[str] = None
    kerberos_cache: Optional[str] = None
    kerberos_delegate: Optional[bool] = None
    kerberos_force_initiate: Optional[bool] = None
    kerberos_hostname: Optional[str] = None
    kerberos_keytab: Optional[str] = None
    kerberos_principal: Optional[str] = None
    log_requests: Optional[bool] = None
    metric_patterns: Optional[MetricPatterns] = None
    min_collection_interval: Optional[float] = None
    ntlm_domain: Optional[str] = None
    password: Optional[str] = None
    persist_connections: Optional[bool] = None
    proxy: Optional[Proxy] = None
    read_timeout: Optional[float] = None
    request_size: Optional[float] = None
    service: Optional[str] = None
    skip_proxy: Optional[bool] = None
    tags: Optional[Sequence[str]] = None
    timeout: Optional[float] = None
    tls_ca_cert: Optional[str] = None
    tls_cert: Optional[str] = None
    tls_ignore_warning: Optional[bool] = None
    tls_private_key: Optional[str] = None
    tls_protocols_allowed: Optional[Sequence[str]] = None
    tls_use_host_header: Optional[bool] = None
    tls_verify: Optional[bool] = None
    use_legacy_auth_encoding: Optional[bool] = None
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

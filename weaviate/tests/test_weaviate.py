# (C) Datadog, Inc. 2023-present
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)
from typing import Any, Callable, Dict  # noqa: F401

import pytest

from datadog_checks.base import AgentCheck  # noqa: F401
from datadog_checks.base.constants import ServiceCheck
from datadog_checks.base.stubs.aggregator import AggregatorStub  # noqa: F401
from datadog_checks.weaviate import WeaviateCheck

from .common import API_METRICS, MOCKED_INSTANCE, TEST_METRICS
from .utils import get_fixture_path


def test_check_mock_weaviate(dd_run_check, aggregator, mock_http_response):
    mock_http_response(file_path=get_fixture_path('weaviate_metrics.txt'))
    check = WeaviateCheck('weaviate', {}, [MOCKED_INSTANCE])
    dd_run_check(check)

    for metric in TEST_METRICS:
        aggregator.assert_metric(metric, at_least=1)

    aggregator.assert_all_metrics_covered()
    aggregator.assert_service_check('weaviate.openmetrics.health', ServiceCheck.OK)


def test_check_mock_weaviate_node(dd_run_check, aggregator, mock_http_response):
    mock_http_response(file_path=get_fixture_path('nodes_api.txt'))
    check = WeaviateCheck('weaviate', {}, [MOCKED_INSTANCE])
    dd_run_check(check)

    for metric in API_METRICS:
        aggregator.assert_metric(metric, at_least=1)

    aggregator.assert_service_check('weaviate.node.status', ServiceCheck.OK)
    aggregator.assert_all_metrics_covered()


def test_check_mock_liveness(dd_run_check, aggregator, mock_http_response):
    mock_http_response(status_code=404)

    check = WeaviateCheck('weaviate', {}, [MOCKED_INSTANCE])
    dd_run_check(check)

    # No metrics should be submitted
    aggregator.assert_all_metrics_covered()
    aggregator.assert_service_check('weaviate.liveness.status', ServiceCheck.CRITICAL)


@pytest.mark.integration
def test_check_mock_weaviate_metadata(dd_run_check, datadog_agent, mock_http_response):
    mock_http_response(file_path=get_fixture_path('meta_api.txt'))
    check = WeaviateCheck('weaviate', {}, [MOCKED_INSTANCE])
    check.check_id = 'test:123'
    dd_run_check(check)

    raw_version = "1.19.1"
    major, minor, patch = raw_version.split('.')
    version_metadata = {
        'version.scheme': 'semver',
        'version.major': major,
        'version.minor': minor,
        'version.patch': patch,
        'version.raw': raw_version,
    }

    datadog_agent.assert_metadata('test:123', version_metadata)

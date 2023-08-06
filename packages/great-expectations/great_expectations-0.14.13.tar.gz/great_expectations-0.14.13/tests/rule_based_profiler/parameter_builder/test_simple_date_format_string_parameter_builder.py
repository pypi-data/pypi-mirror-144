from typing import Set

import pytest

import great_expectations.exceptions.exceptions as ge_exceptions
from great_expectations.data_context import DataContext
from great_expectations.execution_engine.execution_engine import MetricDomainTypes
from great_expectations.rule_based_profiler.helpers.util import (
    get_parameter_value_and_validate_return_type,
)
from great_expectations.rule_based_profiler.parameter_builder import (
    SimpleDateFormatStringParameterBuilder,
)
from great_expectations.rule_based_profiler.parameter_builder.simple_date_format_string_parameter_builder import (
    DEFAULT_CANDIDATE_STRINGS,
)
from great_expectations.rule_based_profiler.types import Domain, ParameterContainer

DEFAULT_CANDIDATE_STRINGS: Set[str] = {
    "%H:%M:%S",
    "%H:%M:%S,%f",
    "%H:%M:%S.%f",
    "%Y %b %d %H:%M:%S.%f",
    "%Y %b %d %H:%M:%S.%f %Z",
    "%Y %b %d %H:%M:%S.%f*%Z",
    "%Y%m%d %H:%M:%S.%f",
    "%Y-%m-%d",
    "%Y-%m-%d %H:%M:%S",
    "%Y-%m-%d %H:%M:%S %z",
    "%Y-%m-%d %H:%M:%S%z",
    "%Y-%m-%d %H:%M:%S,%f",
    "%Y-%m-%d %H:%M:%S,%f%z",
    "%Y-%m-%d %H:%M:%S.%f",
    "%Y-%m-%d %H:%M:%S.%f%z",
    "%Y-%m-%d'T'%H:%M:%S",
    "%Y-%m-%d'T'%H:%M:%S%z",
    "%Y-%m-%d'T'%H:%M:%S'%z'",
    "%Y-%m-%d'T'%H:%M:%S.%f",
    "%Y-%m-%d'T'%H:%M:%S.%f'%z'",
    "%Y-%m-%d*%H:%M:%S",
    "%Y-%m-%d*%H:%M:%S:%f",
    "%Y-%m-%dT%z",
    "%Y/%m/%d",
    "%Y/%m/%d*%H:%M:%S",
    "%b %d %H:%M:%S",
    "%b %d %H:%M:%S %Y",
    "%b %d %H:%M:%S %z",
    "%b %d %H:%M:%S %z %Y",
    "%b %d %Y %H:%M:%S",
    "%b %d, %Y %H:%M:%S %p",
    "%d %b %Y %H:%M:%S",
    "%d %b %Y %H:%M:%S*%f",
    "%d-%b-%Y %H:%M:%S",
    "%d-%b-%Y %H:%M:%S.%f",
    "%d-%m-%Y",
    "%d/%b %H:%M:%S,%f",
    "%d/%b/%Y %H:%M:%S",
    "%d/%b/%Y:%H:%M:%S",
    "%d/%b/%Y:%H:%M:%S %z",
    "%d/%m/%Y",
    "%m%d_%H:%M:%S",
    "%m%d_%H:%M:%S.%f",
    "%m-%d-%Y",
    "%m/%d/%Y",
    "%m/%d/%Y %H:%M:%S %p",
    "%m/%d/%Y %H:%M:%S %p:%f",
    "%m/%d/%Y %H:%M:%S %z",
    "%m/%d/%Y*%H:%M:%S",
    "%m/%d/%Y*%H:%M:%S*%f",
    "%m/%d/%y %H:%M:%S %z",
    "%m/%d/%y*%H:%M:%S",
    "%y%m%d %H:%M:%S",
    "%y-%m-%d",
    "%y-%m-%d %H:%M:%S",
    "%y-%m-%d %H:%M:%S,%f",
    "%y-%m-%d %H:%M:%S,%f %z",
    "%y/%m/%d",
    "%y/%m/%d %H:%M:%S",
}


def test_simple_date_format_parameter_builder_instantiation(
    alice_columnar_table_single_batch_context,
):
    data_context: DataContext = alice_columnar_table_single_batch_context

    date_format_string_parameter: SimpleDateFormatStringParameterBuilder = (
        SimpleDateFormatStringParameterBuilder(
            name="my_simple_date_format_string_parameter_builder",
            data_context=data_context,
        )
    )

    assert date_format_string_parameter.threshold == 1.0
    assert date_format_string_parameter.candidate_strings == DEFAULT_CANDIDATE_STRINGS


def test_simple_date_format_parameter_builder_zero_batch_id_error(
    alice_columnar_table_single_batch_context,
):
    data_context: DataContext = alice_columnar_table_single_batch_context

    date_format_string_parameter: SimpleDateFormatStringParameterBuilder = (
        SimpleDateFormatStringParameterBuilder(
            name="my_simple_date_format_string_parameter_builder",
            data_context=data_context,
        )
    )
    parameter_container: ParameterContainer = ParameterContainer(parameter_nodes=None)
    domain: Domain = Domain(domain_type=MetricDomainTypes.COLUMN)

    with pytest.raises(ge_exceptions.ProfilerExecutionError) as e:
        date_format_string_parameter.build_parameters(
            parameter_container=parameter_container, domain=domain
        )

    assert (
        str(e.value)
        == "Utilizing a SimpleDateFormatStringParameterBuilder requires a non-empty list of batch identifiers."
    )


def test_simple_date_format_parameter_builder_alice(
    alice_columnar_table_single_batch_context,
):
    data_context: DataContext = alice_columnar_table_single_batch_context

    batch_request: dict = {
        "datasource_name": "alice_columnar_table_single_batch_datasource",
        "data_connector_name": "alice_columnar_table_single_batch_data_connector",
        "data_asset_name": "alice_columnar_table_single_batch_data_asset",
    }

    metric_domain_kwargs = {"column": "event_ts"}

    date_format_string_parameter: SimpleDateFormatStringParameterBuilder = (
        SimpleDateFormatStringParameterBuilder(
            name="my_date_format",
            metric_domain_kwargs=metric_domain_kwargs,
            batch_request=batch_request,
            data_context=data_context,
        )
    )

    assert date_format_string_parameter.candidate_strings == DEFAULT_CANDIDATE_STRINGS
    assert date_format_string_parameter._threshold == 1.0

    parameter_container: ParameterContainer = ParameterContainer(parameter_nodes=None)
    domain: Domain = Domain(
        domain_type=MetricDomainTypes.COLUMN, domain_kwargs=metric_domain_kwargs
    )

    assert parameter_container.parameter_nodes is None

    date_format_string_parameter.build_parameters(
        parameter_container=parameter_container, domain=domain
    )

    # noinspection PyTypeChecker
    assert len(parameter_container.parameter_nodes) == 1

    fully_qualified_parameter_name_for_value: str = "$parameter.my_date_format"
    expected_value: dict = {
        "value": "%Y-%m-%d %H:%M:%S",
        "details": {
            "success_ratio": 1.0,
            "candidate_strings": sorted(DEFAULT_CANDIDATE_STRINGS),
        },
    }

    actual_value: dict = get_parameter_value_and_validate_return_type(
        parameter_reference=fully_qualified_parameter_name_for_value,
        expected_return_type=dict,
        domain=domain,
        parameters={domain.id: parameter_container},
    )

    assert actual_value == expected_value


def test_simple_date_format_parameter_builder_bobby(
    bobby_columnar_table_multi_batch_deterministic_data_context,
):
    data_context: DataContext = (
        bobby_columnar_table_multi_batch_deterministic_data_context
    )

    metric_domain_kwargs: dict = {"column": "pickup_datetime"}
    candidate_strings: list[str] = [
        "%Y-%m-%d",
        "%Y-%m-%d %H:%M:%S",
    ]
    threshold: float = 0.9
    batch_request: dict = {
        "datasource_name": "taxi_pandas",
        "data_connector_name": "monthly",
        "data_asset_name": "my_reports",
    }

    date_format_string_parameter: SimpleDateFormatStringParameterBuilder = (
        SimpleDateFormatStringParameterBuilder(
            name="my_simple_date_format_string_parameter_builder",
            metric_domain_kwargs=metric_domain_kwargs,
            candidate_strings=candidate_strings,
            threshold=threshold,
            batch_request=batch_request,
            data_context=data_context,
        )
    )

    assert date_format_string_parameter._candidate_strings == set(candidate_strings)
    assert date_format_string_parameter._threshold == 0.9

    parameter_container: ParameterContainer = ParameterContainer(parameter_nodes=None)
    domain: Domain = Domain(
        domain_type=MetricDomainTypes.COLUMN, domain_kwargs=metric_domain_kwargs
    )

    assert parameter_container.parameter_nodes is None

    date_format_string_parameter.build_parameters(
        parameter_container=parameter_container, domain=domain
    )

    assert (
        parameter_container.parameter_nodes is None
        or len(parameter_container.parameter_nodes) == 1
    )

    fully_qualified_parameter_name_for_value: str = (
        "$parameter.my_simple_date_format_string_parameter_builder.value"
    )
    expected_value: str = "%Y-%m-%d %H:%M:%S"

    actual_value: str = get_parameter_value_and_validate_return_type(
        parameter_reference=fully_qualified_parameter_name_for_value,
        expected_return_type=str,
        domain=domain,
        parameters={domain.id: parameter_container},
    )

    assert actual_value == expected_value

    fully_qualified_parameter_name_for_meta: str = (
        "$parameter.my_simple_date_format_string_parameter_builder.details"
    )
    expected_meta: dict = {
        "success_ratio": 1.0,
        "candidate_strings": candidate_strings,
    }
    meta: dict = get_parameter_value_and_validate_return_type(
        parameter_reference=fully_qualified_parameter_name_for_meta,
        expected_return_type=dict,
        domain=domain,
        parameters={domain.id: parameter_container},
    )
    assert meta == expected_meta

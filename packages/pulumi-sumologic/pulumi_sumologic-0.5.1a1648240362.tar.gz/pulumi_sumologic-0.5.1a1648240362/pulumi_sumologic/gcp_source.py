# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities
from . import outputs
from ._inputs import *

__all__ = ['GcpSourceArgs', 'GcpSource']

@pulumi.input_type
class GcpSourceArgs:
    def __init__(__self__, *,
                 collector_id: pulumi.Input[int],
                 authentication: Optional[pulumi.Input['GcpSourceAuthenticationArgs']] = None,
                 automatic_date_parsing: Optional[pulumi.Input[bool]] = None,
                 category: Optional[pulumi.Input[str]] = None,
                 content_type: Optional[pulumi.Input[str]] = None,
                 cutoff_relative_time: Optional[pulumi.Input[str]] = None,
                 cutoff_timestamp: Optional[pulumi.Input[int]] = None,
                 default_date_formats: Optional[pulumi.Input[Sequence[pulumi.Input['GcpSourceDefaultDateFormatArgs']]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 fields: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 filters: Optional[pulumi.Input[Sequence[pulumi.Input['GcpSourceFilterArgs']]]] = None,
                 force_timezone: Optional[pulumi.Input[bool]] = None,
                 host_name: Optional[pulumi.Input[str]] = None,
                 manual_prefix_regexp: Optional[pulumi.Input[str]] = None,
                 message_per_request: Optional[pulumi.Input[bool]] = None,
                 multiline_processing_enabled: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 path: Optional[pulumi.Input['GcpSourcePathArgs']] = None,
                 timezone: Optional[pulumi.Input[str]] = None,
                 use_autoline_matching: Optional[pulumi.Input[bool]] = None):
        """
        The set of arguments for constructing a GcpSource resource.
        """
        pulumi.set(__self__, "collector_id", collector_id)
        if authentication is not None:
            pulumi.set(__self__, "authentication", authentication)
        if automatic_date_parsing is not None:
            pulumi.set(__self__, "automatic_date_parsing", automatic_date_parsing)
        if category is not None:
            pulumi.set(__self__, "category", category)
        if content_type is not None:
            pulumi.set(__self__, "content_type", content_type)
        if cutoff_relative_time is not None:
            pulumi.set(__self__, "cutoff_relative_time", cutoff_relative_time)
        if cutoff_timestamp is not None:
            pulumi.set(__self__, "cutoff_timestamp", cutoff_timestamp)
        if default_date_formats is not None:
            pulumi.set(__self__, "default_date_formats", default_date_formats)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if fields is not None:
            pulumi.set(__self__, "fields", fields)
        if filters is not None:
            pulumi.set(__self__, "filters", filters)
        if force_timezone is not None:
            pulumi.set(__self__, "force_timezone", force_timezone)
        if host_name is not None:
            pulumi.set(__self__, "host_name", host_name)
        if manual_prefix_regexp is not None:
            pulumi.set(__self__, "manual_prefix_regexp", manual_prefix_regexp)
        if message_per_request is not None:
            pulumi.set(__self__, "message_per_request", message_per_request)
        if multiline_processing_enabled is not None:
            pulumi.set(__self__, "multiline_processing_enabled", multiline_processing_enabled)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if path is not None:
            pulumi.set(__self__, "path", path)
        if timezone is not None:
            pulumi.set(__self__, "timezone", timezone)
        if use_autoline_matching is not None:
            pulumi.set(__self__, "use_autoline_matching", use_autoline_matching)

    @property
    @pulumi.getter(name="collectorId")
    def collector_id(self) -> pulumi.Input[int]:
        return pulumi.get(self, "collector_id")

    @collector_id.setter
    def collector_id(self, value: pulumi.Input[int]):
        pulumi.set(self, "collector_id", value)

    @property
    @pulumi.getter
    def authentication(self) -> Optional[pulumi.Input['GcpSourceAuthenticationArgs']]:
        return pulumi.get(self, "authentication")

    @authentication.setter
    def authentication(self, value: Optional[pulumi.Input['GcpSourceAuthenticationArgs']]):
        pulumi.set(self, "authentication", value)

    @property
    @pulumi.getter(name="automaticDateParsing")
    def automatic_date_parsing(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "automatic_date_parsing")

    @automatic_date_parsing.setter
    def automatic_date_parsing(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "automatic_date_parsing", value)

    @property
    @pulumi.getter
    def category(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "category")

    @category.setter
    def category(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "category", value)

    @property
    @pulumi.getter(name="contentType")
    def content_type(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "content_type")

    @content_type.setter
    def content_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "content_type", value)

    @property
    @pulumi.getter(name="cutoffRelativeTime")
    def cutoff_relative_time(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "cutoff_relative_time")

    @cutoff_relative_time.setter
    def cutoff_relative_time(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cutoff_relative_time", value)

    @property
    @pulumi.getter(name="cutoffTimestamp")
    def cutoff_timestamp(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "cutoff_timestamp")

    @cutoff_timestamp.setter
    def cutoff_timestamp(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "cutoff_timestamp", value)

    @property
    @pulumi.getter(name="defaultDateFormats")
    def default_date_formats(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['GcpSourceDefaultDateFormatArgs']]]]:
        return pulumi.get(self, "default_date_formats")

    @default_date_formats.setter
    def default_date_formats(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['GcpSourceDefaultDateFormatArgs']]]]):
        pulumi.set(self, "default_date_formats", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def fields(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        return pulumi.get(self, "fields")

    @fields.setter
    def fields(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "fields", value)

    @property
    @pulumi.getter
    def filters(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['GcpSourceFilterArgs']]]]:
        return pulumi.get(self, "filters")

    @filters.setter
    def filters(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['GcpSourceFilterArgs']]]]):
        pulumi.set(self, "filters", value)

    @property
    @pulumi.getter(name="forceTimezone")
    def force_timezone(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "force_timezone")

    @force_timezone.setter
    def force_timezone(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "force_timezone", value)

    @property
    @pulumi.getter(name="hostName")
    def host_name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "host_name")

    @host_name.setter
    def host_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "host_name", value)

    @property
    @pulumi.getter(name="manualPrefixRegexp")
    def manual_prefix_regexp(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "manual_prefix_regexp")

    @manual_prefix_regexp.setter
    def manual_prefix_regexp(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "manual_prefix_regexp", value)

    @property
    @pulumi.getter(name="messagePerRequest")
    def message_per_request(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "message_per_request")

    @message_per_request.setter
    def message_per_request(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "message_per_request", value)

    @property
    @pulumi.getter(name="multilineProcessingEnabled")
    def multiline_processing_enabled(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "multiline_processing_enabled")

    @multiline_processing_enabled.setter
    def multiline_processing_enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "multiline_processing_enabled", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def path(self) -> Optional[pulumi.Input['GcpSourcePathArgs']]:
        return pulumi.get(self, "path")

    @path.setter
    def path(self, value: Optional[pulumi.Input['GcpSourcePathArgs']]):
        pulumi.set(self, "path", value)

    @property
    @pulumi.getter
    def timezone(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "timezone")

    @timezone.setter
    def timezone(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "timezone", value)

    @property
    @pulumi.getter(name="useAutolineMatching")
    def use_autoline_matching(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "use_autoline_matching")

    @use_autoline_matching.setter
    def use_autoline_matching(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "use_autoline_matching", value)


@pulumi.input_type
class _GcpSourceState:
    def __init__(__self__, *,
                 authentication: Optional[pulumi.Input['GcpSourceAuthenticationArgs']] = None,
                 automatic_date_parsing: Optional[pulumi.Input[bool]] = None,
                 category: Optional[pulumi.Input[str]] = None,
                 collector_id: Optional[pulumi.Input[int]] = None,
                 content_type: Optional[pulumi.Input[str]] = None,
                 cutoff_relative_time: Optional[pulumi.Input[str]] = None,
                 cutoff_timestamp: Optional[pulumi.Input[int]] = None,
                 default_date_formats: Optional[pulumi.Input[Sequence[pulumi.Input['GcpSourceDefaultDateFormatArgs']]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 fields: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 filters: Optional[pulumi.Input[Sequence[pulumi.Input['GcpSourceFilterArgs']]]] = None,
                 force_timezone: Optional[pulumi.Input[bool]] = None,
                 host_name: Optional[pulumi.Input[str]] = None,
                 manual_prefix_regexp: Optional[pulumi.Input[str]] = None,
                 message_per_request: Optional[pulumi.Input[bool]] = None,
                 multiline_processing_enabled: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 path: Optional[pulumi.Input['GcpSourcePathArgs']] = None,
                 timezone: Optional[pulumi.Input[str]] = None,
                 url: Optional[pulumi.Input[str]] = None,
                 use_autoline_matching: Optional[pulumi.Input[bool]] = None):
        """
        Input properties used for looking up and filtering GcpSource resources.
        :param pulumi.Input[str] url: The HTTP endpoint to use for sending data to this source.
        """
        if authentication is not None:
            pulumi.set(__self__, "authentication", authentication)
        if automatic_date_parsing is not None:
            pulumi.set(__self__, "automatic_date_parsing", automatic_date_parsing)
        if category is not None:
            pulumi.set(__self__, "category", category)
        if collector_id is not None:
            pulumi.set(__self__, "collector_id", collector_id)
        if content_type is not None:
            pulumi.set(__self__, "content_type", content_type)
        if cutoff_relative_time is not None:
            pulumi.set(__self__, "cutoff_relative_time", cutoff_relative_time)
        if cutoff_timestamp is not None:
            pulumi.set(__self__, "cutoff_timestamp", cutoff_timestamp)
        if default_date_formats is not None:
            pulumi.set(__self__, "default_date_formats", default_date_formats)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if fields is not None:
            pulumi.set(__self__, "fields", fields)
        if filters is not None:
            pulumi.set(__self__, "filters", filters)
        if force_timezone is not None:
            pulumi.set(__self__, "force_timezone", force_timezone)
        if host_name is not None:
            pulumi.set(__self__, "host_name", host_name)
        if manual_prefix_regexp is not None:
            pulumi.set(__self__, "manual_prefix_regexp", manual_prefix_regexp)
        if message_per_request is not None:
            pulumi.set(__self__, "message_per_request", message_per_request)
        if multiline_processing_enabled is not None:
            pulumi.set(__self__, "multiline_processing_enabled", multiline_processing_enabled)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if path is not None:
            pulumi.set(__self__, "path", path)
        if timezone is not None:
            pulumi.set(__self__, "timezone", timezone)
        if url is not None:
            pulumi.set(__self__, "url", url)
        if use_autoline_matching is not None:
            pulumi.set(__self__, "use_autoline_matching", use_autoline_matching)

    @property
    @pulumi.getter
    def authentication(self) -> Optional[pulumi.Input['GcpSourceAuthenticationArgs']]:
        return pulumi.get(self, "authentication")

    @authentication.setter
    def authentication(self, value: Optional[pulumi.Input['GcpSourceAuthenticationArgs']]):
        pulumi.set(self, "authentication", value)

    @property
    @pulumi.getter(name="automaticDateParsing")
    def automatic_date_parsing(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "automatic_date_parsing")

    @automatic_date_parsing.setter
    def automatic_date_parsing(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "automatic_date_parsing", value)

    @property
    @pulumi.getter
    def category(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "category")

    @category.setter
    def category(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "category", value)

    @property
    @pulumi.getter(name="collectorId")
    def collector_id(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "collector_id")

    @collector_id.setter
    def collector_id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "collector_id", value)

    @property
    @pulumi.getter(name="contentType")
    def content_type(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "content_type")

    @content_type.setter
    def content_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "content_type", value)

    @property
    @pulumi.getter(name="cutoffRelativeTime")
    def cutoff_relative_time(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "cutoff_relative_time")

    @cutoff_relative_time.setter
    def cutoff_relative_time(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cutoff_relative_time", value)

    @property
    @pulumi.getter(name="cutoffTimestamp")
    def cutoff_timestamp(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "cutoff_timestamp")

    @cutoff_timestamp.setter
    def cutoff_timestamp(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "cutoff_timestamp", value)

    @property
    @pulumi.getter(name="defaultDateFormats")
    def default_date_formats(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['GcpSourceDefaultDateFormatArgs']]]]:
        return pulumi.get(self, "default_date_formats")

    @default_date_formats.setter
    def default_date_formats(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['GcpSourceDefaultDateFormatArgs']]]]):
        pulumi.set(self, "default_date_formats", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def fields(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        return pulumi.get(self, "fields")

    @fields.setter
    def fields(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "fields", value)

    @property
    @pulumi.getter
    def filters(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['GcpSourceFilterArgs']]]]:
        return pulumi.get(self, "filters")

    @filters.setter
    def filters(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['GcpSourceFilterArgs']]]]):
        pulumi.set(self, "filters", value)

    @property
    @pulumi.getter(name="forceTimezone")
    def force_timezone(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "force_timezone")

    @force_timezone.setter
    def force_timezone(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "force_timezone", value)

    @property
    @pulumi.getter(name="hostName")
    def host_name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "host_name")

    @host_name.setter
    def host_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "host_name", value)

    @property
    @pulumi.getter(name="manualPrefixRegexp")
    def manual_prefix_regexp(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "manual_prefix_regexp")

    @manual_prefix_regexp.setter
    def manual_prefix_regexp(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "manual_prefix_regexp", value)

    @property
    @pulumi.getter(name="messagePerRequest")
    def message_per_request(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "message_per_request")

    @message_per_request.setter
    def message_per_request(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "message_per_request", value)

    @property
    @pulumi.getter(name="multilineProcessingEnabled")
    def multiline_processing_enabled(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "multiline_processing_enabled")

    @multiline_processing_enabled.setter
    def multiline_processing_enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "multiline_processing_enabled", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def path(self) -> Optional[pulumi.Input['GcpSourcePathArgs']]:
        return pulumi.get(self, "path")

    @path.setter
    def path(self, value: Optional[pulumi.Input['GcpSourcePathArgs']]):
        pulumi.set(self, "path", value)

    @property
    @pulumi.getter
    def timezone(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "timezone")

    @timezone.setter
    def timezone(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "timezone", value)

    @property
    @pulumi.getter
    def url(self) -> Optional[pulumi.Input[str]]:
        """
        The HTTP endpoint to use for sending data to this source.
        """
        return pulumi.get(self, "url")

    @url.setter
    def url(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "url", value)

    @property
    @pulumi.getter(name="useAutolineMatching")
    def use_autoline_matching(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "use_autoline_matching")

    @use_autoline_matching.setter
    def use_autoline_matching(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "use_autoline_matching", value)


class GcpSource(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 authentication: Optional[pulumi.Input[pulumi.InputType['GcpSourceAuthenticationArgs']]] = None,
                 automatic_date_parsing: Optional[pulumi.Input[bool]] = None,
                 category: Optional[pulumi.Input[str]] = None,
                 collector_id: Optional[pulumi.Input[int]] = None,
                 content_type: Optional[pulumi.Input[str]] = None,
                 cutoff_relative_time: Optional[pulumi.Input[str]] = None,
                 cutoff_timestamp: Optional[pulumi.Input[int]] = None,
                 default_date_formats: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['GcpSourceDefaultDateFormatArgs']]]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 fields: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 filters: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['GcpSourceFilterArgs']]]]] = None,
                 force_timezone: Optional[pulumi.Input[bool]] = None,
                 host_name: Optional[pulumi.Input[str]] = None,
                 manual_prefix_regexp: Optional[pulumi.Input[str]] = None,
                 message_per_request: Optional[pulumi.Input[bool]] = None,
                 multiline_processing_enabled: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 path: Optional[pulumi.Input[pulumi.InputType['GcpSourcePathArgs']]] = None,
                 timezone: Optional[pulumi.Input[str]] = None,
                 use_autoline_matching: Optional[pulumi.Input[bool]] = None,
                 __props__=None):
        """
        Provides a [Sumo Logic Google Cloud Platform Source](https://help.sumologic.com/03Send-Data/Sources/02Sources-for-Hosted-Collectors/Google-Cloud-Platform-Source).

        ***Note:*** Google no longer requires a pub/sub domain to be [verified](https://cloud.google.com/pubsub/docs/push). You no longer have to set up domain verification with your GCP Source endpoint.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_sumologic as sumologic

        collector = sumologic.Collector("collector", description="Just testing this")
        gcp_source = sumologic.GcpSource("gcpSource",
            category="gcp",
            collector_id=collector.id,
            description="My description")
        ```

        ## Import

        Sumo Logic Google Cloud Platform sources can be imported using the collector and source IDs (`collector/source`), e.g.hcl

        ```sh
         $ pulumi import sumologic:index/gcpSource:GcpSource test 100000001/100000001
        ```

         Sumo Logic Google Cloud Platform sources can be imported using the collector name and source name (`collectorName/sourceName`), e.g.hcl

        ```sh
         $ pulumi import sumologic:index/gcpSource:GcpSource test my-test-collector/my-test-source
        ```

         [1]https://help.sumologic.com/Send_Data/Sources/03Use_JSON_to_Configure_Sources/JSON_Parameters_for_Hosted_Sources [2]https://help.sumologic.com/03Send-Data/Sources/02Sources-for-Hosted-Collectors/Google-Cloud-Platform-Source [3]https://cloud.google.com/pubsub/docs/push

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: GcpSourceArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a [Sumo Logic Google Cloud Platform Source](https://help.sumologic.com/03Send-Data/Sources/02Sources-for-Hosted-Collectors/Google-Cloud-Platform-Source).

        ***Note:*** Google no longer requires a pub/sub domain to be [verified](https://cloud.google.com/pubsub/docs/push). You no longer have to set up domain verification with your GCP Source endpoint.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_sumologic as sumologic

        collector = sumologic.Collector("collector", description="Just testing this")
        gcp_source = sumologic.GcpSource("gcpSource",
            category="gcp",
            collector_id=collector.id,
            description="My description")
        ```

        ## Import

        Sumo Logic Google Cloud Platform sources can be imported using the collector and source IDs (`collector/source`), e.g.hcl

        ```sh
         $ pulumi import sumologic:index/gcpSource:GcpSource test 100000001/100000001
        ```

         Sumo Logic Google Cloud Platform sources can be imported using the collector name and source name (`collectorName/sourceName`), e.g.hcl

        ```sh
         $ pulumi import sumologic:index/gcpSource:GcpSource test my-test-collector/my-test-source
        ```

         [1]https://help.sumologic.com/Send_Data/Sources/03Use_JSON_to_Configure_Sources/JSON_Parameters_for_Hosted_Sources [2]https://help.sumologic.com/03Send-Data/Sources/02Sources-for-Hosted-Collectors/Google-Cloud-Platform-Source [3]https://cloud.google.com/pubsub/docs/push

        :param str resource_name: The name of the resource.
        :param GcpSourceArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(GcpSourceArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 authentication: Optional[pulumi.Input[pulumi.InputType['GcpSourceAuthenticationArgs']]] = None,
                 automatic_date_parsing: Optional[pulumi.Input[bool]] = None,
                 category: Optional[pulumi.Input[str]] = None,
                 collector_id: Optional[pulumi.Input[int]] = None,
                 content_type: Optional[pulumi.Input[str]] = None,
                 cutoff_relative_time: Optional[pulumi.Input[str]] = None,
                 cutoff_timestamp: Optional[pulumi.Input[int]] = None,
                 default_date_formats: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['GcpSourceDefaultDateFormatArgs']]]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 fields: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 filters: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['GcpSourceFilterArgs']]]]] = None,
                 force_timezone: Optional[pulumi.Input[bool]] = None,
                 host_name: Optional[pulumi.Input[str]] = None,
                 manual_prefix_regexp: Optional[pulumi.Input[str]] = None,
                 message_per_request: Optional[pulumi.Input[bool]] = None,
                 multiline_processing_enabled: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 path: Optional[pulumi.Input[pulumi.InputType['GcpSourcePathArgs']]] = None,
                 timezone: Optional[pulumi.Input[str]] = None,
                 use_autoline_matching: Optional[pulumi.Input[bool]] = None,
                 __props__=None):
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = GcpSourceArgs.__new__(GcpSourceArgs)

            __props__.__dict__["authentication"] = authentication
            __props__.__dict__["automatic_date_parsing"] = automatic_date_parsing
            __props__.__dict__["category"] = category
            if collector_id is None and not opts.urn:
                raise TypeError("Missing required property 'collector_id'")
            __props__.__dict__["collector_id"] = collector_id
            __props__.__dict__["content_type"] = content_type
            __props__.__dict__["cutoff_relative_time"] = cutoff_relative_time
            __props__.__dict__["cutoff_timestamp"] = cutoff_timestamp
            __props__.__dict__["default_date_formats"] = default_date_formats
            __props__.__dict__["description"] = description
            __props__.__dict__["fields"] = fields
            __props__.__dict__["filters"] = filters
            __props__.__dict__["force_timezone"] = force_timezone
            __props__.__dict__["host_name"] = host_name
            __props__.__dict__["manual_prefix_regexp"] = manual_prefix_regexp
            __props__.__dict__["message_per_request"] = message_per_request
            __props__.__dict__["multiline_processing_enabled"] = multiline_processing_enabled
            __props__.__dict__["name"] = name
            __props__.__dict__["path"] = path
            __props__.__dict__["timezone"] = timezone
            __props__.__dict__["use_autoline_matching"] = use_autoline_matching
            __props__.__dict__["url"] = None
        super(GcpSource, __self__).__init__(
            'sumologic:index/gcpSource:GcpSource',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            authentication: Optional[pulumi.Input[pulumi.InputType['GcpSourceAuthenticationArgs']]] = None,
            automatic_date_parsing: Optional[pulumi.Input[bool]] = None,
            category: Optional[pulumi.Input[str]] = None,
            collector_id: Optional[pulumi.Input[int]] = None,
            content_type: Optional[pulumi.Input[str]] = None,
            cutoff_relative_time: Optional[pulumi.Input[str]] = None,
            cutoff_timestamp: Optional[pulumi.Input[int]] = None,
            default_date_formats: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['GcpSourceDefaultDateFormatArgs']]]]] = None,
            description: Optional[pulumi.Input[str]] = None,
            fields: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            filters: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['GcpSourceFilterArgs']]]]] = None,
            force_timezone: Optional[pulumi.Input[bool]] = None,
            host_name: Optional[pulumi.Input[str]] = None,
            manual_prefix_regexp: Optional[pulumi.Input[str]] = None,
            message_per_request: Optional[pulumi.Input[bool]] = None,
            multiline_processing_enabled: Optional[pulumi.Input[bool]] = None,
            name: Optional[pulumi.Input[str]] = None,
            path: Optional[pulumi.Input[pulumi.InputType['GcpSourcePathArgs']]] = None,
            timezone: Optional[pulumi.Input[str]] = None,
            url: Optional[pulumi.Input[str]] = None,
            use_autoline_matching: Optional[pulumi.Input[bool]] = None) -> 'GcpSource':
        """
        Get an existing GcpSource resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] url: The HTTP endpoint to use for sending data to this source.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _GcpSourceState.__new__(_GcpSourceState)

        __props__.__dict__["authentication"] = authentication
        __props__.__dict__["automatic_date_parsing"] = automatic_date_parsing
        __props__.__dict__["category"] = category
        __props__.__dict__["collector_id"] = collector_id
        __props__.__dict__["content_type"] = content_type
        __props__.__dict__["cutoff_relative_time"] = cutoff_relative_time
        __props__.__dict__["cutoff_timestamp"] = cutoff_timestamp
        __props__.__dict__["default_date_formats"] = default_date_formats
        __props__.__dict__["description"] = description
        __props__.__dict__["fields"] = fields
        __props__.__dict__["filters"] = filters
        __props__.__dict__["force_timezone"] = force_timezone
        __props__.__dict__["host_name"] = host_name
        __props__.__dict__["manual_prefix_regexp"] = manual_prefix_regexp
        __props__.__dict__["message_per_request"] = message_per_request
        __props__.__dict__["multiline_processing_enabled"] = multiline_processing_enabled
        __props__.__dict__["name"] = name
        __props__.__dict__["path"] = path
        __props__.__dict__["timezone"] = timezone
        __props__.__dict__["url"] = url
        __props__.__dict__["use_autoline_matching"] = use_autoline_matching
        return GcpSource(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def authentication(self) -> pulumi.Output[Optional['outputs.GcpSourceAuthentication']]:
        return pulumi.get(self, "authentication")

    @property
    @pulumi.getter(name="automaticDateParsing")
    def automatic_date_parsing(self) -> pulumi.Output[Optional[bool]]:
        return pulumi.get(self, "automatic_date_parsing")

    @property
    @pulumi.getter
    def category(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "category")

    @property
    @pulumi.getter(name="collectorId")
    def collector_id(self) -> pulumi.Output[int]:
        return pulumi.get(self, "collector_id")

    @property
    @pulumi.getter(name="contentType")
    def content_type(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "content_type")

    @property
    @pulumi.getter(name="cutoffRelativeTime")
    def cutoff_relative_time(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "cutoff_relative_time")

    @property
    @pulumi.getter(name="cutoffTimestamp")
    def cutoff_timestamp(self) -> pulumi.Output[Optional[int]]:
        return pulumi.get(self, "cutoff_timestamp")

    @property
    @pulumi.getter(name="defaultDateFormats")
    def default_date_formats(self) -> pulumi.Output[Optional[Sequence['outputs.GcpSourceDefaultDateFormat']]]:
        return pulumi.get(self, "default_date_formats")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def fields(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        return pulumi.get(self, "fields")

    @property
    @pulumi.getter
    def filters(self) -> pulumi.Output[Optional[Sequence['outputs.GcpSourceFilter']]]:
        return pulumi.get(self, "filters")

    @property
    @pulumi.getter(name="forceTimezone")
    def force_timezone(self) -> pulumi.Output[Optional[bool]]:
        return pulumi.get(self, "force_timezone")

    @property
    @pulumi.getter(name="hostName")
    def host_name(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "host_name")

    @property
    @pulumi.getter(name="manualPrefixRegexp")
    def manual_prefix_regexp(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "manual_prefix_regexp")

    @property
    @pulumi.getter(name="messagePerRequest")
    def message_per_request(self) -> pulumi.Output[Optional[bool]]:
        return pulumi.get(self, "message_per_request")

    @property
    @pulumi.getter(name="multilineProcessingEnabled")
    def multiline_processing_enabled(self) -> pulumi.Output[Optional[bool]]:
        return pulumi.get(self, "multiline_processing_enabled")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def path(self) -> pulumi.Output[Optional['outputs.GcpSourcePath']]:
        return pulumi.get(self, "path")

    @property
    @pulumi.getter
    def timezone(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "timezone")

    @property
    @pulumi.getter
    def url(self) -> pulumi.Output[str]:
        """
        The HTTP endpoint to use for sending data to this source.
        """
        return pulumi.get(self, "url")

    @property
    @pulumi.getter(name="useAutolineMatching")
    def use_autoline_matching(self) -> pulumi.Output[Optional[bool]]:
        return pulumi.get(self, "use_autoline_matching")


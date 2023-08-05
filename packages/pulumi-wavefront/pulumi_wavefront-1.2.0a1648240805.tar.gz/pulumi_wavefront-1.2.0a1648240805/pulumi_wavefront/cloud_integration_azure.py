# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['CloudIntegrationAzureArgs', 'CloudIntegrationAzure']

@pulumi.input_type
class CloudIntegrationAzureArgs:
    def __init__(__self__, *,
                 client_id: pulumi.Input[str],
                 client_secret: pulumi.Input[str],
                 service: pulumi.Input[str],
                 tenant: pulumi.Input[str],
                 additional_tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 category_filters: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 force_save: Optional[pulumi.Input[bool]] = None,
                 metric_filter_regex: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resource_group_filters: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 service_refresh_rate_in_minutes: Optional[pulumi.Input[int]] = None):
        """
        The set of arguments for constructing a CloudIntegrationAzure resource.
        :param pulumi.Input[str] client_id: Client id for an azure service account within your project
        :param pulumi.Input[str] client_secret: Client secret for an Azure service account within your project
        :param pulumi.Input[str] service: A value denoting which cloud service this service integrates with
        :param pulumi.Input[str] tenant: Tenant Id for an Azure service account within your project
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] additional_tags: A list of point tag key-values to add to every point ingested using this integration
        :param pulumi.Input[Sequence[pulumi.Input[str]]] category_filters: A list of Azure Activity Log categories.
        :param pulumi.Input[bool] force_save: Forces this resource to save, even if errors are present
        :param pulumi.Input[str] metric_filter_regex: A regular expression that a metric name must match (case-insensitively) in order to be ingested
        :param pulumi.Input[str] name: The human-readable name of this integration
        :param pulumi.Input[Sequence[pulumi.Input[str]]] resource_group_filters: A list of Azure resource groups from which to pull metrics
        :param pulumi.Input[int] service_refresh_rate_in_minutes: How often, in minutes, to refresh the service
        """
        pulumi.set(__self__, "client_id", client_id)
        pulumi.set(__self__, "client_secret", client_secret)
        pulumi.set(__self__, "service", service)
        pulumi.set(__self__, "tenant", tenant)
        if additional_tags is not None:
            pulumi.set(__self__, "additional_tags", additional_tags)
        if category_filters is not None:
            pulumi.set(__self__, "category_filters", category_filters)
        if force_save is not None:
            pulumi.set(__self__, "force_save", force_save)
        if metric_filter_regex is not None:
            pulumi.set(__self__, "metric_filter_regex", metric_filter_regex)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if resource_group_filters is not None:
            pulumi.set(__self__, "resource_group_filters", resource_group_filters)
        if service_refresh_rate_in_minutes is not None:
            pulumi.set(__self__, "service_refresh_rate_in_minutes", service_refresh_rate_in_minutes)

    @property
    @pulumi.getter(name="clientId")
    def client_id(self) -> pulumi.Input[str]:
        """
        Client id for an azure service account within your project
        """
        return pulumi.get(self, "client_id")

    @client_id.setter
    def client_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "client_id", value)

    @property
    @pulumi.getter(name="clientSecret")
    def client_secret(self) -> pulumi.Input[str]:
        """
        Client secret for an Azure service account within your project
        """
        return pulumi.get(self, "client_secret")

    @client_secret.setter
    def client_secret(self, value: pulumi.Input[str]):
        pulumi.set(self, "client_secret", value)

    @property
    @pulumi.getter
    def service(self) -> pulumi.Input[str]:
        """
        A value denoting which cloud service this service integrates with
        """
        return pulumi.get(self, "service")

    @service.setter
    def service(self, value: pulumi.Input[str]):
        pulumi.set(self, "service", value)

    @property
    @pulumi.getter
    def tenant(self) -> pulumi.Input[str]:
        """
        Tenant Id for an Azure service account within your project
        """
        return pulumi.get(self, "tenant")

    @tenant.setter
    def tenant(self, value: pulumi.Input[str]):
        pulumi.set(self, "tenant", value)

    @property
    @pulumi.getter(name="additionalTags")
    def additional_tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        A list of point tag key-values to add to every point ingested using this integration
        """
        return pulumi.get(self, "additional_tags")

    @additional_tags.setter
    def additional_tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "additional_tags", value)

    @property
    @pulumi.getter(name="categoryFilters")
    def category_filters(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        A list of Azure Activity Log categories.
        """
        return pulumi.get(self, "category_filters")

    @category_filters.setter
    def category_filters(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "category_filters", value)

    @property
    @pulumi.getter(name="forceSave")
    def force_save(self) -> Optional[pulumi.Input[bool]]:
        """
        Forces this resource to save, even if errors are present
        """
        return pulumi.get(self, "force_save")

    @force_save.setter
    def force_save(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "force_save", value)

    @property
    @pulumi.getter(name="metricFilterRegex")
    def metric_filter_regex(self) -> Optional[pulumi.Input[str]]:
        """
        A regular expression that a metric name must match (case-insensitively) in order to be ingested
        """
        return pulumi.get(self, "metric_filter_regex")

    @metric_filter_regex.setter
    def metric_filter_regex(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "metric_filter_regex", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The human-readable name of this integration
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="resourceGroupFilters")
    def resource_group_filters(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        A list of Azure resource groups from which to pull metrics
        """
        return pulumi.get(self, "resource_group_filters")

    @resource_group_filters.setter
    def resource_group_filters(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "resource_group_filters", value)

    @property
    @pulumi.getter(name="serviceRefreshRateInMinutes")
    def service_refresh_rate_in_minutes(self) -> Optional[pulumi.Input[int]]:
        """
        How often, in minutes, to refresh the service
        """
        return pulumi.get(self, "service_refresh_rate_in_minutes")

    @service_refresh_rate_in_minutes.setter
    def service_refresh_rate_in_minutes(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "service_refresh_rate_in_minutes", value)


@pulumi.input_type
class _CloudIntegrationAzureState:
    def __init__(__self__, *,
                 additional_tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 category_filters: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 client_id: Optional[pulumi.Input[str]] = None,
                 client_secret: Optional[pulumi.Input[str]] = None,
                 force_save: Optional[pulumi.Input[bool]] = None,
                 metric_filter_regex: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resource_group_filters: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 service: Optional[pulumi.Input[str]] = None,
                 service_refresh_rate_in_minutes: Optional[pulumi.Input[int]] = None,
                 tenant: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering CloudIntegrationAzure resources.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] additional_tags: A list of point tag key-values to add to every point ingested using this integration
        :param pulumi.Input[Sequence[pulumi.Input[str]]] category_filters: A list of Azure Activity Log categories.
        :param pulumi.Input[str] client_id: Client id for an azure service account within your project
        :param pulumi.Input[str] client_secret: Client secret for an Azure service account within your project
        :param pulumi.Input[bool] force_save: Forces this resource to save, even if errors are present
        :param pulumi.Input[str] metric_filter_regex: A regular expression that a metric name must match (case-insensitively) in order to be ingested
        :param pulumi.Input[str] name: The human-readable name of this integration
        :param pulumi.Input[Sequence[pulumi.Input[str]]] resource_group_filters: A list of Azure resource groups from which to pull metrics
        :param pulumi.Input[str] service: A value denoting which cloud service this service integrates with
        :param pulumi.Input[int] service_refresh_rate_in_minutes: How often, in minutes, to refresh the service
        :param pulumi.Input[str] tenant: Tenant Id for an Azure service account within your project
        """
        if additional_tags is not None:
            pulumi.set(__self__, "additional_tags", additional_tags)
        if category_filters is not None:
            pulumi.set(__self__, "category_filters", category_filters)
        if client_id is not None:
            pulumi.set(__self__, "client_id", client_id)
        if client_secret is not None:
            pulumi.set(__self__, "client_secret", client_secret)
        if force_save is not None:
            pulumi.set(__self__, "force_save", force_save)
        if metric_filter_regex is not None:
            pulumi.set(__self__, "metric_filter_regex", metric_filter_regex)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if resource_group_filters is not None:
            pulumi.set(__self__, "resource_group_filters", resource_group_filters)
        if service is not None:
            pulumi.set(__self__, "service", service)
        if service_refresh_rate_in_minutes is not None:
            pulumi.set(__self__, "service_refresh_rate_in_minutes", service_refresh_rate_in_minutes)
        if tenant is not None:
            pulumi.set(__self__, "tenant", tenant)

    @property
    @pulumi.getter(name="additionalTags")
    def additional_tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        A list of point tag key-values to add to every point ingested using this integration
        """
        return pulumi.get(self, "additional_tags")

    @additional_tags.setter
    def additional_tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "additional_tags", value)

    @property
    @pulumi.getter(name="categoryFilters")
    def category_filters(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        A list of Azure Activity Log categories.
        """
        return pulumi.get(self, "category_filters")

    @category_filters.setter
    def category_filters(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "category_filters", value)

    @property
    @pulumi.getter(name="clientId")
    def client_id(self) -> Optional[pulumi.Input[str]]:
        """
        Client id for an azure service account within your project
        """
        return pulumi.get(self, "client_id")

    @client_id.setter
    def client_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "client_id", value)

    @property
    @pulumi.getter(name="clientSecret")
    def client_secret(self) -> Optional[pulumi.Input[str]]:
        """
        Client secret for an Azure service account within your project
        """
        return pulumi.get(self, "client_secret")

    @client_secret.setter
    def client_secret(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "client_secret", value)

    @property
    @pulumi.getter(name="forceSave")
    def force_save(self) -> Optional[pulumi.Input[bool]]:
        """
        Forces this resource to save, even if errors are present
        """
        return pulumi.get(self, "force_save")

    @force_save.setter
    def force_save(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "force_save", value)

    @property
    @pulumi.getter(name="metricFilterRegex")
    def metric_filter_regex(self) -> Optional[pulumi.Input[str]]:
        """
        A regular expression that a metric name must match (case-insensitively) in order to be ingested
        """
        return pulumi.get(self, "metric_filter_regex")

    @metric_filter_regex.setter
    def metric_filter_regex(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "metric_filter_regex", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The human-readable name of this integration
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="resourceGroupFilters")
    def resource_group_filters(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        A list of Azure resource groups from which to pull metrics
        """
        return pulumi.get(self, "resource_group_filters")

    @resource_group_filters.setter
    def resource_group_filters(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "resource_group_filters", value)

    @property
    @pulumi.getter
    def service(self) -> Optional[pulumi.Input[str]]:
        """
        A value denoting which cloud service this service integrates with
        """
        return pulumi.get(self, "service")

    @service.setter
    def service(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "service", value)

    @property
    @pulumi.getter(name="serviceRefreshRateInMinutes")
    def service_refresh_rate_in_minutes(self) -> Optional[pulumi.Input[int]]:
        """
        How often, in minutes, to refresh the service
        """
        return pulumi.get(self, "service_refresh_rate_in_minutes")

    @service_refresh_rate_in_minutes.setter
    def service_refresh_rate_in_minutes(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "service_refresh_rate_in_minutes", value)

    @property
    @pulumi.getter
    def tenant(self) -> Optional[pulumi.Input[str]]:
        """
        Tenant Id for an Azure service account within your project
        """
        return pulumi.get(self, "tenant")

    @tenant.setter
    def tenant(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "tenant", value)


class CloudIntegrationAzure(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 additional_tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 category_filters: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 client_id: Optional[pulumi.Input[str]] = None,
                 client_secret: Optional[pulumi.Input[str]] = None,
                 force_save: Optional[pulumi.Input[bool]] = None,
                 metric_filter_regex: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resource_group_filters: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 service: Optional[pulumi.Input[str]] = None,
                 service_refresh_rate_in_minutes: Optional[pulumi.Input[int]] = None,
                 tenant: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Provides a Wavefront Cloud Integration for Azure. This allows azure cloud integrations to be created,
        updated, and deleted.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_wavefront as wavefront

        azure_activity_log = wavefront.CloudIntegrationAzureActivityLog("azureActivityLog",
            client_id="client-id2",
            client_secret="client-secret2",
            tenant="my-tenant2")
        ```

        ## Import

        Azure Cloud Integrations can be imported using the `id`, e.g.

        ```sh
         $ pulumi import wavefront:index/cloudIntegrationAzure:CloudIntegrationAzure azure a411c16b-3cf7-4f03-bf11-8ca05aab898d
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] additional_tags: A list of point tag key-values to add to every point ingested using this integration
        :param pulumi.Input[Sequence[pulumi.Input[str]]] category_filters: A list of Azure Activity Log categories.
        :param pulumi.Input[str] client_id: Client id for an azure service account within your project
        :param pulumi.Input[str] client_secret: Client secret for an Azure service account within your project
        :param pulumi.Input[bool] force_save: Forces this resource to save, even if errors are present
        :param pulumi.Input[str] metric_filter_regex: A regular expression that a metric name must match (case-insensitively) in order to be ingested
        :param pulumi.Input[str] name: The human-readable name of this integration
        :param pulumi.Input[Sequence[pulumi.Input[str]]] resource_group_filters: A list of Azure resource groups from which to pull metrics
        :param pulumi.Input[str] service: A value denoting which cloud service this service integrates with
        :param pulumi.Input[int] service_refresh_rate_in_minutes: How often, in minutes, to refresh the service
        :param pulumi.Input[str] tenant: Tenant Id for an Azure service account within your project
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: CloudIntegrationAzureArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a Wavefront Cloud Integration for Azure. This allows azure cloud integrations to be created,
        updated, and deleted.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_wavefront as wavefront

        azure_activity_log = wavefront.CloudIntegrationAzureActivityLog("azureActivityLog",
            client_id="client-id2",
            client_secret="client-secret2",
            tenant="my-tenant2")
        ```

        ## Import

        Azure Cloud Integrations can be imported using the `id`, e.g.

        ```sh
         $ pulumi import wavefront:index/cloudIntegrationAzure:CloudIntegrationAzure azure a411c16b-3cf7-4f03-bf11-8ca05aab898d
        ```

        :param str resource_name: The name of the resource.
        :param CloudIntegrationAzureArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(CloudIntegrationAzureArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 additional_tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 category_filters: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 client_id: Optional[pulumi.Input[str]] = None,
                 client_secret: Optional[pulumi.Input[str]] = None,
                 force_save: Optional[pulumi.Input[bool]] = None,
                 metric_filter_regex: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resource_group_filters: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 service: Optional[pulumi.Input[str]] = None,
                 service_refresh_rate_in_minutes: Optional[pulumi.Input[int]] = None,
                 tenant: Optional[pulumi.Input[str]] = None,
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
            __props__ = CloudIntegrationAzureArgs.__new__(CloudIntegrationAzureArgs)

            __props__.__dict__["additional_tags"] = additional_tags
            __props__.__dict__["category_filters"] = category_filters
            if client_id is None and not opts.urn:
                raise TypeError("Missing required property 'client_id'")
            __props__.__dict__["client_id"] = client_id
            if client_secret is None and not opts.urn:
                raise TypeError("Missing required property 'client_secret'")
            __props__.__dict__["client_secret"] = client_secret
            __props__.__dict__["force_save"] = force_save
            __props__.__dict__["metric_filter_regex"] = metric_filter_regex
            __props__.__dict__["name"] = name
            __props__.__dict__["resource_group_filters"] = resource_group_filters
            if service is None and not opts.urn:
                raise TypeError("Missing required property 'service'")
            __props__.__dict__["service"] = service
            __props__.__dict__["service_refresh_rate_in_minutes"] = service_refresh_rate_in_minutes
            if tenant is None and not opts.urn:
                raise TypeError("Missing required property 'tenant'")
            __props__.__dict__["tenant"] = tenant
        super(CloudIntegrationAzure, __self__).__init__(
            'wavefront:index/cloudIntegrationAzure:CloudIntegrationAzure',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            additional_tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            category_filters: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            client_id: Optional[pulumi.Input[str]] = None,
            client_secret: Optional[pulumi.Input[str]] = None,
            force_save: Optional[pulumi.Input[bool]] = None,
            metric_filter_regex: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            resource_group_filters: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            service: Optional[pulumi.Input[str]] = None,
            service_refresh_rate_in_minutes: Optional[pulumi.Input[int]] = None,
            tenant: Optional[pulumi.Input[str]] = None) -> 'CloudIntegrationAzure':
        """
        Get an existing CloudIntegrationAzure resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] additional_tags: A list of point tag key-values to add to every point ingested using this integration
        :param pulumi.Input[Sequence[pulumi.Input[str]]] category_filters: A list of Azure Activity Log categories.
        :param pulumi.Input[str] client_id: Client id for an azure service account within your project
        :param pulumi.Input[str] client_secret: Client secret for an Azure service account within your project
        :param pulumi.Input[bool] force_save: Forces this resource to save, even if errors are present
        :param pulumi.Input[str] metric_filter_regex: A regular expression that a metric name must match (case-insensitively) in order to be ingested
        :param pulumi.Input[str] name: The human-readable name of this integration
        :param pulumi.Input[Sequence[pulumi.Input[str]]] resource_group_filters: A list of Azure resource groups from which to pull metrics
        :param pulumi.Input[str] service: A value denoting which cloud service this service integrates with
        :param pulumi.Input[int] service_refresh_rate_in_minutes: How often, in minutes, to refresh the service
        :param pulumi.Input[str] tenant: Tenant Id for an Azure service account within your project
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _CloudIntegrationAzureState.__new__(_CloudIntegrationAzureState)

        __props__.__dict__["additional_tags"] = additional_tags
        __props__.__dict__["category_filters"] = category_filters
        __props__.__dict__["client_id"] = client_id
        __props__.__dict__["client_secret"] = client_secret
        __props__.__dict__["force_save"] = force_save
        __props__.__dict__["metric_filter_regex"] = metric_filter_regex
        __props__.__dict__["name"] = name
        __props__.__dict__["resource_group_filters"] = resource_group_filters
        __props__.__dict__["service"] = service
        __props__.__dict__["service_refresh_rate_in_minutes"] = service_refresh_rate_in_minutes
        __props__.__dict__["tenant"] = tenant
        return CloudIntegrationAzure(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="additionalTags")
    def additional_tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        A list of point tag key-values to add to every point ingested using this integration
        """
        return pulumi.get(self, "additional_tags")

    @property
    @pulumi.getter(name="categoryFilters")
    def category_filters(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        A list of Azure Activity Log categories.
        """
        return pulumi.get(self, "category_filters")

    @property
    @pulumi.getter(name="clientId")
    def client_id(self) -> pulumi.Output[str]:
        """
        Client id for an azure service account within your project
        """
        return pulumi.get(self, "client_id")

    @property
    @pulumi.getter(name="clientSecret")
    def client_secret(self) -> pulumi.Output[str]:
        """
        Client secret for an Azure service account within your project
        """
        return pulumi.get(self, "client_secret")

    @property
    @pulumi.getter(name="forceSave")
    def force_save(self) -> pulumi.Output[Optional[bool]]:
        """
        Forces this resource to save, even if errors are present
        """
        return pulumi.get(self, "force_save")

    @property
    @pulumi.getter(name="metricFilterRegex")
    def metric_filter_regex(self) -> pulumi.Output[Optional[str]]:
        """
        A regular expression that a metric name must match (case-insensitively) in order to be ingested
        """
        return pulumi.get(self, "metric_filter_regex")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The human-readable name of this integration
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="resourceGroupFilters")
    def resource_group_filters(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        A list of Azure resource groups from which to pull metrics
        """
        return pulumi.get(self, "resource_group_filters")

    @property
    @pulumi.getter
    def service(self) -> pulumi.Output[str]:
        """
        A value denoting which cloud service this service integrates with
        """
        return pulumi.get(self, "service")

    @property
    @pulumi.getter(name="serviceRefreshRateInMinutes")
    def service_refresh_rate_in_minutes(self) -> pulumi.Output[Optional[int]]:
        """
        How often, in minutes, to refresh the service
        """
        return pulumi.get(self, "service_refresh_rate_in_minutes")

    @property
    @pulumi.getter
    def tenant(self) -> pulumi.Output[str]:
        """
        Tenant Id for an Azure service account within your project
        """
        return pulumi.get(self, "tenant")


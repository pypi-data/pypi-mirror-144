# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['CloudIntegrationGcpBillingArgs', 'CloudIntegrationGcpBilling']

@pulumi.input_type
class CloudIntegrationGcpBillingArgs:
    def __init__(__self__, *,
                 api_key: pulumi.Input[str],
                 json_key: pulumi.Input[str],
                 project_id: pulumi.Input[str],
                 service: pulumi.Input[str],
                 additional_tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 force_save: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 service_refresh_rate_in_minutes: Optional[pulumi.Input[int]] = None):
        """
        The set of arguments for constructing a CloudIntegrationGcpBilling resource.
        :param pulumi.Input[str] api_key: API key for Google Cloud Platform (GCP)
        :param pulumi.Input[str] json_key: Private key for a Google Cloud Platform (GCP) service account within your project.
               The account must be at least granted Monitoring Viewer permissions. This key must be in the JSON format generated by GCP.
        :param pulumi.Input[str] project_id: The Google Cloud Platform (GCP) Project Id
        :param pulumi.Input[str] service: A value denoting which cloud service this service integrates with
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] additional_tags: A list of point tag key-values to add to every point ingested using this integration
        :param pulumi.Input[bool] force_save: Forces this resource to save, even if errors are present
        :param pulumi.Input[str] name: The human-readable name of this integration
        :param pulumi.Input[int] service_refresh_rate_in_minutes: How often, in minutes, to refresh the service
        """
        pulumi.set(__self__, "api_key", api_key)
        pulumi.set(__self__, "json_key", json_key)
        pulumi.set(__self__, "project_id", project_id)
        pulumi.set(__self__, "service", service)
        if additional_tags is not None:
            pulumi.set(__self__, "additional_tags", additional_tags)
        if force_save is not None:
            pulumi.set(__self__, "force_save", force_save)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if service_refresh_rate_in_minutes is not None:
            pulumi.set(__self__, "service_refresh_rate_in_minutes", service_refresh_rate_in_minutes)

    @property
    @pulumi.getter(name="apiKey")
    def api_key(self) -> pulumi.Input[str]:
        """
        API key for Google Cloud Platform (GCP)
        """
        return pulumi.get(self, "api_key")

    @api_key.setter
    def api_key(self, value: pulumi.Input[str]):
        pulumi.set(self, "api_key", value)

    @property
    @pulumi.getter(name="jsonKey")
    def json_key(self) -> pulumi.Input[str]:
        """
        Private key for a Google Cloud Platform (GCP) service account within your project.
        The account must be at least granted Monitoring Viewer permissions. This key must be in the JSON format generated by GCP.
        """
        return pulumi.get(self, "json_key")

    @json_key.setter
    def json_key(self, value: pulumi.Input[str]):
        pulumi.set(self, "json_key", value)

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> pulumi.Input[str]:
        """
        The Google Cloud Platform (GCP) Project Id
        """
        return pulumi.get(self, "project_id")

    @project_id.setter
    def project_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "project_id", value)

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
class _CloudIntegrationGcpBillingState:
    def __init__(__self__, *,
                 additional_tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 api_key: Optional[pulumi.Input[str]] = None,
                 force_save: Optional[pulumi.Input[bool]] = None,
                 json_key: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project_id: Optional[pulumi.Input[str]] = None,
                 service: Optional[pulumi.Input[str]] = None,
                 service_refresh_rate_in_minutes: Optional[pulumi.Input[int]] = None):
        """
        Input properties used for looking up and filtering CloudIntegrationGcpBilling resources.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] additional_tags: A list of point tag key-values to add to every point ingested using this integration
        :param pulumi.Input[str] api_key: API key for Google Cloud Platform (GCP)
        :param pulumi.Input[bool] force_save: Forces this resource to save, even if errors are present
        :param pulumi.Input[str] json_key: Private key for a Google Cloud Platform (GCP) service account within your project.
               The account must be at least granted Monitoring Viewer permissions. This key must be in the JSON format generated by GCP.
        :param pulumi.Input[str] name: The human-readable name of this integration
        :param pulumi.Input[str] project_id: The Google Cloud Platform (GCP) Project Id
        :param pulumi.Input[str] service: A value denoting which cloud service this service integrates with
        :param pulumi.Input[int] service_refresh_rate_in_minutes: How often, in minutes, to refresh the service
        """
        if additional_tags is not None:
            pulumi.set(__self__, "additional_tags", additional_tags)
        if api_key is not None:
            pulumi.set(__self__, "api_key", api_key)
        if force_save is not None:
            pulumi.set(__self__, "force_save", force_save)
        if json_key is not None:
            pulumi.set(__self__, "json_key", json_key)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if project_id is not None:
            pulumi.set(__self__, "project_id", project_id)
        if service is not None:
            pulumi.set(__self__, "service", service)
        if service_refresh_rate_in_minutes is not None:
            pulumi.set(__self__, "service_refresh_rate_in_minutes", service_refresh_rate_in_minutes)

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
    @pulumi.getter(name="apiKey")
    def api_key(self) -> Optional[pulumi.Input[str]]:
        """
        API key for Google Cloud Platform (GCP)
        """
        return pulumi.get(self, "api_key")

    @api_key.setter
    def api_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "api_key", value)

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
    @pulumi.getter(name="jsonKey")
    def json_key(self) -> Optional[pulumi.Input[str]]:
        """
        Private key for a Google Cloud Platform (GCP) service account within your project.
        The account must be at least granted Monitoring Viewer permissions. This key must be in the JSON format generated by GCP.
        """
        return pulumi.get(self, "json_key")

    @json_key.setter
    def json_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "json_key", value)

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
    @pulumi.getter(name="projectId")
    def project_id(self) -> Optional[pulumi.Input[str]]:
        """
        The Google Cloud Platform (GCP) Project Id
        """
        return pulumi.get(self, "project_id")

    @project_id.setter
    def project_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project_id", value)

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


class CloudIntegrationGcpBilling(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 additional_tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 api_key: Optional[pulumi.Input[str]] = None,
                 force_save: Optional[pulumi.Input[bool]] = None,
                 json_key: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project_id: Optional[pulumi.Input[str]] = None,
                 service: Optional[pulumi.Input[str]] = None,
                 service_refresh_rate_in_minutes: Optional[pulumi.Input[int]] = None,
                 __props__=None):
        """
        Provides a Wavefront Cloud Integration for GCP Billing. This allows GCP Billing cloud integrations to be created,
        updated, and deleted.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_wavefront as wavefront

        gcp_billing = wavefront.CloudIntegrationGcpBilling("gcpBilling",
            api_key="example-api-key",
            json_key=\"\"\"{...your gcp key ...}

        \"\"\",
            project_id="example-gcp-project")
        ```

        ## Import

        GCP Billing Cloud Integrations can be imported using the `id`, e.g.

        ```sh
         $ pulumi import wavefront:index/cloudIntegrationGcpBilling:CloudIntegrationGcpBilling gcp_billing a411c16b-3cf7-4f03-bf11-8ca05aab898d
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] additional_tags: A list of point tag key-values to add to every point ingested using this integration
        :param pulumi.Input[str] api_key: API key for Google Cloud Platform (GCP)
        :param pulumi.Input[bool] force_save: Forces this resource to save, even if errors are present
        :param pulumi.Input[str] json_key: Private key for a Google Cloud Platform (GCP) service account within your project.
               The account must be at least granted Monitoring Viewer permissions. This key must be in the JSON format generated by GCP.
        :param pulumi.Input[str] name: The human-readable name of this integration
        :param pulumi.Input[str] project_id: The Google Cloud Platform (GCP) Project Id
        :param pulumi.Input[str] service: A value denoting which cloud service this service integrates with
        :param pulumi.Input[int] service_refresh_rate_in_minutes: How often, in minutes, to refresh the service
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: CloudIntegrationGcpBillingArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a Wavefront Cloud Integration for GCP Billing. This allows GCP Billing cloud integrations to be created,
        updated, and deleted.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_wavefront as wavefront

        gcp_billing = wavefront.CloudIntegrationGcpBilling("gcpBilling",
            api_key="example-api-key",
            json_key=\"\"\"{...your gcp key ...}

        \"\"\",
            project_id="example-gcp-project")
        ```

        ## Import

        GCP Billing Cloud Integrations can be imported using the `id`, e.g.

        ```sh
         $ pulumi import wavefront:index/cloudIntegrationGcpBilling:CloudIntegrationGcpBilling gcp_billing a411c16b-3cf7-4f03-bf11-8ca05aab898d
        ```

        :param str resource_name: The name of the resource.
        :param CloudIntegrationGcpBillingArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(CloudIntegrationGcpBillingArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 additional_tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 api_key: Optional[pulumi.Input[str]] = None,
                 force_save: Optional[pulumi.Input[bool]] = None,
                 json_key: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project_id: Optional[pulumi.Input[str]] = None,
                 service: Optional[pulumi.Input[str]] = None,
                 service_refresh_rate_in_minutes: Optional[pulumi.Input[int]] = None,
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
            __props__ = CloudIntegrationGcpBillingArgs.__new__(CloudIntegrationGcpBillingArgs)

            __props__.__dict__["additional_tags"] = additional_tags
            if api_key is None and not opts.urn:
                raise TypeError("Missing required property 'api_key'")
            __props__.__dict__["api_key"] = api_key
            __props__.__dict__["force_save"] = force_save
            if json_key is None and not opts.urn:
                raise TypeError("Missing required property 'json_key'")
            __props__.__dict__["json_key"] = json_key
            __props__.__dict__["name"] = name
            if project_id is None and not opts.urn:
                raise TypeError("Missing required property 'project_id'")
            __props__.__dict__["project_id"] = project_id
            if service is None and not opts.urn:
                raise TypeError("Missing required property 'service'")
            __props__.__dict__["service"] = service
            __props__.__dict__["service_refresh_rate_in_minutes"] = service_refresh_rate_in_minutes
        super(CloudIntegrationGcpBilling, __self__).__init__(
            'wavefront:index/cloudIntegrationGcpBilling:CloudIntegrationGcpBilling',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            additional_tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            api_key: Optional[pulumi.Input[str]] = None,
            force_save: Optional[pulumi.Input[bool]] = None,
            json_key: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            project_id: Optional[pulumi.Input[str]] = None,
            service: Optional[pulumi.Input[str]] = None,
            service_refresh_rate_in_minutes: Optional[pulumi.Input[int]] = None) -> 'CloudIntegrationGcpBilling':
        """
        Get an existing CloudIntegrationGcpBilling resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] additional_tags: A list of point tag key-values to add to every point ingested using this integration
        :param pulumi.Input[str] api_key: API key for Google Cloud Platform (GCP)
        :param pulumi.Input[bool] force_save: Forces this resource to save, even if errors are present
        :param pulumi.Input[str] json_key: Private key for a Google Cloud Platform (GCP) service account within your project.
               The account must be at least granted Monitoring Viewer permissions. This key must be in the JSON format generated by GCP.
        :param pulumi.Input[str] name: The human-readable name of this integration
        :param pulumi.Input[str] project_id: The Google Cloud Platform (GCP) Project Id
        :param pulumi.Input[str] service: A value denoting which cloud service this service integrates with
        :param pulumi.Input[int] service_refresh_rate_in_minutes: How often, in minutes, to refresh the service
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _CloudIntegrationGcpBillingState.__new__(_CloudIntegrationGcpBillingState)

        __props__.__dict__["additional_tags"] = additional_tags
        __props__.__dict__["api_key"] = api_key
        __props__.__dict__["force_save"] = force_save
        __props__.__dict__["json_key"] = json_key
        __props__.__dict__["name"] = name
        __props__.__dict__["project_id"] = project_id
        __props__.__dict__["service"] = service
        __props__.__dict__["service_refresh_rate_in_minutes"] = service_refresh_rate_in_minutes
        return CloudIntegrationGcpBilling(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="additionalTags")
    def additional_tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        A list of point tag key-values to add to every point ingested using this integration
        """
        return pulumi.get(self, "additional_tags")

    @property
    @pulumi.getter(name="apiKey")
    def api_key(self) -> pulumi.Output[str]:
        """
        API key for Google Cloud Platform (GCP)
        """
        return pulumi.get(self, "api_key")

    @property
    @pulumi.getter(name="forceSave")
    def force_save(self) -> pulumi.Output[Optional[bool]]:
        """
        Forces this resource to save, even if errors are present
        """
        return pulumi.get(self, "force_save")

    @property
    @pulumi.getter(name="jsonKey")
    def json_key(self) -> pulumi.Output[str]:
        """
        Private key for a Google Cloud Platform (GCP) service account within your project.
        The account must be at least granted Monitoring Viewer permissions. This key must be in the JSON format generated by GCP.
        """
        return pulumi.get(self, "json_key")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The human-readable name of this integration
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> pulumi.Output[str]:
        """
        The Google Cloud Platform (GCP) Project Id
        """
        return pulumi.get(self, "project_id")

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


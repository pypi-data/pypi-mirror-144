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

__all__ = ['MdbElasticSearchClusterArgs', 'MdbElasticSearchCluster']

@pulumi.input_type
class MdbElasticSearchClusterArgs:
    def __init__(__self__, *,
                 config: pulumi.Input['MdbElasticSearchClusterConfigArgs'],
                 environment: pulumi.Input[str],
                 network_id: pulumi.Input[str],
                 deletion_protection: Optional[pulumi.Input[bool]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 folder_id: Optional[pulumi.Input[str]] = None,
                 hosts: Optional[pulumi.Input[Sequence[pulumi.Input['MdbElasticSearchClusterHostArgs']]]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 maintenance_window: Optional[pulumi.Input['MdbElasticSearchClusterMaintenanceWindowArgs']] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 security_group_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 service_account_id: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a MdbElasticSearchCluster resource.
        :param pulumi.Input['MdbElasticSearchClusterConfigArgs'] config: Configuration of the Elasticsearch cluster. The structure is documented below.
        :param pulumi.Input[str] environment: Deployment environment of the Elasticsearch cluster. Can be either `PRESTABLE` or `PRODUCTION`.
        :param pulumi.Input[str] network_id: ID of the network, to which the Elasticsearch cluster belongs.
        :param pulumi.Input[bool] deletion_protection: Inhibits deletion of the cluster.  Can be either `true` or `false`.
        :param pulumi.Input[str] description: Description of the Elasticsearch cluster.
        :param pulumi.Input[str] folder_id: The ID of the folder that the resource belongs to. If it is not provided, the default provider folder is used.
        :param pulumi.Input[Sequence[pulumi.Input['MdbElasticSearchClusterHostArgs']]] hosts: A host of the Elasticsearch cluster. The structure is documented below.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] labels: A set of key/value label pairs to assign to the Elasticsearch cluster.
        :param pulumi.Input[str] name: User defined host name.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] security_group_ids: A set of ids of security groups assigned to hosts of the cluster.
        :param pulumi.Input[str] service_account_id: ID of the service account authorized for this cluster.
        """
        pulumi.set(__self__, "config", config)
        pulumi.set(__self__, "environment", environment)
        pulumi.set(__self__, "network_id", network_id)
        if deletion_protection is not None:
            pulumi.set(__self__, "deletion_protection", deletion_protection)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if folder_id is not None:
            pulumi.set(__self__, "folder_id", folder_id)
        if hosts is not None:
            pulumi.set(__self__, "hosts", hosts)
        if labels is not None:
            pulumi.set(__self__, "labels", labels)
        if maintenance_window is not None:
            pulumi.set(__self__, "maintenance_window", maintenance_window)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if security_group_ids is not None:
            pulumi.set(__self__, "security_group_ids", security_group_ids)
        if service_account_id is not None:
            pulumi.set(__self__, "service_account_id", service_account_id)

    @property
    @pulumi.getter
    def config(self) -> pulumi.Input['MdbElasticSearchClusterConfigArgs']:
        """
        Configuration of the Elasticsearch cluster. The structure is documented below.
        """
        return pulumi.get(self, "config")

    @config.setter
    def config(self, value: pulumi.Input['MdbElasticSearchClusterConfigArgs']):
        pulumi.set(self, "config", value)

    @property
    @pulumi.getter
    def environment(self) -> pulumi.Input[str]:
        """
        Deployment environment of the Elasticsearch cluster. Can be either `PRESTABLE` or `PRODUCTION`.
        """
        return pulumi.get(self, "environment")

    @environment.setter
    def environment(self, value: pulumi.Input[str]):
        pulumi.set(self, "environment", value)

    @property
    @pulumi.getter(name="networkId")
    def network_id(self) -> pulumi.Input[str]:
        """
        ID of the network, to which the Elasticsearch cluster belongs.
        """
        return pulumi.get(self, "network_id")

    @network_id.setter
    def network_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "network_id", value)

    @property
    @pulumi.getter(name="deletionProtection")
    def deletion_protection(self) -> Optional[pulumi.Input[bool]]:
        """
        Inhibits deletion of the cluster.  Can be either `true` or `false`.
        """
        return pulumi.get(self, "deletion_protection")

    @deletion_protection.setter
    def deletion_protection(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "deletion_protection", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Description of the Elasticsearch cluster.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="folderId")
    def folder_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the folder that the resource belongs to. If it is not provided, the default provider folder is used.
        """
        return pulumi.get(self, "folder_id")

    @folder_id.setter
    def folder_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "folder_id", value)

    @property
    @pulumi.getter
    def hosts(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['MdbElasticSearchClusterHostArgs']]]]:
        """
        A host of the Elasticsearch cluster. The structure is documented below.
        """
        return pulumi.get(self, "hosts")

    @hosts.setter
    def hosts(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['MdbElasticSearchClusterHostArgs']]]]):
        pulumi.set(self, "hosts", value)

    @property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        A set of key/value label pairs to assign to the Elasticsearch cluster.
        """
        return pulumi.get(self, "labels")

    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "labels", value)

    @property
    @pulumi.getter(name="maintenanceWindow")
    def maintenance_window(self) -> Optional[pulumi.Input['MdbElasticSearchClusterMaintenanceWindowArgs']]:
        return pulumi.get(self, "maintenance_window")

    @maintenance_window.setter
    def maintenance_window(self, value: Optional[pulumi.Input['MdbElasticSearchClusterMaintenanceWindowArgs']]):
        pulumi.set(self, "maintenance_window", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        User defined host name.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        A set of ids of security groups assigned to hosts of the cluster.
        """
        return pulumi.get(self, "security_group_ids")

    @security_group_ids.setter
    def security_group_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "security_group_ids", value)

    @property
    @pulumi.getter(name="serviceAccountId")
    def service_account_id(self) -> Optional[pulumi.Input[str]]:
        """
        ID of the service account authorized for this cluster.
        """
        return pulumi.get(self, "service_account_id")

    @service_account_id.setter
    def service_account_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "service_account_id", value)


@pulumi.input_type
class _MdbElasticSearchClusterState:
    def __init__(__self__, *,
                 config: Optional[pulumi.Input['MdbElasticSearchClusterConfigArgs']] = None,
                 created_at: Optional[pulumi.Input[str]] = None,
                 deletion_protection: Optional[pulumi.Input[bool]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 environment: Optional[pulumi.Input[str]] = None,
                 folder_id: Optional[pulumi.Input[str]] = None,
                 health: Optional[pulumi.Input[str]] = None,
                 hosts: Optional[pulumi.Input[Sequence[pulumi.Input['MdbElasticSearchClusterHostArgs']]]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 maintenance_window: Optional[pulumi.Input['MdbElasticSearchClusterMaintenanceWindowArgs']] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 network_id: Optional[pulumi.Input[str]] = None,
                 security_group_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 service_account_id: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering MdbElasticSearchCluster resources.
        :param pulumi.Input['MdbElasticSearchClusterConfigArgs'] config: Configuration of the Elasticsearch cluster. The structure is documented below.
        :param pulumi.Input[str] created_at: Creation timestamp of the key.
        :param pulumi.Input[bool] deletion_protection: Inhibits deletion of the cluster.  Can be either `true` or `false`.
        :param pulumi.Input[str] description: Description of the Elasticsearch cluster.
        :param pulumi.Input[str] environment: Deployment environment of the Elasticsearch cluster. Can be either `PRESTABLE` or `PRODUCTION`.
        :param pulumi.Input[str] folder_id: The ID of the folder that the resource belongs to. If it is not provided, the default provider folder is used.
        :param pulumi.Input[str] health: Aggregated health of the cluster. Can be either `ALIVE`, `DEGRADED`, `DEAD` or `HEALTH_UNKNOWN`.
               For more information see `health` field of JSON representation in [the official documentation](https://cloud.yandex.com/docs/managed-elasticsearch/api-ref/Cluster/).
        :param pulumi.Input[Sequence[pulumi.Input['MdbElasticSearchClusterHostArgs']]] hosts: A host of the Elasticsearch cluster. The structure is documented below.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] labels: A set of key/value label pairs to assign to the Elasticsearch cluster.
        :param pulumi.Input[str] name: User defined host name.
        :param pulumi.Input[str] network_id: ID of the network, to which the Elasticsearch cluster belongs.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] security_group_ids: A set of ids of security groups assigned to hosts of the cluster.
        :param pulumi.Input[str] service_account_id: ID of the service account authorized for this cluster.
        :param pulumi.Input[str] status: Status of the cluster. Can be either `CREATING`, `STARTING`, `RUNNING`, `UPDATING`, `STOPPING`, `STOPPED`, `ERROR` or `STATUS_UNKNOWN`.
               For more information see `status` field of JSON representation in [the official documentation](https://cloud.yandex.com/docs/managed-elasticsearch/api-ref/Cluster/).
        """
        if config is not None:
            pulumi.set(__self__, "config", config)
        if created_at is not None:
            pulumi.set(__self__, "created_at", created_at)
        if deletion_protection is not None:
            pulumi.set(__self__, "deletion_protection", deletion_protection)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if environment is not None:
            pulumi.set(__self__, "environment", environment)
        if folder_id is not None:
            pulumi.set(__self__, "folder_id", folder_id)
        if health is not None:
            pulumi.set(__self__, "health", health)
        if hosts is not None:
            pulumi.set(__self__, "hosts", hosts)
        if labels is not None:
            pulumi.set(__self__, "labels", labels)
        if maintenance_window is not None:
            pulumi.set(__self__, "maintenance_window", maintenance_window)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if network_id is not None:
            pulumi.set(__self__, "network_id", network_id)
        if security_group_ids is not None:
            pulumi.set(__self__, "security_group_ids", security_group_ids)
        if service_account_id is not None:
            pulumi.set(__self__, "service_account_id", service_account_id)
        if status is not None:
            pulumi.set(__self__, "status", status)

    @property
    @pulumi.getter
    def config(self) -> Optional[pulumi.Input['MdbElasticSearchClusterConfigArgs']]:
        """
        Configuration of the Elasticsearch cluster. The structure is documented below.
        """
        return pulumi.get(self, "config")

    @config.setter
    def config(self, value: Optional[pulumi.Input['MdbElasticSearchClusterConfigArgs']]):
        pulumi.set(self, "config", value)

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[pulumi.Input[str]]:
        """
        Creation timestamp of the key.
        """
        return pulumi.get(self, "created_at")

    @created_at.setter
    def created_at(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "created_at", value)

    @property
    @pulumi.getter(name="deletionProtection")
    def deletion_protection(self) -> Optional[pulumi.Input[bool]]:
        """
        Inhibits deletion of the cluster.  Can be either `true` or `false`.
        """
        return pulumi.get(self, "deletion_protection")

    @deletion_protection.setter
    def deletion_protection(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "deletion_protection", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Description of the Elasticsearch cluster.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def environment(self) -> Optional[pulumi.Input[str]]:
        """
        Deployment environment of the Elasticsearch cluster. Can be either `PRESTABLE` or `PRODUCTION`.
        """
        return pulumi.get(self, "environment")

    @environment.setter
    def environment(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "environment", value)

    @property
    @pulumi.getter(name="folderId")
    def folder_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the folder that the resource belongs to. If it is not provided, the default provider folder is used.
        """
        return pulumi.get(self, "folder_id")

    @folder_id.setter
    def folder_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "folder_id", value)

    @property
    @pulumi.getter
    def health(self) -> Optional[pulumi.Input[str]]:
        """
        Aggregated health of the cluster. Can be either `ALIVE`, `DEGRADED`, `DEAD` or `HEALTH_UNKNOWN`.
        For more information see `health` field of JSON representation in [the official documentation](https://cloud.yandex.com/docs/managed-elasticsearch/api-ref/Cluster/).
        """
        return pulumi.get(self, "health")

    @health.setter
    def health(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "health", value)

    @property
    @pulumi.getter
    def hosts(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['MdbElasticSearchClusterHostArgs']]]]:
        """
        A host of the Elasticsearch cluster. The structure is documented below.
        """
        return pulumi.get(self, "hosts")

    @hosts.setter
    def hosts(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['MdbElasticSearchClusterHostArgs']]]]):
        pulumi.set(self, "hosts", value)

    @property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        A set of key/value label pairs to assign to the Elasticsearch cluster.
        """
        return pulumi.get(self, "labels")

    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "labels", value)

    @property
    @pulumi.getter(name="maintenanceWindow")
    def maintenance_window(self) -> Optional[pulumi.Input['MdbElasticSearchClusterMaintenanceWindowArgs']]:
        return pulumi.get(self, "maintenance_window")

    @maintenance_window.setter
    def maintenance_window(self, value: Optional[pulumi.Input['MdbElasticSearchClusterMaintenanceWindowArgs']]):
        pulumi.set(self, "maintenance_window", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        User defined host name.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="networkId")
    def network_id(self) -> Optional[pulumi.Input[str]]:
        """
        ID of the network, to which the Elasticsearch cluster belongs.
        """
        return pulumi.get(self, "network_id")

    @network_id.setter
    def network_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "network_id", value)

    @property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        A set of ids of security groups assigned to hosts of the cluster.
        """
        return pulumi.get(self, "security_group_ids")

    @security_group_ids.setter
    def security_group_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "security_group_ids", value)

    @property
    @pulumi.getter(name="serviceAccountId")
    def service_account_id(self) -> Optional[pulumi.Input[str]]:
        """
        ID of the service account authorized for this cluster.
        """
        return pulumi.get(self, "service_account_id")

    @service_account_id.setter
    def service_account_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "service_account_id", value)

    @property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[str]]:
        """
        Status of the cluster. Can be either `CREATING`, `STARTING`, `RUNNING`, `UPDATING`, `STOPPING`, `STOPPED`, `ERROR` or `STATUS_UNKNOWN`.
        For more information see `status` field of JSON representation in [the official documentation](https://cloud.yandex.com/docs/managed-elasticsearch/api-ref/Cluster/).
        """
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "status", value)


class MdbElasticSearchCluster(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 config: Optional[pulumi.Input[pulumi.InputType['MdbElasticSearchClusterConfigArgs']]] = None,
                 deletion_protection: Optional[pulumi.Input[bool]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 environment: Optional[pulumi.Input[str]] = None,
                 folder_id: Optional[pulumi.Input[str]] = None,
                 hosts: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['MdbElasticSearchClusterHostArgs']]]]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 maintenance_window: Optional[pulumi.Input[pulumi.InputType['MdbElasticSearchClusterMaintenanceWindowArgs']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 network_id: Optional[pulumi.Input[str]] = None,
                 security_group_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 service_account_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Manages a Elasticsearch cluster within the Yandex.Cloud. For more information, see
        [the official documentation](https://cloud.yandex.com/docs/managed-elasticsearch/concepts).

        ## Import

        A cluster can be imported using the `id` of the resource, e.g.

        ```sh
         $ pulumi import yandex:index/mdbElasticSearchCluster:MdbElasticSearchCluster foo cluster_id
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['MdbElasticSearchClusterConfigArgs']] config: Configuration of the Elasticsearch cluster. The structure is documented below.
        :param pulumi.Input[bool] deletion_protection: Inhibits deletion of the cluster.  Can be either `true` or `false`.
        :param pulumi.Input[str] description: Description of the Elasticsearch cluster.
        :param pulumi.Input[str] environment: Deployment environment of the Elasticsearch cluster. Can be either `PRESTABLE` or `PRODUCTION`.
        :param pulumi.Input[str] folder_id: The ID of the folder that the resource belongs to. If it is not provided, the default provider folder is used.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['MdbElasticSearchClusterHostArgs']]]] hosts: A host of the Elasticsearch cluster. The structure is documented below.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] labels: A set of key/value label pairs to assign to the Elasticsearch cluster.
        :param pulumi.Input[str] name: User defined host name.
        :param pulumi.Input[str] network_id: ID of the network, to which the Elasticsearch cluster belongs.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] security_group_ids: A set of ids of security groups assigned to hosts of the cluster.
        :param pulumi.Input[str] service_account_id: ID of the service account authorized for this cluster.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: MdbElasticSearchClusterArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages a Elasticsearch cluster within the Yandex.Cloud. For more information, see
        [the official documentation](https://cloud.yandex.com/docs/managed-elasticsearch/concepts).

        ## Import

        A cluster can be imported using the `id` of the resource, e.g.

        ```sh
         $ pulumi import yandex:index/mdbElasticSearchCluster:MdbElasticSearchCluster foo cluster_id
        ```

        :param str resource_name: The name of the resource.
        :param MdbElasticSearchClusterArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(MdbElasticSearchClusterArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 config: Optional[pulumi.Input[pulumi.InputType['MdbElasticSearchClusterConfigArgs']]] = None,
                 deletion_protection: Optional[pulumi.Input[bool]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 environment: Optional[pulumi.Input[str]] = None,
                 folder_id: Optional[pulumi.Input[str]] = None,
                 hosts: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['MdbElasticSearchClusterHostArgs']]]]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 maintenance_window: Optional[pulumi.Input[pulumi.InputType['MdbElasticSearchClusterMaintenanceWindowArgs']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 network_id: Optional[pulumi.Input[str]] = None,
                 security_group_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 service_account_id: Optional[pulumi.Input[str]] = None,
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
            __props__ = MdbElasticSearchClusterArgs.__new__(MdbElasticSearchClusterArgs)

            if config is None and not opts.urn:
                raise TypeError("Missing required property 'config'")
            __props__.__dict__["config"] = config
            __props__.__dict__["deletion_protection"] = deletion_protection
            __props__.__dict__["description"] = description
            if environment is None and not opts.urn:
                raise TypeError("Missing required property 'environment'")
            __props__.__dict__["environment"] = environment
            __props__.__dict__["folder_id"] = folder_id
            __props__.__dict__["hosts"] = hosts
            __props__.__dict__["labels"] = labels
            __props__.__dict__["maintenance_window"] = maintenance_window
            __props__.__dict__["name"] = name
            if network_id is None and not opts.urn:
                raise TypeError("Missing required property 'network_id'")
            __props__.__dict__["network_id"] = network_id
            __props__.__dict__["security_group_ids"] = security_group_ids
            __props__.__dict__["service_account_id"] = service_account_id
            __props__.__dict__["created_at"] = None
            __props__.__dict__["health"] = None
            __props__.__dict__["status"] = None
        super(MdbElasticSearchCluster, __self__).__init__(
            'yandex:index/mdbElasticSearchCluster:MdbElasticSearchCluster',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            config: Optional[pulumi.Input[pulumi.InputType['MdbElasticSearchClusterConfigArgs']]] = None,
            created_at: Optional[pulumi.Input[str]] = None,
            deletion_protection: Optional[pulumi.Input[bool]] = None,
            description: Optional[pulumi.Input[str]] = None,
            environment: Optional[pulumi.Input[str]] = None,
            folder_id: Optional[pulumi.Input[str]] = None,
            health: Optional[pulumi.Input[str]] = None,
            hosts: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['MdbElasticSearchClusterHostArgs']]]]] = None,
            labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            maintenance_window: Optional[pulumi.Input[pulumi.InputType['MdbElasticSearchClusterMaintenanceWindowArgs']]] = None,
            name: Optional[pulumi.Input[str]] = None,
            network_id: Optional[pulumi.Input[str]] = None,
            security_group_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            service_account_id: Optional[pulumi.Input[str]] = None,
            status: Optional[pulumi.Input[str]] = None) -> 'MdbElasticSearchCluster':
        """
        Get an existing MdbElasticSearchCluster resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['MdbElasticSearchClusterConfigArgs']] config: Configuration of the Elasticsearch cluster. The structure is documented below.
        :param pulumi.Input[str] created_at: Creation timestamp of the key.
        :param pulumi.Input[bool] deletion_protection: Inhibits deletion of the cluster.  Can be either `true` or `false`.
        :param pulumi.Input[str] description: Description of the Elasticsearch cluster.
        :param pulumi.Input[str] environment: Deployment environment of the Elasticsearch cluster. Can be either `PRESTABLE` or `PRODUCTION`.
        :param pulumi.Input[str] folder_id: The ID of the folder that the resource belongs to. If it is not provided, the default provider folder is used.
        :param pulumi.Input[str] health: Aggregated health of the cluster. Can be either `ALIVE`, `DEGRADED`, `DEAD` or `HEALTH_UNKNOWN`.
               For more information see `health` field of JSON representation in [the official documentation](https://cloud.yandex.com/docs/managed-elasticsearch/api-ref/Cluster/).
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['MdbElasticSearchClusterHostArgs']]]] hosts: A host of the Elasticsearch cluster. The structure is documented below.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] labels: A set of key/value label pairs to assign to the Elasticsearch cluster.
        :param pulumi.Input[str] name: User defined host name.
        :param pulumi.Input[str] network_id: ID of the network, to which the Elasticsearch cluster belongs.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] security_group_ids: A set of ids of security groups assigned to hosts of the cluster.
        :param pulumi.Input[str] service_account_id: ID of the service account authorized for this cluster.
        :param pulumi.Input[str] status: Status of the cluster. Can be either `CREATING`, `STARTING`, `RUNNING`, `UPDATING`, `STOPPING`, `STOPPED`, `ERROR` or `STATUS_UNKNOWN`.
               For more information see `status` field of JSON representation in [the official documentation](https://cloud.yandex.com/docs/managed-elasticsearch/api-ref/Cluster/).
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _MdbElasticSearchClusterState.__new__(_MdbElasticSearchClusterState)

        __props__.__dict__["config"] = config
        __props__.__dict__["created_at"] = created_at
        __props__.__dict__["deletion_protection"] = deletion_protection
        __props__.__dict__["description"] = description
        __props__.__dict__["environment"] = environment
        __props__.__dict__["folder_id"] = folder_id
        __props__.__dict__["health"] = health
        __props__.__dict__["hosts"] = hosts
        __props__.__dict__["labels"] = labels
        __props__.__dict__["maintenance_window"] = maintenance_window
        __props__.__dict__["name"] = name
        __props__.__dict__["network_id"] = network_id
        __props__.__dict__["security_group_ids"] = security_group_ids
        __props__.__dict__["service_account_id"] = service_account_id
        __props__.__dict__["status"] = status
        return MdbElasticSearchCluster(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def config(self) -> pulumi.Output['outputs.MdbElasticSearchClusterConfig']:
        """
        Configuration of the Elasticsearch cluster. The structure is documented below.
        """
        return pulumi.get(self, "config")

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> pulumi.Output[str]:
        """
        Creation timestamp of the key.
        """
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter(name="deletionProtection")
    def deletion_protection(self) -> pulumi.Output[bool]:
        """
        Inhibits deletion of the cluster.  Can be either `true` or `false`.
        """
        return pulumi.get(self, "deletion_protection")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        Description of the Elasticsearch cluster.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def environment(self) -> pulumi.Output[str]:
        """
        Deployment environment of the Elasticsearch cluster. Can be either `PRESTABLE` or `PRODUCTION`.
        """
        return pulumi.get(self, "environment")

    @property
    @pulumi.getter(name="folderId")
    def folder_id(self) -> pulumi.Output[str]:
        """
        The ID of the folder that the resource belongs to. If it is not provided, the default provider folder is used.
        """
        return pulumi.get(self, "folder_id")

    @property
    @pulumi.getter
    def health(self) -> pulumi.Output[str]:
        """
        Aggregated health of the cluster. Can be either `ALIVE`, `DEGRADED`, `DEAD` or `HEALTH_UNKNOWN`.
        For more information see `health` field of JSON representation in [the official documentation](https://cloud.yandex.com/docs/managed-elasticsearch/api-ref/Cluster/).
        """
        return pulumi.get(self, "health")

    @property
    @pulumi.getter
    def hosts(self) -> pulumi.Output[Sequence['outputs.MdbElasticSearchClusterHost']]:
        """
        A host of the Elasticsearch cluster. The structure is documented below.
        """
        return pulumi.get(self, "hosts")

    @property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        A set of key/value label pairs to assign to the Elasticsearch cluster.
        """
        return pulumi.get(self, "labels")

    @property
    @pulumi.getter(name="maintenanceWindow")
    def maintenance_window(self) -> pulumi.Output['outputs.MdbElasticSearchClusterMaintenanceWindow']:
        return pulumi.get(self, "maintenance_window")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        User defined host name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="networkId")
    def network_id(self) -> pulumi.Output[str]:
        """
        ID of the network, to which the Elasticsearch cluster belongs.
        """
        return pulumi.get(self, "network_id")

    @property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        A set of ids of security groups assigned to hosts of the cluster.
        """
        return pulumi.get(self, "security_group_ids")

    @property
    @pulumi.getter(name="serviceAccountId")
    def service_account_id(self) -> pulumi.Output[Optional[str]]:
        """
        ID of the service account authorized for this cluster.
        """
        return pulumi.get(self, "service_account_id")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[str]:
        """
        Status of the cluster. Can be either `CREATING`, `STARTING`, `RUNNING`, `UPDATING`, `STOPPING`, `STOPPED`, `ERROR` or `STATUS_UNKNOWN`.
        For more information see `status` field of JSON representation in [the official documentation](https://cloud.yandex.com/docs/managed-elasticsearch/api-ref/Cluster/).
        """
        return pulumi.get(self, "status")


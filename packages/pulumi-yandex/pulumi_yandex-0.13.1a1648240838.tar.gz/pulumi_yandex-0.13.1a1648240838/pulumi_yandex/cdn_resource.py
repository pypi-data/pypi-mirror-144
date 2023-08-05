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

__all__ = ['CdnResourceArgs', 'CdnResource']

@pulumi.input_type
class CdnResourceArgs:
    def __init__(__self__, *,
                 active: Optional[pulumi.Input[bool]] = None,
                 cname: Optional[pulumi.Input[str]] = None,
                 options: Optional[pulumi.Input['CdnResourceOptionsArgs']] = None,
                 origin_group_id: Optional[pulumi.Input[int]] = None,
                 origin_group_name: Optional[pulumi.Input[str]] = None,
                 origin_protocol: Optional[pulumi.Input[str]] = None,
                 secondary_hostnames: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 ssl_certificate: Optional[pulumi.Input['CdnResourceSslCertificateArgs']] = None,
                 updated_at: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a CdnResource resource.
        :param pulumi.Input[bool] active: Flag to create Resource either in active or disabled state. True - the content from CDN is available to clients.
        :param pulumi.Input[str] cname: CDN endpoint CNAME, must be unique among resources.
        :param pulumi.Input['CdnResourceOptionsArgs'] options: CDN Resource settings and options to tune CDN edge behavior.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] secondary_hostnames: list of secondary hostname strings.
        """
        if active is not None:
            pulumi.set(__self__, "active", active)
        if cname is not None:
            pulumi.set(__self__, "cname", cname)
        if options is not None:
            pulumi.set(__self__, "options", options)
        if origin_group_id is not None:
            pulumi.set(__self__, "origin_group_id", origin_group_id)
        if origin_group_name is not None:
            pulumi.set(__self__, "origin_group_name", origin_group_name)
        if origin_protocol is not None:
            pulumi.set(__self__, "origin_protocol", origin_protocol)
        if secondary_hostnames is not None:
            pulumi.set(__self__, "secondary_hostnames", secondary_hostnames)
        if ssl_certificate is not None:
            pulumi.set(__self__, "ssl_certificate", ssl_certificate)
        if updated_at is not None:
            pulumi.set(__self__, "updated_at", updated_at)

    @property
    @pulumi.getter
    def active(self) -> Optional[pulumi.Input[bool]]:
        """
        Flag to create Resource either in active or disabled state. True - the content from CDN is available to clients.
        """
        return pulumi.get(self, "active")

    @active.setter
    def active(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "active", value)

    @property
    @pulumi.getter
    def cname(self) -> Optional[pulumi.Input[str]]:
        """
        CDN endpoint CNAME, must be unique among resources.
        """
        return pulumi.get(self, "cname")

    @cname.setter
    def cname(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cname", value)

    @property
    @pulumi.getter
    def options(self) -> Optional[pulumi.Input['CdnResourceOptionsArgs']]:
        """
        CDN Resource settings and options to tune CDN edge behavior.
        """
        return pulumi.get(self, "options")

    @options.setter
    def options(self, value: Optional[pulumi.Input['CdnResourceOptionsArgs']]):
        pulumi.set(self, "options", value)

    @property
    @pulumi.getter(name="originGroupId")
    def origin_group_id(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "origin_group_id")

    @origin_group_id.setter
    def origin_group_id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "origin_group_id", value)

    @property
    @pulumi.getter(name="originGroupName")
    def origin_group_name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "origin_group_name")

    @origin_group_name.setter
    def origin_group_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "origin_group_name", value)

    @property
    @pulumi.getter(name="originProtocol")
    def origin_protocol(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "origin_protocol")

    @origin_protocol.setter
    def origin_protocol(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "origin_protocol", value)

    @property
    @pulumi.getter(name="secondaryHostnames")
    def secondary_hostnames(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        list of secondary hostname strings.
        """
        return pulumi.get(self, "secondary_hostnames")

    @secondary_hostnames.setter
    def secondary_hostnames(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "secondary_hostnames", value)

    @property
    @pulumi.getter(name="sslCertificate")
    def ssl_certificate(self) -> Optional[pulumi.Input['CdnResourceSslCertificateArgs']]:
        return pulumi.get(self, "ssl_certificate")

    @ssl_certificate.setter
    def ssl_certificate(self, value: Optional[pulumi.Input['CdnResourceSslCertificateArgs']]):
        pulumi.set(self, "ssl_certificate", value)

    @property
    @pulumi.getter(name="updatedAt")
    def updated_at(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "updated_at")

    @updated_at.setter
    def updated_at(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "updated_at", value)


@pulumi.input_type
class _CdnResourceState:
    def __init__(__self__, *,
                 active: Optional[pulumi.Input[bool]] = None,
                 cname: Optional[pulumi.Input[str]] = None,
                 created_at: Optional[pulumi.Input[str]] = None,
                 folder_id: Optional[pulumi.Input[str]] = None,
                 options: Optional[pulumi.Input['CdnResourceOptionsArgs']] = None,
                 origin_group_id: Optional[pulumi.Input[int]] = None,
                 origin_group_name: Optional[pulumi.Input[str]] = None,
                 origin_protocol: Optional[pulumi.Input[str]] = None,
                 secondary_hostnames: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 ssl_certificate: Optional[pulumi.Input['CdnResourceSslCertificateArgs']] = None,
                 updated_at: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering CdnResource resources.
        :param pulumi.Input[bool] active: Flag to create Resource either in active or disabled state. True - the content from CDN is available to clients.
        :param pulumi.Input[str] cname: CDN endpoint CNAME, must be unique among resources.
        :param pulumi.Input[str] created_at: Creation timestamp of the IoT Core Device
        :param pulumi.Input['CdnResourceOptionsArgs'] options: CDN Resource settings and options to tune CDN edge behavior.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] secondary_hostnames: list of secondary hostname strings.
        """
        if active is not None:
            pulumi.set(__self__, "active", active)
        if cname is not None:
            pulumi.set(__self__, "cname", cname)
        if created_at is not None:
            pulumi.set(__self__, "created_at", created_at)
        if folder_id is not None:
            pulumi.set(__self__, "folder_id", folder_id)
        if options is not None:
            pulumi.set(__self__, "options", options)
        if origin_group_id is not None:
            pulumi.set(__self__, "origin_group_id", origin_group_id)
        if origin_group_name is not None:
            pulumi.set(__self__, "origin_group_name", origin_group_name)
        if origin_protocol is not None:
            pulumi.set(__self__, "origin_protocol", origin_protocol)
        if secondary_hostnames is not None:
            pulumi.set(__self__, "secondary_hostnames", secondary_hostnames)
        if ssl_certificate is not None:
            pulumi.set(__self__, "ssl_certificate", ssl_certificate)
        if updated_at is not None:
            pulumi.set(__self__, "updated_at", updated_at)

    @property
    @pulumi.getter
    def active(self) -> Optional[pulumi.Input[bool]]:
        """
        Flag to create Resource either in active or disabled state. True - the content from CDN is available to clients.
        """
        return pulumi.get(self, "active")

    @active.setter
    def active(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "active", value)

    @property
    @pulumi.getter
    def cname(self) -> Optional[pulumi.Input[str]]:
        """
        CDN endpoint CNAME, must be unique among resources.
        """
        return pulumi.get(self, "cname")

    @cname.setter
    def cname(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cname", value)

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[pulumi.Input[str]]:
        """
        Creation timestamp of the IoT Core Device
        """
        return pulumi.get(self, "created_at")

    @created_at.setter
    def created_at(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "created_at", value)

    @property
    @pulumi.getter(name="folderId")
    def folder_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "folder_id")

    @folder_id.setter
    def folder_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "folder_id", value)

    @property
    @pulumi.getter
    def options(self) -> Optional[pulumi.Input['CdnResourceOptionsArgs']]:
        """
        CDN Resource settings and options to tune CDN edge behavior.
        """
        return pulumi.get(self, "options")

    @options.setter
    def options(self, value: Optional[pulumi.Input['CdnResourceOptionsArgs']]):
        pulumi.set(self, "options", value)

    @property
    @pulumi.getter(name="originGroupId")
    def origin_group_id(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "origin_group_id")

    @origin_group_id.setter
    def origin_group_id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "origin_group_id", value)

    @property
    @pulumi.getter(name="originGroupName")
    def origin_group_name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "origin_group_name")

    @origin_group_name.setter
    def origin_group_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "origin_group_name", value)

    @property
    @pulumi.getter(name="originProtocol")
    def origin_protocol(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "origin_protocol")

    @origin_protocol.setter
    def origin_protocol(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "origin_protocol", value)

    @property
    @pulumi.getter(name="secondaryHostnames")
    def secondary_hostnames(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        list of secondary hostname strings.
        """
        return pulumi.get(self, "secondary_hostnames")

    @secondary_hostnames.setter
    def secondary_hostnames(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "secondary_hostnames", value)

    @property
    @pulumi.getter(name="sslCertificate")
    def ssl_certificate(self) -> Optional[pulumi.Input['CdnResourceSslCertificateArgs']]:
        return pulumi.get(self, "ssl_certificate")

    @ssl_certificate.setter
    def ssl_certificate(self, value: Optional[pulumi.Input['CdnResourceSslCertificateArgs']]):
        pulumi.set(self, "ssl_certificate", value)

    @property
    @pulumi.getter(name="updatedAt")
    def updated_at(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "updated_at")

    @updated_at.setter
    def updated_at(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "updated_at", value)


class CdnResource(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 active: Optional[pulumi.Input[bool]] = None,
                 cname: Optional[pulumi.Input[str]] = None,
                 options: Optional[pulumi.Input[pulumi.InputType['CdnResourceOptionsArgs']]] = None,
                 origin_group_id: Optional[pulumi.Input[int]] = None,
                 origin_group_name: Optional[pulumi.Input[str]] = None,
                 origin_protocol: Optional[pulumi.Input[str]] = None,
                 secondary_hostnames: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 ssl_certificate: Optional[pulumi.Input[pulumi.InputType['CdnResourceSslCertificateArgs']]] = None,
                 updated_at: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Allows management of [Yandex.Cloud CDN Resource](https://cloud.yandex.ru/docs/cdn/concepts/resource).

        > **_NOTE:_**  CDN provider must be activated prior usage of CDN resources, either via UI console or via yc cli command: ```yc cdn provider activate --folder-id <folder-id> --type gcore```

        ## Example Usage

        ```python
        import pulumi
        import pulumi_yandex as yandex

        my_resource = yandex.CdnResource("myResource",
            cname="cdn1.yandex-example.ru",
            active=False,
            origin_protocol="https",
            secondary_hostnames=[
                "cdn-example-1.yandex.ru",
                "cdn-example-2.yandex.ru",
            ],
            origin_group_id=yandex_cdn_origin_group["foo_cdn_group_by_id"]["id"],
            options=yandex.CdnResourceOptionsArgs(
                edge_cache_settings=345600,
                ignore_cookie=True,
            ))
        ```

        ## Import

        A origin group can be imported using any of these accepted formats

        ```sh
         $ pulumi import yandex:index/cdnResource:CdnResource default origin_group_id
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] active: Flag to create Resource either in active or disabled state. True - the content from CDN is available to clients.
        :param pulumi.Input[str] cname: CDN endpoint CNAME, must be unique among resources.
        :param pulumi.Input[pulumi.InputType['CdnResourceOptionsArgs']] options: CDN Resource settings and options to tune CDN edge behavior.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] secondary_hostnames: list of secondary hostname strings.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[CdnResourceArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Allows management of [Yandex.Cloud CDN Resource](https://cloud.yandex.ru/docs/cdn/concepts/resource).

        > **_NOTE:_**  CDN provider must be activated prior usage of CDN resources, either via UI console or via yc cli command: ```yc cdn provider activate --folder-id <folder-id> --type gcore```

        ## Example Usage

        ```python
        import pulumi
        import pulumi_yandex as yandex

        my_resource = yandex.CdnResource("myResource",
            cname="cdn1.yandex-example.ru",
            active=False,
            origin_protocol="https",
            secondary_hostnames=[
                "cdn-example-1.yandex.ru",
                "cdn-example-2.yandex.ru",
            ],
            origin_group_id=yandex_cdn_origin_group["foo_cdn_group_by_id"]["id"],
            options=yandex.CdnResourceOptionsArgs(
                edge_cache_settings=345600,
                ignore_cookie=True,
            ))
        ```

        ## Import

        A origin group can be imported using any of these accepted formats

        ```sh
         $ pulumi import yandex:index/cdnResource:CdnResource default origin_group_id
        ```

        :param str resource_name: The name of the resource.
        :param CdnResourceArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(CdnResourceArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 active: Optional[pulumi.Input[bool]] = None,
                 cname: Optional[pulumi.Input[str]] = None,
                 options: Optional[pulumi.Input[pulumi.InputType['CdnResourceOptionsArgs']]] = None,
                 origin_group_id: Optional[pulumi.Input[int]] = None,
                 origin_group_name: Optional[pulumi.Input[str]] = None,
                 origin_protocol: Optional[pulumi.Input[str]] = None,
                 secondary_hostnames: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 ssl_certificate: Optional[pulumi.Input[pulumi.InputType['CdnResourceSslCertificateArgs']]] = None,
                 updated_at: Optional[pulumi.Input[str]] = None,
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
            __props__ = CdnResourceArgs.__new__(CdnResourceArgs)

            __props__.__dict__["active"] = active
            __props__.__dict__["cname"] = cname
            __props__.__dict__["options"] = options
            __props__.__dict__["origin_group_id"] = origin_group_id
            __props__.__dict__["origin_group_name"] = origin_group_name
            __props__.__dict__["origin_protocol"] = origin_protocol
            __props__.__dict__["secondary_hostnames"] = secondary_hostnames
            __props__.__dict__["ssl_certificate"] = ssl_certificate
            __props__.__dict__["updated_at"] = updated_at
            __props__.__dict__["created_at"] = None
            __props__.__dict__["folder_id"] = None
        super(CdnResource, __self__).__init__(
            'yandex:index/cdnResource:CdnResource',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            active: Optional[pulumi.Input[bool]] = None,
            cname: Optional[pulumi.Input[str]] = None,
            created_at: Optional[pulumi.Input[str]] = None,
            folder_id: Optional[pulumi.Input[str]] = None,
            options: Optional[pulumi.Input[pulumi.InputType['CdnResourceOptionsArgs']]] = None,
            origin_group_id: Optional[pulumi.Input[int]] = None,
            origin_group_name: Optional[pulumi.Input[str]] = None,
            origin_protocol: Optional[pulumi.Input[str]] = None,
            secondary_hostnames: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            ssl_certificate: Optional[pulumi.Input[pulumi.InputType['CdnResourceSslCertificateArgs']]] = None,
            updated_at: Optional[pulumi.Input[str]] = None) -> 'CdnResource':
        """
        Get an existing CdnResource resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] active: Flag to create Resource either in active or disabled state. True - the content from CDN is available to clients.
        :param pulumi.Input[str] cname: CDN endpoint CNAME, must be unique among resources.
        :param pulumi.Input[str] created_at: Creation timestamp of the IoT Core Device
        :param pulumi.Input[pulumi.InputType['CdnResourceOptionsArgs']] options: CDN Resource settings and options to tune CDN edge behavior.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] secondary_hostnames: list of secondary hostname strings.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _CdnResourceState.__new__(_CdnResourceState)

        __props__.__dict__["active"] = active
        __props__.__dict__["cname"] = cname
        __props__.__dict__["created_at"] = created_at
        __props__.__dict__["folder_id"] = folder_id
        __props__.__dict__["options"] = options
        __props__.__dict__["origin_group_id"] = origin_group_id
        __props__.__dict__["origin_group_name"] = origin_group_name
        __props__.__dict__["origin_protocol"] = origin_protocol
        __props__.__dict__["secondary_hostnames"] = secondary_hostnames
        __props__.__dict__["ssl_certificate"] = ssl_certificate
        __props__.__dict__["updated_at"] = updated_at
        return CdnResource(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def active(self) -> pulumi.Output[Optional[bool]]:
        """
        Flag to create Resource either in active or disabled state. True - the content from CDN is available to clients.
        """
        return pulumi.get(self, "active")

    @property
    @pulumi.getter
    def cname(self) -> pulumi.Output[str]:
        """
        CDN endpoint CNAME, must be unique among resources.
        """
        return pulumi.get(self, "cname")

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> pulumi.Output[str]:
        """
        Creation timestamp of the IoT Core Device
        """
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter(name="folderId")
    def folder_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "folder_id")

    @property
    @pulumi.getter
    def options(self) -> pulumi.Output['outputs.CdnResourceOptions']:
        """
        CDN Resource settings and options to tune CDN edge behavior.
        """
        return pulumi.get(self, "options")

    @property
    @pulumi.getter(name="originGroupId")
    def origin_group_id(self) -> pulumi.Output[Optional[int]]:
        return pulumi.get(self, "origin_group_id")

    @property
    @pulumi.getter(name="originGroupName")
    def origin_group_name(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "origin_group_name")

    @property
    @pulumi.getter(name="originProtocol")
    def origin_protocol(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "origin_protocol")

    @property
    @pulumi.getter(name="secondaryHostnames")
    def secondary_hostnames(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        list of secondary hostname strings.
        """
        return pulumi.get(self, "secondary_hostnames")

    @property
    @pulumi.getter(name="sslCertificate")
    def ssl_certificate(self) -> pulumi.Output[Optional['outputs.CdnResourceSslCertificate']]:
        return pulumi.get(self, "ssl_certificate")

    @property
    @pulumi.getter(name="updatedAt")
    def updated_at(self) -> pulumi.Output[str]:
        return pulumi.get(self, "updated_at")


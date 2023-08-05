# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = [
    'GetResourcemanagerFolderResult',
    'AwaitableGetResourcemanagerFolderResult',
    'get_resourcemanager_folder',
    'get_resourcemanager_folder_output',
]

@pulumi.output_type
class GetResourcemanagerFolderResult:
    """
    A collection of values returned by getResourcemanagerFolder.
    """
    def __init__(__self__, cloud_id=None, created_at=None, description=None, folder_id=None, id=None, labels=None, name=None, status=None):
        if cloud_id and not isinstance(cloud_id, str):
            raise TypeError("Expected argument 'cloud_id' to be a str")
        pulumi.set(__self__, "cloud_id", cloud_id)
        if created_at and not isinstance(created_at, str):
            raise TypeError("Expected argument 'created_at' to be a str")
        pulumi.set(__self__, "created_at", created_at)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if folder_id and not isinstance(folder_id, str):
            raise TypeError("Expected argument 'folder_id' to be a str")
        pulumi.set(__self__, "folder_id", folder_id)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if labels and not isinstance(labels, dict):
            raise TypeError("Expected argument 'labels' to be a dict")
        pulumi.set(__self__, "labels", labels)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)

    @property
    @pulumi.getter(name="cloudId")
    def cloud_id(self) -> str:
        """
        ID of the cloud that contains the folder.
        """
        return pulumi.get(self, "cloud_id")

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> str:
        """
        Folder creation timestamp.
        """
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        Description of the folder.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="folderId")
    def folder_id(self) -> str:
        return pulumi.get(self, "folder_id")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def labels(self) -> Optional[Mapping[str, str]]:
        """
        A map of labels applied to this folder.
        """
        return pulumi.get(self, "labels")

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def status(self) -> str:
        """
        Current status of the folder.
        """
        return pulumi.get(self, "status")


class AwaitableGetResourcemanagerFolderResult(GetResourcemanagerFolderResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetResourcemanagerFolderResult(
            cloud_id=self.cloud_id,
            created_at=self.created_at,
            description=self.description,
            folder_id=self.folder_id,
            id=self.id,
            labels=self.labels,
            name=self.name,
            status=self.status)


def get_resourcemanager_folder(cloud_id: Optional[str] = None,
                               folder_id: Optional[str] = None,
                               labels: Optional[Mapping[str, str]] = None,
                               name: Optional[str] = None,
                               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetResourcemanagerFolderResult:
    """
    Use this data source to get information about a Yandex Resource Manager Folder. For more information, see
    [the official documentation](https://cloud.yandex.com/docs/resource-manager/concepts/resources-hierarchy#folder).

    ```python
    import pulumi
    import pulumi_yandex as yandex

    my_folder1 = yandex.get_resourcemanager_folder(folder_id="folder_id_number_1")
    my_folder2 = yandex.get_resourcemanager_folder(cloud_id="some_cloud_id",
        name="folder_name")
    pulumi.export("myFolder1Name", my_folder1.name)
    pulumi.export("myFolder2CloudId", my_folder2.cloud_id)
    ```


    :param str cloud_id: Cloud that the resource belongs to. If value is omitted, the default provider cloud is used.
    :param str folder_id: ID of the folder.
    :param Mapping[str, str] labels: A map of labels applied to this folder.
    :param str name: Name of the folder.
    """
    __args__ = dict()
    __args__['cloudId'] = cloud_id
    __args__['folderId'] = folder_id
    __args__['labels'] = labels
    __args__['name'] = name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('yandex:index/getResourcemanagerFolder:getResourcemanagerFolder', __args__, opts=opts, typ=GetResourcemanagerFolderResult).value

    return AwaitableGetResourcemanagerFolderResult(
        cloud_id=__ret__.cloud_id,
        created_at=__ret__.created_at,
        description=__ret__.description,
        folder_id=__ret__.folder_id,
        id=__ret__.id,
        labels=__ret__.labels,
        name=__ret__.name,
        status=__ret__.status)


@_utilities.lift_output_func(get_resourcemanager_folder)
def get_resourcemanager_folder_output(cloud_id: Optional[pulumi.Input[Optional[str]]] = None,
                                      folder_id: Optional[pulumi.Input[Optional[str]]] = None,
                                      labels: Optional[pulumi.Input[Optional[Mapping[str, str]]]] = None,
                                      name: Optional[pulumi.Input[Optional[str]]] = None,
                                      opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetResourcemanagerFolderResult]:
    """
    Use this data source to get information about a Yandex Resource Manager Folder. For more information, see
    [the official documentation](https://cloud.yandex.com/docs/resource-manager/concepts/resources-hierarchy#folder).

    ```python
    import pulumi
    import pulumi_yandex as yandex

    my_folder1 = yandex.get_resourcemanager_folder(folder_id="folder_id_number_1")
    my_folder2 = yandex.get_resourcemanager_folder(cloud_id="some_cloud_id",
        name="folder_name")
    pulumi.export("myFolder1Name", my_folder1.name)
    pulumi.export("myFolder2CloudId", my_folder2.cloud_id)
    ```


    :param str cloud_id: Cloud that the resource belongs to. If value is omitted, the default provider cloud is used.
    :param str folder_id: ID of the folder.
    :param Mapping[str, str] labels: A map of labels applied to this folder.
    :param str name: Name of the folder.
    """
    ...

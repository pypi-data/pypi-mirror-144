# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = [
    'GetComputeImageResult',
    'AwaitableGetComputeImageResult',
    'get_compute_image',
    'get_compute_image_output',
]

@pulumi.output_type
class GetComputeImageResult:
    """
    A collection of values returned by getComputeImage.
    """
    def __init__(__self__, created_at=None, description=None, family=None, folder_id=None, id=None, image_id=None, labels=None, min_disk_size=None, name=None, os_type=None, pooled=None, product_ids=None, size=None, status=None):
        if created_at and not isinstance(created_at, str):
            raise TypeError("Expected argument 'created_at' to be a str")
        pulumi.set(__self__, "created_at", created_at)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if family and not isinstance(family, str):
            raise TypeError("Expected argument 'family' to be a str")
        pulumi.set(__self__, "family", family)
        if folder_id and not isinstance(folder_id, str):
            raise TypeError("Expected argument 'folder_id' to be a str")
        pulumi.set(__self__, "folder_id", folder_id)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if image_id and not isinstance(image_id, str):
            raise TypeError("Expected argument 'image_id' to be a str")
        pulumi.set(__self__, "image_id", image_id)
        if labels and not isinstance(labels, dict):
            raise TypeError("Expected argument 'labels' to be a dict")
        pulumi.set(__self__, "labels", labels)
        if min_disk_size and not isinstance(min_disk_size, int):
            raise TypeError("Expected argument 'min_disk_size' to be a int")
        pulumi.set(__self__, "min_disk_size", min_disk_size)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if os_type and not isinstance(os_type, str):
            raise TypeError("Expected argument 'os_type' to be a str")
        pulumi.set(__self__, "os_type", os_type)
        if pooled and not isinstance(pooled, bool):
            raise TypeError("Expected argument 'pooled' to be a bool")
        pulumi.set(__self__, "pooled", pooled)
        if product_ids and not isinstance(product_ids, list):
            raise TypeError("Expected argument 'product_ids' to be a list")
        pulumi.set(__self__, "product_ids", product_ids)
        if size and not isinstance(size, int):
            raise TypeError("Expected argument 'size' to be a int")
        pulumi.set(__self__, "size", size)
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> str:
        """
        Image creation timestamp.
        """
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        An optional description of this image.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def family(self) -> str:
        """
        The OS family name of the image.
        """
        return pulumi.get(self, "family")

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
    @pulumi.getter(name="imageId")
    def image_id(self) -> str:
        return pulumi.get(self, "image_id")

    @property
    @pulumi.getter
    def labels(self) -> Mapping[str, str]:
        """
        A map of labels applied to this image.
        """
        return pulumi.get(self, "labels")

    @property
    @pulumi.getter(name="minDiskSize")
    def min_disk_size(self) -> int:
        """
        Minimum size of the disk which is created from this image.
        """
        return pulumi.get(self, "min_disk_size")

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="osType")
    def os_type(self) -> str:
        """
        Operating system type that the image contains.
        """
        return pulumi.get(self, "os_type")

    @property
    @pulumi.getter
    def pooled(self) -> bool:
        """
        Optimize the image to create a disk.
        """
        return pulumi.get(self, "pooled")

    @property
    @pulumi.getter(name="productIds")
    def product_ids(self) -> Sequence[str]:
        """
        License IDs that indicate which licenses are attached to this image.
        """
        return pulumi.get(self, "product_ids")

    @property
    @pulumi.getter
    def size(self) -> int:
        """
        The size of the image, specified in Gb.
        """
        return pulumi.get(self, "size")

    @property
    @pulumi.getter
    def status(self) -> str:
        """
        The status of the image.
        """
        return pulumi.get(self, "status")


class AwaitableGetComputeImageResult(GetComputeImageResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetComputeImageResult(
            created_at=self.created_at,
            description=self.description,
            family=self.family,
            folder_id=self.folder_id,
            id=self.id,
            image_id=self.image_id,
            labels=self.labels,
            min_disk_size=self.min_disk_size,
            name=self.name,
            os_type=self.os_type,
            pooled=self.pooled,
            product_ids=self.product_ids,
            size=self.size,
            status=self.status)


def get_compute_image(family: Optional[str] = None,
                      folder_id: Optional[str] = None,
                      image_id: Optional[str] = None,
                      name: Optional[str] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetComputeImageResult:
    """
    Use this data source to access information about an existing resource.

    :param str family: The family name of an image. Used to search the latest image in a family.
    :param str folder_id: Folder that the resource belongs to. If value is omitted, the default provider folder is used.
    :param str image_id: The ID of a specific image.
    :param str name: The name of the image.
    """
    __args__ = dict()
    __args__['family'] = family
    __args__['folderId'] = folder_id
    __args__['imageId'] = image_id
    __args__['name'] = name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('yandex:index/getComputeImage:getComputeImage', __args__, opts=opts, typ=GetComputeImageResult).value

    return AwaitableGetComputeImageResult(
        created_at=__ret__.created_at,
        description=__ret__.description,
        family=__ret__.family,
        folder_id=__ret__.folder_id,
        id=__ret__.id,
        image_id=__ret__.image_id,
        labels=__ret__.labels,
        min_disk_size=__ret__.min_disk_size,
        name=__ret__.name,
        os_type=__ret__.os_type,
        pooled=__ret__.pooled,
        product_ids=__ret__.product_ids,
        size=__ret__.size,
        status=__ret__.status)


@_utilities.lift_output_func(get_compute_image)
def get_compute_image_output(family: Optional[pulumi.Input[Optional[str]]] = None,
                             folder_id: Optional[pulumi.Input[Optional[str]]] = None,
                             image_id: Optional[pulumi.Input[Optional[str]]] = None,
                             name: Optional[pulumi.Input[Optional[str]]] = None,
                             opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetComputeImageResult]:
    """
    Use this data source to access information about an existing resource.

    :param str family: The family name of an image. Used to search the latest image in a family.
    :param str folder_id: Folder that the resource belongs to. If value is omitted, the default provider folder is used.
    :param str image_id: The ID of a specific image.
    :param str name: The name of the image.
    """
    ...

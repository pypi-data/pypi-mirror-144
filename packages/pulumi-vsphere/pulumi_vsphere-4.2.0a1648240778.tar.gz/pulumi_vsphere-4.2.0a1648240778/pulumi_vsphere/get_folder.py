# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = [
    'GetFolderResult',
    'AwaitableGetFolderResult',
    'get_folder',
    'get_folder_output',
]

@pulumi.output_type
class GetFolderResult:
    """
    A collection of values returned by getFolder.
    """
    def __init__(__self__, id=None, path=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if path and not isinstance(path, str):
            raise TypeError("Expected argument 'path' to be a str")
        pulumi.set(__self__, "path", path)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def path(self) -> str:
        return pulumi.get(self, "path")


class AwaitableGetFolderResult(GetFolderResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetFolderResult(
            id=self.id,
            path=self.path)


def get_folder(path: Optional[str] = None,
               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetFolderResult:
    """
    The `Folder` data source can be used to get the general attributes of a
    vSphere inventory folder. Paths are absolute and include must include the
    datacenter.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_vsphere as vsphere

    folder = vsphere.get_folder(path="/dc1/datastore/folder1")
    ```


    :param str path: The absolute path of the folder. For example, given a
           default datacenter of `default-dc`, a folder of type `vm`, and a folder name
           of `test-folder`, the resulting path would be
           `/default-dc/vm/test-folder`. The valid folder types to be used in
           the path are: `vm`, `host`, `datacenter`, `datastore`, or `network`.
    """
    __args__ = dict()
    __args__['path'] = path
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('vsphere:index/getFolder:getFolder', __args__, opts=opts, typ=GetFolderResult).value

    return AwaitableGetFolderResult(
        id=__ret__.id,
        path=__ret__.path)


@_utilities.lift_output_func(get_folder)
def get_folder_output(path: Optional[pulumi.Input[str]] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetFolderResult]:
    """
    The `Folder` data source can be used to get the general attributes of a
    vSphere inventory folder. Paths are absolute and include must include the
    datacenter.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_vsphere as vsphere

    folder = vsphere.get_folder(path="/dc1/datastore/folder1")
    ```


    :param str path: The absolute path of the folder. For example, given a
           default datacenter of `default-dc`, a folder of type `vm`, and a folder name
           of `test-folder`, the resulting path would be
           `/default-dc/vm/test-folder`. The valid folder types to be used in
           the path are: `vm`, `host`, `datacenter`, `datastore`, or `network`.
    """
    ...

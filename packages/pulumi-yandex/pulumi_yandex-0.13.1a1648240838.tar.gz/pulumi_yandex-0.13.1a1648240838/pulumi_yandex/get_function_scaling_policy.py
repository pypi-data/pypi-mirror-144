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

__all__ = [
    'GetFunctionScalingPolicyResult',
    'AwaitableGetFunctionScalingPolicyResult',
    'get_function_scaling_policy',
    'get_function_scaling_policy_output',
]

@pulumi.output_type
class GetFunctionScalingPolicyResult:
    """
    A collection of values returned by getFunctionScalingPolicy.
    """
    def __init__(__self__, function_id=None, id=None, policies=None):
        if function_id and not isinstance(function_id, str):
            raise TypeError("Expected argument 'function_id' to be a str")
        pulumi.set(__self__, "function_id", function_id)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if policies and not isinstance(policies, list):
            raise TypeError("Expected argument 'policies' to be a list")
        pulumi.set(__self__, "policies", policies)

    @property
    @pulumi.getter(name="functionId")
    def function_id(self) -> str:
        return pulumi.get(self, "function_id")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def policies(self) -> Sequence['outputs.GetFunctionScalingPolicyPolicyResult']:
        return pulumi.get(self, "policies")


class AwaitableGetFunctionScalingPolicyResult(GetFunctionScalingPolicyResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetFunctionScalingPolicyResult(
            function_id=self.function_id,
            id=self.id,
            policies=self.policies)


def get_function_scaling_policy(function_id: Optional[str] = None,
                                policies: Optional[Sequence[pulumi.InputType['GetFunctionScalingPolicyPolicyArgs']]] = None,
                                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetFunctionScalingPolicyResult:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['functionId'] = function_id
    __args__['policies'] = policies
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('yandex:index/getFunctionScalingPolicy:getFunctionScalingPolicy', __args__, opts=opts, typ=GetFunctionScalingPolicyResult).value

    return AwaitableGetFunctionScalingPolicyResult(
        function_id=__ret__.function_id,
        id=__ret__.id,
        policies=__ret__.policies)


@_utilities.lift_output_func(get_function_scaling_policy)
def get_function_scaling_policy_output(function_id: Optional[pulumi.Input[str]] = None,
                                       policies: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetFunctionScalingPolicyPolicyArgs']]]]] = None,
                                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetFunctionScalingPolicyResult]:
    """
    Use this data source to access information about an existing resource.
    """
    ...

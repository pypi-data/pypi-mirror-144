# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs

__all__ = [
    'GetSecretResult',
    'AwaitableGetSecretResult',
    'get_secret',
    'get_secret_output',
]

@pulumi.output_type
class GetSecretResult:
    """
    A collection of values returned by getSecret.
    """
    def __init__(__self__, acl_only=None, acls=None, algorithm=None, bit_length=None, content_types=None, created_at=None, created_at_filter=None, creator_id=None, expiration=None, expiration_filter=None, id=None, metadata=None, mode=None, name=None, payload=None, payload_content_encoding=None, payload_content_type=None, region=None, secret_ref=None, secret_type=None, status=None, updated_at=None, updated_at_filter=None):
        if acl_only and not isinstance(acl_only, bool):
            raise TypeError("Expected argument 'acl_only' to be a bool")
        pulumi.set(__self__, "acl_only", acl_only)
        if acls and not isinstance(acls, list):
            raise TypeError("Expected argument 'acls' to be a list")
        pulumi.set(__self__, "acls", acls)
        if algorithm and not isinstance(algorithm, str):
            raise TypeError("Expected argument 'algorithm' to be a str")
        pulumi.set(__self__, "algorithm", algorithm)
        if bit_length and not isinstance(bit_length, int):
            raise TypeError("Expected argument 'bit_length' to be a int")
        pulumi.set(__self__, "bit_length", bit_length)
        if content_types and not isinstance(content_types, dict):
            raise TypeError("Expected argument 'content_types' to be a dict")
        pulumi.set(__self__, "content_types", content_types)
        if created_at and not isinstance(created_at, str):
            raise TypeError("Expected argument 'created_at' to be a str")
        pulumi.set(__self__, "created_at", created_at)
        if created_at_filter and not isinstance(created_at_filter, str):
            raise TypeError("Expected argument 'created_at_filter' to be a str")
        pulumi.set(__self__, "created_at_filter", created_at_filter)
        if creator_id and not isinstance(creator_id, str):
            raise TypeError("Expected argument 'creator_id' to be a str")
        pulumi.set(__self__, "creator_id", creator_id)
        if expiration and not isinstance(expiration, str):
            raise TypeError("Expected argument 'expiration' to be a str")
        pulumi.set(__self__, "expiration", expiration)
        if expiration_filter and not isinstance(expiration_filter, str):
            raise TypeError("Expected argument 'expiration_filter' to be a str")
        pulumi.set(__self__, "expiration_filter", expiration_filter)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if metadata and not isinstance(metadata, dict):
            raise TypeError("Expected argument 'metadata' to be a dict")
        pulumi.set(__self__, "metadata", metadata)
        if mode and not isinstance(mode, str):
            raise TypeError("Expected argument 'mode' to be a str")
        pulumi.set(__self__, "mode", mode)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if payload and not isinstance(payload, str):
            raise TypeError("Expected argument 'payload' to be a str")
        pulumi.set(__self__, "payload", payload)
        if payload_content_encoding and not isinstance(payload_content_encoding, str):
            raise TypeError("Expected argument 'payload_content_encoding' to be a str")
        pulumi.set(__self__, "payload_content_encoding", payload_content_encoding)
        if payload_content_type and not isinstance(payload_content_type, str):
            raise TypeError("Expected argument 'payload_content_type' to be a str")
        pulumi.set(__self__, "payload_content_type", payload_content_type)
        if region and not isinstance(region, str):
            raise TypeError("Expected argument 'region' to be a str")
        pulumi.set(__self__, "region", region)
        if secret_ref and not isinstance(secret_ref, str):
            raise TypeError("Expected argument 'secret_ref' to be a str")
        pulumi.set(__self__, "secret_ref", secret_ref)
        if secret_type and not isinstance(secret_type, str):
            raise TypeError("Expected argument 'secret_type' to be a str")
        pulumi.set(__self__, "secret_type", secret_type)
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)
        if updated_at and not isinstance(updated_at, str):
            raise TypeError("Expected argument 'updated_at' to be a str")
        pulumi.set(__self__, "updated_at", updated_at)
        if updated_at_filter and not isinstance(updated_at_filter, str):
            raise TypeError("Expected argument 'updated_at_filter' to be a str")
        pulumi.set(__self__, "updated_at_filter", updated_at_filter)

    @property
    @pulumi.getter(name="aclOnly")
    def acl_only(self) -> Optional[bool]:
        """
        See Argument Reference above.
        """
        return pulumi.get(self, "acl_only")

    @property
    @pulumi.getter
    def acls(self) -> Sequence['outputs.GetSecretAclResult']:
        """
        The list of ACLs assigned to a secret. The `read` structure is described below.
        """
        return pulumi.get(self, "acls")

    @property
    @pulumi.getter
    def algorithm(self) -> Optional[str]:
        """
        See Argument Reference above.
        """
        return pulumi.get(self, "algorithm")

    @property
    @pulumi.getter(name="bitLength")
    def bit_length(self) -> Optional[int]:
        """
        See Argument Reference above.
        """
        return pulumi.get(self, "bit_length")

    @property
    @pulumi.getter(name="contentTypes")
    def content_types(self) -> Mapping[str, Any]:
        """
        The map of the content types, assigned on the secret.
        """
        return pulumi.get(self, "content_types")

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> str:
        """
        The date the secret ACL was created.
        """
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter(name="createdAtFilter")
    def created_at_filter(self) -> Optional[str]:
        """
        See Argument Reference above.
        """
        return pulumi.get(self, "created_at_filter")

    @property
    @pulumi.getter(name="creatorId")
    def creator_id(self) -> str:
        """
        The creator of the secret.
        """
        return pulumi.get(self, "creator_id")

    @property
    @pulumi.getter
    def expiration(self) -> str:
        """
        The date the secret will expire.
        """
        return pulumi.get(self, "expiration")

    @property
    @pulumi.getter(name="expirationFilter")
    def expiration_filter(self) -> Optional[str]:
        """
        See Argument Reference above.
        """
        return pulumi.get(self, "expiration_filter")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def metadata(self) -> Mapping[str, Any]:
        """
        The map of metadata, assigned on the secret, which has been
        explicitly and implicitly added.
        """
        return pulumi.get(self, "metadata")

    @property
    @pulumi.getter
    def mode(self) -> Optional[str]:
        """
        See Argument Reference above.
        """
        return pulumi.get(self, "mode")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        See Argument Reference above.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def payload(self) -> str:
        """
        The secret payload.
        """
        return pulumi.get(self, "payload")

    @property
    @pulumi.getter(name="payloadContentEncoding")
    def payload_content_encoding(self) -> str:
        """
        The Secret encoding.
        """
        return pulumi.get(self, "payload_content_encoding")

    @property
    @pulumi.getter(name="payloadContentType")
    def payload_content_type(self) -> str:
        """
        The Secret content type.
        """
        return pulumi.get(self, "payload_content_type")

    @property
    @pulumi.getter
    def region(self) -> Optional[str]:
        """
        See Argument Reference above.
        """
        return pulumi.get(self, "region")

    @property
    @pulumi.getter(name="secretRef")
    def secret_ref(self) -> str:
        """
        The secret reference / where to find the secret.
        """
        return pulumi.get(self, "secret_ref")

    @property
    @pulumi.getter(name="secretType")
    def secret_type(self) -> Optional[str]:
        """
        See Argument Reference above.
        """
        return pulumi.get(self, "secret_type")

    @property
    @pulumi.getter
    def status(self) -> str:
        """
        The status of the secret.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="updatedAt")
    def updated_at(self) -> str:
        """
        The date the secret ACL was last updated.
        """
        return pulumi.get(self, "updated_at")

    @property
    @pulumi.getter(name="updatedAtFilter")
    def updated_at_filter(self) -> Optional[str]:
        """
        See Argument Reference above.
        """
        return pulumi.get(self, "updated_at_filter")


class AwaitableGetSecretResult(GetSecretResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSecretResult(
            acl_only=self.acl_only,
            acls=self.acls,
            algorithm=self.algorithm,
            bit_length=self.bit_length,
            content_types=self.content_types,
            created_at=self.created_at,
            created_at_filter=self.created_at_filter,
            creator_id=self.creator_id,
            expiration=self.expiration,
            expiration_filter=self.expiration_filter,
            id=self.id,
            metadata=self.metadata,
            mode=self.mode,
            name=self.name,
            payload=self.payload,
            payload_content_encoding=self.payload_content_encoding,
            payload_content_type=self.payload_content_type,
            region=self.region,
            secret_ref=self.secret_ref,
            secret_type=self.secret_type,
            status=self.status,
            updated_at=self.updated_at,
            updated_at_filter=self.updated_at_filter)


def get_secret(acl_only: Optional[bool] = None,
               algorithm: Optional[str] = None,
               bit_length: Optional[int] = None,
               created_at_filter: Optional[str] = None,
               expiration_filter: Optional[str] = None,
               mode: Optional[str] = None,
               name: Optional[str] = None,
               region: Optional[str] = None,
               secret_type: Optional[str] = None,
               updated_at_filter: Optional[str] = None,
               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetSecretResult:
    """
    Use this data source to access information about an existing resource.

    :param bool acl_only: Select the Secret with an ACL that contains the user.
           Project scope is ignored. Defaults to `false`.
    :param str algorithm: The Secret algorithm.
    :param int bit_length: The Secret bit length.
    :param str created_at_filter: Date filter to select the Secret with
           created matching the specified criteria. See Date Filters below for more
           detail.
    :param str expiration_filter: Date filter to select the Secret with
           expiration matching the specified criteria. See Date Filters below for more
           detail.
    :param str mode: The Secret mode.
    :param str name: The Secret name.
    :param str region: The region in which to obtain the V1 KeyManager client.
           A KeyManager client is needed to fetch a secret. If omitted, the `region`
           argument of the provider is used.
    :param str secret_type: The Secret type. For more information see
           [Secret types](https://docs.openstack.org/barbican/latest/api/reference/secret_types.html).
    :param str updated_at_filter: Date filter to select the Secret with
           updated matching the specified criteria. See Date Filters below for more
           detail.
    """
    __args__ = dict()
    __args__['aclOnly'] = acl_only
    __args__['algorithm'] = algorithm
    __args__['bitLength'] = bit_length
    __args__['createdAtFilter'] = created_at_filter
    __args__['expirationFilter'] = expiration_filter
    __args__['mode'] = mode
    __args__['name'] = name
    __args__['region'] = region
    __args__['secretType'] = secret_type
    __args__['updatedAtFilter'] = updated_at_filter
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('openstack:keymanager/getSecret:getSecret', __args__, opts=opts, typ=GetSecretResult).value

    return AwaitableGetSecretResult(
        acl_only=__ret__.acl_only,
        acls=__ret__.acls,
        algorithm=__ret__.algorithm,
        bit_length=__ret__.bit_length,
        content_types=__ret__.content_types,
        created_at=__ret__.created_at,
        created_at_filter=__ret__.created_at_filter,
        creator_id=__ret__.creator_id,
        expiration=__ret__.expiration,
        expiration_filter=__ret__.expiration_filter,
        id=__ret__.id,
        metadata=__ret__.metadata,
        mode=__ret__.mode,
        name=__ret__.name,
        payload=__ret__.payload,
        payload_content_encoding=__ret__.payload_content_encoding,
        payload_content_type=__ret__.payload_content_type,
        region=__ret__.region,
        secret_ref=__ret__.secret_ref,
        secret_type=__ret__.secret_type,
        status=__ret__.status,
        updated_at=__ret__.updated_at,
        updated_at_filter=__ret__.updated_at_filter)


@_utilities.lift_output_func(get_secret)
def get_secret_output(acl_only: Optional[pulumi.Input[Optional[bool]]] = None,
                      algorithm: Optional[pulumi.Input[Optional[str]]] = None,
                      bit_length: Optional[pulumi.Input[Optional[int]]] = None,
                      created_at_filter: Optional[pulumi.Input[Optional[str]]] = None,
                      expiration_filter: Optional[pulumi.Input[Optional[str]]] = None,
                      mode: Optional[pulumi.Input[Optional[str]]] = None,
                      name: Optional[pulumi.Input[Optional[str]]] = None,
                      region: Optional[pulumi.Input[Optional[str]]] = None,
                      secret_type: Optional[pulumi.Input[Optional[str]]] = None,
                      updated_at_filter: Optional[pulumi.Input[Optional[str]]] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetSecretResult]:
    """
    Use this data source to access information about an existing resource.

    :param bool acl_only: Select the Secret with an ACL that contains the user.
           Project scope is ignored. Defaults to `false`.
    :param str algorithm: The Secret algorithm.
    :param int bit_length: The Secret bit length.
    :param str created_at_filter: Date filter to select the Secret with
           created matching the specified criteria. See Date Filters below for more
           detail.
    :param str expiration_filter: Date filter to select the Secret with
           expiration matching the specified criteria. See Date Filters below for more
           detail.
    :param str mode: The Secret mode.
    :param str name: The Secret name.
    :param str region: The region in which to obtain the V1 KeyManager client.
           A KeyManager client is needed to fetch a secret. If omitted, the `region`
           argument of the provider is used.
    :param str secret_type: The Secret type. For more information see
           [Secret types](https://docs.openstack.org/barbican/latest/api/reference/secret_types.html).
    :param str updated_at_filter: Date filter to select the Secret with
           updated matching the specified criteria. See Date Filters below for more
           detail.
    """
    ...

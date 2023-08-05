# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['IamServiceAccountApiKeyArgs', 'IamServiceAccountApiKey']

@pulumi.input_type
class IamServiceAccountApiKeyArgs:
    def __init__(__self__, *,
                 service_account_id: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None,
                 pgp_key: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a IamServiceAccountApiKey resource.
        :param pulumi.Input[str] service_account_id: ID of the service account to an API key for.
        :param pulumi.Input[str] description: The description of the key.
        :param pulumi.Input[str] pgp_key: An optional PGP key to encrypt the resulting secret key material. May either be a base64-encoded public key or a keybase username in the form `keybase:keybaseusername`.
        """
        pulumi.set(__self__, "service_account_id", service_account_id)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if pgp_key is not None:
            pulumi.set(__self__, "pgp_key", pgp_key)

    @property
    @pulumi.getter(name="serviceAccountId")
    def service_account_id(self) -> pulumi.Input[str]:
        """
        ID of the service account to an API key for.
        """
        return pulumi.get(self, "service_account_id")

    @service_account_id.setter
    def service_account_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "service_account_id", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The description of the key.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="pgpKey")
    def pgp_key(self) -> Optional[pulumi.Input[str]]:
        """
        An optional PGP key to encrypt the resulting secret key material. May either be a base64-encoded public key or a keybase username in the form `keybase:keybaseusername`.
        """
        return pulumi.get(self, "pgp_key")

    @pgp_key.setter
    def pgp_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "pgp_key", value)


@pulumi.input_type
class _IamServiceAccountApiKeyState:
    def __init__(__self__, *,
                 created_at: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 encrypted_secret_key: Optional[pulumi.Input[str]] = None,
                 key_fingerprint: Optional[pulumi.Input[str]] = None,
                 pgp_key: Optional[pulumi.Input[str]] = None,
                 secret_key: Optional[pulumi.Input[str]] = None,
                 service_account_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering IamServiceAccountApiKey resources.
        :param pulumi.Input[str] created_at: Creation timestamp of the static access key.
        :param pulumi.Input[str] description: The description of the key.
        :param pulumi.Input[str] encrypted_secret_key: The encrypted secret key, base64 encoded. This is only populated when `pgp_key` is supplied.
        :param pulumi.Input[str] key_fingerprint: The fingerprint of the PGP key used to encrypt the secret key. This is only populated when `pgp_key` is supplied.
        :param pulumi.Input[str] pgp_key: An optional PGP key to encrypt the resulting secret key material. May either be a base64-encoded public key or a keybase username in the form `keybase:keybaseusername`.
        :param pulumi.Input[str] secret_key: The secret key. This is only populated when no `pgp_key` is provided.
        :param pulumi.Input[str] service_account_id: ID of the service account to an API key for.
        """
        if created_at is not None:
            pulumi.set(__self__, "created_at", created_at)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if encrypted_secret_key is not None:
            pulumi.set(__self__, "encrypted_secret_key", encrypted_secret_key)
        if key_fingerprint is not None:
            pulumi.set(__self__, "key_fingerprint", key_fingerprint)
        if pgp_key is not None:
            pulumi.set(__self__, "pgp_key", pgp_key)
        if secret_key is not None:
            pulumi.set(__self__, "secret_key", secret_key)
        if service_account_id is not None:
            pulumi.set(__self__, "service_account_id", service_account_id)

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[pulumi.Input[str]]:
        """
        Creation timestamp of the static access key.
        """
        return pulumi.get(self, "created_at")

    @created_at.setter
    def created_at(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "created_at", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The description of the key.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="encryptedSecretKey")
    def encrypted_secret_key(self) -> Optional[pulumi.Input[str]]:
        """
        The encrypted secret key, base64 encoded. This is only populated when `pgp_key` is supplied.
        """
        return pulumi.get(self, "encrypted_secret_key")

    @encrypted_secret_key.setter
    def encrypted_secret_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "encrypted_secret_key", value)

    @property
    @pulumi.getter(name="keyFingerprint")
    def key_fingerprint(self) -> Optional[pulumi.Input[str]]:
        """
        The fingerprint of the PGP key used to encrypt the secret key. This is only populated when `pgp_key` is supplied.
        """
        return pulumi.get(self, "key_fingerprint")

    @key_fingerprint.setter
    def key_fingerprint(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "key_fingerprint", value)

    @property
    @pulumi.getter(name="pgpKey")
    def pgp_key(self) -> Optional[pulumi.Input[str]]:
        """
        An optional PGP key to encrypt the resulting secret key material. May either be a base64-encoded public key or a keybase username in the form `keybase:keybaseusername`.
        """
        return pulumi.get(self, "pgp_key")

    @pgp_key.setter
    def pgp_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "pgp_key", value)

    @property
    @pulumi.getter(name="secretKey")
    def secret_key(self) -> Optional[pulumi.Input[str]]:
        """
        The secret key. This is only populated when no `pgp_key` is provided.
        """
        return pulumi.get(self, "secret_key")

    @secret_key.setter
    def secret_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "secret_key", value)

    @property
    @pulumi.getter(name="serviceAccountId")
    def service_account_id(self) -> Optional[pulumi.Input[str]]:
        """
        ID of the service account to an API key for.
        """
        return pulumi.get(self, "service_account_id")

    @service_account_id.setter
    def service_account_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "service_account_id", value)


class IamServiceAccountApiKey(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 pgp_key: Optional[pulumi.Input[str]] = None,
                 service_account_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Allows management of a [Yandex.Cloud IAM service account API key](https://cloud.yandex.com/docs/iam/concepts/authorization/api-key).
        The API key is a private key used for simplified authorization in the Yandex.Cloud API. API keys are only used for [service accounts](https://cloud.yandex.com/docs/iam/concepts/users/service-accounts).

        API keys do not expire. This means that this authentication method is simpler, but less secure. Use it if you can't automatically request an [IAM token](https://cloud.yandex.com/docs/iam/concepts/authorization/iam-token).

        ## Example Usage

        This snippet creates an API key.

        ```python
        import pulumi
        import pulumi_yandex as yandex

        sa_api_key = yandex.IamServiceAccountApiKey("sa-api-key",
            description="api key for authorization",
            pgp_key="keybase:keybaseusername",
            service_account_id="some_sa_id")
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: The description of the key.
        :param pulumi.Input[str] pgp_key: An optional PGP key to encrypt the resulting secret key material. May either be a base64-encoded public key or a keybase username in the form `keybase:keybaseusername`.
        :param pulumi.Input[str] service_account_id: ID of the service account to an API key for.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: IamServiceAccountApiKeyArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Allows management of a [Yandex.Cloud IAM service account API key](https://cloud.yandex.com/docs/iam/concepts/authorization/api-key).
        The API key is a private key used for simplified authorization in the Yandex.Cloud API. API keys are only used for [service accounts](https://cloud.yandex.com/docs/iam/concepts/users/service-accounts).

        API keys do not expire. This means that this authentication method is simpler, but less secure. Use it if you can't automatically request an [IAM token](https://cloud.yandex.com/docs/iam/concepts/authorization/iam-token).

        ## Example Usage

        This snippet creates an API key.

        ```python
        import pulumi
        import pulumi_yandex as yandex

        sa_api_key = yandex.IamServiceAccountApiKey("sa-api-key",
            description="api key for authorization",
            pgp_key="keybase:keybaseusername",
            service_account_id="some_sa_id")
        ```

        :param str resource_name: The name of the resource.
        :param IamServiceAccountApiKeyArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(IamServiceAccountApiKeyArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 pgp_key: Optional[pulumi.Input[str]] = None,
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
            __props__ = IamServiceAccountApiKeyArgs.__new__(IamServiceAccountApiKeyArgs)

            __props__.__dict__["description"] = description
            __props__.__dict__["pgp_key"] = pgp_key
            if service_account_id is None and not opts.urn:
                raise TypeError("Missing required property 'service_account_id'")
            __props__.__dict__["service_account_id"] = service_account_id
            __props__.__dict__["created_at"] = None
            __props__.__dict__["encrypted_secret_key"] = None
            __props__.__dict__["key_fingerprint"] = None
            __props__.__dict__["secret_key"] = None
        super(IamServiceAccountApiKey, __self__).__init__(
            'yandex:index/iamServiceAccountApiKey:IamServiceAccountApiKey',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            created_at: Optional[pulumi.Input[str]] = None,
            description: Optional[pulumi.Input[str]] = None,
            encrypted_secret_key: Optional[pulumi.Input[str]] = None,
            key_fingerprint: Optional[pulumi.Input[str]] = None,
            pgp_key: Optional[pulumi.Input[str]] = None,
            secret_key: Optional[pulumi.Input[str]] = None,
            service_account_id: Optional[pulumi.Input[str]] = None) -> 'IamServiceAccountApiKey':
        """
        Get an existing IamServiceAccountApiKey resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] created_at: Creation timestamp of the static access key.
        :param pulumi.Input[str] description: The description of the key.
        :param pulumi.Input[str] encrypted_secret_key: The encrypted secret key, base64 encoded. This is only populated when `pgp_key` is supplied.
        :param pulumi.Input[str] key_fingerprint: The fingerprint of the PGP key used to encrypt the secret key. This is only populated when `pgp_key` is supplied.
        :param pulumi.Input[str] pgp_key: An optional PGP key to encrypt the resulting secret key material. May either be a base64-encoded public key or a keybase username in the form `keybase:keybaseusername`.
        :param pulumi.Input[str] secret_key: The secret key. This is only populated when no `pgp_key` is provided.
        :param pulumi.Input[str] service_account_id: ID of the service account to an API key for.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _IamServiceAccountApiKeyState.__new__(_IamServiceAccountApiKeyState)

        __props__.__dict__["created_at"] = created_at
        __props__.__dict__["description"] = description
        __props__.__dict__["encrypted_secret_key"] = encrypted_secret_key
        __props__.__dict__["key_fingerprint"] = key_fingerprint
        __props__.__dict__["pgp_key"] = pgp_key
        __props__.__dict__["secret_key"] = secret_key
        __props__.__dict__["service_account_id"] = service_account_id
        return IamServiceAccountApiKey(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> pulumi.Output[str]:
        """
        Creation timestamp of the static access key.
        """
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        The description of the key.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="encryptedSecretKey")
    def encrypted_secret_key(self) -> pulumi.Output[str]:
        """
        The encrypted secret key, base64 encoded. This is only populated when `pgp_key` is supplied.
        """
        return pulumi.get(self, "encrypted_secret_key")

    @property
    @pulumi.getter(name="keyFingerprint")
    def key_fingerprint(self) -> pulumi.Output[str]:
        """
        The fingerprint of the PGP key used to encrypt the secret key. This is only populated when `pgp_key` is supplied.
        """
        return pulumi.get(self, "key_fingerprint")

    @property
    @pulumi.getter(name="pgpKey")
    def pgp_key(self) -> pulumi.Output[Optional[str]]:
        """
        An optional PGP key to encrypt the resulting secret key material. May either be a base64-encoded public key or a keybase username in the form `keybase:keybaseusername`.
        """
        return pulumi.get(self, "pgp_key")

    @property
    @pulumi.getter(name="secretKey")
    def secret_key(self) -> pulumi.Output[str]:
        """
        The secret key. This is only populated when no `pgp_key` is provided.
        """
        return pulumi.get(self, "secret_key")

    @property
    @pulumi.getter(name="serviceAccountId")
    def service_account_id(self) -> pulumi.Output[str]:
        """
        ID of the service account to an API key for.
        """
        return pulumi.get(self, "service_account_id")


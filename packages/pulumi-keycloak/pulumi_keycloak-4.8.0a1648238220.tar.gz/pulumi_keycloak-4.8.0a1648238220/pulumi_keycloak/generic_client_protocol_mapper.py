# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['GenericClientProtocolMapperArgs', 'GenericClientProtocolMapper']

@pulumi.input_type
class GenericClientProtocolMapperArgs:
    def __init__(__self__, *,
                 config: pulumi.Input[Mapping[str, Any]],
                 protocol: pulumi.Input[str],
                 protocol_mapper: pulumi.Input[str],
                 realm_id: pulumi.Input[str],
                 client_id: Optional[pulumi.Input[str]] = None,
                 client_scope_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a GenericClientProtocolMapper resource.
        :param pulumi.Input[Mapping[str, Any]] config: A map with key / value pairs for configuring the protocol mapper. The supported keys depends on the protocol mapper.
        :param pulumi.Input[str] protocol: The type of client (either `openid-connect` or `saml`). The type must match the type of the client.
        :param pulumi.Input[str] protocol_mapper: The name of the protocol mapper. The protocol mapper must be compatible with the specified client.
        :param pulumi.Input[str] realm_id: The realm this protocol mapper exists within.
        :param pulumi.Input[str] client_id: The client this protocol mapper is attached to.
        :param pulumi.Input[str] client_scope_id: The mapper's associated client scope. Cannot be used at the same time as client_id.
        :param pulumi.Input[str] name: The display name of this protocol mapper in the GUI.
        """
        pulumi.set(__self__, "config", config)
        pulumi.set(__self__, "protocol", protocol)
        pulumi.set(__self__, "protocol_mapper", protocol_mapper)
        pulumi.set(__self__, "realm_id", realm_id)
        if client_id is not None:
            pulumi.set(__self__, "client_id", client_id)
        if client_scope_id is not None:
            pulumi.set(__self__, "client_scope_id", client_scope_id)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def config(self) -> pulumi.Input[Mapping[str, Any]]:
        """
        A map with key / value pairs for configuring the protocol mapper. The supported keys depends on the protocol mapper.
        """
        return pulumi.get(self, "config")

    @config.setter
    def config(self, value: pulumi.Input[Mapping[str, Any]]):
        pulumi.set(self, "config", value)

    @property
    @pulumi.getter
    def protocol(self) -> pulumi.Input[str]:
        """
        The type of client (either `openid-connect` or `saml`). The type must match the type of the client.
        """
        return pulumi.get(self, "protocol")

    @protocol.setter
    def protocol(self, value: pulumi.Input[str]):
        pulumi.set(self, "protocol", value)

    @property
    @pulumi.getter(name="protocolMapper")
    def protocol_mapper(self) -> pulumi.Input[str]:
        """
        The name of the protocol mapper. The protocol mapper must be compatible with the specified client.
        """
        return pulumi.get(self, "protocol_mapper")

    @protocol_mapper.setter
    def protocol_mapper(self, value: pulumi.Input[str]):
        pulumi.set(self, "protocol_mapper", value)

    @property
    @pulumi.getter(name="realmId")
    def realm_id(self) -> pulumi.Input[str]:
        """
        The realm this protocol mapper exists within.
        """
        return pulumi.get(self, "realm_id")

    @realm_id.setter
    def realm_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "realm_id", value)

    @property
    @pulumi.getter(name="clientId")
    def client_id(self) -> Optional[pulumi.Input[str]]:
        """
        The client this protocol mapper is attached to.
        """
        return pulumi.get(self, "client_id")

    @client_id.setter
    def client_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "client_id", value)

    @property
    @pulumi.getter(name="clientScopeId")
    def client_scope_id(self) -> Optional[pulumi.Input[str]]:
        """
        The mapper's associated client scope. Cannot be used at the same time as client_id.
        """
        return pulumi.get(self, "client_scope_id")

    @client_scope_id.setter
    def client_scope_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "client_scope_id", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The display name of this protocol mapper in the GUI.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class _GenericClientProtocolMapperState:
    def __init__(__self__, *,
                 client_id: Optional[pulumi.Input[str]] = None,
                 client_scope_id: Optional[pulumi.Input[str]] = None,
                 config: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 protocol: Optional[pulumi.Input[str]] = None,
                 protocol_mapper: Optional[pulumi.Input[str]] = None,
                 realm_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering GenericClientProtocolMapper resources.
        :param pulumi.Input[str] client_id: The client this protocol mapper is attached to.
        :param pulumi.Input[str] client_scope_id: The mapper's associated client scope. Cannot be used at the same time as client_id.
        :param pulumi.Input[Mapping[str, Any]] config: A map with key / value pairs for configuring the protocol mapper. The supported keys depends on the protocol mapper.
        :param pulumi.Input[str] name: The display name of this protocol mapper in the GUI.
        :param pulumi.Input[str] protocol: The type of client (either `openid-connect` or `saml`). The type must match the type of the client.
        :param pulumi.Input[str] protocol_mapper: The name of the protocol mapper. The protocol mapper must be compatible with the specified client.
        :param pulumi.Input[str] realm_id: The realm this protocol mapper exists within.
        """
        if client_id is not None:
            pulumi.set(__self__, "client_id", client_id)
        if client_scope_id is not None:
            pulumi.set(__self__, "client_scope_id", client_scope_id)
        if config is not None:
            pulumi.set(__self__, "config", config)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if protocol is not None:
            pulumi.set(__self__, "protocol", protocol)
        if protocol_mapper is not None:
            pulumi.set(__self__, "protocol_mapper", protocol_mapper)
        if realm_id is not None:
            pulumi.set(__self__, "realm_id", realm_id)

    @property
    @pulumi.getter(name="clientId")
    def client_id(self) -> Optional[pulumi.Input[str]]:
        """
        The client this protocol mapper is attached to.
        """
        return pulumi.get(self, "client_id")

    @client_id.setter
    def client_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "client_id", value)

    @property
    @pulumi.getter(name="clientScopeId")
    def client_scope_id(self) -> Optional[pulumi.Input[str]]:
        """
        The mapper's associated client scope. Cannot be used at the same time as client_id.
        """
        return pulumi.get(self, "client_scope_id")

    @client_scope_id.setter
    def client_scope_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "client_scope_id", value)

    @property
    @pulumi.getter
    def config(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        """
        A map with key / value pairs for configuring the protocol mapper. The supported keys depends on the protocol mapper.
        """
        return pulumi.get(self, "config")

    @config.setter
    def config(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "config", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The display name of this protocol mapper in the GUI.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def protocol(self) -> Optional[pulumi.Input[str]]:
        """
        The type of client (either `openid-connect` or `saml`). The type must match the type of the client.
        """
        return pulumi.get(self, "protocol")

    @protocol.setter
    def protocol(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "protocol", value)

    @property
    @pulumi.getter(name="protocolMapper")
    def protocol_mapper(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the protocol mapper. The protocol mapper must be compatible with the specified client.
        """
        return pulumi.get(self, "protocol_mapper")

    @protocol_mapper.setter
    def protocol_mapper(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "protocol_mapper", value)

    @property
    @pulumi.getter(name="realmId")
    def realm_id(self) -> Optional[pulumi.Input[str]]:
        """
        The realm this protocol mapper exists within.
        """
        return pulumi.get(self, "realm_id")

    @realm_id.setter
    def realm_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "realm_id", value)


class GenericClientProtocolMapper(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 client_id: Optional[pulumi.Input[str]] = None,
                 client_scope_id: Optional[pulumi.Input[str]] = None,
                 config: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 protocol: Optional[pulumi.Input[str]] = None,
                 protocol_mapper: Optional[pulumi.Input[str]] = None,
                 realm_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Allows for creating and managing protocol mappers for both types of clients (openid-connect and saml) within Keycloak.

        There are two uses cases for using this resource:
        * If you implemented a custom protocol mapper, this resource can be used to configure it
        * If the provider doesn't support a particular protocol mapper, this resource can be used instead.

        Due to the generic nature of this mapper, it is less user-friendly and more prone to configuration errors.
        Therefore, if possible, a specific mapper should be used.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_keycloak as keycloak

        realm = keycloak.Realm("realm",
            realm="my-realm",
            enabled=True)
        saml_client = keycloak.saml.Client("samlClient",
            realm_id=realm.id,
            client_id="test-client")
        saml_hardcode_attribute_mapper = keycloak.GenericClientProtocolMapper("samlHardcodeAttributeMapper",
            realm_id=realm.id,
            client_id=saml_client.id,
            protocol="saml",
            protocol_mapper="saml-hardcode-attribute-mapper",
            config={
                "attribute.name": "name",
                "attribute.nameformat": "Basic",
                "attribute.value": "value",
                "friendly.name": "display name",
            })
        ```

        ## Import

        Protocol mappers can be imported using the following format`{{realm_id}}/client/{{client_keycloak_id}}/{{protocol_mapper_id}}` Examplebash

        ```sh
         $ pulumi import keycloak:index/genericClientProtocolMapper:GenericClientProtocolMapper saml_hardcode_attribute_mapper my-realm/client/a7202154-8793-4656-b655-1dd18c181e14/71602afa-f7d1-4788-8c49-ef8fd00af0f4
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] client_id: The client this protocol mapper is attached to.
        :param pulumi.Input[str] client_scope_id: The mapper's associated client scope. Cannot be used at the same time as client_id.
        :param pulumi.Input[Mapping[str, Any]] config: A map with key / value pairs for configuring the protocol mapper. The supported keys depends on the protocol mapper.
        :param pulumi.Input[str] name: The display name of this protocol mapper in the GUI.
        :param pulumi.Input[str] protocol: The type of client (either `openid-connect` or `saml`). The type must match the type of the client.
        :param pulumi.Input[str] protocol_mapper: The name of the protocol mapper. The protocol mapper must be compatible with the specified client.
        :param pulumi.Input[str] realm_id: The realm this protocol mapper exists within.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: GenericClientProtocolMapperArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Allows for creating and managing protocol mappers for both types of clients (openid-connect and saml) within Keycloak.

        There are two uses cases for using this resource:
        * If you implemented a custom protocol mapper, this resource can be used to configure it
        * If the provider doesn't support a particular protocol mapper, this resource can be used instead.

        Due to the generic nature of this mapper, it is less user-friendly and more prone to configuration errors.
        Therefore, if possible, a specific mapper should be used.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_keycloak as keycloak

        realm = keycloak.Realm("realm",
            realm="my-realm",
            enabled=True)
        saml_client = keycloak.saml.Client("samlClient",
            realm_id=realm.id,
            client_id="test-client")
        saml_hardcode_attribute_mapper = keycloak.GenericClientProtocolMapper("samlHardcodeAttributeMapper",
            realm_id=realm.id,
            client_id=saml_client.id,
            protocol="saml",
            protocol_mapper="saml-hardcode-attribute-mapper",
            config={
                "attribute.name": "name",
                "attribute.nameformat": "Basic",
                "attribute.value": "value",
                "friendly.name": "display name",
            })
        ```

        ## Import

        Protocol mappers can be imported using the following format`{{realm_id}}/client/{{client_keycloak_id}}/{{protocol_mapper_id}}` Examplebash

        ```sh
         $ pulumi import keycloak:index/genericClientProtocolMapper:GenericClientProtocolMapper saml_hardcode_attribute_mapper my-realm/client/a7202154-8793-4656-b655-1dd18c181e14/71602afa-f7d1-4788-8c49-ef8fd00af0f4
        ```

        :param str resource_name: The name of the resource.
        :param GenericClientProtocolMapperArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(GenericClientProtocolMapperArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 client_id: Optional[pulumi.Input[str]] = None,
                 client_scope_id: Optional[pulumi.Input[str]] = None,
                 config: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 protocol: Optional[pulumi.Input[str]] = None,
                 protocol_mapper: Optional[pulumi.Input[str]] = None,
                 realm_id: Optional[pulumi.Input[str]] = None,
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
            __props__ = GenericClientProtocolMapperArgs.__new__(GenericClientProtocolMapperArgs)

            __props__.__dict__["client_id"] = client_id
            __props__.__dict__["client_scope_id"] = client_scope_id
            if config is None and not opts.urn:
                raise TypeError("Missing required property 'config'")
            __props__.__dict__["config"] = config
            __props__.__dict__["name"] = name
            if protocol is None and not opts.urn:
                raise TypeError("Missing required property 'protocol'")
            __props__.__dict__["protocol"] = protocol
            if protocol_mapper is None and not opts.urn:
                raise TypeError("Missing required property 'protocol_mapper'")
            __props__.__dict__["protocol_mapper"] = protocol_mapper
            if realm_id is None and not opts.urn:
                raise TypeError("Missing required property 'realm_id'")
            __props__.__dict__["realm_id"] = realm_id
        super(GenericClientProtocolMapper, __self__).__init__(
            'keycloak:index/genericClientProtocolMapper:GenericClientProtocolMapper',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            client_id: Optional[pulumi.Input[str]] = None,
            client_scope_id: Optional[pulumi.Input[str]] = None,
            config: Optional[pulumi.Input[Mapping[str, Any]]] = None,
            name: Optional[pulumi.Input[str]] = None,
            protocol: Optional[pulumi.Input[str]] = None,
            protocol_mapper: Optional[pulumi.Input[str]] = None,
            realm_id: Optional[pulumi.Input[str]] = None) -> 'GenericClientProtocolMapper':
        """
        Get an existing GenericClientProtocolMapper resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] client_id: The client this protocol mapper is attached to.
        :param pulumi.Input[str] client_scope_id: The mapper's associated client scope. Cannot be used at the same time as client_id.
        :param pulumi.Input[Mapping[str, Any]] config: A map with key / value pairs for configuring the protocol mapper. The supported keys depends on the protocol mapper.
        :param pulumi.Input[str] name: The display name of this protocol mapper in the GUI.
        :param pulumi.Input[str] protocol: The type of client (either `openid-connect` or `saml`). The type must match the type of the client.
        :param pulumi.Input[str] protocol_mapper: The name of the protocol mapper. The protocol mapper must be compatible with the specified client.
        :param pulumi.Input[str] realm_id: The realm this protocol mapper exists within.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _GenericClientProtocolMapperState.__new__(_GenericClientProtocolMapperState)

        __props__.__dict__["client_id"] = client_id
        __props__.__dict__["client_scope_id"] = client_scope_id
        __props__.__dict__["config"] = config
        __props__.__dict__["name"] = name
        __props__.__dict__["protocol"] = protocol
        __props__.__dict__["protocol_mapper"] = protocol_mapper
        __props__.__dict__["realm_id"] = realm_id
        return GenericClientProtocolMapper(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="clientId")
    def client_id(self) -> pulumi.Output[Optional[str]]:
        """
        The client this protocol mapper is attached to.
        """
        return pulumi.get(self, "client_id")

    @property
    @pulumi.getter(name="clientScopeId")
    def client_scope_id(self) -> pulumi.Output[Optional[str]]:
        """
        The mapper's associated client scope. Cannot be used at the same time as client_id.
        """
        return pulumi.get(self, "client_scope_id")

    @property
    @pulumi.getter
    def config(self) -> pulumi.Output[Mapping[str, Any]]:
        """
        A map with key / value pairs for configuring the protocol mapper. The supported keys depends on the protocol mapper.
        """
        return pulumi.get(self, "config")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The display name of this protocol mapper in the GUI.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def protocol(self) -> pulumi.Output[str]:
        """
        The type of client (either `openid-connect` or `saml`). The type must match the type of the client.
        """
        return pulumi.get(self, "protocol")

    @property
    @pulumi.getter(name="protocolMapper")
    def protocol_mapper(self) -> pulumi.Output[str]:
        """
        The name of the protocol mapper. The protocol mapper must be compatible with the specified client.
        """
        return pulumi.get(self, "protocol_mapper")

    @property
    @pulumi.getter(name="realmId")
    def realm_id(self) -> pulumi.Output[str]:
        """
        The realm this protocol mapper exists within.
        """
        return pulumi.get(self, "realm_id")


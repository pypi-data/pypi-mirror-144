# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = [
    'GetDomainResult',
    'AwaitableGetDomainResult',
    'get_domain',
    'get_domain_output',
]

@pulumi.output_type
class GetDomainResult:
    """
    A collection of values returned by getDomain.
    """
    def __init__(__self__, axfr_ips=None, description=None, domain=None, expire_sec=None, group=None, id=None, master_ips=None, refresh_sec=None, retry_sec=None, soa_email=None, status=None, tags=None, ttl_sec=None, type=None):
        if axfr_ips and not isinstance(axfr_ips, list):
            raise TypeError("Expected argument 'axfr_ips' to be a list")
        pulumi.set(__self__, "axfr_ips", axfr_ips)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if domain and not isinstance(domain, str):
            raise TypeError("Expected argument 'domain' to be a str")
        pulumi.set(__self__, "domain", domain)
        if expire_sec and not isinstance(expire_sec, int):
            raise TypeError("Expected argument 'expire_sec' to be a int")
        pulumi.set(__self__, "expire_sec", expire_sec)
        if group and not isinstance(group, str):
            raise TypeError("Expected argument 'group' to be a str")
        pulumi.set(__self__, "group", group)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if master_ips and not isinstance(master_ips, list):
            raise TypeError("Expected argument 'master_ips' to be a list")
        pulumi.set(__self__, "master_ips", master_ips)
        if refresh_sec and not isinstance(refresh_sec, int):
            raise TypeError("Expected argument 'refresh_sec' to be a int")
        pulumi.set(__self__, "refresh_sec", refresh_sec)
        if retry_sec and not isinstance(retry_sec, int):
            raise TypeError("Expected argument 'retry_sec' to be a int")
        pulumi.set(__self__, "retry_sec", retry_sec)
        if soa_email and not isinstance(soa_email, str):
            raise TypeError("Expected argument 'soa_email' to be a str")
        pulumi.set(__self__, "soa_email", soa_email)
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)
        if ttl_sec and not isinstance(ttl_sec, int):
            raise TypeError("Expected argument 'ttl_sec' to be a int")
        pulumi.set(__self__, "ttl_sec", ttl_sec)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="axfrIps")
    def axfr_ips(self) -> Sequence[str]:
        return pulumi.get(self, "axfr_ips")

    @property
    @pulumi.getter
    def description(self) -> str:
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def domain(self) -> Optional[str]:
        return pulumi.get(self, "domain")

    @property
    @pulumi.getter(name="expireSec")
    def expire_sec(self) -> int:
        return pulumi.get(self, "expire_sec")

    @property
    @pulumi.getter
    def group(self) -> str:
        return pulumi.get(self, "group")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="masterIps")
    def master_ips(self) -> Sequence[str]:
        return pulumi.get(self, "master_ips")

    @property
    @pulumi.getter(name="refreshSec")
    def refresh_sec(self) -> int:
        return pulumi.get(self, "refresh_sec")

    @property
    @pulumi.getter(name="retrySec")
    def retry_sec(self) -> int:
        return pulumi.get(self, "retry_sec")

    @property
    @pulumi.getter(name="soaEmail")
    def soa_email(self) -> str:
        return pulumi.get(self, "soa_email")

    @property
    @pulumi.getter
    def status(self) -> str:
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def tags(self) -> Sequence[str]:
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="ttlSec")
    def ttl_sec(self) -> int:
        return pulumi.get(self, "ttl_sec")

    @property
    @pulumi.getter
    def type(self) -> str:
        return pulumi.get(self, "type")


class AwaitableGetDomainResult(GetDomainResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDomainResult(
            axfr_ips=self.axfr_ips,
            description=self.description,
            domain=self.domain,
            expire_sec=self.expire_sec,
            group=self.group,
            id=self.id,
            master_ips=self.master_ips,
            refresh_sec=self.refresh_sec,
            retry_sec=self.retry_sec,
            soa_email=self.soa_email,
            status=self.status,
            tags=self.tags,
            ttl_sec=self.ttl_sec,
            type=self.type)


def get_domain(domain: Optional[str] = None,
               id: Optional[str] = None,
               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDomainResult:
    """
    Provides information about a Linode domain.

    ## Example Usage

    The following example shows how one might use this data source to access information about a Linode domain.

    ```python
    import pulumi
    import pulumi_linode as linode

    foo = linode.get_domain(id="1234567")
    bar = linode.get_domain(domain="bar.example.com")
    ```
    ## Attributes

    The Linode Domain resource exports the following attributes:

    * `id` - The unique ID of this Domain.

    * `domain` - The domain this Domain represents. These must be unique in our system; you cannot have two Domains representing the same domain

    * `type` - If this Domain represents the authoritative source of information for the domain it describes, or if it is a read-only copy of a master (also called a slave) (`master`, `slave`)

    * `group` - The group this Domain belongs to.

    * `status` - Used to control whether this Domain is currently being rendered. (`disabled`, `active`)

    * `description` - A description for this Domain.

    * `master_ips` - The IP addresses representing the master DNS for this Domain.

    * `axfr_ips` - The list of IPs that may perform a zone transfer for this Domain.

    * `ttl_sec` - 'Time to Live'-the amount of time in seconds that this Domain's records may be cached by resolvers or other domain servers.

    * `retry_sec` - The interval, in seconds, at which a failed refresh should be retried.

    * `expire_sec` - The amount of time in seconds that may pass before this Domain is no longer authoritative.

    * `refresh_sec` - The amount of time in seconds before this Domain should be refreshed.

    * `soa_email` - Start of Authority email address.

    * `tags` - An array of tags applied to this object.


    :param str domain: The unique domain name of the Domain record to query.
    :param str id: The unique numeric ID of the Domain record to query.
    """
    __args__ = dict()
    __args__['domain'] = domain
    __args__['id'] = id
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('linode:index/getDomain:getDomain', __args__, opts=opts, typ=GetDomainResult).value

    return AwaitableGetDomainResult(
        axfr_ips=__ret__.axfr_ips,
        description=__ret__.description,
        domain=__ret__.domain,
        expire_sec=__ret__.expire_sec,
        group=__ret__.group,
        id=__ret__.id,
        master_ips=__ret__.master_ips,
        refresh_sec=__ret__.refresh_sec,
        retry_sec=__ret__.retry_sec,
        soa_email=__ret__.soa_email,
        status=__ret__.status,
        tags=__ret__.tags,
        ttl_sec=__ret__.ttl_sec,
        type=__ret__.type)


@_utilities.lift_output_func(get_domain)
def get_domain_output(domain: Optional[pulumi.Input[Optional[str]]] = None,
                      id: Optional[pulumi.Input[Optional[str]]] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetDomainResult]:
    """
    Provides information about a Linode domain.

    ## Example Usage

    The following example shows how one might use this data source to access information about a Linode domain.

    ```python
    import pulumi
    import pulumi_linode as linode

    foo = linode.get_domain(id="1234567")
    bar = linode.get_domain(domain="bar.example.com")
    ```
    ## Attributes

    The Linode Domain resource exports the following attributes:

    * `id` - The unique ID of this Domain.

    * `domain` - The domain this Domain represents. These must be unique in our system; you cannot have two Domains representing the same domain

    * `type` - If this Domain represents the authoritative source of information for the domain it describes, or if it is a read-only copy of a master (also called a slave) (`master`, `slave`)

    * `group` - The group this Domain belongs to.

    * `status` - Used to control whether this Domain is currently being rendered. (`disabled`, `active`)

    * `description` - A description for this Domain.

    * `master_ips` - The IP addresses representing the master DNS for this Domain.

    * `axfr_ips` - The list of IPs that may perform a zone transfer for this Domain.

    * `ttl_sec` - 'Time to Live'-the amount of time in seconds that this Domain's records may be cached by resolvers or other domain servers.

    * `retry_sec` - The interval, in seconds, at which a failed refresh should be retried.

    * `expire_sec` - The amount of time in seconds that may pass before this Domain is no longer authoritative.

    * `refresh_sec` - The amount of time in seconds before this Domain should be refreshed.

    * `soa_email` - Start of Authority email address.

    * `tags` - An array of tags applied to this object.


    :param str domain: The unique domain name of the Domain record to query.
    :param str id: The unique numeric ID of the Domain record to query.
    """
    ...

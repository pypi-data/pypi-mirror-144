# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['AlertPolicyChannelArgs', 'AlertPolicyChannel']

@pulumi.input_type
class AlertPolicyChannelArgs:
    def __init__(__self__, *,
                 channel_ids: pulumi.Input[Sequence[pulumi.Input[int]]],
                 policy_id: pulumi.Input[int],
                 account_id: Optional[pulumi.Input[int]] = None):
        """
        The set of arguments for constructing a AlertPolicyChannel resource.
        :param pulumi.Input[Sequence[pulumi.Input[int]]] channel_ids: Array of channel IDs to apply to the specified policy. We recommended sorting channel IDs in ascending order to avoid drift in your state.
        :param pulumi.Input[int] policy_id: The ID of the policy.
        :param pulumi.Input[int] account_id: Determines the New Relic account where the alert policy channel will be created. Defaults to the account associated with the API key used.
        """
        pulumi.set(__self__, "channel_ids", channel_ids)
        pulumi.set(__self__, "policy_id", policy_id)
        if account_id is not None:
            pulumi.set(__self__, "account_id", account_id)

    @property
    @pulumi.getter(name="channelIds")
    def channel_ids(self) -> pulumi.Input[Sequence[pulumi.Input[int]]]:
        """
        Array of channel IDs to apply to the specified policy. We recommended sorting channel IDs in ascending order to avoid drift in your state.
        """
        return pulumi.get(self, "channel_ids")

    @channel_ids.setter
    def channel_ids(self, value: pulumi.Input[Sequence[pulumi.Input[int]]]):
        pulumi.set(self, "channel_ids", value)

    @property
    @pulumi.getter(name="policyId")
    def policy_id(self) -> pulumi.Input[int]:
        """
        The ID of the policy.
        """
        return pulumi.get(self, "policy_id")

    @policy_id.setter
    def policy_id(self, value: pulumi.Input[int]):
        pulumi.set(self, "policy_id", value)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> Optional[pulumi.Input[int]]:
        """
        Determines the New Relic account where the alert policy channel will be created. Defaults to the account associated with the API key used.
        """
        return pulumi.get(self, "account_id")

    @account_id.setter
    def account_id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "account_id", value)


@pulumi.input_type
class _AlertPolicyChannelState:
    def __init__(__self__, *,
                 account_id: Optional[pulumi.Input[int]] = None,
                 channel_ids: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None,
                 policy_id: Optional[pulumi.Input[int]] = None):
        """
        Input properties used for looking up and filtering AlertPolicyChannel resources.
        :param pulumi.Input[int] account_id: Determines the New Relic account where the alert policy channel will be created. Defaults to the account associated with the API key used.
        :param pulumi.Input[Sequence[pulumi.Input[int]]] channel_ids: Array of channel IDs to apply to the specified policy. We recommended sorting channel IDs in ascending order to avoid drift in your state.
        :param pulumi.Input[int] policy_id: The ID of the policy.
        """
        if account_id is not None:
            pulumi.set(__self__, "account_id", account_id)
        if channel_ids is not None:
            pulumi.set(__self__, "channel_ids", channel_ids)
        if policy_id is not None:
            pulumi.set(__self__, "policy_id", policy_id)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> Optional[pulumi.Input[int]]:
        """
        Determines the New Relic account where the alert policy channel will be created. Defaults to the account associated with the API key used.
        """
        return pulumi.get(self, "account_id")

    @account_id.setter
    def account_id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "account_id", value)

    @property
    @pulumi.getter(name="channelIds")
    def channel_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[int]]]]:
        """
        Array of channel IDs to apply to the specified policy. We recommended sorting channel IDs in ascending order to avoid drift in your state.
        """
        return pulumi.get(self, "channel_ids")

    @channel_ids.setter
    def channel_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]]):
        pulumi.set(self, "channel_ids", value)

    @property
    @pulumi.getter(name="policyId")
    def policy_id(self) -> Optional[pulumi.Input[int]]:
        """
        The ID of the policy.
        """
        return pulumi.get(self, "policy_id")

    @policy_id.setter
    def policy_id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "policy_id", value)


class AlertPolicyChannel(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_id: Optional[pulumi.Input[int]] = None,
                 channel_ids: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None,
                 policy_id: Optional[pulumi.Input[int]] = None,
                 __props__=None):
        """
        Use this resource to map alert policies to alert channels in New Relic.

        ## Example Usage

        The example below will apply multiple alert channels to an existing New Relic alert policy.

        ```python
        import pulumi
        import pulumi_newrelic as newrelic

        example_policy = newrelic.get_alert_policy(name="my-alert-policy")
        # Creates an email alert channel.
        email_channel = newrelic.AlertChannel("emailChannel",
            type="email",
            config=newrelic.AlertChannelConfigArgs(
                recipients="foo@example.com",
                include_json_attachment="1",
            ))
        # Creates a Slack alert channel.
        slack_channel = newrelic.AlertChannel("slackChannel",
            type="slack",
            config=newrelic.AlertChannelConfigArgs(
                channel="#example-channel",
                url="http://example-org.slack.com",
            ))
        # Applies the created channels above to the alert policy
        # referenced at the top of the config.
        foo = newrelic.AlertPolicyChannel("foo",
            policy_id=newrelic_alert_policy["example_policy"]["id"],
            channel_ids=[
                email_channel.id,
                slack_channel.id,
            ])
        ```

        ## Import

        Alert policy channels can be imported using the following notation`<policyID>:<channelID>:<channelID>`, e.g.

        ```sh
         $ pulumi import newrelic:index/alertPolicyChannel:AlertPolicyChannel foo 123456:3462754:2938324
        ```

         When importing `newrelic_alert_policy_channel` resource, the attribute `channel_ids`\* will be set in your Terraform state. You can import multiple channels as long as those channel IDs are included as part of the import ID hash.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[int] account_id: Determines the New Relic account where the alert policy channel will be created. Defaults to the account associated with the API key used.
        :param pulumi.Input[Sequence[pulumi.Input[int]]] channel_ids: Array of channel IDs to apply to the specified policy. We recommended sorting channel IDs in ascending order to avoid drift in your state.
        :param pulumi.Input[int] policy_id: The ID of the policy.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: AlertPolicyChannelArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Use this resource to map alert policies to alert channels in New Relic.

        ## Example Usage

        The example below will apply multiple alert channels to an existing New Relic alert policy.

        ```python
        import pulumi
        import pulumi_newrelic as newrelic

        example_policy = newrelic.get_alert_policy(name="my-alert-policy")
        # Creates an email alert channel.
        email_channel = newrelic.AlertChannel("emailChannel",
            type="email",
            config=newrelic.AlertChannelConfigArgs(
                recipients="foo@example.com",
                include_json_attachment="1",
            ))
        # Creates a Slack alert channel.
        slack_channel = newrelic.AlertChannel("slackChannel",
            type="slack",
            config=newrelic.AlertChannelConfigArgs(
                channel="#example-channel",
                url="http://example-org.slack.com",
            ))
        # Applies the created channels above to the alert policy
        # referenced at the top of the config.
        foo = newrelic.AlertPolicyChannel("foo",
            policy_id=newrelic_alert_policy["example_policy"]["id"],
            channel_ids=[
                email_channel.id,
                slack_channel.id,
            ])
        ```

        ## Import

        Alert policy channels can be imported using the following notation`<policyID>:<channelID>:<channelID>`, e.g.

        ```sh
         $ pulumi import newrelic:index/alertPolicyChannel:AlertPolicyChannel foo 123456:3462754:2938324
        ```

         When importing `newrelic_alert_policy_channel` resource, the attribute `channel_ids`\* will be set in your Terraform state. You can import multiple channels as long as those channel IDs are included as part of the import ID hash.

        :param str resource_name: The name of the resource.
        :param AlertPolicyChannelArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AlertPolicyChannelArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_id: Optional[pulumi.Input[int]] = None,
                 channel_ids: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None,
                 policy_id: Optional[pulumi.Input[int]] = None,
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
            __props__ = AlertPolicyChannelArgs.__new__(AlertPolicyChannelArgs)

            __props__.__dict__["account_id"] = account_id
            if channel_ids is None and not opts.urn:
                raise TypeError("Missing required property 'channel_ids'")
            __props__.__dict__["channel_ids"] = channel_ids
            if policy_id is None and not opts.urn:
                raise TypeError("Missing required property 'policy_id'")
            __props__.__dict__["policy_id"] = policy_id
        super(AlertPolicyChannel, __self__).__init__(
            'newrelic:index/alertPolicyChannel:AlertPolicyChannel',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            account_id: Optional[pulumi.Input[int]] = None,
            channel_ids: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None,
            policy_id: Optional[pulumi.Input[int]] = None) -> 'AlertPolicyChannel':
        """
        Get an existing AlertPolicyChannel resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[int] account_id: Determines the New Relic account where the alert policy channel will be created. Defaults to the account associated with the API key used.
        :param pulumi.Input[Sequence[pulumi.Input[int]]] channel_ids: Array of channel IDs to apply to the specified policy. We recommended sorting channel IDs in ascending order to avoid drift in your state.
        :param pulumi.Input[int] policy_id: The ID of the policy.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _AlertPolicyChannelState.__new__(_AlertPolicyChannelState)

        __props__.__dict__["account_id"] = account_id
        __props__.__dict__["channel_ids"] = channel_ids
        __props__.__dict__["policy_id"] = policy_id
        return AlertPolicyChannel(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> pulumi.Output[int]:
        """
        Determines the New Relic account where the alert policy channel will be created. Defaults to the account associated with the API key used.
        """
        return pulumi.get(self, "account_id")

    @property
    @pulumi.getter(name="channelIds")
    def channel_ids(self) -> pulumi.Output[Sequence[int]]:
        """
        Array of channel IDs to apply to the specified policy. We recommended sorting channel IDs in ascending order to avoid drift in your state.
        """
        return pulumi.get(self, "channel_ids")

    @property
    @pulumi.getter(name="policyId")
    def policy_id(self) -> pulumi.Output[int]:
        """
        The ID of the policy.
        """
        return pulumi.get(self, "policy_id")


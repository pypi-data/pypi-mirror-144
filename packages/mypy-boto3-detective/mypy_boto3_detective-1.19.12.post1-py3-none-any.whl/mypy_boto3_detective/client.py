"""
Type annotations for detective service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_detective/client/)

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_detective.client import DetectiveClient

    session = Session()
    client: DetectiveClient = session.client("detective")
    ```
"""
from typing import Any, Dict, Mapping, Sequence, Type

from botocore.client import BaseClient, ClientMeta

from .type_defs import (
    AccountTypeDef,
    CreateGraphResponseTypeDef,
    CreateMembersResponseTypeDef,
    DeleteMembersResponseTypeDef,
    GetMembersResponseTypeDef,
    ListGraphsResponseTypeDef,
    ListInvitationsResponseTypeDef,
    ListMembersResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
)

__all__ = ("DetectiveClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Mapping[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]


class DetectiveClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/detective.html#Detective.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_detective/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        DetectiveClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/detective.html#Detective.Client.exceptions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_detective/client/#exceptions)
        """

    def accept_invitation(self, *, GraphArn: str) -> None:
        """
        Accepts an invitation for the member account to contribute data to a behavior
        graph.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/detective.html#Detective.Client.accept_invitation)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_detective/client/#accept_invitation)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/detective.html#Detective.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_detective/client/#can_paginate)
        """

    def create_graph(self, *, Tags: Mapping[str, str] = ...) -> CreateGraphResponseTypeDef:
        """
        Creates a new behavior graph for the calling account, and sets that account as
        the administrator account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/detective.html#Detective.Client.create_graph)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_detective/client/#create_graph)
        """

    def create_members(
        self,
        *,
        GraphArn: str,
        Accounts: Sequence["AccountTypeDef"],
        Message: str = ...,
        DisableEmailNotification: bool = ...
    ) -> CreateMembersResponseTypeDef:
        """
        Sends a request to invite the specified AWS accounts to be member accounts in
        the behavior graph.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/detective.html#Detective.Client.create_members)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_detective/client/#create_members)
        """

    def delete_graph(self, *, GraphArn: str) -> None:
        """
        Disables the specified behavior graph and queues it to be deleted.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/detective.html#Detective.Client.delete_graph)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_detective/client/#delete_graph)
        """

    def delete_members(
        self, *, GraphArn: str, AccountIds: Sequence[str]
    ) -> DeleteMembersResponseTypeDef:
        """
        Deletes one or more member accounts from the administrator account's behavior
        graph.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/detective.html#Detective.Client.delete_members)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_detective/client/#delete_members)
        """

    def disassociate_membership(self, *, GraphArn: str) -> None:
        """
        Removes the member account from the specified behavior graph.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/detective.html#Detective.Client.disassociate_membership)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_detective/client/#disassociate_membership)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        Generate a presigned url given a client, its method, and arguments.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/detective.html#Detective.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_detective/client/#generate_presigned_url)
        """

    def get_members(self, *, GraphArn: str, AccountIds: Sequence[str]) -> GetMembersResponseTypeDef:
        """
        Returns the membership details for specified member accounts for a behavior
        graph.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/detective.html#Detective.Client.get_members)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_detective/client/#get_members)
        """

    def list_graphs(
        self, *, NextToken: str = ..., MaxResults: int = ...
    ) -> ListGraphsResponseTypeDef:
        """
        Returns the list of behavior graphs that the calling account is an administrator
        account of.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/detective.html#Detective.Client.list_graphs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_detective/client/#list_graphs)
        """

    def list_invitations(
        self, *, NextToken: str = ..., MaxResults: int = ...
    ) -> ListInvitationsResponseTypeDef:
        """
        Retrieves the list of open and accepted behavior graph invitations for the
        member account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/detective.html#Detective.Client.list_invitations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_detective/client/#list_invitations)
        """

    def list_members(
        self, *, GraphArn: str, NextToken: str = ..., MaxResults: int = ...
    ) -> ListMembersResponseTypeDef:
        """
        Retrieves the list of member accounts for a behavior graph.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/detective.html#Detective.Client.list_members)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_detective/client/#list_members)
        """

    def list_tags_for_resource(self, *, ResourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        Returns the tag values that are assigned to a behavior graph.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/detective.html#Detective.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_detective/client/#list_tags_for_resource)
        """

    def reject_invitation(self, *, GraphArn: str) -> None:
        """
        Rejects an invitation to contribute the account data to a behavior graph.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/detective.html#Detective.Client.reject_invitation)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_detective/client/#reject_invitation)
        """

    def start_monitoring_member(self, *, GraphArn: str, AccountId: str) -> None:
        """
        Sends a request to enable data ingest for a member account that has a status of
        `ACCEPTED_BUT_DISABLED` .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/detective.html#Detective.Client.start_monitoring_member)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_detective/client/#start_monitoring_member)
        """

    def tag_resource(self, *, ResourceArn: str, Tags: Mapping[str, str]) -> Dict[str, Any]:
        """
        Applies tag values to a behavior graph.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/detective.html#Detective.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_detective/client/#tag_resource)
        """

    def untag_resource(self, *, ResourceArn: str, TagKeys: Sequence[str]) -> Dict[str, Any]:
        """
        Removes tags from a behavior graph.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/detective.html#Detective.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_detective/client/#untag_resource)
        """

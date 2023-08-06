"""
Type annotations for route53-recovery-readiness service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_readiness/client/)

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_route53_recovery_readiness.client import Route53RecoveryReadinessClient

    session = Session()
    client: Route53RecoveryReadinessClient = session.client("route53-recovery-readiness")
    ```
"""
import sys
from typing import Any, Dict, Mapping, Sequence, Type, overload

from botocore.client import BaseClient, ClientMeta

from .paginator import (
    GetCellReadinessSummaryPaginator,
    GetReadinessCheckResourceStatusPaginator,
    GetReadinessCheckStatusPaginator,
    GetRecoveryGroupReadinessSummaryPaginator,
    ListCellsPaginator,
    ListCrossAccountAuthorizationsPaginator,
    ListReadinessChecksPaginator,
    ListRecoveryGroupsPaginator,
    ListResourceSetsPaginator,
    ListRulesPaginator,
)
from .type_defs import (
    CreateCellResponseTypeDef,
    CreateCrossAccountAuthorizationResponseTypeDef,
    CreateReadinessCheckResponseTypeDef,
    CreateRecoveryGroupResponseTypeDef,
    CreateResourceSetResponseTypeDef,
    GetArchitectureRecommendationsResponseTypeDef,
    GetCellReadinessSummaryResponseTypeDef,
    GetCellResponseTypeDef,
    GetReadinessCheckResourceStatusResponseTypeDef,
    GetReadinessCheckResponseTypeDef,
    GetReadinessCheckStatusResponseTypeDef,
    GetRecoveryGroupReadinessSummaryResponseTypeDef,
    GetRecoveryGroupResponseTypeDef,
    GetResourceSetResponseTypeDef,
    ListCellsResponseTypeDef,
    ListCrossAccountAuthorizationsResponseTypeDef,
    ListReadinessChecksResponseTypeDef,
    ListRecoveryGroupsResponseTypeDef,
    ListResourceSetsResponseTypeDef,
    ListRulesResponseTypeDef,
    ListTagsForResourcesResponseTypeDef,
    ResourceTypeDef,
    UpdateCellResponseTypeDef,
    UpdateReadinessCheckResponseTypeDef,
    UpdateRecoveryGroupResponseTypeDef,
    UpdateResourceSetResponseTypeDef,
)

if sys.version_info >= (3, 9):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("Route53RecoveryReadinessClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Mapping[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class Route53RecoveryReadinessClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-readiness.html#Route53RecoveryReadiness.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_readiness/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        Route53RecoveryReadinessClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-readiness.html#Route53RecoveryReadiness.Client.exceptions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_readiness/client/#exceptions)
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-readiness.html#Route53RecoveryReadiness.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_readiness/client/#can_paginate)
        """
    def create_cell(
        self, *, CellName: str, Cells: Sequence[str] = ..., Tags: Mapping[str, str] = ...
    ) -> CreateCellResponseTypeDef:
        """
        Creates a new Cell.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-readiness.html#Route53RecoveryReadiness.Client.create_cell)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_readiness/client/#create_cell)
        """
    def create_cross_account_authorization(
        self, *, CrossAccountAuthorization: str
    ) -> CreateCrossAccountAuthorizationResponseTypeDef:
        """
        Create a new cross account readiness authorization.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-readiness.html#Route53RecoveryReadiness.Client.create_cross_account_authorization)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_readiness/client/#create_cross_account_authorization)
        """
    def create_readiness_check(
        self, *, ReadinessCheckName: str, ResourceSetName: str, Tags: Mapping[str, str] = ...
    ) -> CreateReadinessCheckResponseTypeDef:
        """
        Creates a new Readiness Check.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-readiness.html#Route53RecoveryReadiness.Client.create_readiness_check)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_readiness/client/#create_readiness_check)
        """
    def create_recovery_group(
        self, *, RecoveryGroupName: str, Cells: Sequence[str] = ..., Tags: Mapping[str, str] = ...
    ) -> CreateRecoveryGroupResponseTypeDef:
        """
        Creates a new Recovery Group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-readiness.html#Route53RecoveryReadiness.Client.create_recovery_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_readiness/client/#create_recovery_group)
        """
    def create_resource_set(
        self,
        *,
        ResourceSetName: str,
        ResourceSetType: str,
        Resources: Sequence["ResourceTypeDef"],
        Tags: Mapping[str, str] = ...
    ) -> CreateResourceSetResponseTypeDef:
        """
        Creates a new Resource Set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-readiness.html#Route53RecoveryReadiness.Client.create_resource_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_readiness/client/#create_resource_set)
        """
    def delete_cell(self, *, CellName: str) -> None:
        """
        Deletes an existing Cell.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-readiness.html#Route53RecoveryReadiness.Client.delete_cell)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_readiness/client/#delete_cell)
        """
    def delete_cross_account_authorization(
        self, *, CrossAccountAuthorization: str
    ) -> Dict[str, Any]:
        """
        Delete cross account readiness authorization See also: [AWS API
        Documentation](https://docs.aws.amazon.com/goto/WebAPI/route53-recovery-
        readiness-2019-12-02/DeleteCrossAccountAuthorization).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-readiness.html#Route53RecoveryReadiness.Client.delete_cross_account_authorization)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_readiness/client/#delete_cross_account_authorization)
        """
    def delete_readiness_check(self, *, ReadinessCheckName: str) -> None:
        """
        Deletes an existing Readiness Check.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-readiness.html#Route53RecoveryReadiness.Client.delete_readiness_check)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_readiness/client/#delete_readiness_check)
        """
    def delete_recovery_group(self, *, RecoveryGroupName: str) -> None:
        """
        Deletes an existing Recovery Group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-readiness.html#Route53RecoveryReadiness.Client.delete_recovery_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_readiness/client/#delete_recovery_group)
        """
    def delete_resource_set(self, *, ResourceSetName: str) -> None:
        """
        Deletes an existing Resource Set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-readiness.html#Route53RecoveryReadiness.Client.delete_resource_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_readiness/client/#delete_resource_set)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-readiness.html#Route53RecoveryReadiness.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_readiness/client/#generate_presigned_url)
        """
    def get_architecture_recommendations(
        self, *, RecoveryGroupName: str, MaxResults: int = ..., NextToken: str = ...
    ) -> GetArchitectureRecommendationsResponseTypeDef:
        """
        Returns a collection of recommendations to improve resilliance and readiness
        check quality for a Recovery Group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-readiness.html#Route53RecoveryReadiness.Client.get_architecture_recommendations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_readiness/client/#get_architecture_recommendations)
        """
    def get_cell(self, *, CellName: str) -> GetCellResponseTypeDef:
        """
        Returns information about a Cell.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-readiness.html#Route53RecoveryReadiness.Client.get_cell)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_readiness/client/#get_cell)
        """
    def get_cell_readiness_summary(
        self, *, CellName: str, MaxResults: int = ..., NextToken: str = ...
    ) -> GetCellReadinessSummaryResponseTypeDef:
        """
        Returns information about readiness of a Cell.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-readiness.html#Route53RecoveryReadiness.Client.get_cell_readiness_summary)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_readiness/client/#get_cell_readiness_summary)
        """
    def get_readiness_check(self, *, ReadinessCheckName: str) -> GetReadinessCheckResponseTypeDef:
        """
        Returns information about a ReadinessCheck.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-readiness.html#Route53RecoveryReadiness.Client.get_readiness_check)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_readiness/client/#get_readiness_check)
        """
    def get_readiness_check_resource_status(
        self,
        *,
        ReadinessCheckName: str,
        ResourceIdentifier: str,
        MaxResults: int = ...,
        NextToken: str = ...
    ) -> GetReadinessCheckResourceStatusResponseTypeDef:
        """
        Returns detailed information about the status of an individual resource within a
        Readiness Check's Resource Set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-readiness.html#Route53RecoveryReadiness.Client.get_readiness_check_resource_status)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_readiness/client/#get_readiness_check_resource_status)
        """
    def get_readiness_check_status(
        self, *, ReadinessCheckName: str, MaxResults: int = ..., NextToken: str = ...
    ) -> GetReadinessCheckStatusResponseTypeDef:
        """
        Returns information about the status of a Readiness Check.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-readiness.html#Route53RecoveryReadiness.Client.get_readiness_check_status)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_readiness/client/#get_readiness_check_status)
        """
    def get_recovery_group(self, *, RecoveryGroupName: str) -> GetRecoveryGroupResponseTypeDef:
        """
        Returns information about a Recovery Group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-readiness.html#Route53RecoveryReadiness.Client.get_recovery_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_readiness/client/#get_recovery_group)
        """
    def get_recovery_group_readiness_summary(
        self, *, RecoveryGroupName: str, MaxResults: int = ..., NextToken: str = ...
    ) -> GetRecoveryGroupReadinessSummaryResponseTypeDef:
        """
        Returns information about a Recovery Group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-readiness.html#Route53RecoveryReadiness.Client.get_recovery_group_readiness_summary)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_readiness/client/#get_recovery_group_readiness_summary)
        """
    def get_resource_set(self, *, ResourceSetName: str) -> GetResourceSetResponseTypeDef:
        """
        Returns information about a Resource Set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-readiness.html#Route53RecoveryReadiness.Client.get_resource_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_readiness/client/#get_resource_set)
        """
    def list_cells(
        self, *, MaxResults: int = ..., NextToken: str = ...
    ) -> ListCellsResponseTypeDef:
        """
        Returns a collection of Cells.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-readiness.html#Route53RecoveryReadiness.Client.list_cells)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_readiness/client/#list_cells)
        """
    def list_cross_account_authorizations(
        self, *, MaxResults: int = ..., NextToken: str = ...
    ) -> ListCrossAccountAuthorizationsResponseTypeDef:
        """
        Returns a collection of cross account readiness authorizations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-readiness.html#Route53RecoveryReadiness.Client.list_cross_account_authorizations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_readiness/client/#list_cross_account_authorizations)
        """
    def list_readiness_checks(
        self, *, MaxResults: int = ..., NextToken: str = ...
    ) -> ListReadinessChecksResponseTypeDef:
        """
        Returns a collection of Readiness Checks.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-readiness.html#Route53RecoveryReadiness.Client.list_readiness_checks)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_readiness/client/#list_readiness_checks)
        """
    def list_recovery_groups(
        self, *, MaxResults: int = ..., NextToken: str = ...
    ) -> ListRecoveryGroupsResponseTypeDef:
        """
        Returns a collection of Recovery Groups.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-readiness.html#Route53RecoveryReadiness.Client.list_recovery_groups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_readiness/client/#list_recovery_groups)
        """
    def list_resource_sets(
        self, *, MaxResults: int = ..., NextToken: str = ...
    ) -> ListResourceSetsResponseTypeDef:
        """
        Returns a collection of Resource Sets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-readiness.html#Route53RecoveryReadiness.Client.list_resource_sets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_readiness/client/#list_resource_sets)
        """
    def list_rules(
        self, *, MaxResults: int = ..., NextToken: str = ..., ResourceType: str = ...
    ) -> ListRulesResponseTypeDef:
        """
        Returns a collection of rules that are applied as part of Readiness Checks.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-readiness.html#Route53RecoveryReadiness.Client.list_rules)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_readiness/client/#list_rules)
        """
    def list_tags_for_resources(self, *, ResourceArn: str) -> ListTagsForResourcesResponseTypeDef:
        """
        Returns a list of the tags assigned to the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-readiness.html#Route53RecoveryReadiness.Client.list_tags_for_resources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_readiness/client/#list_tags_for_resources)
        """
    def tag_resource(self, *, ResourceArn: str, Tags: Mapping[str, str]) -> Dict[str, Any]:
        """
        Adds tags to the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-readiness.html#Route53RecoveryReadiness.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_readiness/client/#tag_resource)
        """
    def untag_resource(self, *, ResourceArn: str, TagKeys: Sequence[str]) -> None:
        """
        Removes tags from the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-readiness.html#Route53RecoveryReadiness.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_readiness/client/#untag_resource)
        """
    def update_cell(self, *, CellName: str, Cells: Sequence[str]) -> UpdateCellResponseTypeDef:
        """
        Updates an existing Cell.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-readiness.html#Route53RecoveryReadiness.Client.update_cell)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_readiness/client/#update_cell)
        """
    def update_readiness_check(
        self, *, ReadinessCheckName: str, ResourceSetName: str
    ) -> UpdateReadinessCheckResponseTypeDef:
        """
        Updates an exisiting Readiness Check.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-readiness.html#Route53RecoveryReadiness.Client.update_readiness_check)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_readiness/client/#update_readiness_check)
        """
    def update_recovery_group(
        self, *, Cells: Sequence[str], RecoveryGroupName: str
    ) -> UpdateRecoveryGroupResponseTypeDef:
        """
        Updates an existing Recovery Group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-readiness.html#Route53RecoveryReadiness.Client.update_recovery_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_readiness/client/#update_recovery_group)
        """
    def update_resource_set(
        self, *, ResourceSetName: str, ResourceSetType: str, Resources: Sequence["ResourceTypeDef"]
    ) -> UpdateResourceSetResponseTypeDef:
        """
        Updates an existing Resource Set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-readiness.html#Route53RecoveryReadiness.Client.update_resource_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_readiness/client/#update_resource_set)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["get_cell_readiness_summary"]
    ) -> GetCellReadinessSummaryPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-readiness.html#Route53RecoveryReadiness.Client.get_paginator)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_readiness/client/#get_paginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["get_readiness_check_resource_status"]
    ) -> GetReadinessCheckResourceStatusPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-readiness.html#Route53RecoveryReadiness.Client.get_paginator)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_readiness/client/#get_paginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["get_readiness_check_status"]
    ) -> GetReadinessCheckStatusPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-readiness.html#Route53RecoveryReadiness.Client.get_paginator)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_readiness/client/#get_paginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["get_recovery_group_readiness_summary"]
    ) -> GetRecoveryGroupReadinessSummaryPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-readiness.html#Route53RecoveryReadiness.Client.get_paginator)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_readiness/client/#get_paginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_cells"]) -> ListCellsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-readiness.html#Route53RecoveryReadiness.Client.get_paginator)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_readiness/client/#get_paginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_cross_account_authorizations"]
    ) -> ListCrossAccountAuthorizationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-readiness.html#Route53RecoveryReadiness.Client.get_paginator)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_readiness/client/#get_paginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_readiness_checks"]
    ) -> ListReadinessChecksPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-readiness.html#Route53RecoveryReadiness.Client.get_paginator)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_readiness/client/#get_paginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_recovery_groups"]
    ) -> ListRecoveryGroupsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-readiness.html#Route53RecoveryReadiness.Client.get_paginator)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_readiness/client/#get_paginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_resource_sets"]
    ) -> ListResourceSetsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-readiness.html#Route53RecoveryReadiness.Client.get_paginator)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_readiness/client/#get_paginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_rules"]) -> ListRulesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-readiness.html#Route53RecoveryReadiness.Client.get_paginator)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_readiness/client/#get_paginator)
        """

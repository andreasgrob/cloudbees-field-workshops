"""Generated message classes for workflowexecutions version v1beta.

Execute workflows created with Workflows API.
"""
# NOTE: This file is autogenerated and should not be edited by hand.

from __future__ import absolute_import

from apitools.base.protorpclite import messages as _messages
from apitools.base.py import encoding


package = 'workflowexecutions'


class CancelExecutionRequest(_messages.Message):
  r"""Request for the CancelExecution method."""


class Error(_messages.Message):
  r"""Error describes why the execution was abnormally terminated.

  Fields:
    context: Human readable stack trace string.
    payload: Error message and data returned represented as a JSON string.
    stackTrace: Stack trace with detailed information of where error was
      generated.
  """

  context = _messages.StringField(1)
  payload = _messages.StringField(2)
  stackTrace = _messages.MessageField('StackTrace', 3)


class Execution(_messages.Message):
  r"""A running instance of a [Workflow](/workflows/docs/reference/rest/v1beta
  /projects.locations.workflows).

  Enums:
    StateValueValuesEnum: Output only. Current state of the execution.

  Fields:
    argument: Input parameters of the execution represented as a JSON string.
      The size limit is 32KB. *Note*: If you are using the REST API directly
      to run your workflow, you must escape any JSON string value of
      `argument`. Example:
      `'{"argument":"{\"firstName\":\"FIRST\",\"lastName\":\"LAST\"}"}'`
    endTime: Output only. Marks the end of execution, successful or not.
    error: Output only. The error which caused the execution to finish
      prematurely. The value is only present if the execution's state is
      `FAILED` or `CANCELLED`.
    name: Output only. The resource name of the execution. Format: projects/{p
      roject}/locations/{location}/workflows/{workflow}/executions/{execution}
    result: Output only. Output of the execution represented as a JSON string.
      The value can only be present if the execution's state is `SUCCEEDED`.
    startTime: Output only. Marks the beginning of execution.
    state: Output only. Current state of the execution.
    workflowRevisionId: Output only. Revision of the workflow this execution
      is using.
  """

  class StateValueValuesEnum(_messages.Enum):
    r"""Output only. Current state of the execution.

    Values:
      STATE_UNSPECIFIED: Invalid state.
      ACTIVE: The execution is in progress.
      SUCCEEDED: The execution finished successfully.
      FAILED: The execution failed with an error.
      CANCELLED: The execution was stopped intentionally.
    """
    STATE_UNSPECIFIED = 0
    ACTIVE = 1
    SUCCEEDED = 2
    FAILED = 3
    CANCELLED = 4

  argument = _messages.StringField(1)
  endTime = _messages.StringField(2)
  error = _messages.MessageField('Error', 3)
  name = _messages.StringField(4)
  result = _messages.StringField(5)
  startTime = _messages.StringField(6)
  state = _messages.EnumField('StateValueValuesEnum', 7)
  workflowRevisionId = _messages.StringField(8)


class ListExecutionsResponse(_messages.Message):
  r"""Response for the ListExecutions method.

  Fields:
    executions: The executions which match the request.
    nextPageToken: A token, which can be sent as `page_token` to retrieve the
      next page. If this field is omitted, there are no subsequent pages.
  """

  executions = _messages.MessageField('Execution', 1, repeated=True)
  nextPageToken = _messages.StringField(2)


class StackTrace(_messages.Message):
  r"""A collection of stack elements (frames) where an error occurred.

  Fields:
    elements: An array of Stack elements.
  """

  elements = _messages.MessageField('StackTraceElement', 1, repeated=True)


class StackTraceElement(_messages.Message):
  r"""A single stack element (frame) where an error occurred.

  Fields:
    column: The source code column position (of the line) the current
      instruction was generated from.
    line: The source code line number the current instruction was generated
      from.
    routine: The routine where the error occurred.
    step: The step the error occurred at.
  """

  column = _messages.IntegerField(1)
  line = _messages.IntegerField(2)
  routine = _messages.StringField(3)
  step = _messages.StringField(4)


class StandardQueryParameters(_messages.Message):
  r"""Query parameters accepted by all methods.

  Enums:
    FXgafvValueValuesEnum: V1 error format.
    AltValueValuesEnum: Data format for response.

  Fields:
    f__xgafv: V1 error format.
    access_token: OAuth access token.
    alt: Data format for response.
    callback: JSONP
    fields: Selector specifying which fields to include in a partial response.
    key: API key. Your API key identifies your project and provides you with
      API access, quota, and reports. Required unless you provide an OAuth 2.0
      token.
    oauth_token: OAuth 2.0 token for the current user.
    prettyPrint: Returns response with indentations and line breaks.
    quotaUser: Available to use for quota purposes for server-side
      applications. Can be any arbitrary string assigned to a user, but should
      not exceed 40 characters.
    trace: A tracing token of the form "token:<tokenid>" to include in api
      requests.
    uploadType: Legacy upload protocol for media (e.g. "media", "multipart").
    upload_protocol: Upload protocol for media (e.g. "raw", "multipart").
  """

  class AltValueValuesEnum(_messages.Enum):
    r"""Data format for response.

    Values:
      json: Responses with Content-Type of application/json
      media: Media download with context-dependent Content-Type
      proto: Responses with Content-Type of application/x-protobuf
    """
    json = 0
    media = 1
    proto = 2

  class FXgafvValueValuesEnum(_messages.Enum):
    r"""V1 error format.

    Values:
      _1: v1 error format
      _2: v2 error format
    """
    _1 = 0
    _2 = 1

  f__xgafv = _messages.EnumField('FXgafvValueValuesEnum', 1)
  access_token = _messages.StringField(2)
  alt = _messages.EnumField('AltValueValuesEnum', 3, default='json')
  callback = _messages.StringField(4)
  fields = _messages.StringField(5)
  key = _messages.StringField(6)
  oauth_token = _messages.StringField(7)
  prettyPrint = _messages.BooleanField(8, default=True)
  quotaUser = _messages.StringField(9)
  trace = _messages.StringField(10)
  uploadType = _messages.StringField(11)
  upload_protocol = _messages.StringField(12)


class WorkflowexecutionsProjectsLocationsWorkflowsExecutionsCancelRequest(_messages.Message):
  r"""A WorkflowexecutionsProjectsLocationsWorkflowsExecutionsCancelRequest
  object.

  Fields:
    cancelExecutionRequest: A CancelExecutionRequest resource to be passed as
      the request body.
    name: Required. Name of the execution to be cancelled. Format: projects/{p
      roject}/locations/{location}/workflows/{workflow}/executions/{execution}
  """

  cancelExecutionRequest = _messages.MessageField('CancelExecutionRequest', 1)
  name = _messages.StringField(2, required=True)


class WorkflowexecutionsProjectsLocationsWorkflowsExecutionsCreateRequest(_messages.Message):
  r"""A WorkflowexecutionsProjectsLocationsWorkflowsExecutionsCreateRequest
  object.

  Fields:
    execution: A Execution resource to be passed as the request body.
    parent: Required. Name of the workflow for which an execution should be
      created. Format:
      projects/{project}/locations/{location}/workflows/{workflow} The latest
      revision of the workflow will be used.
  """

  execution = _messages.MessageField('Execution', 1)
  parent = _messages.StringField(2, required=True)


class WorkflowexecutionsProjectsLocationsWorkflowsExecutionsGetRequest(_messages.Message):
  r"""A WorkflowexecutionsProjectsLocationsWorkflowsExecutionsGetRequest
  object.

  Enums:
    ViewValueValuesEnum: Optional. A view defining which fields should be
      filled in the returned execution. The API will default to the FULL view.

  Fields:
    name: Required. Name of the execution to be retrieved. Format: projects/{p
      roject}/locations/{location}/workflows/{workflow}/executions/{execution}
    view: Optional. A view defining which fields should be filled in the
      returned execution. The API will default to the FULL view.
  """

  class ViewValueValuesEnum(_messages.Enum):
    r"""Optional. A view defining which fields should be filled in the
    returned execution. The API will default to the FULL view.

    Values:
      EXECUTION_VIEW_UNSPECIFIED: The default / unset value.
      BASIC: Includes only basic metadata about the execution. Following
        fields are returned: name, start_time, end_time, state and
        workflow_revision_id.
      FULL: Includes all data.
    """
    EXECUTION_VIEW_UNSPECIFIED = 0
    BASIC = 1
    FULL = 2

  name = _messages.StringField(1, required=True)
  view = _messages.EnumField('ViewValueValuesEnum', 2)


class WorkflowexecutionsProjectsLocationsWorkflowsExecutionsListRequest(_messages.Message):
  r"""A WorkflowexecutionsProjectsLocationsWorkflowsExecutionsListRequest
  object.

  Enums:
    ViewValueValuesEnum: Optional. A view defining which fields should be
      filled in the returned executions. The API will default to the BASIC
      view.

  Fields:
    pageSize: Maximum number of executions to return per call. Max supported
      value depends on the selected Execution view: it's 10000 for BASIC and
      100 for FULL. The default value used if the field is not specified is
      100, regardless of the selected view. Values greater than the max value
      will be coerced down to it.
    pageToken: A page token, received from a previous `ListExecutions` call.
      Provide this to retrieve the subsequent page. When paginating, all other
      parameters provided to `ListExecutions` must match the call that
      provided the page token.
    parent: Required. Name of the workflow for which the executions should be
      listed. Format:
      projects/{project}/locations/{location}/workflows/{workflow}
    view: Optional. A view defining which fields should be filled in the
      returned executions. The API will default to the BASIC view.
  """

  class ViewValueValuesEnum(_messages.Enum):
    r"""Optional. A view defining which fields should be filled in the
    returned executions. The API will default to the BASIC view.

    Values:
      EXECUTION_VIEW_UNSPECIFIED: The default / unset value.
      BASIC: Includes only basic metadata about the execution. Following
        fields are returned: name, start_time, end_time, state and
        workflow_revision_id.
      FULL: Includes all data.
    """
    EXECUTION_VIEW_UNSPECIFIED = 0
    BASIC = 1
    FULL = 2

  pageSize = _messages.IntegerField(1, variant=_messages.Variant.INT32)
  pageToken = _messages.StringField(2)
  parent = _messages.StringField(3, required=True)
  view = _messages.EnumField('ViewValueValuesEnum', 4)


encoding.AddCustomJsonFieldMapping(
    StandardQueryParameters, 'f__xgafv', '$.xgafv')
encoding.AddCustomJsonEnumMapping(
    StandardQueryParameters.FXgafvValueValuesEnum, '_1', '1')
encoding.AddCustomJsonEnumMapping(
    StandardQueryParameters.FXgafvValueValuesEnum, '_2', '2')

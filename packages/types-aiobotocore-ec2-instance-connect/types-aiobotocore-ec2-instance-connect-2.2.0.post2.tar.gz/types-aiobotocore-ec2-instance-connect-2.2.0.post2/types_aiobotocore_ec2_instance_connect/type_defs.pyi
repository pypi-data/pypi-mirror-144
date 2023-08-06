"""
Type annotations for ec2-instance-connect service type definitions.

[Open documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_ec2_instance_connect/type_defs/)

Usage::

    ```python
    from types_aiobotocore_ec2_instance_connect.type_defs import ResponseMetadataTypeDef

    data: ResponseMetadataTypeDef = {...}
    ```
"""
import sys
from typing import Dict

from typing_extensions import NotRequired

if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "ResponseMetadataTypeDef",
    "SendSSHPublicKeyRequestRequestTypeDef",
    "SendSSHPublicKeyResponseTypeDef",
    "SendSerialConsoleSSHPublicKeyRequestRequestTypeDef",
    "SendSerialConsoleSSHPublicKeyResponseTypeDef",
)

ResponseMetadataTypeDef = TypedDict(
    "ResponseMetadataTypeDef",
    {
        "RequestId": str,
        "HostId": str,
        "HTTPStatusCode": int,
        "HTTPHeaders": Dict[str, str],
        "RetryAttempts": int,
    },
)

SendSSHPublicKeyRequestRequestTypeDef = TypedDict(
    "SendSSHPublicKeyRequestRequestTypeDef",
    {
        "InstanceId": str,
        "InstanceOSUser": str,
        "SSHPublicKey": str,
        "AvailabilityZone": NotRequired[str],
    },
)

SendSSHPublicKeyResponseTypeDef = TypedDict(
    "SendSSHPublicKeyResponseTypeDef",
    {
        "RequestId": str,
        "Success": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SendSerialConsoleSSHPublicKeyRequestRequestTypeDef = TypedDict(
    "SendSerialConsoleSSHPublicKeyRequestRequestTypeDef",
    {
        "InstanceId": str,
        "SSHPublicKey": str,
        "SerialPort": NotRequired[int],
    },
)

SendSerialConsoleSSHPublicKeyResponseTypeDef = TypedDict(
    "SendSerialConsoleSSHPublicKeyResponseTypeDef",
    {
        "RequestId": str,
        "Success": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

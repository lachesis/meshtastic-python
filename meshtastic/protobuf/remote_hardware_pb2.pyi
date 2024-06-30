"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import google.protobuf.descriptor
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class HardwareMessage(google.protobuf.message.Message):
    """
    An example app to show off the module system. This message is used for
    REMOTE_HARDWARE_APP PortNums.
    Also provides easy remote access to any GPIO.
    In the future other remote hardware operations can be added based on user interest
    (i.e. serial output, spi/i2c input/output).
    FIXME - currently this feature is turned on by default which is dangerous
    because no security yet (beyond the channel mechanism).
    It should be off by default and then protected based on some TBD mechanism
    (a special channel once multichannel support is included?)
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _Type:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _TypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[HardwareMessage._Type.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        UNSET: HardwareMessage._Type.ValueType  # 0
        """
        Unset/unused
        """
        WRITE_GPIOS: HardwareMessage._Type.ValueType  # 1
        """
        Set gpio gpios based on gpio_mask/gpio_value
        """
        WATCH_GPIOS: HardwareMessage._Type.ValueType  # 2
        """
        We are now interested in watching the gpio_mask gpios.
        If the selected gpios change, please broadcast GPIOS_CHANGED.
        Will implicitly change the gpios requested to be INPUT gpios.
        """
        GPIOS_CHANGED: HardwareMessage._Type.ValueType  # 3
        """
        The gpios listed in gpio_mask have changed, the new values are listed in gpio_value
        """
        READ_GPIOS: HardwareMessage._Type.ValueType  # 4
        """
        Read the gpios specified in gpio_mask, send back a READ_GPIOS_REPLY reply with gpio_value populated
        """
        READ_GPIOS_REPLY: HardwareMessage._Type.ValueType  # 5
        """
        A reply to READ_GPIOS. gpio_mask and gpio_value will be populated
        """

    class Type(_Type, metaclass=_TypeEnumTypeWrapper):
        """
        TODO: REPLACE
        """

    UNSET: HardwareMessage.Type.ValueType  # 0
    """
    Unset/unused
    """
    WRITE_GPIOS: HardwareMessage.Type.ValueType  # 1
    """
    Set gpio gpios based on gpio_mask/gpio_value
    """
    WATCH_GPIOS: HardwareMessage.Type.ValueType  # 2
    """
    We are now interested in watching the gpio_mask gpios.
    If the selected gpios change, please broadcast GPIOS_CHANGED.
    Will implicitly change the gpios requested to be INPUT gpios.
    """
    GPIOS_CHANGED: HardwareMessage.Type.ValueType  # 3
    """
    The gpios listed in gpio_mask have changed, the new values are listed in gpio_value
    """
    READ_GPIOS: HardwareMessage.Type.ValueType  # 4
    """
    Read the gpios specified in gpio_mask, send back a READ_GPIOS_REPLY reply with gpio_value populated
    """
    READ_GPIOS_REPLY: HardwareMessage.Type.ValueType  # 5
    """
    A reply to READ_GPIOS. gpio_mask and gpio_value will be populated
    """

    TYPE_FIELD_NUMBER: builtins.int
    GPIO_MASK_FIELD_NUMBER: builtins.int
    GPIO_VALUE_FIELD_NUMBER: builtins.int
    type: global___HardwareMessage.Type.ValueType
    """
    What type of HardwareMessage is this?
    """
    gpio_mask: builtins.int
    """
    What gpios are we changing. Not used for all MessageTypes, see MessageType for details
    """
    gpio_value: builtins.int
    """
    For gpios that were listed in gpio_mask as valid, what are the signal levels for those gpios.
    Not used for all MessageTypes, see MessageType for details
    """
    def __init__(
        self,
        *,
        type: global___HardwareMessage.Type.ValueType = ...,
        gpio_mask: builtins.int = ...,
        gpio_value: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["gpio_mask", b"gpio_mask", "gpio_value", b"gpio_value", "type", b"type"]) -> None: ...

global___HardwareMessage = HardwareMessage
# This file is dual licensed under the terms of the Apache License, Version
# 2.0, and the BSD License. See the LICENSE file in the root of this repository
# for complete details.

try:
    from typing import final
except ImportError:
    from typing_extensions import final


@final
class InfinityType:
    __slots__ = ()

    def __repr__(self) -> str:
        return "Infinity"


@final
class NegativeInfinityType:
    __slots__ = ()

    def __repr__(self) -> str:
        return "-Infinity"


Infinity = InfinityType()
NegativeInfinity = NegativeInfinityType()

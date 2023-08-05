# Copyright: (c) 2022, Swimlane <info@swimlane.com>
# MIT License (see LICENSE or https://opensource.org/licenses/MIT)

from typing import (
    AnyStr,
    List,
)
from attr import (
    define,
    field
)

from .base import CreatedByUser


@define
class UserLight:
    id: AnyStr = field()
    name: AnyStr = field()
    disabled: bool = field()

    def __init__(self, **kwargs):
        from ..base import Base
        Base().scrub(kwargs)
        self.__attrs_init__(**kwargs)

@define
class User(UserLight):
    """A Swimlane User object model
    """
    active: bool = field()
    currentFailedLogInAttempts: int = field()
    displayName: AnyStr = field()
    email: AnyStr = field()
    firstName: AnyStr = field()
    isLdapUser: bool = field()
    isLocked: bool = field()
    isOTPVerified: bool = field()
    isOtpEnforced: bool = field()
    isOtpExempted: bool = field()
    isOtpUser: bool = field()
    isSystemUser: bool = field()
    lastName: AnyStr = field()
    lastPasswordChangedDate: AnyStr = field()
    
    sessionTimeoutType: AnyStr = field()
    timeZoneId: AnyStr = field()
    userName: AnyStr = field()
    passwordComplexityScore: int = field()
    passwordResetRequired: bool = field()
    middleInitial: AnyStr = field(default=None)
    lastLogin: AnyStr = field(default=None)
    primaryGroup: CreatedByUser = field(default={})
    createdByUser: CreatedByUser = field(default={})
    createdDate: AnyStr = field(default='')
    modifiedByUser: CreatedByUser = field(default={})
    modifiedDate: AnyStr = field(default='')
    favorites: dict = field(default={})
    permissions: dict = field(default={})
    roles: List = field(default=[])
    groups: List = field(default=[])

    def __init__(self, **kwargs):
        from ..base import Base
        Base().scrub(kwargs)
        self.__attrs_init__(**kwargs)

    def __attrs_post_init__(self):
        if self.roles:
            role_list = []
            from .role import Role
            for role in self.roles:
                try:
                    role_list.append(Role(**role))
                except Exception as e:
                    raise e
            self.roles = role_list
        if self.groups:
            from .group import Group
            group_list = []
            for group in self.groups:
                try:
                    group_list.append(Group(**group))
                except Exception as e:
                    raise e
            self.groups = group_list

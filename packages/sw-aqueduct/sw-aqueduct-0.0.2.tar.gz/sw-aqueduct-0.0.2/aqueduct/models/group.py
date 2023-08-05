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
class Group:
    """A Swimlane Group object model
    """
    disabled: bool = field()
    id: AnyStr = field()
    name: AnyStr = field()
    description: AnyStr = field(default='')
    createdByUser: CreatedByUser = field(default={})
    createdDate: AnyStr = field(default='')
    modifiedByUser: CreatedByUser = field(default={})
    modifiedDate: AnyStr = field(default='')
    permissions: dict = field(default={})
    roles: List = field(default=[])
    users: List = field(default=[])
    groups: List = field(default=[])

    def __init__(self, **kwargs):
        from ..base import Base
        Base().scrub(kwargs)
        self.__attrs_init__(**kwargs)

    def __attrs_post_init__(self):
        if self.users:
            from .user import User
            user_list = []
            for user in self.users:
                try:
                    user_list.append(User(**user))
                except Exception as e:
                    pass
            self.users = user_list
        if self.groups:
            group_list = []
            for group in self.groups:
                try:
                    group_list.append(Group(**group))
                except Exception as e:
                    raise e
            self.groups = group_list
        if self.roles:
            from .role import Role
            role_list = []
            for role in self.roles:
                try:
                    role_list.append(Role(**role))
                except Exception as e:
                    pass
            self.roles = role_list

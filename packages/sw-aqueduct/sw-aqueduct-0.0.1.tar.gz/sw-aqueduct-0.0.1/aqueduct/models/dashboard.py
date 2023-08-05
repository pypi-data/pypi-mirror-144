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


@define
class ReportItems:
    cardType: AnyStr = field()
    reportId: AnyStr = field()
    id: AnyStr = field()
    name: AnyStr = field()
    description: AnyStr = field()
    autoRefreshMilliseconds: int = field()
    row: int = field()
    col: int = field()
    sizeX: int = field()
    sizeY: int = field()


@define
class Dashboard:
    workspaces: List = field()
    timelineEnabled: bool = field()
    minTimelineDate: AnyStr = field()
    maxTimelineDate: AnyStr = field()
    createdDate: AnyStr = field()
    modifiedDate: AnyStr = field()
    uid: AnyStr = field()
    version: int = field()
    id: AnyStr = field()
    name: AnyStr = field()
    disabled: bool = field()
    description: AnyStr = field(default=None)
    allowed: List = field(default=[])
    permissions: dict = field(default={})
    createdByUser: dict = field(default={})
    modifiedByUser: dict = field(default={})
    timelineFilters: dict = field(default={})
    items: List[ReportItems] = field(default=[])

    def __init__(self, **kwargs):
        from ..base import Base
        Base().scrub(kwargs)
        self.__attrs_init__(**kwargs)

    def __attrs_post_init__(self):
        if self.items:
            item_list = []
            for item in self.items:
                try:
                    item_list.append(ReportItems(**item))
                except Exception as e:
                    pass
            self.items = item_list

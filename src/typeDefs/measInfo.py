from typing import TypedDict, Optional


class IMeasInfo(TypedDict):
    file_tag: str
    entity_tag: str
    metric_name: str
    time_offset_hrs_mins: str
    address: str
    aggregation_strategy: Optional[str]
    equation: Optional[str]

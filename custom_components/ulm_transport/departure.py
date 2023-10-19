#pylint: disable=duplicate-code
from dataclasses import dataclass
from datetime import datetime
import re
from .const import TRANSPORT_TYPE_VISUALS, DEFAULT_ICON


@dataclass
class Departure:
    line_name: str
    line_type: str
    timestamp: int
    time: datetime
    gap: int
    platform: str | None = None
    direction: str | None = None
    icon: str | None = None
    bg_color: str | None = None
    fallback_color: str | None = None

    @classmethod
    def from_dict(cls, source):
        line_type = source.get("VehicleCategory")
        line_visuals = TRANSPORT_TYPE_VISUALS.get(line_type) or {}

        # get timestamp
        time_str = source.get("DepartureTimeActual") or source.get("DepartureTimeScheduled")
        # Parse the timestamp and drop timezone information
        timestamp = datetime.fromisoformat(time_str).replace(tzinfo=None)
        # Get the current time
        now = datetime.now()
        # Calculate the difference in time
        time_difference = now - timestamp
        # Get the total difference in minutes
        gap = int(time_difference.total_seconds() / 60)
        # Format the datetime object to display hour and minute
        time = timestamp.strftime("%H:%M")

        return cls(
            line_name=source.get("RouteName"),
            line_type=line_type,
            gap=gap,
            timestamp=timestamp,
            time=time,
            direction=source.get("DepartureDirectionText"),
            platform=source.get("PlatformName"),
            icon=line_visuals.get("icon") or DEFAULT_ICON,
            bg_color=source.get("line", {}).get("color", {}).get("bg"),
            fallback_color=line_visuals.get("color"),
        )

    def to_dict(self):
        return {
            "line_name": self.line_name,
            "line_type": self.line_type,
            "time": self.time,
            "gap": self.gap,
            "platform": self.platform,
            "direction": self.direction,
            "color": self.fallback_color or self.bg_color,
        }
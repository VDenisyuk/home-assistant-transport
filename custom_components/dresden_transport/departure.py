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
        line_type = source.get("Mot")
        line_visuals = TRANSPORT_TYPE_VISUALS.get(line_type) or {}
        time_str = source.get("RealTime") or source.get("ScheduledTime")
        res = re.search(r'\d+', time_str) 
        time = int(int(res.group()) / 1000)
        gap = round((datetime.fromtimestamp(time) - datetime.now()).total_seconds() / 60)
        return cls(
            line_name=source.get("LineName"),
            line_type=line_type,
            gap=gap,
            timestamp=time,
            time=datetime.fromtimestamp(time).strftime("%H:%M"),
            direction=source.get("Direction"),
            platform=source.get("Platform", {}).get("Name"),
            icon=line_visuals.get("icon") or DEFAULT_ICON,
            bg_color=source.get("line", {}).get("color", {}).get("bg"),
            fallback_color=line_visuals.get("color"),
        )
    @classmethod
    def from_dict_dir(cls, source):
        line_type = source.get("MotChain", [])[0].get("Type")
        line_visuals = TRANSPORT_TYPE_VISUALS.get(line_type) or {}
        time_str = source.get("PartialRoutes",[])[0].get("RegularStops",[])[0].get("DepartureTime")
        line_name = source.get("MotChain", [])[0].get("Name")
        line_type = source.get("MotChain", [])[0].get("Type")
        direction = source.get("MotChain", [])[0].get("Direction")
        platform = source.get("PartialRoutes", [])[0].get("RegularStops", [])[0].get("Platform", {}).get("Name")
        bg_color = source.get("line", {}).get("color", {}).get("bg")
        fallback_color = line_visuals.get("color")
        
        res = re.search(r'\d+', time_str) 
        time = int(int(res.group()) / 1000)
        gap = round((datetime.fromtimestamp(time) - datetime.now()).total_seconds() / 60)
        return cls(
            line_name=line_name,
            line_type=line_type,
            gap=gap,
            timestamp=time,
            time=datetime.fromtimestamp(time).strftime("%H:%M"),
            direction=direction,
            platform=platform,
            icon=line_visuals.get("icon") or DEFAULT_ICON,
            bg_color=bg_color,
            fallback_color=fallback_color,
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

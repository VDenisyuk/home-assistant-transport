#pylint: disable=duplicate-code
from datetime import timedelta

DOMAIN = "dresden_transport"
SCAN_INTERVAL = timedelta(seconds=90)
API_ENDPOINT = "https://webapi.vvo-online.de/dm"
API_MAX_RESULTS = 10

DEFAULT_ICON = "mdi:clock"

CONF_DEPARTURES = "departures"
CONF_DEPARTURES_NAME = "name"
CONF_DEPARTURES_STOP_ID = "stop_id"
CONF_DEPARTURES_WALKING_TIME = "walking_time"
CONF_DEPARTURES_DIRECTION = "direction"
CONF_TYPE_SUBURBAN = "suburban"
CONF_TYPE_SUBWAY = "subway"
CONF_TYPE_TRAM = "Tram"
CONF_TYPE_BUS = "CityBus"
CONF_TYPE_FERRY = "ferry"
CONF_TYPE_EXPRESS = "express"
CONF_TYPE_REGIONAL = "regional"

TRANSPORT_TYPE_VISUALS = {
    CONF_TYPE_SUBURBAN: {
        "code": "S",
        "icon": "mdi:subway-variant",
        "color": "#008D4F",
    },
    CONF_TYPE_SUBWAY: {
        "code": "U",
        "icon": "mdi:subway",
        "color": "#2864A6",
    },
    CONF_TYPE_TRAM: {
        "code": "M",
        "icon": "mdi:tram",
        "color": "#D82020",
    },
    CONF_TYPE_BUS: {
        "code": "BUS",
        "icon": "mdi:bus",
        "color": "#A5027D"
    },
    CONF_TYPE_FERRY: {
        "code": "F",
        "icon": "mdi:ferry",
        "color": "#0080BA"
    },
    CONF_TYPE_EXPRESS: {
        "code": "Train",
        "icon": "mdi:train",
        "color": "#4D4D4D"
    },
    CONF_TYPE_REGIONAL: {
        "code": "RE",
        "icon": "mdi:train",
        "color": "#F01414"
    }
}

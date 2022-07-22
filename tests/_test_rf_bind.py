#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
"""RAMSES RF - a RAMSES-II protocol decoder & analyser.

Test the payload parsers and corresponding output (schema, traits, params, status).
"""

import json
from copy import deepcopy

from serial.tools import list_ports

from ramses_rf.const import SZ_SCHEDULE, SZ_TOTAL_FRAGS, SZ_ZONE_IDX, Code
from ramses_rf.schemas import SZ_DISABLE_DISCOVERY
from ramses_rf.system.schedule import (
    DAY_OF_WEEK,
    ENABLED,
    HEAT_SETPOINT,
    SCH_SCHEDULE_DHW,
    SCH_SCHEDULE_ZON,
    SWITCHPOINTS,
    TIME_OF_DAY,
)

from tests.common import TEST_DIR, load_test_gwy_alt as load_test_gwy

WORK_DIR = f"{TEST_DIR}/rf_engine"


if ports := [c for c in list_ports.comports() if c.device[-7:-1] == "ttyACM"]:
    from ramses_rf import Gateway

    SERIAL_PORT = ports[0].device
    GWY_ID = "01:145038"

else:
    from tests.mock import MockGateway as Gateway

    SERIAL_PORT = "/dev/ttyMOCK"
    GWY_ID = "01:000730"


# import tracemalloc
# tracemalloc.start()


# async def test_ww_0404_zone():

#     gwy, tcs = await load_test_gwy(config={SZ_DISABLE_DISCOVERY: True})
#     await gwy.start(start_discovery=False)  # may: SerialException

#     if tcs.zones:
#         await write_schedule(tcs.zones[0])

#     await gwy.stop()

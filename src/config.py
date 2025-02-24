# System level config
SEED = 10
NUMBER_UE = 20000
# SATELLITE_R = 25 * 1000
SATELLITE_R = 30 * 1000
SATELLITE_V = 7.56 * 1000
SATELLITE_GROUND_DELAY = 3
SATELLITE_SATELLITE_DELAY = 1
CORE_DELAY = 10
DURATION = 22000
RETRANSMIT = True
RETRANSMIT_THRESHOLD = SATELLITE_GROUND_DELAY * 2 + SATELLITE_SATELLITE_DELAY * 2 + 22
MAX_RETRANSMIT = 15
CPU_SCALE = 1
QUEUED_SIZE = 500
GROUP_AREA_L = 1 * 1000 #This is to compare with group handover

# Parameters
#TODO
# 1. The UEs will perform random access only the first time, which means the satellites will first goes to the massive UEs.
# 1.1 If restricting only one random access is weird, we can assign UEs during configuration.
# 2. Handover Decision should be set too.

# This labels the initial position of satellites
HORIZONTAL_DISTANCE = 1.25 * SATELLITE_R
VERTICAL_DISTANCE = 1.25 * SATELLITE_R

POS_SATELLITES = {
     1: (-2*SATELLITE_R, 0),
     2: (-2*SATELLITE_R - HORIZONTAL_DISTANCE , 0),
     3: (-2*SATELLITE_R - 2*HORIZONTAL_DISTANCE, 0),

    # 4: (-2*SATELLITE_R, VERTICAL_DISTANCE),
    # 5: (-2*SATELLITE_R - HORIZONTAL_DISTANCE, VERTICAL_DISTANCE),
    # 6: (-2*SATELLITE_R - 2*HORIZONTAL_DISTANCE, VERTICAL_DISTANCE),
    #
    # 7: (-2*SATELLITE_R, -VERTICAL_DISTANCE),
    # 8: (-2*SATELLITE_R - HORIZONTAL_DISTANCE, -VERTICAL_DISTANCE),
    # 9: (-2*SATELLITE_R - 2*HORIZONTAL_DISTANCE, -VERTICAL_DISTANCE),
 }

MEASUREMENT_REPORT = "MEASUREMENT_REPORT"
HANDOVER_REQUEST = "HANDOVER_REQUEST"
HANDOVER_ACKNOWLEDGE = "HANDOVER_ACKNOWLEDGE"
RRC_RECONFIGURATION = "RRC_RECONFIGURATION"
RRC_RECONFIGURATION_COMPLETE = "RRC_RECONFIGURATION_COMPLETE"
RRC_RECONFIGURATION_COMPLETE_RESPONSE = "RRC_RECONFIGURATION_COMPLETE_RESPONSE"
PATH_SHIFT_REQUEST = "PATH_SHIFT_REQUEST"
RETRANSMISSION = "RETRANSMISSION"
AMF_RESPONSE = "AMF_RESPONSE"

# physical layer: 0.05 ms
# encryption: 0.1 ms
# decryption: 0.1 ms
# logic: 0.05 ms
# hash: 0.05 ms

PROCESSING_TIME = {
    MEASUREMENT_REPORT: 0.35 * CPU_SCALE,
    HANDOVER_REQUEST: 0.3 * CPU_SCALE,
    HANDOVER_ACKNOWLEDGE: 0.3 * CPU_SCALE,
    RRC_RECONFIGURATION_COMPLETE: 0.3 * CPU_SCALE,
    PATH_SHIFT_REQUEST: 0.3,
    RETRANSMISSION: 0.35 * CPU_SCALE,
    AMF_RESPONSE: 0.15 * CPU_SCALE,
}

# TODO Under change, the message and Queue size.
'''
The satellite will handle inter-satellite tasks and Random access request at first priority
Random Access and inter-satellite messages will not be restricted to Queue Size.
because that's not the beginning of a handover.
'''

SATELLITE_CPU = 4
UE_CPU = 4

'''
The below constants defined the state machine of UE
'''
# The UE is actively communicating with source base station
# and the UE has not made any action
ACTIVE = "ACTIVE"
# The UE sent the measurement report and waiting for configuration
WAITING_RRC_CONFIGURATION = "WAITING_RRC_CONFIGURATION"
# The UE lost the connection without being RRC configured
# MEANING that the UE failed to be handoff.
INACTIVE = "INACTIVE"
# The UE has received the RRC configuration message
RRC_CONFIGURED = "RRC_CONFIGURED"
# The UE has sent the random access request with RRC_RECONFIGURATION_COMPLETE
WAITING_RRC_RECONFIGURATION_COMPLETE_RESPONSE = "WAITING_RRC_RECONFIGURATION_COMPLETE_RESPONSE"


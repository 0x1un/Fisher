from enum import Enum



class PendingStatus(Enum):
    Wait = 1
    Success = 2
    Reject = 3
    Cancel = 4


import pythoncom
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import (
    AudioUtilities,
    IAudioEndpointVolume,
)


def set_volume(percent: int):

    pythoncom.CoInitialize()

    if percent < 0:
        percent = 0

    if percent > 100:
        percent = 100

    devices = AudioUtilities.GetSpeakers()

    interface = devices.Activate(
        IAudioEndpointVolume._iid_,
        CLSCTX_ALL,
        None,
    )

    volume = cast(
        interface,
        POINTER(IAudioEndpointVolume),
    )

    volume.SetMasterVolumeLevelScalar(
        percent / 100,
        None,
    )

    return f"Volume set to {percent}%"
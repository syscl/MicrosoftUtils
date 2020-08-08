#!/usr/bin/env python3

import os

# Clean MS 365 in LaunchDaemons
LAUNCH_DAEMONS = [
    "com.microsoft.office.licensingV2.helper.plist",
    "com.microsoft.autoupdate.helper.plist",
    "com.microsoft.onedriveupdaterdaemon.plist",
]
LAUNCH_AGENTS = ["com.microsoft.update.agent.plist"]
PRIVILEGED_HELPER_TOOLS = [
    "com.microsoft.office.licensingV2.helper",
    "com.microsoft.autoupdate.helper",
]
PREFERENCES = ["com.microsoft.office.licensingV2.plist"]
CONTAINER = [
    "com.microsoft.errorreporting",
    "com.microsoft.Excel",
    "com.microsoft.netlib.shipassertprocess",
    "com.microsoft.Office365ServiceV2",
    "com.microsoft.onedrive.findersync",
    "com.microsoft.Outlook",
    "com.microsoft.Powerpoint",
    "com.microsoft.RMS-XPCService",
    "com.microsoft.Word",
    "com.microsoft.onenote.mac",
]
COOKIES = [
    "com.microsoft.onedrive.binarycookies",
    "com.microsoft.onedriveupdater.binarycookies",
]
GROUP_CONTAINERS = [
    "UBF8T346G9.ms",
    "UBF8T346G9.Office",
    "UBF8T346G9.OfficeOneDriveSyncIntegration",
    "UBF8T346G9.OfficeOsfWebHost",
    "UBF8T346G9.OneDriveStandaloneSuite",
]


def remove(path):
    if os.path.isdir(path):
        os.rmdir(path)
    elif os.path.isfile(path):
        os.remove(path)


def rm_r(dir, filenames):
    for f in filenames:
        remove(os.path.join(dir, f))


HOME_LIB: str = os.path.join(os.getenv("HOME"), "Library")
rm_r("/Library/LaunchDaemons", LAUNCH_DAEMONS)
rm_r("/Library/LaunchAgents", LAUNCH_AGENTS)
rm_r("/Library/PrivilegedHelperTools", PRIVILEGED_HELPER_TOOLS)
rm_r(os.path.join(HOME_LIB, "Containers"), CONTAINER)
rm_r(os.path.join(HOME_LIB, "Group Containers"), GROUP_CONTAINERS)
rm_r(os.path.join(HOME_LIB, "COOKIES"), COOKIES)

os.exit(0)

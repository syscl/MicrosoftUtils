# Microsoft Utilities
- A repo to make Microsoft crap easy to use

# Remove Edge from macOS completely (refer [here](https://www.reddit.com/r/MicrosoftEdge/comments/1166b9k/how_to_remove_edge_from_mac_completely/))
One may find that Edge has many residue on the system, you cannot uninstall it completely. Here's how to remove it completely:
- Drag the `Microsoft Edge` to trash then remove it
- Delete itmes:
```
sudo rm -rf /Library/Application\ Suport/Microsoft/MAU2.0
for file in "/Library/Application Suport/Microsoft/MAU2.0" "~/Library/Application Support/Microsoft" "~/Library/Application Support/Microsoft Edge" "/Library/LaunchAgents/com.microsoft/update/agent.plist" "/Library/LaunchDaemons/com.microsoft/autoupdate.helper.plist" sudo rm -rf $file  
```

# Reset/clean Microsoft 365 completely on macOS

Microsoft 365 cannot login to personal account even with reinstalling, this requires a complete clean up in the system. To achieve it, just execute the `clean_ms365_mac.py` on your macOS.

# Disable memory compression 
A direct way to disable memory compression is by disabling the whole superfetch function at once, however, with large memory space on modern laptops nowadays, it is better to keep superfetch on while memory compression off. Because memory compression not only give pressure to CPU but always hits the performance of the system, shorten the battery life, thus I would recommend disable only memory compression feature in powershell by ```Disable-MMAgent```, the options are as following:
```
Disable-MMAgent
       [-ApplicationLaunchPrefetching]
       [-ApplicationPreLaunch]
       [-OperationAPI]
       [-PageCombining]
       [-MemoryCompression]
       [-CimSession <CimSession[]>]
       [-ThrottleLimit <Int32>]
       [-AsJob]
       [<CommonParameters>]
```
To diable memory compression, only type in 
```
Disable-MMAgent -MemoryCompression
```

To ensure the memory features on or off, we can use ```get-mmagent``` command.

# Remove ```Xbox``` crap
```
Get-AppxPackage *Microsoft.XboxApp* | Remove-AppxPackage
```

# Remove ```3D-Object```
Double click the ```remove_3D_Object.reg``` under ```regs``` foler to override the setting in register.

# Remove redudant graphics card options in right click memu
As we know, graphic vendors are willing to add this function to our right click and we barely use it, the problem is that it caused lag and make our right click memu not clean/tidy. So to remove it, run ```clean_graphics_options.cmd``` under ```scripts``` folder as Administration.

# Extract lock screen wallpaper
Run ```extract_lockscreen_wallpaper.ps1``` under ```scripts``` folder

# Remove visual studio right click option
Merge the ```remove_open_vs_option.reg``` from ```regs```

# [NVIDIA Graphics Firmware Update Tool for DisplayPort 1.3 and 1.4 Displays](https://www.nvidia.com/en-us/drivers/nv-uefi-update-x64/)
To enable the latest DisplayPort 1.3 / 1.4 features, your graphics card may require a firmware update.

Without the update, systems that are connected to a DisplayPort 1.3 / 1.4 monitor could experience blank screens on boot until the OS loads, or could experience a hang on boot.

The NVIDIA Firmware Updater will detect whether the firmware update is needed, and if needed, will give the user the option to update it.

If you are currently experiencing a blank screen or hang on boot with a DP 1.3 or 1.4 monitor, please try one of the following workarounds in order to run the tool:

Boot using DVI or HDMI
Boot using a different monitor
Change boot mode from UEFI to Legacy; or Legacy to UEFI.
Boot using an alternate graphics source (secondary or integrated graphics card)
Once you have the tool downloaded, please run the tool and follow the on-screen instructions.

The latest NVIDIA graphics card drivers can be downloaded from: https://www.nvidia.com/Download/index.aspx

For 32-bit NVIDIA Graphics Firmware Update Tool for DisplayPort 1.3 and 1.4, please download here.

# Install latest STMicroelectronics 3-Axis Digital Accelerometer driver for Windows 10 1803+
When updating to 1803 and later, the STMicroelectronics 3-Axis driver from Dell's website did not work properly, so we need a new WHQL driver to resolve this issue.

# Update Windows 10 to Windows 11 without minimal hardware restriction
The easy path reference tools: [MediaCreationTool.bat](https://github.com/AveYo/MediaCreationTool.bat), [Windows11Upgrade](https://github.com/coofcookie/Windows11Upgrade). I used the `MediaCreationTool` to download the ISO, then use `Windows11Upgrade` to load the ISO then update.

# Install Acrobat Reader DC to another partition
- Download and install the [enterprise version](http://get.adobe.com/reader/enterprise/)
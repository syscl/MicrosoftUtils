# Win2Use
- A document notes userful optimizations and tunning for crap Windows.

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

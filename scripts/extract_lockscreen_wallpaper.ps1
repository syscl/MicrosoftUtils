add-type -AssemblyName System.Drawing

New-Item "$($env:USERPROFILE)\Documents\AutoWallpaper" -ItemType directory -Force;

New-Item "$($env:USERPROFILE)\Documents\AutoWallpaper\CopyAssets" -ItemType directory -Force;

New-Item "$($env:USERPROFILE)\Documents\AutoWallpaper\Desktop" -ItemType directory -Force;

New-Item "$($env:USERPROFILE)\Documents\AutoWallpaper\Mobile" -ItemType directory -Force;

foreach($file in (Get-Item "$($env:LOCALAPPDATA)\Packages\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\LocalState\Assets\*"))

{

if ((Get-Item $file).length -lt 100kb) { continue }

Copy-Item $file.FullName "$($env:USERPROFILE)\Documents\AutoWallpaper\CopyAssets\$($file.Name).jpg";

}

foreach($newfile in (Get-Item "$($env:USERPROFILE)\Documents\AutoWallpaper\CopyAssets\*"))

{

$image = New-Object -comObject WIA.ImageFile;

$image.LoadFile($newfile.FullName);

if($image.Width.ToString() -eq "1920"){ Move-Item $newfile.FullName "$($env:USERPROFILE)\Documents\AutoWallpaper\Desktop" -Force; }

elseif($image.Width.ToString() -eq "1080"){ Move-Item $newfile.FullName "$($env:USERPROFILE)\Documents\AutoWallpaper\Mobile" -Force; }

}

Remove-Item "$($env:USERPROFILE)\Documents\AutoWallpaper\CopyAssets";
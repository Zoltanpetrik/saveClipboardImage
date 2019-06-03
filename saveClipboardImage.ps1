Add-Type -AssemblyName System.Windows.Forms

if ($([System.Windows.Forms.Clipboard]::ContainsImage())) {

	$image =    [System.Windows.Forms.Clipboard]::GetImage()
	$filename = (Get-Item -Path ".\").FullName + '\data\' + [guid]::newguid().ToString() + '.png'

	[System.Drawing.Bitmap]$image.Save($filename, [System.Drawing.Imaging.ImageFormat]::Png)

	mspaint "$filename"
	
	"$filename" | clip
} else {
	"nil" | clip
}
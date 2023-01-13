# Blender Screen To Text Addon

## How To Set Up
- Install the source code as a zip file
- Do not unzip
- Open Blender
- Go to Edit/Preferences/Addons and in the top right select install
- Browse to the downloaded zip file
- Install
- The addon should be installed into Blender's script directory and the zip file can be deleted

## How It Works

This addon renders the current viewport (be it in solid view, material preview, or render view) and overlays the screen area with the image converted to ASCII characters. While this works when multiple 3D viewports are open, the overlay will only scale to the size of one of them (allowing the user to specify a window size is in the TO DO list). 

<img width="250" alt="image" src="https://user-images.githubusercontent.com/114180322/212216482-bd1bacdf-e890-48c8-bebd-c4d844621f0d.png">

- Users can specify the set of ASCII text characters to screen project arbitrarily; the text scales left to right as darkest to brightest character. Spaces in the text specifier will be ignored. 
- The activated check box is the only way to turn on and off the addon operator.
- Font proportion will scale the font so that each character is the `overlay size / font porportion`
- The font path allows the user to specify any font to use, however the font will likely need to be monospace in order to function properly
- Lock Camera to View is an already existing Blender function that is useful for this overlay since the projection comes from the camera.
- The graph allows users to manually control how brightness levels will be matched to ASCII characters

<img width="600" alt="image" src="https://user-images.githubusercontent.com/114180322/212220209-a82acec5-5860-416e-bd28-f8bccb957f15.png">

<img width="600" alt="image" src="https://user-images.githubusercontent.com/114180322/212220421-63d5681f-678b-4ccc-b8e9-3c599c82b6a0.png">

## Developement
The current version of the addon is Blender 3.4.1

### To Do:
- ability to render: as a .txt string or actual image
- customizable blank background color
- allow option for user to specify overlay dimensions rather than fit screen as much as possible
- better handling of failed font pathing since only monospaced fonts will work well
- customizable color of the font
- allow user to specify color channel when mapping brightness to ASCII
- dynamicallly change range values of "font sizer" function, right now the max assumed font size is hardcoded at 250

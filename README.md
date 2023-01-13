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

<img width="143" alt="image" src="https://user-images.githubusercontent.com/114180322/212216482-bd1bacdf-e890-48c8-bebd-c4d844621f0d.png">

- Users can specify the set of text characters they to project arbitrarily; the text scales left to right as darkest to brightest character. Spaces in the text specifier will be ignored. 
- The activated check box is the only way to turn on and off the addon.
- Font proportion will scale the font so that each character is the `viewport size / font porportion`
- The font path allows the user to specify any font to use, however they will likely need to be monospace in order to function properly
- Lock Camera to View is an already existing Blender function that is useful for this overlay since the projection comes from the camera.
- The graph allows users to manually control how brightness levels will be matched to ASCII characters

## Developement
The current version of the addon is Blender 3.4.1

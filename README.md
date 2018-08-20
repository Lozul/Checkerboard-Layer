# GIMP Checkerboard-Layer Plugin
A simple plugin for the GIMP image editing app, add a layer to the current image with a checkerboard pattern and a low opacity.

Copyright 2018 Louis Gasnault

![tuto](https://media.giphy.com/media/enreHzbi6nRBcVVmXY/giphy.gif)

## Quickstart
You want an easy way to add a checkerboard pattern to your image in GIMP? This plugin is for you.

**Installing:**

* Download the `CheckerboardLayer.py` file
* Copy it to your home gimp directory for plugins
  * Windows: `C:\Users\username\AppData\Roaming\GIMP\2.10\plug-ins`
  * Linux: `~/.gimp-2.10/plugins`
* Start GIMP

**How to use:**

* Create a new file `File` > `New ...`
* Then go to `Layer` > `Add checkerboard`
* A layer is automatically added to your image with the pattern

![buton](https://media.giphy.com/media/2WGRJlAIMbwAIm99lt/giphy.gif)

**What he do**

* Create a new layer (RGBA) with a configurable opacity
* Fill it with a checkerboard patter based on your foreground and background color
* If your image resolution is under 1000x1000px, the 'white' tiles are erased (bigger, GIMP crashed due to color selection)

**Why?**

This plugin can help people to make pixel-art.

**Report bug:**

job.louisgasnault@gmail.com

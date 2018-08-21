#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is a plug-in for GIMP who add a checkerboard layer, find it here `Layer` > `Add checkerboard`
# Copyright (C) 2018  Louis Gasnault <job.louisgasnault@gmail.com>

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.

from gimpfu import *

def plugin_main(timg, tdrawable, opacity = 15):

  # timg : Current image
  # tdrawable : Curent layer
  # opacity : Opacity of the checkerboard layer
  
  # - Get the width and height of the drawable
  w = tdrawable.width
  h = tdrawable.height
  img = timg

  # - Gret a new layer, with transparency, the chosed opacity and with normal mode, and add it to the image
  layer_one = gimp.Layer(img, "Checkerboard", w, h, RGBA_IMAGE, opacity, 28)
  img.add_layer(layer_one, 0)

  # - Use the plugin checkerboard to generate the pattern, select the background color, erase it, unselect the image
  pdb.plug_in_checkerboard(img, layer_one, 0, 1)
  pdb.gimp_image_select_color(img, 0, layer_one, gimp.get_background())
  pdb.gimp_edit_clear(layer_one)
  pdb.gimp_selection_none(img)

register(
  "addCheckerboard",
  "Add a checkerboard layer",
  "Add a checkerboard layer",
  "Louis Gasnault",
  "Louis Gasnault",
  "2018",
  "<Image>/Layer/Add checkerboard",
  "RGB*, GRAY*",
  [
    (PF_SLIDER, "opacity", "Opacity", 15, (0, 100, 1))
  ],
  [],
  plugin_main)

main()
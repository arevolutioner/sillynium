"""
--------------------------------------------------------------------------------
sillynium.py - Work in Progress Automated python script generator for selenium. 
--------------------------------------------------------------------------------
This script fetches a given website and allows you to draw boxes to it (current)
--------------------------------------------------------------------------------
Copyright (C) <2020>  
<Author/s: sillynium.com, https://github.com/con-dog/sillynium>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
--------------------------------------------------------------------------------
"""
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


# set up webdriver options
options = webdriver.ChromeOptions()
options.headless = False
options.add_argument("--start-fullscreen")
options.add_experimental_option("excludeSwitches", ['enable-automation'])

driver = webdriver.Chrome(
    options=options, executable_path=ChromeDriverManager(log_level=0).install()
    )

# Get URL
driver.get("https://www.google.com/")

# Get document.body scrollheight/scrollwidth
scroll_height = driver.execute_script('return document.body.scrollHeight')
scroll_width = driver.execute_script('return document.body.scrollWidth')

# This is where it gets ugly, brace yourselve's pure HTML/CSS/JS with Python
iframe = """`
<iframe srcdoc=
        '<!DOCTYPE html>
        <html lang="en">
            <head>
                <meta charset="utf-8">
                <title>Paint</title>
                <style>
                    #container { position: relative; }
                #imageView { border: 0px solid #000; }
                #imageTemp { position: absolute; top: 0px; left: 0px; }
                    label {
                        position: relative;
                        z-index: -10000;
                    }
                </style>
            </head>
            <body>
                <label>Drawing tool:
                    <select id="dtool">
                        <option value="rect">Rectangle</option>
                        <option value="pencil">Pencil</option>
                    </select>
                </label>
                <div id="container">""" + f"""
          <canvas id="imageView" width="{scroll_width}" height="{scroll_height}" 
          ></canvas>
          <canvas id="imageTemp" width="{scroll_width}" height="{scroll_height}"
          ></canvas></div>""" + """
                <script>

                    /* © 2009 ROBO Design
 * http://www.robodesign.ro
 */

// Keep everything in anonymous function, called on window load.
if(window.addEventListener) {
window.addEventListener("load", function () {
  var canvas, context, canvaso, contexto;

  // The active tool instance.
  var tool;
  var tool_default = "rect";

  function init () {
    // Find the canvas element.
    canvaso = document.getElementById("imageView");
    if (!canvaso) {
      alert("Error: I cannot find the canvas element!");
      return;
    }

    if (!canvaso.getContext) {
      alert("Error: no canvas.getContext!");
      return;
    }

    // Get the 2D canvas context.
    contexto = canvaso.getContext("2d");
    if (!contexto) {
      alert("Error: failed to getContext!");
      return;
    }

    // Add the temporary canvas.
    var container = canvaso.parentNode;
    canvas = document.createElement("canvas");
    if (!canvas) {
      alert("Error: I cannot create a new canvas element!");
      return;
    }

    canvas.id     = "imageTemp";
    canvas.width  = canvaso.width;
    canvas.height = canvaso.height;
    container.appendChild(canvas);

    context = canvas.getContext("2d");

    // Get the tool select input.
    var tool_select = document.getElementById("dtool");
    if (!tool_select) {
      alert("Error: failed to get the dtool element!");
      return;
    }
    tool_select.addEventListener("change", ev_tool_change, false);

    // Activate the default tool.
    if (tools[tool_default]) {
      tool = new tools[tool_default]();
      tool_select.value = tool_default;
    }

    // Attach the mousedown, mousemove and mouseup event listeners.
    canvas.addEventListener("mousedown", ev_canvas, false);
    canvas.addEventListener("mousemove", ev_canvas, false);
    canvas.addEventListener("mouseup",   ev_canvas, false);
  }

  // The general-purpose event handler. This function just determines the mouse
  // position relative to the canvas element.
  function ev_canvas (ev) {
    if (ev.layerX || ev.layerX == 0) { // Firefox
      ev._x = ev.layerX;
      ev._y = ev.layerY;
    } else if (ev.offsetX || ev.offsetX == 0) { // Opera
      ev._x = ev.offsetX;
      ev._y = ev.offsetY;
    }

    // Call the event handler of the tool.
    var func = tool[ev.type];
    if (func) {
      func(ev);
    }
  }

  // The event handler for any changes made to the tool selector.
  function ev_tool_change (ev) {
    if (tools[this.value]) {
      tool = new tools[this.value]();
    }
  }

  // This function draws the #imageTemp canvas on top of #imageView, after which
  // #imageTemp is cleared. This function is called each time when the user
  // completes a drawing operation.
  function img_update () {
    contexto.drawImage(canvas, 0, 0);
    context.clearRect(0, 0, canvas.width, canvas.height);
  }

  // This object holds the implementation of each drawing tool.
  var tools = {};

  // The drawing pencil.
  tools.pencil = function () {
    var tool = this;
    this.started = false;

    // This is called when you start holding down the mouse button.
    // This starts the pencil drawing.
    this.mousedown = function (ev) {
        context.beginPath();
        context.moveTo(ev._x, ev._y);
        tool.started = true;
    };

    // This function is called every time you move the mouse. Obviously, it only
    // draws if the tool.started state is set to true (when you are holding down
    // the mouse button).
    this.mousemove = function (ev) {
      if (tool.started) {
        context.lineTo(ev._x, ev._y);
        context.stroke();
      }
    };

    // This is called when you release the mouse button.
    this.mouseup = function (ev) {
      if (tool.started) {
        tool.mousemove(ev);
        tool.started = false;
        img_update();
      }
    };
  };

  // The rectangle tool.
  tools.rect = function () {
    var tool = this;
    this.started = false;

    this.mousedown = function (ev) {
      tool.started = true;
      tool.x0 = ev._x;
      tool.y0 = ev._y;
    };

    this.mousemove = function (ev) {
      if (!tool.started) {
        return;
      }

      var x = Math.min(ev._x,  tool.x0),
          y = Math.min(ev._y,  tool.y0),
          w = Math.abs(ev._x - tool.x0),
          h = Math.abs(ev._y - tool.y0);

      context.clearRect(0, 0, canvas.width, canvas.height);

      if (!w || !h) {
        return;
      }

      context.strokeRect(x, y, w, h);
    };

    this.mouseup = function (ev) {
      if (tool.started) {
        tool.mousemove(ev);
        tool.started = false;
        img_update();
      }
    };
  };

  init();

}, false); }




                </script>
            </body>
        </html>'
                scrolling="auto" frameborder="0"
                style="width:100%;
                        height:100vh;
                        border:none;
                        position: absolute;
                        left: 0;
                        top: 0;
                        z-index:1000000"
        ></iframe>`


"""

# Insert the iframe into the current webpage to draw
driver.execute_script(f'document.body.innerHTML += {iframe}')

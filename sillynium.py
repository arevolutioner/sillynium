"""
File to run via cmd line, but a web extension is looking better currently..
"""
import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


# set up webdriver options
options = webdriver.ChromeOptions()
options.headless = False
options.add_experimental_option("excludeSwitches", ['enable-automation'])
# options.add_extension("HTML\Bookmark_extension\Bookmark_extension.crx")

driver = webdriver.Chrome(
    options=options, executable_path=ChromeDriverManager(log_level=0).install()
    )

# First page that opens should have a back ground which gives instructions.
# Or it should just load directly to Sillynium.com to drive page traffic
driver.get("https://www.reddit.com/")

js = """`
<iframe srcdoc=
        '<!DOCTYPE html>
        <html lang="en">
            <head>
                <meta charset="utf-8">
                <title>Paint</title>
                <style>
                    #container { position: relative; }
                #imageView { border: 10px solid #000; }
                #imageTemp { position: absolute; top: 1px; left: 1px; }
                    label {
                        position: relative;
                        z-index: 1;
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
                <div id="container">
                    <canvas id="imageView" width="500" height="2000"></canvas>
                    <canvas id="imageTemp" width="500" height="2000"></canvas>
                </div>
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

driver.execute_script(f'document.body.innerHTML += {js}')

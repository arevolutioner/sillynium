"""
--------------------------------------------------------------------------------
poc.py - A proof of concept for an automated python script generator for
selenium. 
Thank you for your understanding, time, and interest!

For full version please use and contribute to sillynium.py
--------------------------------------------------------------------------------
This script fetches a screenshot of the window view of a given website.
Screenshot is saved locally and opened via opencv. The user draws colored
rectangles over the elements they desire with mouse. Colors are mapped to keys
and actions (1:red:input-text), (2:orange:grab-text), (3:green:click-button).
Press r to clear screen and q to quit drawing. Rectangle coords/colors are
logged as reference to element location on a site. Finally, script is generated
and saved locally based on colors of rectangles & includes boilerplate code.
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

import ctypes
import os
import sys

import cv2
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


URL = "https://www.autoinsurancequotes.com/"  # used as has many element types


def shape_selection(event, x, y, flags, param):
    """
    Monitor mouse events and record coordinates to draw to the screen
    """
    # grab references to the global variables
    global num_rects, ref_point

    # if the left mouse button was clicked, record and cache the starting
    # (x, y) coordinates and indicate that drawing is being performed
    if event == cv2.EVENT_LBUTTONDOWN:
        ref_point = [(x, y)]
        cache_start.append((x, y))

    # if the left mouse button was released record and cache the stop
    # (x, y) coordinates and indicate that drawing is finished
    elif event == cv2.EVENT_LBUTTONUP:
        ref_point.append((x, y))
        cache_stop.append((x, y))

    # draw a rectangle around where the mouse is pressed and dragged
        cv2.rectangle(
            image, ref_point[0], ref_point[1], color=color, thickness=5
            )
        num_rects += 1
        cache_color.append((color))
        cv2.imshow("Sillynium", image)


# step 1: get screensize
user32 = ctypes.windll.user32  # get user screensize (WINDOWS 10)
screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

# step 2: set up webdriver
options = webdriver.ChromeOptions()
options.headless = True
driver = webdriver.Chrome(
    options=options, executable_path=ChromeDriverManager(log_level=0).install()
    )
driver.set_window_size(screensize[0], screensize[1])  # match screensize

# step 3: fetch URL
driver.get(URL)

# step 4: screenshot the page window and save in cwd
driver.find_element_by_tag_name('body').screenshot('page_screenshot.png')

# step 5: retrieve screenshot and draw on it
ref_point = []
cache_start = []
cache_stop = []
cache_color = []

global color, num_rects
color = (0, 0, 0)  # default black for "do nothing"
num_rects = 0

image = cv2.imread("page_screenshot.png")  # load the image
clone = image.copy()  # clone the image
cv2.namedWindow("Sillynium")  # name window "Sillynium"
cv2.setMouseCallback("Sillynium", shape_selection)  # call shape_selection

loop_flag = True

# update image with drawings
while loop_flag:
    # display the image and wait for a keypress / mouse event
    cv2.imshow("Sillynium", image)
    key = cv2.waitKey(1) & 0xFF

    # press 1 to change color to red
    if key == ord("1"):
        color = (0, 0, 255)
        print("Red selected")

    # press 2 to change color to orange
    if key == ord("2"):
        color = (0, 127, 255)
        print("Orange selected")

    # press 3 to change color to green
    if key == ord("3"):
        color = (0, 255, 0)
        print("Green selected")

    # press 'r' to reset the window and caches
    if key == ord("r"):
        image = clone.copy()
        cache_start = []
        cache_stop = []
        cache_color = []

    # press 'q' to break from the loop by setting loop_flag to False
    elif key == ord("q"):
        print("Leaving element selector and generating script!")
        loop_flag = False

# close all open windows for image "Sillynium"
cv2.destroyAllWindows()

# step 6: use the drawn rectangle attributes to update element_finders list
element_finder = []
# loop through all created rectangles
for i in range(num_rects):
    start_x = cache_start[i][0]
    stop_x = cache_stop[i][0]
    start_y = cache_start[i][1]
    stop_y = cache_stop[i][1]
    color = cache_color[i]

    # get centers of each rectangle
    x_center = (start_x + stop_x) // 2  # floored as px must be whole number
    y_center = (start_y + stop_y) // 2  # floored as px must be whole number
    element_finder.append((x_center, y_center, color))

# step 7: write to a local py file aka generate a script
filename = "generated_script.py"  # used as a generic landing point

# write to lines "boiler-plate type code" ideally this would be a configurable
# file rather than harcoded.
with open(filename, 'w') as f:
    f.write(
        "'''\n"
        "Copyright (C) <2020>\n"
        "<Authors: sillynium.com, https:///github.com//con-dog//sillynium, you\n>"
        f"\n{filename} - Hello there! I'm an auto-generated python script!\n\n"
        "I'm not very good just yet, and serve just as a proof of concept.\n"
        "Full version please visit https:///github.com//con-dog//sillynium.git \n\n"
        "But, if you like my lite versionyou can help make me great by\n"
        "\n'''\n\n"
        "from selenium import webdriver\n"
        "from webdriver_manager.chrome import ChromeDriverManager\n\n"
        f"URL = '{URL}'\n\n"
        "options = webdriver.ChromeOptions()\n"
        "options.add_argument('--start-maximized')\n\n"
        "driver = webdriver.Chrome(\n"
        "    options=options, executable_path=ChromeDriverManager().install()"
        "\n)\n"
        "driver.get(URL)\n\n"
        )

    # for each rectangle reference in element_finder...
    for ref in element_finder:
        # get the web element based on the refs (rectangles) x and y values
        element = driver.execute_script(
            """return document.elementFromPoint(arguments[0],arguments[1]);""",
            ref[0], ref[1]
                                        )

        # get elements attributes
        elem_tag_name = element.tag_name
        elem_text = element.text
        elem_id = element.get_attribute('id')
        elem_type = element.get_attribute('type')
        elem_value = element.get_attribute('value')
        elem_class = element.get_attribute('class')
        elem_outer_html = element.get_attribute('outerHTML')

        # now check what to do based on the rectangles color
        # non boiler-plate code
        if ref[2] == (0, 0, 255):  # if rectangle is red
            f.write(
                f"driver.find_element_by_id('{elem_id}').send_keys('12345')\n"
                )
        elif ref[2] == (0, 127, 255):  # if rectangle is orange
            f.write(
                "print(driver.find_element_by_tag_name"
                f"('{elem_tag_name}').text)\n"
                )
        elif ref[2] == (0, 255, 0):  # if rectangle is green
            f.write(
                f"driver.find_element_by_id('{elem_id}').click()\n"
                )

    # boiler-plate to close driver and kill chromedriver.exe
    f.write("driver.close()\n")
    f.write("driver.quit()\n")

driver.close() // close driver
driver.quit() // kill chromdriver process

print(
    f"POC automated Selenium script '{filename}' has been created at location"
    f"\n'{os.getcwd()+'/'+filename}'"
    )

sys.exit()

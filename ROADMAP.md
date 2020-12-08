# ROADMAP

# Table of contents
1. [Proof of Concept](#POC)
2. [Sillynium](#Now)
3. [TODO](#TODO)
4. [Sillynium's Future](#Future)


## 1.0 Proof of Concept <a name="POC"></a>
[concept/poc.py](concept/poc.py) is a proof of concept program. However, it is a good starting point to show the inspiration behind ***sillynium***.

poc.py fetches the desired URL in the background, by running selenium webdriver in headless mode. It then gets a screenshot of the current window *ONLY*.
This screenshot is an *exact* representation of that window. You draw coloured boxes on this screenshot, and as you draw, the coordinates and colours are recorded. 

Each colour has a *different function* - *red* is used for locating "text-input" elements, *green* is used for locating "button" elements, for example. Once drawing is complete, you exit the drawing window, and the recorded coordinates are cross-checked against the actual elements at that position in the headless driver, and the element is returned. This is repeated for all elements. 

Now that we have all the elements (and all their possible attributes if we so desire), we enter the script generating area of the code. The colour of the box is used to tell the script generating part of the program what to do with each element. Back to our *red* example, this tells the script generator *"the element that corresponds to the red box at position (x, y) is an input-text element, so write code to represent that functionality."* This is repeated for each box that was drawn. What you end up with is some boiler-plate code, and your generated code. This is all combined into your brand new selenium automation script called *"generated.py"*.

See [concept/poc.py](concept/poc.py) to run it and test it out. You will discover very quickly that it is limited, and a webpage screenshot is a dead-end. That is why moving forward, sillynium must work by drawing directly to the webpage. See [Sillynium](#Now) about how this can be achieved.

For visual learners, a visual explanation of [concept/poc.py](concept/poc.py) is below:![Proof of Concept Flowchart](concept/poc_flowchart.jpg)


## 2.0 Sillynium <a name="Now"></a>
[sillynium.py](sillynium.py) is the natural extension to the proof of concept, and draws directly to the webpage.

This comes with quite some complexity however. The current working approach to achieve this is as follows:
- Load URL via Selenium Webdriver
- Retrieve webpage body's scrollheight and scrollwidth values
- Inject a transparent iframe into webpage, with dimensions the exact size of the page body
- Set iframe z-index very high, to place it as the top-most element in the page
- The iframe contains an entire inline HTML document as its source
- This HTML src document contains an HTML Canvas + inline JavaScript functions to create the drawing functionality of the iframe

*And as crazy as it sounds*, ***it works!*** The webpage can be drawn on! But there is still work to be done!

The iframe and the HTML content is developed in a completely separate file called [draw_rect.html](HTML\CSS\JS/draw_rect.html). The way to achieve desired functionality is to ensure it works in isolation (ie: If I load [draw_rect.html](HTML\CSS\JS/draw_rect.html), can I draw on the screen?). When this file works, the content is ported over to the [sillynium.py](sillynium.py) file inside the iframe and executed via driver.execute_script().

***Easy right?***

## 3.0 TODO <a name="TODO"></a>
Most of the work TODO is actually on the HTML/CSS/JS side. This work then needs to be ported over to the [sillynium.py](sillynium.py) file. 

Heres a pretty good timeline and idea of what needs to be done - contribute where and if you can!

### 3.1 [draw_rect.html](HTML\CSS\JS/draw_rect.html) - Ensure iframe width/height = webpage scrollwidth/scrollheight ###

### 3.2 Webpage + [draw_rect.html](HTML\CSS\JS/draw_rect.html) - Synchronise iframe scroll with parent window scroll ###

### 3.3 [draw_rect.html](HTML\CSS\JS/draw_rect.html) - Update to remove pencil functionality (not-used) ###

### 3.4 [draw_rect.html](HTML\CSS\JS/draw_rect.html) - Create a draggable toolbar ###

### 3.5 [draw_rect.html](HTML\CSS\JS/draw_rect.html) - Add a simple colour picker (inside toolbar) ###

### 3.6 [draw_rect.html](HTML\CSS\JS/draw_rect.html) - Colour picker to change colour of Box (inside toolbar) ###

### 3.7 [draw_rect.html](HTML\CSS\JS/draw_rect.html) - Collect drawn box/es coordinates + colours ###

### 3.8 [draw_rect.html](HTML\CSS\JS/draw_rect.html) - Create undo function ###

### 3.9 [draw_rect.html](HTML\CSS\JS/draw_rect.html) - Create reset function ###

### 3.10 [draw_rect.html](HTML\CSS\JS/draw_rect.html) - Create finish drawing function ###

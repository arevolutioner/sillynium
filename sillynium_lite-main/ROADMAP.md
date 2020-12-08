# ROADMAP

# Table of contents
1. [Background to sillynium_lite](#POC)
2. [Ideas for sillynium_lite](#ideas)


## 1.0 Proof of Concept <a name="POC"></a>
[sillynium_lite.py](sillynium_lite.py) is a proof of concept program. 
It fetches the desired URL in the background in headless mode. It then gets a screenshot of the current window ONLY, not the whole page (yet)
See [sillynium_lite.py](sillynium_lite.py) to run and test out.

The basic flow of the concept code follows below
![poc_flowchart](images/sillynium_poc_flow.png)


## 2.0 Ideas go here!
From browsing around stack overflow, you can get a full page screenshot including scroll content!
- Have played around with getting an entire body screenshot back, and that worked fine. 

However, the image that gets returned in most cases is far too large to draw to, therefore:
- Need to then create a tkinter/opencv/pygame window that can scroll the length and width of the returned screenshot.
- Or figure out alternative ways
- Or, use the full version 😉

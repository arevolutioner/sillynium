# ROADMAP

# Table of contents
1. [Proof of Concept](#POC)
2. [Sillynium's Future](#Future)


## 1.0 Proof of Concept <a name="POC"></a>
[concept/poc.py](concept/poc.py) is a proof of concept program. It's a good starting point to show the inspiration behind sillynium.

poc.py fetches the desired URL in the background, by running selenium webdriver in headless mode. It then gets a screenshot of the current window *ONLY*, not the whole page.
See [concept/poc.py](concept/poc.py) to run it and test it out. You will discover very quickly that it is limited, and a webpage screenshot is a dead-end. That is why moving forward, sillynium must work by drawing directly to the webpage. See [Sillynium's Future](#Future)

The basic idea of [concept/poc.py](concept/poc.py) is below:
![Proof of Concept Flowchart](concept/sillynium_poc_flow.png)


## 2.0 Sillynium's Future <a name="Future"></a>
From browsing around stack overflow, you can get a full page screenshot including scroll content!
- Have played around with getting an entire body screenshot back, and that worked fine. 

However, the image that gets returned in most cases is far too large to draw to, therefore:
- Need to then create a tkinter/opencv/pygame window that can scroll the length and width of the returned screenshot.
- Or figure out alternative ways
- Or, use the full version 😉

Instructions
-------------------

iframe.html - Contains a simple canvas element that should show a transparent
box with black border on screen. This is a modified version of the opera tut,
and is used while following the tut

test.html - Contains a blank html head and body, with a cyan background.
This is where an inline iframe should be inserted eventually via code

***test_+_iframe.html*** WORKING DO NOT CHANGE - Contains the blank html with the injected iframe.html
if working correctly, should see a cyan background with a small transparent box
with a black border, that can be drawn on. Can also test on live sites via chrome console -> document.body.innerHTML += `<iframe......</iframe>`

Follow this StackOverflow question to insert iframe as html
https://stackoverflow.com/questions/6102636/html-code-as-iframe-source-rather-than-a-url

Changing scrolling to auto is REQUIRED to see/scroll entire iframe

**If there is an error appearing after playing around with iframe, make sure you are ONLY adding FUNCTIONS WITHIN THE <script> ^ </script> TAGS!
This is usually the first thing to fix the error. Next is to ENSURE ALL ''Quotes'' within the script tags are double quotes, as the entire iframe srcdoc is wrapped by single quotes**
-------------------------------------------------------------------------------

Notes
-------------------
When inserting HTML in iframe you must remove ALL ' single quotes and replace
with " double quotes (or vice versa). Then wrap the entire srcdoc in single
quotes(') or vice versa.

Remve bookmarks or just keep the one? Selenium.com? It seems a bit hacky loading
profiles, instead find a way to add a draggable hovering box.

Maybe keep bookmarklets as a way to re-open the dialog boxes if they are closed?
Or, why not just include an extension that can be clicked on that launches the
toolbar?

-------------------------------------------------------------------------------

Plan
-------------------
1) Make parent site white background - DONE
2) Inject purple iframe into parent site with HTML code as src - DONE
3) Match iframe size to that of parent - DONE
4) Test drawing functionality of iframe.html and test_+_iframe.html - DONE
5) Test on a live site - DONE
6) Expand the canvas of the iframe/body/canvas to fill more of screen - DONE
7) Play around with making chrome extensions to hold instructions etc
, Need to check if folder / name already exists!
8) Convert extension to crx file
9) Try to load extension into driver via addEncodedExtensions - FAILS
9.1) Try to load via add_extensions - WORKS
9.2) Maybe add an additional extension that auto opens the bookmark - NOPE
9.3) Or make a user profile and add it to directory - DONE
9.4) Only add bookmarks if they aren't already there - DONE
9.5) Fix bookmark index positions (0-5) - DONE
9.6) Add a way to prevent editing bookmarks? Or not needed?
9.7) Minify / obfuscate bookmarks? 
9.8) Create extension that generates draggable toolbar on click 
toolbar contains all drawing functions, Then allows user to draw to page
10) Add color picker, remove junk code 


-------------------------------------------------------------------------------

Working
-------------------
iframe.html - is currently drawing on a site when opened from file explorer

test_+_iframe.html - is also working!

now testing on a live site..... google.com by adding just the <iframe></iframe>
portion of the test_+_iframe to the site via document.body.innerHTML += `....`
SUCCESS!!!! IT WORKS!!!!

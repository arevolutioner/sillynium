/*
background.js - Created by Connor Talbot for "Sillynium"(C) 3/12/2020 (DDMMYYYY)
*/

// Customised message on open! May need to remove this?
// Or use as a generic welcome? Or just use page back ground as welcome
// and howto?

/*
try{
  alert('Open the Browser Console.');
}catch(e){
}
*/

// Log in developer console
function onBookmarkAdded(bookmarkItem) {
  console.log("Bookmark added with ID: " + bookmarkItem.id, bookmarkItem);
}

// Create the donate bookmark
function createDonateBookmark(){
    chrome.bookmarks.create({
      title: "Donate",
      url: "https://developer.mozilla.org/Add-ons/WebExtensions/API/bookmarks/create",
      parentId: "1" // // Bookmarks bar Id - Add to bookmarks bar directory
    }, onBookmarkAdded);
}

// Create the instructions bookmark
function createInstructionsBookmark(){
    chrome.bookmarks.create({
      title: "Instructions",
      url: "https://developer.mozilla.org/Add-ons/WebExtensions/API/bookmarks/create",
      parentId: "1" // Bookmarks bar Id - Add to bookmarks bar directory
    }, onBookmarkAdded);
}

// Create the options bookmark
function createOptionsBookmark(){
    chrome.bookmarks.create({
      title: "Options",
      url: "https://developer.mozilla.org/Add-ons/WebExtensions/API/bookmarks/create",
      parentId: "1" // Bookmarks bar Id - Add to bookmarks bar directory,
    }, onBookmarkAdded);
}

// Create the share bookmark
function createShareBookmark(){
  chrome.bookmarks.create({
    title: "Share",
    url: "https://www.reddit.com/",
    parentId: "1" // Bookmarks bar Id - Add to bookmarks bar directory
  }, onBookmarkAdded);
}

// Create the sillynium.com bookmark
function createSillyniumBookmark(){
    chrome.bookmarks.create({
      title: "Sillynium.com",
      url: "https://developer.mozilla.org/Add-ons/WebExtensions/API/bookmarks/create",
      parentId: "1" // Bookmarks bar Id - Add to bookmarks bar directory
    }, onBookmarkAdded);
}

// Create the tools bookmark
function createToolsBookmark(){
  chrome.bookmarks.create({
    title: "Tools",
    url: "https://developer.mozilla.org/Add-ons/WebExtensions/API/bookmarks/create",
    parentId: "1" // Bookmarks bar Id - Add to bookmarks bar directory
  }, onBookmarkAdded);
}

// Ensure that core bookmarks are always there, if not, create them. If already
// there, do nothing
function ensureBookmarks(children) {
  var donateFlag = 0;
  var instructionFlag = 0;
  var optionsFlag = 0;
  var shareFlag = 0;
  var sillyniumFlag = 0;
  var toolsFlag = 0;

  for (child of children) {

    if (child.title == "Donate") {
      donateFlag++;
    }
    if (child.title == "Instructions") {
      instructionFlag++;
    }
    if (child.title == "Options") {
      optionsFlag++;
    }
    if (child.title == "Share") {
      shareFlag++;
    }
    if (child.title == "Sillynium.com") {
      sillyniumFlag++;
    }
    if (child.title == "Tools") {
      toolsFlag++;
    }

  }

  if (donateFlag == 0) {
    createDonateBookmark();
  }
  if (instructionFlag == 0) {
    createInstructionsBookmark();
  }

  if (optionsFlag == 0) {
    createOptionsBookmark();
  }

  if (shareFlag == 0) {
    createShareBookmark();
  }
  if (sillyniumFlag == 0) {
    createSillyniumBookmark();
  }
  if (toolsFlag == 0) {
    createToolsBookmark();
  }
}



// Move each child if its title matches and not in correct index position
function moveBookmarks(children) {
    for (child of children) {
      if ((child.title == "Donate") && (child.index != 0)) {
        var movingBookmark = chrome.bookmarks.move(
          child.id,                    // string
          {parentId:"1", index:0}      // object
        )
      }
      if ((child.title == "Instructions") && (child.index != 1)) {
        var movingBookmark = chrome.bookmarks.move(
          child.id,                    // string
          {parentId:"1", index:1}      // object
        )
      }
      if ((child.title == "Options") && (child.index != 2)) {
        var movingBookmark = chrome.bookmarks.move(
          child.id,                    // string
          {parentId:"1", index:2}      // object
        )
      }
      if ((child.title == "Share") && (child.index != 3)) {
        var movingBookmark = chrome.bookmarks.move(
          child.id,                    // string
          {parentId:"1", index:3}      // object
        )
      }
      if ((child.title == "Sillynium.com") && (child.index != 4)) {
        var movingBookmark = chrome.bookmarks.move(
          child.id,                    // string
          {parentId:"1", index:4}      // object
        )
      }
      if ((child.title == "Tools") && (child.index != 5)) {
        var movingBookmark = chrome.bookmarks.move(
          child.id,                    // string
          {parentId:"1", index:5}      // object
        )
      }
    }
}

function onRejected(error) {
  console.log(`An error: ${error}`);
}

// Used for creating/updating
var gettingChildren = chrome.bookmarks.getChildren("1",ensureBookmarks);
// Used for moving to correct indexes
var gettingChildren = chrome.bookmarks.getChildren("1",moveBookmarks);


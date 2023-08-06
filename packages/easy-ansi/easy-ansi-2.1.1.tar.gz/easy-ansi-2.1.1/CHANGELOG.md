# Change Log

## v2.1.1

**Date:** 2022-03-27

**Updates:**

* This is an update to the structure of the source code, to better align with industry best-practices for Python.
* Links to documentation and other resources have changed, and have been updated.
* No fixes or updates are made to any actual functionality. It runs identically to v2.1.

## v2.1

**Date:** 2021-11-13

**New Features:**

* Add ability to set window title to screen.
* Add bell (system beep) feature to screen.

**Fixed:**

* Fix demos to go back to menu instead of exiting, if the screen size is too small.

## v2.0.1

**Date:** 2021-08-14

**Notes:**

* Fixes for PyPI publishing.
* No actual Easy ANSI code fixes.

## v2.0.0

**Date:** 2021-08-14

**Notes:**

* This is a complete refactor / rewrite of Easy ANSI.
  * The code is much cleaner, and much easier to use.
* Going forward, the v2 series of the code is the stable, production-ready version.
* This release is **NOT** backwards compatible with the last stable release, v0.3.
* The last stable release, v0.3, is now considered deprecated.

## v1.0

**Date:** 2021-03-03

**What happened to Version 1.0?**

Version 1.0 was completely written and tested thoroughly.  However, I felt I had not made it "easy" enough to use,
so version 2.0 is the next planned release number, as I refactor the code.

## v0.3

**Date:** 2020-03-04

**New Features:**

* cursor: locate_column(x) - move the cursor to a specified column (x) on the current row.
* cursor: next_line(rows_down) - move the cursor to the beginning of the line which is rows_down.
* cursor: previous_line(rows_up) - move the cursor to the beginning of the line which is rows_up.

**Fixed:**

* Remove cursor.get_location() dependency from screen.clear_line(). The flexibility this was meant to allow did not
  work as intended. The row number must be provided in the method call.
* Documentation fixes.

## v0.2.2

**Date:** 2020-03-02

**Fixed:**

* cursor.locate() depended on cursor.get_location() for flexibility, but this flexibility did not work as intended.
  Removed dependency, and both x and y values are required again.

## v0.2.1

**Date:** 2020-02-27

**Fixed:**

* cursor.get_location() was causing EasyANSI as a whole to not work on Windows.

## v0.2

**Date:** 2020-02-23

**New Features:**

* screen: clear_line(row) - will now clear the line the cursor is on if you do not provide a specific row to clear.
* cursor: get_location() - a new function that will return the x, y coordinates of the cursor.
* cursor: locate(x, y) - only one of x or y is now required, the other value, if not supplied, will use the value of
  the cursor location. 

## v0.1

**Date:** 2020-02-22

Initial Release.

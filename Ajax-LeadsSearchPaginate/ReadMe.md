# Leads Search and Pagination - Ajax Assignment

### What works:
  - [x] Async Filtering of the Leads
  - [x] Pagination - even when the filters are working

### Notes:
+ The delay between typing in the text box and firing an AJAX request is set at half a second (500 milliseconds.) Depending on the sensitivity required and speed of the connections, this can be changed in the JS file.

+ The "keypress" event doesn't detect non-word character keypresses which means losing out on 'Delete'/'Backspace' events. So using "keydown" event handler. However, this would require us to filter the exact keypress events we want to cater to (Alpha, Numeric, Backspace, Space, Delete only) which I have not done yet.

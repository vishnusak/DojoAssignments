# Tunes - Ajax Assignment

### Note:
+ The js file (under app/static/js) has two different ways for overcoming the No-Access-Control-Allow-Origin header problem.
  1. Using the server side URL request using the "requests" library as suggested in the assignment
    - more reading about "requests": http://www.pythonforbeginners.com/requests/using-requests-in-python

  2. Using the client side ajax call with "dataType: 'jsonp'" attribute set. This is an option available when we use jQuery for our AJAX
    - This is currently commented out in my code. To use this, first comment out lines 14 thru 31. Then uncomment lines 35 thru 53

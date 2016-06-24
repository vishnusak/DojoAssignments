# Google Directions - Ajax Assignment

### Note:
+ The js file (under app/static/js) has two different ways for overcoming the No-Access-Control-Allow-Origin header problem.
  1. Using the server side URL request using the "requests" library as suggested in the assignment
    - more reading about "requests": http://www.pythonforbeginners.com/requests/using-requests-in-python

  2. Using the client side ajax call with "dataType: 'jsonp'" attribute. This is an option available when we use jQuery for our AJAX
    - This is currently commented out in my code.
    - Curiously, the JSON returned from google was marked as having a syntax error by my browsers when I got it using this method. But when I got it using the requests.get method, everything worked fine.

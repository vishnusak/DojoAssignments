# MessageBoard - Using NodeJS / ExpressJS / MongoDB

## Feature set/ Requirements
1. Login / Registration Page:
  - Use cases:
    - If user is a new user, allow them to register.
    - If already registered, allow them to login.
      - On successful registration / login redirect them to MessageBoard

  - Validations:
    - **First Name / Last Name**
      - _Alphanumeric starting with an Alphabet_
      - _Between 5 to 15 chars long_
    - **email ID**
      - _Valid email ID_
    - **Password / Confirmation**
      - _Minimum 8 chars_
      - _Should contain atleast 1 Upper case alphabet_
      - _Should contain atleast 1 Special character from among **$ # % @ & ! ~**_
      - _Should contain atleast 1 number_

2. MessageBoard Page:
  - Use cases:
    - Allow logged in users to post messages and/or comments
    - For posting comments, users have to click on the `...` button below the message to expand the comments view for that message
    - Toggle the `...` button to open / close the comments view as required.

  - Validations:
    - _Messages / Comments posted shouldn't be empty_

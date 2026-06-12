# Task 1: Understand the Request-Response Cycle
#
# 1)
# -----------------------        -----------------------        -------------------------       -------------------------       ----------------------------        ----------------------------        ----------------------------        ----------------------------
# -                     -        -                     -        -                       -       -                       -       -                          -        -                          -        -                          -        -                          -
# -                     -        -                     -        -                       -       -                       -       -                          -        -                          -        -    middleware.py         -        -       CLIENT             -
# -   CLIENT            -  -->   -   Authentication/   -  ->    -    URL ROUTER         -  ->   -      views.py         -  ->   -        models.py         -  ->    -        views.py          -    ->  -  (Again Authenticates,   - -->    -   (Receives the response -
# - (Sends Request to   -        -   Security/Session  -        -    (Scans for the     -       -    (Calls the model   -       -   Queries the DB and     -        -   Serializes the values  -        -    verifies session,     -        -       in JSON Format)    -
#       api/course)     -        -     Management      -        -   pattern api/course) -       -        defined)       -       -   returns all the values -        -      and returns         -        -     Encrypts response)   -        -                          -
# -                     -        -                     -        -                       -       -                       -       -                          -        -        response          -        -                          -        -                          -
# -----------------------        -----------------------        -------------------------       -------------------------       ----------------------------        ----------------------------        ----------------------------        ----------------------------
#
#                                       MiddleWare                      SERVER                          Views                           Models                              Views                               MiddleWare                          CLIENT
# 
# -> Client sends a request to http://127.0.0.1:8000/api/course to get the list of course.
# -> Server MiddleWare Authenticates the request and checks if it is a valid request. 
# -> The middleWare creates a JWT session token and stores in localstorage of the client for further authenticates which reduces the db queries and also reduces the handshake between server and client.
# -> UrlRouter in server scans the provided request (api/course) in the url_patterns[] and returns to views.py if it is a valid pattern.
# -> views.py calls the respective model defined and models.py returns the values to views.py and views.py will serialize the values and returns the response to middleware
# -> MiddleWare again authenticates and then checks the session key and encrypts the payload and sends it to the client.
# -> client will then read the JSON response and decrypts the received data and display to the user 
# 
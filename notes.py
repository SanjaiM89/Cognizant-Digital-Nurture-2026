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
# 
# 2) Identify where middleware sits in this cycle. Name two built-in Django middleware classes and describe what each does.
# 
# -> MiddleWare sits between the URL Router and Views. While a request arrives it authenticates and sends to URl Router and to recevies the response
# from views and then again authenticates, ensures security enforces like use fo HTTPS are there and then veirfies the session key and then sends the
# JSON response
# 
# Two Built-in Django MiddleWare
# 
# 1) django.contrib.auth.middleware.AuthenticationMiddleware - It checks if user logged in has a valid session key and adds user object
# to the request
# 2) django.contrib.auth.security.SecurityMiddleware - It enforces HTTPS(TLS/SSL Encryption) and adds x-content-type-options and x-xss-protection
# It protects against most common attacks, it adds http headers to the responses from views.
# 
# 3) WSGI vs ASGI
# 
# WSGI (WebServer Gateway Interface) :-
# -> It handles one request at a time per worker
# -> It cannot handle fullduplex (websocket) or long lived connections
# -> It is an synchronous connection i.e handling one request at a time
# -> It takes more time than ASGI execution and uses more resources
# -> By default Django uses WSGI
# 
# ASGI (Asynchronous GateWay Interface):-
# -> It handles more than one request at a time
# -> It can handle fullduplex or long lived connections
# -> It is an asynchronous type connection and also supports sunchronous code
# -> It uses less resources and produces response time by shorter period
# 
# 4) Explain the MVC pattern, then map it to Django's MVT (Model-View-Template): what does each letter correspond to in Django?
# 
# MVC :-
# 
# M - Model, V - View, C - Controller
# 
# * M(Model) -> It manages the application data, It stores and retrieves the data from the database and it applies logic and rules for the 
#                   requirments of the function
# * V(View) -> It is responsible for displaying the data to the user, It uses render and serializes the data
# * C(Controller) -> It handles the user request. It sends the request to the model, model gets the requested data/value and then sends to the 
#                    data/value to the controller, controller then places the data to the views where views render to display the data
# 
# MVT :-
# 
# M - Model, V - View, T - Template
# 
# Django commonly uses MVT pattern for web appliccations
# 
# * M(Model) -> It manages the application data and data strcutures. It applies logic defined and the rules, it stores and retrieves
#               the data form databases.
# * V(view) -> It handles request and response logic, it is responsible for getting the http request and get the values/data from
#               model and render, serialize the data to display to user.
# * T(Template) -> It is the presentation layer, the html page. It uses Django's Template Language(DTL) for dynamic contents
# django_assessment
Assessment for django rest api endpoints...


Go to api/settings.py and add this app in the INSTALLED_APPS array

'APP',


 open the api/urls.py file and add URLs for the APP app
 
 path('APP/', include('APP.urls')),
 
 

Following Files are from APP.

you can run the server, and go to http://127.0.0.1:8000/APP/document/ 


POST /document will create a new document

GET /document will return all the document

GET document/:id/ will return a single document detail

PUT document/:id/ will update a single document

DELETE document/:id/ will delete a document

django-curriculumvitae
======================

A Django project to build a simple CV or Resumé. 
This project is divided in two parts:

1. *curriculumvitae* is a Django app, just to provide the needed models 
and locales
2. *webproject* is a fully working Django project, including templates, styles,
PDF generation and everything needed to configure your Resumé online in a 
couple of steps.

Requirements
------------
All requirements are listed in ``requirements.txt`` and 
``requirements-webproject.txt``. You can install them just running::

        pip install -r requirements

and, if you want to setup the project, in adition you can run::

        pip install -r requirements-webproject.txt

Installation
------------
Just check it out using git, and inside the project, you can install the app 
using::

        python setup.py install

Languages
---------
There is used django-transmeta for translations. You can check at the 
project's web page for more information about it.
Once django-curriculumvitae is installed, you have to check two things 
before create the database. Make sure you have set the default and available 
languages in your ``settings.py``::

        LANGUAGE_CODE = 'es'
        ugettext = lambda s: s # dummy ugettext function, as django's docs say
        LANGUAGES = (
                ('es', ugettext('Spanish')),
                ('en', ugettext('English')),
        )
        
Loading Sample Data
-------------------
A django command is provided int the *webproject* in order to load some sample 
data, just to test the project (of course, you must create the database first).
This only works if your available languages in your ``settings.py`` are 
``'en'`` and ``'es'``::

        python manage.py sampledata

Google Analytics
----------------
If you want to configure your Google Analytics account, just change the 
value of the variable ``GOOGLE_ANALYTICS_CODE`` in ``settings.py`` from 
``None`` to your webpage's Property ID.::

        GOOGLE_ANALYTICS_CODE = "PP-000000000-0"

PDF Generation
--------------
PDF Generation for your Resumé has been easily added thanks to xhtml2pdf and 
django-xhtml2pdf. If you want to disable this, just change the value for the 
following key in ``settings.py`` to ``False``::

        PDF_AVAILABLE = False

Sample Image Provided
---------------------
* Source: [sampleimage.jpg](http://pasalodos.typepad.com/unexpecteddays/2006/10/basic.html)


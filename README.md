django-curriculumvitae
======================

A Django project to build a simple CV or Resumé

Installation
------------
Requirements are listed in requirements.pip. You can install them just running:
        pip install -r requirements.pip

Languages
---------
There is used django-transmeta for translations. You can check at the project's
web page for more information about it.
Once django-curriculum is installed, you have to check two things before create the database. Make sure you have set the default and available languages in your ``settings.py``::

        LANGUAGE_CODE = 'es'
        ugettext = lambda s: s # dummy ugettext function, as django's docs say
        LANGUAGES = (
                ('es', ugettext('Spanish')),
                ('en', ugettext('English')),
        )
        
Loading Sample Data
-------------------
A django command is provided in order to load some sample data, just to test the project (of course, you must create the database first). This only works if your available languages in your ``settings.py`` are ``'en'`` and ``'es'``

        python manage.py sampledata

Google Analytics
----------------
If you want to configure your Google Analytics account, just change the value of the variable ``GOOGLE_ANALYTICS_CODE`` in ``settings.py`` from ``None`` to your webpage's Property ID.

	GOOGLE_ANALYTICS_CODE = "PP-000000000-0"

PDF Generation
--------------
PDF Generation for your Resumé has been easily added thanks to xhtml2pdf and django-xhtml2pdf. If you want to disable this, just change the value for the following key in ``settings.py`` to ``False``

	PDF_AVAILABLE = False

Sample Image Provided
---------------------
* Source: [sampleimage.jpg](http://pasalodos.typepad.com/unexpecteddays/2006/10/basic.html)


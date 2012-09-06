django-curriculumvitae
======================

A Django project to build a simple CV

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

Sample Image Provided
---------------------
* Source: [sampleimage.jpg](http://pasalodos.typepad.com/unexpecteddays/2006/10/basic.html)


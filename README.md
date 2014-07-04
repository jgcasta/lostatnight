Nightcitiesiss Application for georreferencing cities at night images from ISS
==============================================================================

[![Build Status](https://travis-ci.org/jgcasta/lostatnight.svg?branch=master)](https://travis-ci.org/jgcasta/lostatnight)

Based on PyBossa, this application by [José Gómez Castaño](http://guaix.fis.ucm.es/DarkSkies) allows locate a night city picture taken from International Space Station. The application can be used at [Nigth Cites ISS](http://crowdcrafting.org/app/lostatnight)

This application has three files:

*  createTasks.py: for creating the application in PyBossa, and fill it with some tasks.
*  get_image.py: for provide data images.
*  template.html: the view for every task and deal with the data of the answers.
*  tutorial.html: a simple tutorial for the volunteers.

Testing the application
=======================

You need to install the pybossa-client first (use a virtualenv):

```bash
    $ pip install pybossa-client
```
Then, you can follow the next steps:

*  Create an account in PyBossa
*  Copy under your account profile your API-KEY
*  Run python createTasks.py -u http://crowdcrafting.org -k API-KEY
*  Open with your browser the Applications section and choose the FlickrPerson app. This will open the presenter for this demo application.

Documentation
=============

We recommend that you read the section: [Build with PyBossa](http://docs.pybossa.com/en/latest/build_with_pybossa.html) and follow the [step by step tutorial](http://docs.pybossa.com/en/latest/user/tutorial.html).

**NOTE**: This application uses the [pybossa-client](https://pypi.python.org/pypi/pybossa-client) in order to simplify the development of the application and its usage. Check the [documentation](http://pythonhosted.org/pybossa-client/).


LICENSE
=======

Creative Commons Reconocimiento-NoComercial-CompartirIgual 4.0 Internacional License
[![ScreenShot](http://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png)]




Locating cities at night images from ISS
==============================================================================

[![Build Status](https://travis-ci.org/jgcasta/lostatnight.svg?branch=master)](https://travis-ci.org/jgcasta/lostatnight)

We are members of the  Group of Extragalactic Astrophysics and Astronomical Instrumentation from Universidad Coplutense de Madrid. Among our activities is light pollution study, and the energy consumption derived from it. We use images taken from the International Space Station as part of our investigations, provided by Earth Science and Remote Sensing Unit, NASA-Johnson Space Center

To compare the images with the different light sources on the earth, we need to know the city's location. Due to the large number of images, we need your help. Some of these images are from unknown locations for us, and it is very difficult identify them in the pictures. However, a lot of people around the world will know the cities. We need you identify and connect them with its possition point on a map. This application allows you to do this.

The process is very easy. The ISS image will be loaded in the left pannel and a map on the right one. If we know an approximate position of the center of the picture, the map will be centered, and a whole map will be displayed intead. The aim is try to identify the city. You have some simple tools to make zoomin, zoomout and drag the picture. Even you can rotate it click on Shift and left mouse button. 

When you identify one picture, just click on the map to identify its possition. The longitud and latitud pair of coordinates will appear on the list. If you make a mistake, you can delete one point. Jus select it and click on "Delete".

When you finish, click on Save, and another image will be loaded. If you don't know about the picture, just click on "Don't know"

If you need more information about this picture, you can click on "ISS picture data", and NASA data will be displayed. At last, you also can share it through Twitter

We apreciate your job very much 

Video tutorial
==============
[![ScreenShot](http://i.imgur.com/yzdDI5t.png)](http://www.youtube.com/embed/EugFeBm2hDk)


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

Documentation
=============

We recommend that you read the section: [Build with PyBossa](http://docs.pybossa.com/en/latest/build_with_pybossa.html) and follow the [step by step tutorial](http://docs.pybossa.com/en/latest/user/tutorial.html).

**NOTE**: This application uses the [pybossa-client](https://pypi.python.org/pypi/pybossa-client) in order to simplify the development of the application and its usage. Check the [documentation](http://pythonhosted.org/pybossa-client/).


LICENSE
=======

Creative Commons Reconocimiento-NoComercial-CompartirIgual 4.0 Internacional License
[![ScreenShot](http://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png)]




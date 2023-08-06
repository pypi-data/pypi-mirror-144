.. scalecast documentation master file, created by
   sphinx-quickstart on Fri Jan 21 15:40:54 2022.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Official Docs
==========================

Welcome to the official docs for scalecast, an easy-to-use dynamic forecasting library for time series in Python.

.. image:: https://img.shields.io/badge/python-3.7+-blue.svg
 :target: https://pepy.tech/project/scalecast
.. image:: https://static.pepy.tech/personalized-badge/scalecast?period=total&units=international_system&left_color=black&right_color=brightgreen&left_text=Downloads
 :target: https://pepy.tech/project/scalecast
.. image:: https://static.pepy.tech/personalized-badge/scalecast?period=month&units=international_system&left_color=black&right_color=brightgreen&left_text=Downloads/Month
 :target: https://pepy.tech/project/scalecast

Overview
--------------

:doc:`about`
   Who is this meant for and what sets it apart?

:doc:`installation`
   Base package + dependencies.

:doc:`initialization`
   How to call the object and make forecasts.

:doc:`change_log`
   See what's changed.

Index
------
* :ref:`genindex`

.. Hidden TOCs

.. toctree::
   :maxdepth: 4
   :caption: Overview:
   :hidden:  

   about
   installation
   initialization

.. toctree::
   :maxdepth: 4
   :caption: Examples:
   :hidden: 

   Forecaster/examples/eCommerce
   Forecaster/examples/LSTM

.. toctree::
   :maxdepth: 4
   :caption: Scalecast:
   :hidden:

   Forecaster/ForecasterGlobals
   Forecaster/Forecaster
   Forecaster/MVForecaster
   Forecaster/_forecast
   Forecaster/GridGenerator
   Forecaster/Notebook
   Forecaster/Multiseries

.. toctree::
   :maxdepth: 1
   :caption: ChangeLog:  
   :hidden:

   change_log

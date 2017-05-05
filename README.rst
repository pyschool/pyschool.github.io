===============================
PySchool
===============================


.. image:: https://pyschool.io/img/logo.png
        :target: https://pypi.python.org/pypi/py101


Stories to learn Python stuff. Inspired by the great work made by NodeSchool_.

.. _NodeSchool: https://nodeschool.io/

Write New Stories
-----------------

*“The only way to learn a new programming language is by writing programs in it.”*

\― `Dennis Ritchie <https://wikipedia.org/wiki/Dennis_Ritchie>`_

Pyschool could always use more stories, whether as specific python features,
existing libraries, programming concepts, or even programming concepts not
specific to Python itself like event handling, threading and such. New stories
are always welcome :)

Get Started!
~~~~~~~~~~~~

Ready to write your story? Here's how to set up a story `hipyschool` for local
development. All stories derive from the base Story_ library.

.. _Story: https://github.com/pyschool/story

1. Fork/clone/copy the hipyschool_ or the py101_ repo on Github. Those a
   good examples of simple stories to begin with.

.. _hipyschool: https://github.com/pyschool/hipyschool
.. _py101: https://github.com/sophilabs/py101

3. Install your local copy into a virtualenv. Assuming you have
   virtualenvwrapper installed, this is how you could set up your copy for local
   development::

    $ mkvirtualenv my_python_story
    $ cd my_python_story/
    $ python setup.py develop

3. Create a module for your *Story*. For example ``mystory/__init__.py``.
   Define the ``name``, ``title`` and ``adventures`` variables.
   You will have to use the ``gettext()`` function from ``story.translation``
   to receive translations. More on that below.

4. Create one or more *Adventures*. A story is a collection of one or more
   adventures

   a. Create a module for your adventure for example ``mystory/myfirstadventure``
   b. Create the ```README.rst`` file describing your adventure in the previous
      folder
   c. (Optional) Make an Spanish translation. You must name it ``README.es.rst``
   d. In the ``__init__.py`` file define a class called ``Adventure``, that
      derives from BaseAdventure_.

.. _BaseAdventure: https://github.com/pyschool/story/blob/master/story/adventures.py

5. Since the ``gettext()`` function relies on PyBabel_, so you will have to
   initialize the translation  by running::

   $ make msg-init
   $ make msg-extract

   You should see several files for each language in ``mystory/locale/``
   corresponding for the usages of the ``gettext()`` function. If the command
   fail, try again.

6. (Optional) Modify and add translations in the locale files and then run::

   $ make msg

.. _PyBabel: http://babel.pocoo.org/en/latest/

7. It is recommended to create some unit tests for checking your solutions,
   check that your changes pass flake8 and the tests, including testing other
   Python versions with tox::

    $ flake8 my_python_story tests
    $ python setup.py test or py.test
    $ tox

   To get flake8 and tox, just pip install them into your virtualenv.

10. Commit your changes and push your branch to GitHub::

    $ git add .
    $ git commit -m "Your detailed description of your changes."
    $ git push origin

11. Publish_ your package in pip, so it is available publicly

.. _Publish: http://peterdowns.com/posts/first-time-with-pypi.html

11. `Let us know`_ or submit a pull request to the Pyschool GitHub website
    to update our website to include your story.

.. _`Let us know`: https://twitter.com/pyschool

License
-------

PySchool is Copyright (c) 2015-2017 sophilabs, inc.

About
-----

.. image:: https://s3.amazonaws.com/sophilabs-assets/logo/logo_300x66.gif
    :target: https://sophilabs.co

PySchool is maintained and funded by sophilabs, inc. The names and logos for
sophilabs are trademarks of sophilabs, inc.

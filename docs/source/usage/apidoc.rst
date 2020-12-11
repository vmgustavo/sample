.. _usage-apidoc:

API Doc
--------

API Doc is an extension of SPhinx to automatically generate the RST files for Python modules and it's submodules. The command to use:

.. code-block::

   sphinx-apidoc --force --maxdepth 2 --private --module-first --ext-autodoc --ext-viewcode --ext-todo  -o source/module ../sample

The `API Doc Documentation`_ has explanations for each of the options of the command above, but the most important options are explained below:

* ``-o source/module/apidoc``: specifies the directory to create all the files, this assumes the working directory is the ``docs``;
* ``../sample``: specifies the path to the module to be documented.

.. _`API Doc Documentation`: https://www.sphinx-doc.org/en/master/man/sphinx-apidoc.html'

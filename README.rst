consolemsg
==========

Semantically colorifies console output messages with ANSI codes.

The goal of the module is to centralize how console messages are printed
depending on the intent. Instead of ``print()`` you can use:

-  ``step()``
-  ``error()``
-  ``warn()``
-  ``success()``
-  ``out()``

Also ``fail()`` prints an error and exits.

All consolemsg functions, but ``out``, output to ``sys.stderr``, so they
will be separated from your ``stdout`` when piping.

Extra arguments, will be inserted into the message with format.

For serious logging you should use the ``logging`` standard module. This
is a quick and simple solution make the user aware of the relevance of
the outputs.

Also those functions are Py2 backwards compatible, so you can use them
instead of regular ``print`` to make your code portable.

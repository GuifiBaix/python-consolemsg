Changelog
=========

consolemsg 0.3.1 2019-07-26
---------------------------

-  Minor package metadata fixes (change log added)

consolemsg 0.3.0 2019-07-26
---------------------------

-  Dropped support for Python 2 < 2.7.1 and Python 3 < 3.3
-  Two helpers ``u`` and ``b`` that ensures a conversion to unicode or
   bytes regardles being in Py2 or Py3 and using UTF-8 as default
   encoding.
-  New ``out`` function for undecorated, but still portably unicode
   safe, content to stdout
-  Unicode over pipes without needing PYTHONIOENCODING, defaulting to
   utf-8 instead of ASCII

   -  Respects stdout/stderr encoding when PYTHONIOENCODING or any other
      local settings sets it

-  When first parameter is a Py2 str’s is decoded as unicode using using
   UTF-8
-  First parameter can be any formatable type instead of text

consolemsg 0.2.1 2018-02-06
---------------------------

-  Minor package metadata fixes

consolemsg 0.2.0 2018-02-06
---------------------------

-  Extra arguments are inserted into the first one using ``format``
   templating

consolemsg 0.1.0 2016-01-12
---------------------------

-  Backward support for Py2 (avoid using print to stderr)
-  New function ``success`` to show up successful end of tasks messages
   (green)

consolemsg 0.0.0 unreleased
---------------------------

-  First version with ``step``, ``error``, ``warn`` and ``fail``
-  As part of GuifiBaix software ‘suro’

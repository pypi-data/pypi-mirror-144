..
  This description is automatically generated from README.org file.

PyMongoWatch
============

``pymongowatch`` is an extension for the MongoDB's Python driver
`pymongo <https://pymongo.readthedocs.io/en/stable/>`__ which enable
watching and auditing the underlying operations.

MongoDB Community Server doesn't support
`auditing <https://docs.mongodb.com/manual/core/auditing/>`__ and the
`database
profiler <https://docs.mongodb.com/manual/tutorial/manage-the-database-profiler/>`__
is not very flexible. Basically your only option for filtering is to
collect operations that take longer than a certain value. You can't
easily separate the insert log from the query log or you cannot extract
the operations only for a certain collection or a certain set of
queries.

Furthermore, operations at database level are not always the same as
operations in an application. A very simple operation like fetching
documents with
`find <https://pymongo.readthedocs.io/en/stable/api/pymongo/collection.html#pymongo.collection.Collection.find>`__
may be translated to several
`getMore <https://docs.mongodb.com/manual/reference/command/getMore/>`__
operations at database level.

Therefore, if you want to analyze the user behavior by studying the
database queries, a very simple auditing log for each user search
containing the query itself (possibly with deleting value fields to
protect the users' privacy), the number of the documents read from the
database and its time is all you need.

Doing this at database level is not always feasible and doing it
manually at application level may not be very desirable for the
developers. This is when an intermediate tool at library level comes
handy.

``pymongowatch`` can detect and audit operations at application level
without any modifications to existing applications.

Quick Setup
-----------

First you have to install ``pymongowatch``. It is available at `Python
Package Index (PyPI) <https://pypi.org/project/pymongowatch/>`__ and can
be installed with `pip <https://pip.pypa.io/en/stable/>`__. At a
`virtual environment <https://docs.python.org/3/tutorial/venv.html>`__
or system-wide:

.. code:: shell

   pip install pymongowatch

`Other installation
options <https://github.com/admirito/pymongowatch#other-installation-options>`__
such as Debian packages are available, too.

After basic installation, ``pymongo.watcher`` sub-package will be
available and you have two options to go on:

Option 1: Call the watcher at application startup
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This approach is recommended if you have no restrictions on modifying
the pymongo-based application and you don't want any hacks on the
``pymongo`` itself.

.. code:: python

   from pymongo import watcher

   watcher.patch_pymongo()
   watcher.add_logging_handlers()  # Adds a logging.StreamHandler by default

Of course, you can pass your own customized logging handlers to
``add_logging_handlers`` and add filters and formatters as you wish. See
the following sections for more information.

Option 2: No application modification
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you don't own the application or you don't want to even add a single
line of code to your existing application, ``pymongo_mask`` which is
included in the ``pymongowatch`` package comes handy.

``pymongo_mask`` is a directory with a module ``pymongo.py`` which
emulates the ``pymongo`` package by using the real installed
``pymongo``; So if you add ``pymongo_mask`` directory in your Python
application `search path for
modules <https://docs.python.org/3/library/sys.html#sys.path>`__–in
somewhere with more priority than where the real ``pymongo`` is
installed–the mask will be imported in your application instead of the
real ``pymongo``. Nevertheless the mask will work as a proxy to the real
installed ``pymongo`` and your application should work as usual.

The importation of the pymongo mask will also trigger
``watcher.patch_pymongo()`` automatically, so the watchers will be
enabled without any need to change your application source code or even
``pymongo`` library itself.

Furthermore, the pymongo mask will apply the configuration at
``etc/pymongowatch.yaml`` with
`logging.config.dictConfig <https://docs.python.org/3/library/logging.config.html#logging.config.dictConfig>`__
to the loggers of the watchers. A sample
`etc/pymongowatch.yaml <https://github.com/admirito/pymongowatch/blob/master/etc/pymongowatch.yaml>`__
is included in the ``pymongowatch`` package but you can modify it as
needed. The `yaml <https://en.wikipedia.org/wiki/YAML>`__ configuration
follows the `logging dictionary
schema <https://docs.python.org/3/library/logging.config.html#dictionary-schema-details>`__.

Finally, ``pymongowatch`` package includes a
``pymongowatch-install-mask`` script which can help you enable the
pymongo mask with ease:

.. code:: shell

   pymongowatch-install-mask  # follow the interactive instructions

Usage
-----

``pymongowatch`` implements classes such as ``WatchCursor`` (a subclass
of pymongo's ``cursor``) which if used instead of pymongo's ``cursor``
can emit logs as specified. To do so, you need some workaround to make
pymongo's methods to use ``pymongowatch`` classes instead of its
defaults. The ``patch_pymongo`` function is the method that will call
all the patch methods in ``pymongowatch`` classes to replace the default
pymongo underlying classes:

.. code:: python

   from pymongo import watcher

   watcher.patch_pymongo()

All the ``pymongowatch`` watcher classes will use the logger retrieved
with ``pymongo.watcher.logger.get_log_emitter()`` to emit their logs.
Each module will emit the logs with their
`name <https://docs.python.org/3/tutorial/modules.html>`__. So for
example, all the cursor logs will be emitted under the
``pymongo.watcher.cursor``. So you can apply specific logging
configuration for each module or as all the logs has the prefix
``pymongo.watcher`` as their logger name you can apply global
configuration with that name.

.. code:: python

   import logging

   # The following code is not the recommended method for adding handlers
   # to the pymongowatch loggers and is for illustrative purposes only

   global_logger = logging.getLogger("pymongo.watcher")
   # add a stream log handler globally to watch all the logs on the
   # console
   global_logger.addHandler(logging.StreamHandler())

   cursor_logger = logging.getLogger("pymongo.watcher.cursor")
   # add a file handler specifically for cursor logs to store them in
   # file, too.
   cursor_logger.addHandler(logging.FileHandler("/tmp/watch.log"))

Of course you can apply
`filters <https://docs.python.org/3/library/logging.html#filter-objects>`__
and
`formatters <https://docs.python.org/3/library/logging.html#formatter-objects>`__
or add more
`handlers <https://docs.python.org/3/library/logging.html#handler-objects>`__
as you wish but there are some details that you should take care of. The
easiest way to achieve this is by leveraging the
``add_logging_handlers`` method:

.. code:: python

   from pymongo import watcher

   # Add two handlers to get all the watcher logs both in file and
   # console
   console_handler = logging.StreamHandler()
   global_handler = logging.FileHanlder("/tmp/watcher-all.log")
   watcher.add_logging_handlers(console_handler, global_handler)

   # Add a more customized handler for cursor logs
   cursor_simple_handler = logging.FileHanlder("/tmp/watcher-cursor-simple.log")
   watcher.add_logging_handlers(
       cursor_simple_handler,
       logger_name="pymongo.watcher.cursor",
       formatter="{name} - {watch}")

   # Add a more customized handler for cursor logs
   cursor_customized_handler = logging.FileHanlder(
       "/tmp/watcher-cursor-customized.log")
   watcher.add_logging_handlers(
       cursor_customized_handler,
       logger_name="pymongo.watcher.cursor",
       formatter="{asctime} {name}.{watch.Collection} - {watch.Query} fetched "
                 "{watch.RetrievedCount} in {watch.RetrieveTime} seconds")

   # Add another handler to log the full information for cursors in csv
   cursor_csv_handler = logging.FileHanlder(
       "/tmp/watcher-cursor-csv.log")
   watcher.add_logging_handlers(
       cursor_csv_handler,
       logger_name="pymongo.watcher.cursor",
       formatter="{asctime},{name},{watch.csv}")

Note that using ``add_logging_handlers`` has not only the advantage of
simplicity for adding formatters, but also take care of automatically
adding an extra
`logging.handlers.QueueHandler <https://docs.python.org/3/library/logging.handlers.html#queuehandler>`__
and
`logging.handlers.QueueListener <https://docs.python.org/3/library/logging.handlers.html#queuelistener>`__
for each handler to overcome some log mutation issues we discuss later.
It will also add a couple of customized
`filters <https://docs.python.org/3/library/logging.html#filter-objects>`__
to the ``QueueHandler`` that are necessary to fully take advantage of
``pymongowatch``.

You can set the log format by using
`formatters <https://docs.python.org/3/library/logging.html#formatter-objects>`__
either by passing a string as the ``formatter`` option to the
``add_logging_handlers`` or by creating a ``formatter`` object and using
the handler's
`setFormatter <https://docs.python.org/3/library/logging.html#logging.Handler.setFormatter>`__
method directly. In either case the recommended way is to use ``{``
`style <https://docs.python.org/3/library/logging.html#logging.Formatter>`__.
Specially if you want to access inner values with dot notation e.g.
``watch.Query`` or ``watch.Collection`` other styles such as ``%`` and
``$`` (e.g. ``%(watch.Query)s`` or ``${watch.Query}``) will **NOT**
work.

Another useful feature of Python ``logging`` module is its
`filters <https://docs.python.org/3/library/logging.html#filter-objects>`__.
You can use ``filter`` objects not only to filter unwanted logs but also
to modify the ones that you want. ``add_logging_handlers`` will
automatically add some basic filters (such as ``AddPymongoResults``
which will extract information about ``pymongo`` operations results and
add them to the related log), but you can also add your own filters.

``pymongo.watcher.filters`` module implements a couple of useful
configurable filters such as ``ExpressionFilter``, ``ExecuteFilter`` and
``RateFilter``. The `etc/pymongowatch.yaml <./etc/pymongowatch.yaml>`__
has some examples on how to use them.

You can also develop your own logging filters by sub-classing
`logging.Filter <https://docs.python.org/3/library/logging.html#filter-objects>`__
as usual and access the ``record.watch`` in
`filter <https://docs.python.org/3/library/logging.html#logging.Filter.filter>`__
method for investigating or modifying the watcher attributes such as
``DB``, ``Collection``, ``Query``, etc.

.. code:: python

   import logging

   class SlowQueriesOnNewsCollectionFilter(logging.Filter):
       def filter(self, record):
           watch = getattr(record, "watch", {})
           return (watch.get("Collection") == "news" and
                   watch.get("RetrieveTime", 0) > 10)

Or you can add filters to modify the logs:

.. code:: python

   import logging

   def remove_private_data(data):
       if isinstance(data, dict):
           return {k: remove_private_data(v) for k, v in data.items()}
       elif isinstance(data, list):
           return [remove_private_data(i) for i in data]
       return None

   class UserPrivacyFilter(logging.Filter):
       def filter(self, record):
           watch = getattr(record, "watch", {})
           watch.update(remove_private_data(watch))
           return True

Don't forget to add the defined filters to you handlers:

.. code:: python

   my_handler.addFilter(SlowQueriesOnNewsCollectionFilter)
   my_handler.addFilter(UserPrivacyFilter)

Lastly, you can use Python's great
`logging.conig <https://docs.python.org/3/library/logging.config.html#module-logging.config>`__
module and specially the new flexible
`logging.config.dictConfig <https://docs.python.org/3/library/logging.config.html#logging.config.dictConfig>`__
method to apply all the ``handlers``, ``formatters`` and ``filters`` in
a single configuration file. Custom ``pymongowatch`` configuration can
also be applied in the same dictionary.

``pymongowatch`` has even the required filters implemented in
``pymongo.watcher.filters`` module. To see the examples for the
``dictConfig`` configuration with watcher filters refer to the
``etc/pymongowatch.yaml`` file which will be installed via
``pymongowatch`` (if you are using a virtual environment, it would be
inside the venv directory).

dictConfig configuration
------------------------

There is a ``pymongo.watcher.dictConfig`` method that accepts a
configuration dictionary with almost `the same
specification <https://docs.python.org/3/library/logging.config.html#configuration-dictionary-schema>`__
as ``logging.config.dictConfig``. But it will apply custom configuration
required by ``pymongowatch`` itself.

The ``pymongo.watcher.dictConfig`` will not apply the intended logging
configurations such as ``handlers`` and ``formatters``. Instead, it
reads the special key ``watchers`` from the dictionary and apply the
related configuration for ``pymongowatch``. Although you can use the a
single dictionary with both logging configuration and ``watchers`` key
and apply both ``pymongo.watcher.dictConfig`` and
``logging.config.dictConfig``.

For more information about the ``pymongowatch`` configurations please
refer to the ``watchers`` key inside the example
``etc/pymongowatch.yaml`` file that will be installed alongside the
package.

Mutable vs Immutable Logs
-------------------------

Mutable Logs? Is that a thing?

Usually the good thing about logs is that they are immutable. So if you
see a log you can trust it. This is always true when some atomic
operation happens and you have no concerns about the start and end time
of the operation (and you don't have access to a time machine to travel
to the past and change what happened).

But what if you start an operation which we have no idea when will it
end? Suppose we have queried a very large database for a very slow query
that may take some time to get back the full results. Also, we may use a
cursor in our application to fetch data and the application has some
delays itself and we don't want the slowness of the application to
affect the database auditing.

These are the sort of challenges that ``pymongo.watcher.WatchQueue``
tries to fix.

``pymongowatch`` uses ``pymongo.watcher.logger.WatchMessage`` instead of
strings as log messages as described in `using arbitrary objects as
messages <https://docs.python.org/3/howto/logging.html#using-arbitrary-objects-as-messages>`__
in Python's logging HOWTO. ``WatchMessage`` is a sub-class of Python's
dictionaries which are mutable objects.

``WatchMessage`` instances are the ``{watch}`` templates in the format
strings that we saw earlier. They are a ``dict`` so you can access log
attributes with ``[]`` access e.g. ``watch["Query"]``. For more
convenience while using log formatters ``WatchMessage`` provides
attribute access with dot notation e.g. ``watch.Query`` and one of the
reasons why ``{`` style formatting (which let you use dot notation
access) is recommended for logging formatters.

A ``WatchMessage`` is a mutable object and the watcher classes need to
modify the logs from time to time. For example if you fetch more items
from a cursor, they can update the attributes such as ``RetrieveTime``
or ``RetrievedCount``. So we have flexibility and it is ``pymongowatch``
users decision when to emit the final immutable log with the logger
handlers.

In the old versions of ``pymongowatch``, the watcher classes modified
the ``WatchMessage`` even after the emitting the log, leaving the entire
burden for consistency on the ``WatchQueue``. This approach soon became
problematic in multiprocessing environments where the ``WatchMessage``
in the emitter process differs from the one in the queue process.

In the newer versions, ``WatchMessage`` has a unique identifier
``WatchID`` for the ongoing operation. The watcher classes will not only
mutate the previous ``WatchMessage`` but also re-emit the log again and
again on each update (with an incremental meta-data named
``Iteration``). In this way, even if the log has already stored
somewhere as an immutable object (for example in a file as a log record
or in a separate process as an object that cannot see the modifications
to the original ``WatchMessage``) can still receive the updates.

The pitfall is now we may have thousands of updates and consequently
thousands of logs for each operation. But this problem can easily be
handled by ``WatchQueue`` or an external tool such as
``pymongowatch-csv``.

``WatchQueue`` alongside a
`QueueHandler <https://docs.python.org/3/library/logging.handlers.html#queuehandler>`__
is the right tool to make sure we handle logs at right time. A
``WatchQueue`` works like a priority queue in which the earliest logs
has the higher priority but it can also aggregate the updates for each
operation based on the ``WatchID``.

``WatchQueue`` will update the old iterations with the newer ones and
releases the logs when they have the ``final`` iteration mark or when
they have expired. The ``final`` mark is a special case of ``Iteration``
meta-data in each log that indicates the database operation has finished
and the watcher class will not modify this ``WatchMessage`` (with the
specified ``WatchID``) anymore.

Also it is important to note that the highest priority item (for
retrieval) in the ``WatchQueue`` is not always the earliest generated
log. First, the different operations may take different times, and
second, the watcher classes may assign different expiration times to
each operation.

Finally you can set a ``forced_delay_sec`` to add delay to all the logs
in the queue (for example if you are using logging for analytics and you
do care more about accuracy than delay for the logs). This is an
optional keyword arguments that both ``WatchQueue`` constructor and
``add_logging_handlers`` method that we saw earlier accepts.

The ``add_logging_handlers`` has a ``with_queue`` optional argument
which if is ``True`` (the default), will use
``pymongo.watcher.setup_queue_handler`` to setup a
`QueueHandler <https://docs.python.org/3/library/logging.handlers.html#queuehandler>`__
alongside a started
`QueueListener <https://docs.python.org/3/library/logging.handlers.html#queuelistener>`__
for each handler you specify with a ``WatchQueue`` so you usually don't
have to worry about log mutation if you use ``add_logging_handlers`` to
add your handlers to watcher loggers.

A ``pymongowatch-csv`` script is also available after the
``pymongowatch`` installation that can be used to aggregate all the
iterations of a single operation into a single row when you use the
``csv`` format:

.. code:: shell

   pymongowatch-csv aggr /tmp/watch.csv > /tmp/aggregated-watch.csv

Multiprocessing
---------------

Another useful application of
`QueueHandler <https://docs.python.org/3/library/logging.handlers.html#queuehandler>`__
is its use in `logging to a single file from multiple
processes <https://docs.python.org/3/howto/logging-cookbook.html#logging-to-a-single-file-from-multiple-processes>`__.
For this application you have to use a multiprocessing ``Queue``
alongside the ``QueueHandler``. Fortunately ``WatchQueue`` also supports
multiprocessing. All you have to do is to pass ``True`` as the
``enable_multiprocessing`` argument.

This is useful for example when you have a ``pymongo`` based web
application with several web server processes and you need a process
safe method to store the logs in a single file. Its worth noting that in
such environments using the default value for ``enable_multiprocessing``
i.e. ``False`` will result in total failure in logging because the
default ``Queue`` is not multiprocessing and the ``QueueHandler`` and
the ``QueueListener`` will use different queues in different processes.

Passing ``True`` as ``enable_multiprocessing`` in ``WatchQueue``
constructor will makes the constructor to build and return a `proxy
object <https://docs.python.org/3/library/multiprocessing.html#proxy-objects>`__
from a `customized
manager <https://docs.python.org/3/library/multiprocessing.html#customized-managers>`__
which has its own dedicated process. You can also pass
``enable_multiprocessing`` to ``setup_queue_handler`` and
``add_logging_handlers``:

.. code:: python

   # Extra keyword arguments of `add_logging_handlers` will be passed to
   # the newly created WatchQueue for each handler.
   watcher.add_logging_handlers(enable_multiprocessing=True)

Pymongo Versions
----------------

``pymongowatch`` is not a standalone MongoDB library and it relies on
the the MongoDB's Python driver
`pymongo <https://pymongo.readthedocs.io/en/stable/>`__. But does the
pymongo's version matter?

``pymongowatch`` has been tested with the recent versions of ``pymongo``
i.e. ``3.10`` and the newer ``4`` series but you can use it for other
versions at your own risk. If you have any problems you can open an
issue at the `project's issue
tracker <https://github.com/admirito/pymongowatch/issues>`__.

One known difference between ``pymongo`` versions is that they handle
operation closing differently. For example, ``4`` series close the
cursors more intelligently and you can usually see the ``cursor`` logs
very fast without any need to a explicit timeout whereas any ``3``
series usually an explicit timeout is required.

Other Installation Options
--------------------------

Debian Packages
~~~~~~~~~~~~~~~

If you are a `Debian <https://www.debian.org/>`__-based GNU/Linux
distribution user you are in luck! There is a Debian package maintained
in the `project's debian
branch <https://github.com/admirito/pymongowatch/tree/debian>`__ that
can make your installation even easier.

You can find the binary packages at `mrazavi's pymongowatch
PPA <https://launchpad.net/~mrazavi/+archive/ubuntu/pymongowatch>`__ and
to install it on Ubuntu:

.. code:: shell

   sudo add-apt-repository ppa:mrazavi/pymongowatch
   sudo apt update

   sudo apt install python3-pymongowatch

Roadmap
-------

The project `issue
tracker <https://github.com/admirito/pymongowatch/issues>`__ is the main
location to maintain the details for the future development. But here
the cardinal points will be reviewed briefly.

NOTE
   If you see an ugly TODO list below with oversize items, it's not even
   clear which items are DONE and which ones are still TODO, maybe that
   is because this document is written in
   `org-mode <https://orgmode.org/>`__ but you are seeing a bad render
   e.g. in
   `GitHub <https://github.com/github/markup/blob/master/README.md#markups>`__
   or a converted reStructuredText format e.g. because `the lack of
   org-mode support in
   PyPI <https://packaging.python.org/en/latest/guides/making-a-pypi-friendly-readme/>`__.

   That doesn't make org-mode less lovable or inferior. Anyway `org-mode
   is one of the most reasonable markup languages to use for
   text <https://karl-voit.at/2017/09/23/orgmode-as-markup-only/>`__.
   Why not to use it and brag about it?

DONE Support queries with find
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

DONE Support for basic collection operations `#3 <https://github.com/admirito/pymongowatch/issues/3>`__
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

TODO Support for CommandCursor `#4 <https://github.com/admirito/pymongowatch/issues/4>`__
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

DONE Packaging
~~~~~~~~~~~~~~

#. DONE Implement pip package

#. DONE Implement debian package

#. TODO Automatic execution of tests

DOING Tests
~~~~~~~~~~~

#. DOING Unit Tests

   #. DONE Old Implementation

   #. TODO Update with the latest code

DOING Deployment Tests
~~~~~~~~~~~~~~~~~~~~~~

#. DONE Basic Implementation

#. TODO Add more complex tests

DONE Support for multiprocessing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

DONE Improve mutable logs `#2 <https://github.com/admirito/pymongowatch/issues/2>`__: add a unique ID for each operation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

TODO Documentation
~~~~~~~~~~~~~~~~~~

#. DONE Add a README

#. TODO Add Sphinx generated documents

#. TODO Create an online API reference

About
-----

The ``pymongowatch`` has developed mainly by `Mohammad
Razavi <https://github.com/admirito/>`__.

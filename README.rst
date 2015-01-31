Python-CoffeeScript
===================

Python-CoffeeScript is a bridge to the JS CoffeeScript compiler.

A short example
---------------

::

    >>> import coffeescript
    >>> print(coffeescript.compile('add = (a, b) -> a + b'))
    (function() {
      var add;

      add = function(a, b) {
        return a + b;
      };

    }).call(this);

Installation
------------

::

    $ pip install CoffeeScript

or

::

    $ easy_install CoffeeScript

coffee-script.js
----------------

The latest version of coffee-script.js (the script for browser <script
type="text/coffeescript"> tags) can be download from
http://jashkenas.github.com/coffee-script/

License
-------

Released under the MIT license. See LICENSE for details.

You can download current version of coffee-script.js from
http://jashkenas.github.com/coffee-script/extras/coffee-script.js

Changes
-------

.. raw:: html

   <dl>
   <dt>

1.0.11

.. raw:: html

   <dd>
    

-  Updated coffee-script.js to v1.9.0.
-  Dropped support for Python v2.6 and v3.1.
-  Supported Python v3.3 and v3.4.

.. raw:: html

   <dt>

1.0.10

.. raw:: html

   <dd>
    

-  Updated coffee-script.js to v1.8.0.

.. raw:: html

   <dt>

1.0.9

.. raw:: html

   <dd>
    

-  Updated coffee-script.js to v1.7.1.

.. raw:: html

   <dt>

1.0.8

.. raw:: html

   <dd>
    

-  Updated coffee-script.js to v1.6.3. Added download\_link to setup.py.

.. raw:: html

   <dt>

1.0.7

.. raw:: html

   <dd>
    

-  Updated coffee-script.js to v1.6.1.

.. raw:: html

   <dt>

1.0.6

.. raw:: html

   <dd>
    

-  Updated coffee-script.js to v1.5.0.

.. raw:: html

   <dt>

1.0.5

.. raw:: html

   <dd>
    

-  Made compile\_file to accept plural files and Added some utility
   functions.

.. raw:: html

   <dt>

1.0.4

.. raw:: html

   <dd>
    

-  Updated coffee-script.js to v1.4.0.

.. raw:: html

   <dt>

1.0.3

.. raw:: html

   <dd>
    

-  Updated coffee-script.js to v1.3.3.

.. raw:: html

   <dt>

1.0.2

.. raw:: html

   <dd>
    

-  Updated coffee-script.js to v1.3.1.

.. raw:: html

   <dt>

1.0.1

.. raw:: html

   <dd>
    

-  Fixed some small problem in setup.py.

.. raw:: html

   <dt>

1.0.0

.. raw:: html

   <dd>
    

-  First release.

   .. raw:: html

      </dl>



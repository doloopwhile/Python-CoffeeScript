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

coffeescript.js
---------------

The latest version of coffeescript.js (the script for browser <script
type="text/coffeescript"> tags) can be download from
http://coffeescript.org/v2/browser-compiler/coffeescript.js

License
-------

Released under the MIT license. See LICENSE for details.

Changes
-------

2.0.2
~~~~~

-  Updated README (no code changes).

2.0.1
~~~~~

-  Corrected a bug due to wrong file-path.
-  Made zip-safe.
-  Updated coffeescript.js to v2.0.1.

2.0.0
~~~~~

-  Updated coffeescript.js to v2.0.0.

1.1.2
~~~~~

-  Updated coffee-script.js to v1.10.0.

1.1.1
~~~~~

-  Updated coffee-script.js to v1.9.3.

1.1.0
~~~~~

-  Updated coffee-script.js to v1.9.1.

1.0.11
~~~~~~

-  Updated coffee-script.js to v1.9.0.
-  Dropped support for Python v2.6 and v3.1.
-  Supported Python v3.3 and v3.4.

1.0.10
~~~~~~

-  Updated coffee-script.js to v1.8.0.

1.0.9
~~~~~

-  Updated coffee-script.js to v1.7.1.

1.0.8
~~~~~

-  Updated coffee-script.js to v1.6.3. Added download\_link to setup.py.

1.0.7
~~~~~

-  Updated coffee-script.js to v1.6.1.

1.0.6
~~~~~

-  Updated coffee-script.js to v1.5.0.

1.0.5
~~~~~

-  Made compile\_file to accept plural files and Added some utility
   functions.

1.0.4
~~~~~

-  Updated coffee-script.js to v1.4.0.

1.0.3
~~~~~

-  Updated coffee-script.js to v1.3.3.

1.0.2
~~~~~

-  Updated coffee-script.js to v1.3.1.

1.0.1
~~~~~

-  Fixed some small problem in setup.py.

1.0.0
~~~~~

-  First release.

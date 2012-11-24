Python-CoffeeScript
====================
`Python-CoffeeScript` is a bridge to the JS CoffeeScript compiler.

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
-----------------
The latest version of `coffee-script.js` (the script for browser `<script type="text/coffeescript">` tags)
can be download from http://jashkenas.github.com/coffee-script/

License
--------
Copyright (c) 2012 OMOTO Kenji.
Released under the MIT license. See `LICENSE` for details.

You can download current version of `coffee-script.js` from
http://jashkenas.github.com/coffee-script/extras/coffee-script.js

Changes
-------
1.0.5
  Made compile_file to accept plural files and Added some utility functions.
1.0.4
  Updated coffee-script.js to v1.4.0.
1.0.3
  Updated coffee-script.js to v1.3.3.
1.0.2
  Updated coffee-script.js to v1.3.1.
1.0.1
  Fixed some small problem in setup.py.
1.0.0
  First release.

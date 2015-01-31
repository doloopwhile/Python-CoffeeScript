Python-CoffeeScript
===================

Python-CoffeeScript is a bridge to the JS CoffeeScript compiler.

A short example
---------------

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

    $ pip install CoffeeScript

or

    $ easy_install CoffeeScript

coffee-script.js
----------------

The latest version of coffee-script.js (the script for browser
\<script type="text/coffeescript"\> tags) can be download from
<http://jashkenas.github.com/coffee-script/>

License
-------

Released under the MIT license. See LICENSE for details.

You can download current version of coffee-script.js from
<http://jashkenas.github.com/coffee-script/extras/coffee-script.js>

Changes
-------

<dl>
<dt>1.0.10
<dd>
 - Updated coffee-script.js to v1.8.0.

<dt>1.0.9
<dd>
 - Updated coffee-script.js to v1.7.1.

<dt>1.0.8
<dd>
 - Updated coffee-script.js to v1.6.3. Added download\_link to setup.py.

<dt>1.0.7
<dd>
 - Updated coffee-script.js to v1.6.1.

<dt>1.0.6
<dd>
 - Updated coffee-script.js to v1.5.0.

<dt>1.0.5
<dd>
 - Made compile\_file to accept plural files and Added some utility functions.

<dt>1.0.4
<dd>
 - Updated coffee-script.js to v1.4.0.

<dt>1.0.3
<dd>
 - Updated coffee-script.js to v1.3.3.

<dt>1.0.2
<dd>
 - Updated coffee-script.js to v1.3.1.

<dt>1.0.1
<dd>
 - Fixed some small problem in setup.py.

<dt>1.0.0
<dd>
 - First release.
</dl>

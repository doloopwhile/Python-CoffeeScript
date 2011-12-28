CoffeeScript
============
Python CoffeeScript is a bridge to the JS CoffeeScript compiler. 

A short example:

    >>> import coffeescript
    >>> coffeescript.compile('add = (a, b) -> a + b')
    '(function() {\n  var add;\n\n  add = function(a, b) {\n    return a + b;\n  };\
    n\n}).call(this);\n'
    >>> print(coffeescript.compile('add = (a, b) -> a + b'))
    (function() {
      var add;
    
      add = function(a, b) {
        return a + b;
      };
    
    }).call(this);


# Installation

    $ pip install CoffeeScript

or
    
    $ easy_install CoffeeScript


#coffee-script.js
The latest version of coffee-script.js (the script for browser <script type="text/coffeescript"> tags)
can be download from http://jashkenas.github.com/coffee-script/

# License
Copyright (c) 2011 Omoto Kenji.
Released under the MIT license. See `LICENSE` for details.

You can download current version of coffee-script.js from 
http://jashkenas.github.com/coffee-script/extras/coffee-script.js


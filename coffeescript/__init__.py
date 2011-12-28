#!python3
#encoding: shift-jis
from __future__ import division, unicode_literals, print_function

#Copyright (c) 2011 Omoto Kenji

'''
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
'''

__version__ = str('1.0.0')
__author__  = str("Omoto Kenji (doloopwhile@gmail.com)")
__license__ = str("MIT License")

__all__ = 'compile Compiler'.split()

import os
import io
import execjs

EngineError = execjs.RuntimeError
CompilationError = execjs.ProgramError


class Compiler:
    def __init__(self, compiler_script, runtime):
        self._compiler_script = compiler_script
        self._runtime = runtime
        
    def compile(self, script, bare=False):
        if not hasattr(self, '_context'):
            self._context = self._runtime.compile(self._compiler_script)
        return self._context.call("CoffeeScript.compile", script, {'bare':bare})


_compiler = None

def _default_compiler_script():
    from os.path import dirname, join
    filename = join(dirname(__file__), 'coffee-script.js')
    with io.open(filename, encoding='utf8') as fp:
        return fp.read()


def _default_runtime():
    return execjs.get()


def _default_compiler():
    global _compiler
    if _compiler is None:
        _compiler = Compiler(
            _default_compiler_script(),
            _default_runtime()
        )
    return _compiler


def compile(script, bare=False):
    return _default_compiler().compile(script, bare=bare)


def version():
    return _default_compiler().version()



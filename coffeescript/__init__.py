#!/usr/bin/env python3
# -*- coding: ascii -*-
from __future__ import division, unicode_literals, print_function

# Copyright (c) 2011 Omoto Kenji
# Released under the MIT license. See `LICENSE` for details.

'''
Python CoffeeScript is a bridge to the JS CoffeeScript compiler.

A short example:

    >>> import coffeescript
    >>> print(coffeescript.compile('add = (a, b) -> a + b'))
    (function() {
      var add;

      add = function(a, b) {
        return a + b;
      };

    }).call(this);
'''

# A value of __spam__ have to be wrapped with str().
# It is because that __spam__ must be a instance of str() in 2.x and
# "xxxx" is a instance of unicode() due to unicode_literals.

__license__ = str("MIT License")

# The following __version__ is not DRY.
# Same information can be got from setup.py.
# However, __version__ should provited by __init__.py for user-friendliness.
# On the other hand, it is impossible that `from coffeescript import __version__`
# in spite of a dependency on execjs.
# i.e. the import in setup.py fails if execjs has not been installed yet.
__version__ = str("2.0.0")


__all__ = str('''
    compile
    compile_file
    Compiler
    EngineError
    CompilationError
    get_runtime
    get_compiler_script
''').split()

import os
import io
import execjs

EngineError = execjs.RuntimeError
CompilationError = execjs.ProgramError

try:
    _BaseString = basestring
except NameError:
    _BaseString = (str, bytes)


class Compiler:
    '''Wrapper of execution of CoffeeScript compiler script'''
    def __init__(self, compiler_script, runtime):
        '''compiler_script is a CoffeeScript compiler script in JavaScript.
        runtime is a instance of execjs.Runtime.
        '''
        self._compiler_script = compiler_script
        self._runtime = runtime

    def compile(self, script, bare=False):
        '''compile a CoffeeScript code to a JavaScript code.

        if bare is True, then compile the JavaScript without the top-level
        function safety wrapper (like the coffee command).
        '''
        if not hasattr(self, '_context'):
            self._context = self._runtime.compile(self._compiler_script)
        return self._context.call(
            "CoffeeScript.compile", script, {'bare': bare})

    def compile_file(self, filename, encoding="utf-8", bare=False):
        '''compile a CoffeeScript script file to a JavaScript code.

        filename can be a list or tuple of filenames,
        then contents of files are concatenated with line feeds.

        if bare is True, then compile the JavaScript without the top-level
        function safety wrapper (like the coffee command).
        '''
        if isinstance(filename, _BaseString):
            filename = [filename]

        scripts = []
        for f in filename:
            with io.open(f, encoding=encoding) as fp:
                scripts.append(fp.read())

        return self.compile('\n\n'.join(scripts), bare=bare)


def compile(script, bare=False):
    return _default_compiler().compile(script, bare=bare)
compile.__doc__ = Compiler.compile.__doc__


def compile_file(filename, encoding="utf-8", bare=False):
    return _default_compiler().compile_file(
        filename, encoding=encoding, bare=bare)
compile_file.__doc__ = Compiler.compile_file.__doc__


def get_compiler_script():
    '''returns a CoffeeScript compiler script in JavaScript.
    which is used in coffeescript.compile() and coffeescript.compile_file()
    '''
    from os.path import dirname, join
    filename = join(dirname(__file__), 'coffeescript.js')
    with io.open(filename, encoding='utf8') as fp:
        return fp.read()


def get_runtime():
    '''returns an appropriate instance of execjs.Runtime
    which is used in coffeescript.compile() and coffeescript.compile_file()
    '''
    return execjs.get()


_compiler = None


def _default_compiler():
    global _compiler
    if _compiler is None:
        _compiler = Compiler(
            get_compiler_script(),
            get_runtime()
        )
    return _compiler

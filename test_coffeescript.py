#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
from __future__ import unicode_literals, print_function
import sys
import os
import io
import tempfile
from itertools import product

if sys.version_info < (2, 7):
    import unittest2 as unittest
else:
    import unittest

import doctest


import execjs
import coffeescript


coffee_code = """
# このコメントはasciiで表現できない文字列です(This is a non-ascii comment)
helloworld = "こんにちは世界"
add = (x, y) ->
    x + y
"""
hello = "こんにちは"
world = "世界"
helloworld = "こんにちは世界"


splitted_coffee_code = ["""
# このコメントはasciiで表現できない文字列です(This is a non-ascii comment)
helloworld = "こんにちは世界"
""",
"""
add = (x, y) ->
    x + y
"""
]

class CoffeeScriptTest(unittest.TestCase):
    def setUp(self):
        self.runtimes = list(execjs.available_runtimes().values())

        self.encodings = "shift-jis utf-8 euc-jp".split()
        self.compilers = []
        self.compilers.append(coffeescript)  # default compiler

        from os.path import join, dirname
        script_path = join(dirname(coffeescript.__file__), "coffee-script.js")
        with io.open(script_path) as fp:
            compiler_script = fp.read()

        for runtime in self.runtimes:
            self.compilers.append(
                coffeescript.Compiler(compiler_script, runtime))


    def assertExprsSuccess(self, ctx):
        self.assertEqual(ctx.call("add", 1, 2), 3)
        self.assertEqual(ctx.call("add", hello, world), helloworld)
        self.assertEqual(ctx.eval("helloworld"), helloworld)

    def assertExprsFail(self, ctx):
        with self.assertRaises(execjs.ProgramError):
            ctx.call("add", 1, 2)
        with self.assertRaises(execjs.ProgramError):
            ctx.call("add", hello, world)
        with self.assertRaises(execjs.ProgramError):
            ctx.eval("helloworld")

    def test_compile(self):
        for compiler, runtime in product(self.compilers, self.runtimes):
            compile = compiler.compile

            # test bare=True
            jscode = compile(coffee_code, bare=True)
            ctx = runtime.compile(jscode)
            self.assertExprsSuccess(ctx)

            # test bare=False
            jscode = compile(coffee_code, bare=False)
            ctx = runtime.compile(jscode)
            self.assertExprsFail(ctx)

    def combinations_for_compile_file(self):
        return product(
            self.compilers,
            self.encodings,
            self.runtimes,
        )

    def assert_compile_file_success(self, compiler, runtime, filename, encoding, bare):
        jscode = compiler.compile_file(filename, encoding=encoding, bare=bare)
        ctx = runtime.compile(jscode)
        self.assertExprsSuccess(ctx)

    def assert_compile_file_fail(self, compiler, runtime, filename, encoding, bare):
        jscode = compiler.compile_file(filename, encoding=encoding, bare=bare)
        ctx = runtime.compile(jscode)
        self.assertExprsFail(ctx)

    def assert_compile_file_decode_error(self, compiler, runtime, filename, encoding, bare):
        with self.assertRaises(UnicodeDecodeError):
            compiler.compile_file(filename, encoding=encoding, bare=bare)

    def write_temp_files(self, strings, encoding):
        paths = []
        for s in strings:
            (fd, path) = tempfile.mkstemp()
            os.close(fd)
            with io.open(path, "w", encoding=encoding) as fp:
                fp.write(s)
            paths.append(path)
        return paths

    def remove_files(self, paths):
        for p in paths:
            os.remove(p)

    def test_compile_files(self):
        for compiler, encoding, runtime in self.combinations_for_compile_file():
            paths = self.write_temp_files([coffee_code], encoding)
            try:
                filename = paths[0]

                self.assert_compile_file_success(compiler, runtime, filename, encoding, True)
                self.assert_compile_file_fail(compiler, runtime, filename, encoding, False)
                for wrong_encoding in set(self.encodings) - set([encoding]):
                    self.assert_compile_file_decode_error(
                        compiler, runtime, filename, wrong_encoding, True)
                    self.assert_compile_file_decode_error(
                        compiler, runtime, filename, wrong_encoding, False)
            finally:
                self.remove_files(paths)

    def test_compile_splitted_files(self):
        for compiler, encoding, runtime in self.combinations_for_compile_file():
            paths = self.write_temp_files(splitted_coffee_code, encoding)
            try:
                filename = paths

                self.assert_compile_file_success(compiler, runtime, filename, encoding, True)
                self.assert_compile_file_fail(compiler, runtime, filename, encoding, False)
                for wrong_encoding in set(self.encodings) - set([encoding]):
                    self.assert_compile_file_decode_error(
                        compiler, runtime, filename, wrong_encoding, True)
                    self.assert_compile_file_decode_error(
                        compiler, runtime, filename, wrong_encoding, False)
            finally:
                self.remove_files(paths)

def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(coffeescript))
    return tests


def main():
    unittest.main()


if __name__ == "__main__":
    main()

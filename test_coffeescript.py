#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
from __future__ import unicode_literals, print_function
import doctest
import unittest

import os
import io
import tempfile
from itertools import product

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
            self.runtimes
        )

    def test_compile_files(self):
        for compiler, encoding, runtime in self.combinations_for_compile_file():
            compile_file = compiler.compile_file

            (fd, filename) = tempfile.mkstemp()
            os.close(fd)
            try:
                with io.open(filename, "w", encoding=encoding) as fp:
                    fp.write(coffee_code)

                jscode = compile_file(filename, encoding=encoding, bare=True)
                ctx = runtime.compile(jscode)
                self.assertExprsSuccess(ctx)

                jscode = compile_file(filename, encoding=encoding, bare=False)
                ctx = runtime.compile(jscode)
                self.assertExprsFail(ctx)

                for wrong_encoding in set(self.encodings) - set([encoding]):
                    with self.assertRaises(UnicodeDecodeError):
                        compile_file(filename, encoding=wrong_encoding, bare=True)
                    with self.assertRaises(UnicodeDecodeError):
                        compile_file(filename, encoding=wrong_encoding, bare=False)
            finally:
                os.remove(filename)


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(coffeescript))
    return tests


def main():
    unittest.main()


if __name__ == "__main__":
    main()

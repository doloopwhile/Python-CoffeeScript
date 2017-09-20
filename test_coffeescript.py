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
        self.encodings = "shift-jis utf-8 euc-jp".split()

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
        # test bare=True
        jscode = coffeescript.compile(coffee_code, bare=True)
        ctx = execjs.compile(jscode)
        self.assertExprsSuccess(ctx)

        # test bare=False
        jscode = coffeescript.compile(coffee_code, bare=False)
        ctx = execjs.compile(jscode)
        self.assertExprsFail(ctx)

    def assert_compile_file_success(self, filename, encoding, bare):
        jscode = coffeescript.compile_file(filename, encoding=encoding, bare=bare)
        ctx = execjs.compile(jscode)
        self.assertExprsSuccess(ctx)

    def assert_compile_file_fail(self, filename, encoding, bare):
        jscode = coffeescript.compile_file(filename, encoding=encoding, bare=bare)
        ctx = execjs.compile(jscode)
        self.assertExprsFail(ctx)

    def assert_compile_file_decode_error(self, filename, encoding, bare):
        with self.assertRaises(UnicodeDecodeError):
            coffeescript.compile_file(filename, encoding=encoding, bare=bare)

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
        for encoding in self.encodings:
            paths = self.write_temp_files([coffee_code], encoding)
            try:
                filename = paths[0]

                self.assert_compile_file_success(filename, encoding, True)
                self.assert_compile_file_fail(filename, encoding, False)
                for wrong_encoding in set(self.encodings) - set([encoding]):
                    self.assert_compile_file_decode_error(
                        filename, wrong_encoding, True)
                    self.assert_compile_file_decode_error(
                        filename, wrong_encoding, False)
            finally:
                self.remove_files(paths)

    def test_compile_splitted_files(self):
        for encoding in self.encodings:
            paths = self.write_temp_files(splitted_coffee_code, encoding)
            try:
                filename = paths

                self.assert_compile_file_success(filename, encoding, True)
                self.assert_compile_file_fail(filename, encoding, False)
                for wrong_encoding in set(self.encodings) - set([encoding]):
                    self.assert_compile_file_decode_error(
                        filename, wrong_encoding, True)
                    self.assert_compile_file_decode_error(
                        filename, wrong_encoding, False)
            finally:
                self.remove_files(paths)

def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(coffeescript))
    return tests


def main():
    unittest.main()


if __name__ == "__main__":
    main()

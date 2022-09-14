#!/usr/bin/env python3

import unittest

from poetry_deps import parse_package


class TestFileParse(unittest.TestCase):
    def test_basic(self):
        testcase = """name = "cachecontrol"
        version = "0.12.11"
        description = "httplib2 caching for requests"
        category = "main"
        optional = false
        python-versions = ">=3.6"
        """
        expected = {"name": "cachecontrol", "version": "0.12.11", "description": "httplib2 caching for requests",
                    "category": "main", "optional": False, "python-versions": ">=3.6", 'deps': [], 'optional_deps': [], 'rev_deps': []}
        self.assertEqual(parse_package(testcase), expected)


unittest.main()

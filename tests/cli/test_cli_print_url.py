#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.

import subprocess
import unittest


class TestPrintUrlArgument(unittest.TestCase):
    """Test CLI for print-url argument."""

    def test_print_url_argument(self):
        url = r'https://raw.github.com/mozilla/mozdownload/master/README.md'
        try:
            args = ['mozdownload',
                    '--url={url}'.format(url=url),
                    '--print-url']
            output = subprocess.check_output(args, stderr=subprocess.STDOUT)
        except subprocess.CalledProcessError as e:
            output = e.output

        self.assertRegexpMatches(output, url)

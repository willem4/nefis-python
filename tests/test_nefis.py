#!/usr/bin/env python
# -*- coding: utf-8 -*-

# We're using some stuff later

"""
test_nefis
----------------------------------

Tests for `nefis` module.
"""

import pytest  # noqa: F401

from click.testing import CliRunner

import nefis.cnefis
import nefis.cli


class TestNefis(object):

    @classmethod
    def setup_class(cls):
        pass

    def test_cnefis(self):
        """check if we can access cnefis"""
        nefis.cnefis

    @pytest.mark.skip(reason="crashes on windows")
    def test_command_line_interface(self):
        runner = CliRunner()
        result = runner.invoke(nefis.cli.main)
        assert result.exit_code == 0
        assert 'Welcome' in result.output
        help_result = runner.invoke(nefis.cli.main, ['--help'])
        assert help_result.exit_code == 0
        assert '--help  Show this message and exit.' in help_result.output

    @classmethod
    def teardown_class(cls):
        pass

import logging
import os
import tempfile
import faulthandler

import numpy as np
import pytest

import nefis.cnefis
from .utils import (
    nefis_file,
    log_error
)

faulthandler.enable()

nefis_file = nefis_file

logger = logging.getLogger(__name__)


def test_get_version():
    error, version = nefis.cnefis.getnfv()
    log_error(error)
    assert error == 0, "getnfv should return error 0"


def test_crenef_and_clsnef():
    """test creating a file"""
    dat_file = 'attributes.dat'
    def_file = 'attributes.def'
    coding = ' '
    ac_type = 'c'
    fp = -1
    try:
        error, fp = nefis.cnefis.crenef(dat_file, def_file, coding, ac_type)
        log_error(error)
        assert error == 0, "crenef should return error 0"
        error = nefis.cnefis.clsnef(fp)
        log_error(error)
        assert error == 0, "crenef should return error 0"
    finally:
        os.unlink(dat_file)
        os.unlink(def_file)


def test_defelm(nefis_file):

    elm_name = 'Element 1'
    elm_type = 'character'
    elm_single_byte = 20
    elm_quantity = 'names'
    elm_unit = '[-]'
    elm_description = 'Discharge station names'
    elm_count = 1
    elm_dimensions = np.arange(elm_count, dtype='int32').reshape(elm_count)
    elm_dimensions[0] = 20

    error = nefis.cnefis.defelm(
        nefis_file,
        elm_name,
        elm_type,
        elm_single_byte,
        elm_quantity,
        elm_unit,
        elm_description,
        elm_count,
        elm_dimensions
    )
    log_error(error)
    assert error == 0, "expected error 0 for creating element"


def test_defelm2(nefis_file):
    elm_name = 'Elm 2'
    elm_type = 'REAL'
    elm_single_byte = 4
    elm_quantity = 'discharge'
    elm_unit = '[m^3/s]'
    elm_description = 'First element generated by Python'
    elm_count = 2
    elm_dimensions = np.arange(elm_count, dtype='int32').reshape(elm_count)
    elm_dimensions[0] = 20
    elm_dimensions[1] = 5

    error = nefis.cnefis.defelm(
        nefis_file,
        elm_name,
        elm_type,
        elm_single_byte,
        elm_quantity,
        elm_unit,
        elm_description,
        elm_count,
        elm_dimensions
    )
    log_error(error)
    assert error == 0, "expected error 0 for creating element"


def test_defcel(nefis_file):
    # add the 2 elements
    test_defelm(nefis_file)
    test_defelm2(nefis_file)

    # and then create a cell
    cel_name = 'Cell 1'
    cel_names_count = 2
    elm_names = ['Element 1', 'Elm 2']

    error = nefis.cnefis.defcel(nefis_file, cel_name, cel_names_count, elm_names)
    log_error(error)
    assert error == 0, "expected error 0 for defining cel"


def test_defgrp(nefis_file):
    # add the cell
    test_defcel(nefis_file)

    grp_defined = 'Grp 1'
    cel_name = 'Cell 1'
    grp_count = 1
    grp_dimensions = np.arange(5, dtype='int32').reshape(5)
    grp_dimensions[0] = 11
    grp_dimensions[1] = 0
    grp_dimensions[2] = 0
    grp_dimensions[3] = 0
    grp_dimensions[4] = 0
    grp_order = np.arange(5, dtype='int32').reshape(5)
    grp_order[0] = 1
    grp_order[1] = 2
    grp_order[2] = 3
    grp_order[3] = 4
    grp_order[4] = 5

    error = nefis.cnefis.defgrp(nefis_file, grp_defined, cel_name, grp_count, grp_dimensions, grp_order)

    log_error(error)
    assert error == 0, "expected error 0 for defining group"


def test_credat(nefis_file):
    test_defgrp(nefis_file)

    grp_name = 'Group 1'
    grp_defined = 'Grp 1'

    error = nefis.cnefis.credat(nefis_file, grp_name, grp_defined)

    log_error(error)
    assert error == 0, "expected error 0 for creating dat"


def test_putiat(nefis_file):
    test_credat(nefis_file)
    grp_name = 'Group 1'
    att_name = 'Int. Attrib. 1'
    att_value = 1
    error = nefis.cnefis.putiat(nefis_file, grp_name, att_name, att_value)

    log_error(error)
    assert error == 0, "expected error 0 putting integer attribute"


def test_putrat(nefis_file):
    test_credat(nefis_file)
    grp_name = 'Group 1'
    att_name = 'Real Attrib. 1'
    att_value = 1.0
    error = nefis.cnefis.putrat(nefis_file, grp_name, att_name, att_value)
    log_error(error)
    assert error == 0, "expected error 0 putting real attribute"


def test_putsat(nefis_file):
    test_credat(nefis_file)
    grp_name = 'Group 1'
    att_name = 'String Attrib. 1'
    att_value = 'A string'
    error = nefis.cnefis.putsat(nefis_file, grp_name, att_name, att_value)
    log_error(error)
    assert error == 0, "expected error 0 putting string attribute"

def test_getiat(nefis_file):
    test_putiat(nefis_file)
    grp_name = 'Group 1'
    att_name = 'Int. Attrib. 1'
    error, att_value = nefis.cnefis.getiat(nefis_file, grp_name, att_name)
    log_error(error)
    assert error == 0, "expected error 0 getting integer attribute"
    assert att_value == 1, "expected value 1 getting integer attribute"


def test_getrat(nefis_file):
    test_putrat(nefis_file)
    grp_name = 'Group 1'
    att_name = 'Real Attrib. 1'
    error, att_value = nefis.cnefis.getrat(nefis_file, grp_name, att_name)
    log_error(error)
    assert error == 0, "expected error 0 getting integer attribute"
    assert att_value == 1.0, "expected value 1 getting real attribute"


def test_getsat(nefis_file):
    test_putsat(nefis_file)
    grp_name = 'Group 1'
    att_name = 'String Attrib. 1'
    error, att_value = nefis.cnefis.getsat(nefis_file, grp_name, att_name)
    log_error(error)
    assert error == 0, "expected error 0 getting integer attribute"
    assert att_value == 'A string', "expected value 'A string' getting string attribute"

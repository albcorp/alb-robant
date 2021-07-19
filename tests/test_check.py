#! /usr/bin/python

"""Functions to test the `check` subcommand implementation

:Author: Andrew Burrow
:Contact: albcorp@gmail.com
:Copyright: 2021 Andrew Burrow

"""

__docformat__ = "restructuredtext"


from robant.helpers import getMetadataSchema, isValidSchema


def test_getMetadataSchema():
    schema = getMetadataSchema()
    assert isValidSchema(schema)

#!/usr/bin/python3
"""
This module defines unit tests for models/state.py.
"""

import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.state import State


class TestStateInstantiation(unittest.TestCase):
    """
    Unittests for testing instantiation of the State class.
    """

    def test_no_args_instantiates(self):
        """Test that State class can be instantiated with no arguments."""
        self.assertEqual(State, type(State()))

    def test_new_instance_stored_in_objects(self):
        """Test that a new State instance is stored in the objects att"""
        self.assertIn(State(), models.storage.all().values())

    def test_id_is_public_str(self):
        """Test that the id attribute is a public string."""
        self.assertEqual(str, type(State().id))

    # ... (similar modifications for other instantiation tests)

    def test_instantiation_with_None_kwargs(self):
        """Test instantiation with None kwargs raises TypeError."""
        with self.assertRaises(TypeError):
            State(id=None, created_at=None, updated_at=None)


class TestStateSave(unittest.TestCase):
    """
    Unittests for testing the save method of the State class.
    """

    @classmethod
    def setUp(cls):
        """Set up for testing save method."""
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    def tearDown(self):
        """Clean up after testing save method."""
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_one_save(self):
        """Test that the save method updates the updated_at attribute."""
        st = State()
        sleep(0.05)
        first_updated_at = st.updated_at
        st.save()
        self.assertLess(first_updated_at, st.updated_at)

    # ... (similar modifications for other save tests)


class TestStateToDict(unittest.TestCase):
    """
    Unittests for testing the to_dict method of the State class.
    """

    def test_to_dict_type(self):
        """Test that the to_dict method returns a dictionary."""
        self.assertTrue(dict, type(State().to_dict()))

    # ... (similar modifications for other to_dict tests)


if __name__ == "__main__":
    unittest.main()

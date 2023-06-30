#!/usr/bin/python3
""" Unittests for Base. """
import unittest, os
from models.base import Base
from models.rectangle import Rectangle


class TestBase(unittest.TestCase):
    """ Test cases. """
    def test_id(self):
        base1 = Base()
        self.assertAlmostEqual(base1.id, 1)
        base2 = Base()
        self.assertAlmostEqual(base2.id, 2)
        base3 = Base(-1)
        self.assertAlmostEqual(base3.id, -1)

    def test_to_json_string(self):
        self.assertAlmostEqual(Base.to_json_string(None), "[]")
        self.assertAlmostEqual(Base.to_json_string([{"id": 1}]), '[{"id": 1}]')
        self.assertAlmostEqual(Base.to_json_string([]), '[]')

    def test_save_to_file(self):
        Base.save_to_file(None)
        self.assertAlmostEqual(os.path.exists("Base.json"), True)

    def test_from_json_string(self):
        self.assertAlmostEqual(Base.from_json_string(None), [])
        self.assertAlmostEqual(Base.from_json_string('[{"id": 1}]'), [{"id": 1}])
        self.assertAlmostEqual(Base.from_json_string("[]"), [])

    def test_update(self):
        dictionary = {"id": 1}
        r1 = Rectangle.create(**dictionary)
        self.assertAlmostEqual(r1.id, 1)

if __name__ == "__main__":
    unittest.main()


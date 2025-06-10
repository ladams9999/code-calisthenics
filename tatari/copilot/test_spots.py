import unittest
from datetime import time
from spots import get_rotations, to_time

class TestGetRotations(unittest.TestCase):
    def test_morning_only(self):
        self.assertEqual(get_rotations(to_time("7:00 AM")), ["Morning"])

    def test_afternoon_only(self):
        self.assertEqual(get_rotations(to_time("1:00 PM")), ["Afternoon"])

    def test_prime_only(self):
        self.assertEqual(get_rotations(to_time("7:00 PM")), ["Prime"])

    def test_overlap_afternoon_prime(self):
        # 3:30 PM is in both Afternoon (12-4) and Prime (3-8)
        self.assertCountEqual(get_rotations(to_time("3:30 PM")), ["Afternoon", "Prime"])

    def test_overlap_morning_afternoon(self):
        # 12:00 PM is the start of Afternoon, not in Morning
        self.assertEqual(get_rotations(to_time("12:00 PM")), ["Afternoon"])

    def test_overlap_end(self):
        # 8:00 PM is the end of Prime, should not be included
        self.assertEqual(get_rotations(to_time("8:00 PM")), ["Other"])

    def test_other(self):
        # 2:00 AM is not in any rotation
        self.assertEqual(get_rotations(to_time("2:00 AM")), ["Other"])

    def test_empty_string(self):
        with self.assertRaises(ValueError):
            get_rotations(to_time(""))

    def test_none(self):
        with self.assertRaises(TypeError):
            get_rotations(None)

    def test_invalid_format(self):
        with self.assertRaises(ValueError):
            get_rotations(to_time("25:00 PM"))

    def test_non_time_type(self):
        with self.assertRaises(AttributeError):
            get_rotations("not a time object")

if __name__ == "__main__":
    unittest.main()
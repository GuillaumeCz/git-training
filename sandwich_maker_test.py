import unittest
from sandwich_maker import Sandwich, Lettuce, SliceOfBread, Ham, Cheese


class SandwichMakerTestCase(unittest.TestCase):
    def test_create_empty_sandwich(self):
        sandwich = Sandwich()
        self.assertEqual(sandwich.size(), 0)

    def test_is_not_vegan_with_dairy(self):
        sandwich = Sandwich()
        sandwich.add(Cheese())
        self.assertFalse(sandwich.is_vegan())

    def test_is_not_vegan_with_meat(self):
        sandwich = Sandwich()
        sandwich.add(Ham())
        sandwich.add(SliceOfBread())
        self.assertFalse(sandwich.is_vegan())

    def test_is_vegan(self):
        sandwich = Sandwich()
        sandwich.add(Lettuce())
        self.assertTrue(sandwich.is_vegan())

    def test_add_aliment_to_sandwich(self):
        sandwich = Sandwich()
        sandwich.add(Lettuce())
        self.assertEqual(sandwich.size(), 1)

    def test_is_well_composed(self):
        sandwich = Sandwich()
        sandwich.add(SliceOfBread())
        sandwich.add(Lettuce())
        sandwich.add(SliceOfBread())
        self.assertTrue(sandwich.is_well_composed())

    def test_is_not_well_composed(self):
        sandwich = Sandwich()
        sandwich.add(SliceOfBread())
        sandwich.add(Lettuce())
        self.assertFalse(sandwich.is_well_composed())

    def test_reset(self):
        sandwich = Sandwich()
        sandwich.add(Lettuce())
        sandwich.reset()
        self.assertEqual(sandwich.size(), 0)

    def test_remove_last_aliment(self):
        sandwich = Sandwich()
        sandwich.add(Lettuce())
        sandwich.add(Lettuce())
        sandwich.remove_last()
        self.assertEqual(sandwich.size(), 1)


if __name__ == "__main__":
    unittest.main()

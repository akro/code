import unittest
from datetime import date

from src.model import OrderLine, Batch


class MyTestCase(unittest.TestCase):
    def test_allocating_to_a_batch_reduces_the_available_quantity(self):
        batch = Batch("batch-001", "SMALL-TABLE", qty=20, eta=date.today())
        line = OrderLine('order-ref', "SMALL-TABLE", 2)

        batch.allocate(line)

        self.assertEqual(batch.available_quantity, 20 - 2)


if __name__ == '__main__':
    unittest.main()

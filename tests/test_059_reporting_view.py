import unittest

from readmission_signal_board.models import Record
from readmission_signal_board.scoring import score_record


class DepthCheck59(unittest.TestCase):
    def test_059_reporting_view(self):
        record = Record(id="patient-059", exposure=36472, signal=0.827, urgency=9)
        self.assertGreaterEqual(score_record(record), 0)
        self.assertLessEqual(score_record(record), 1)


if __name__ == "__main__":
    unittest.main()

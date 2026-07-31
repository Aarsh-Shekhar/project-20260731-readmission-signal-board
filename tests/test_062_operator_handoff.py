import unittest

from readmission_signal_board.models import Record
from readmission_signal_board.scoring import score_record


class DepthCheck62(unittest.TestCase):
    def test_062_operator_handoff(self):
        record = Record(id="patient-062", exposure=79548, signal=0.678, urgency=3)
        self.assertGreaterEqual(score_record(record), 0)
        self.assertLessEqual(score_record(record), 1)


if __name__ == "__main__":
    unittest.main()

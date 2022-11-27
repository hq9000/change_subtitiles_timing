import unittest
from subtitles_timing_moving import subtitles_timing_moving


class TestSubtitlesTimingMoving(unittest.TestCase):
    def test_convert_one_time_point(self):
        subtest_inputs = [
            ("00:01:05,123", -1.013, "00:01:04,110"),
            ("00:01:05,123", 1.013, "00:01:06,136"),
            ("00:00:05,123", -6, "00:00:00,000"),
        ]

        for original, delta, expected_result in subtest_inputs:
            with self.subTest():
                res = subtitles_timing_moving._convert_one_time_point(original, delta)
                self.assertEquals(expected_result, res)

    def test_convert_time_line(self):
        source_line = "00:01:05,123 --> 00:01:07,110"
        expected_result = "00:01:06,123 --> 00:01:08,110"
        result = subtitles_timing_moving._convert_time_line(source_line, 1.0)
        self.assertEquals(expected_result, result)

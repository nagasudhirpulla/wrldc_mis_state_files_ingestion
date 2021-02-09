import unittest
from src.config.appConfig import loadFileMappings, loadMeasInfo


class TestAppConfig(unittest.TestCase):
    def test_fileMappings(self) -> None:
        """tests the function that tests file mappings config
        """
        fileMappings = loadFileMappings()
        self.assertTrue(fileMappings is not None)
        self.assertFalse(len(fileMappings) == 0)

    def test_measInfo(self) -> None:
        """tests the function that tests file mappings config
        """
        measInfo = loadMeasInfo()
        self.assertTrue(measInfo is not None)
        self.assertFalse(len(measInfo) == 0)

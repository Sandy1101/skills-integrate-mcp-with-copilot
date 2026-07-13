import unittest

from src.app import activities


class MissingGitHubSkillsTest(unittest.TestCase):
    def test_github_skills_activity_is_listed(self):
        self.assertIn("GitHub Skills", activities)

        activity = activities["GitHub Skills"]
        self.assertIn("GitHub", activity["description"])
        self.assertGreater(activity["max_participants"], 0)


if __name__ == "__main__":
    unittest.main()

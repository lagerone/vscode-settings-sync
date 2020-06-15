import filecmp
import os
import shutil
from contextlib import suppress
from unittest import TestCase, mock

from sync_cli import run_sync

_WORKSPACE_DIR = os.path.abspath(
    os.path.join(os.path.dirname(
        os.path.abspath(__file__)), '..', '..')
)

_TEST_FILES_PATH = os.path.join(_WORKSPACE_DIR, "test-files")


class TestSync(TestCase):
    def setUp(self):
        self.tearDown()

    def tearDown(self):
        with suppress(FileNotFoundError):
            shutil.rmtree(os.path.join(_TEST_FILES_PATH,
                                       "empty-target",
                                       ".vscode"))
            shutil.rmtree(os.path.join(_TEST_FILES_PATH,
                                       "target-with-env",
                                       ".vscode"))
            os.remove(os.path.join(_TEST_FILES_PATH,
                                   "empty-target",
                                   ".env"))
            os.remove(os.path.join(_TEST_FILES_PATH,
                                   "empty-target",
                                   ".env.example"))

    def test_should_copy_settings_file_to_target(self):
        # Arrange
        fake_project_dir = os.path.join(
            _TEST_FILES_PATH, "empty-target")

        expected_file = os.path.join(
            fake_project_dir, ".vscode", "settings.json")

        # Act
        with mock.patch("sync_cli.get_project_paths", return_value=[fake_project_dir]):
            run_sync()

        # Assert
        self.assertTrue(os.path.exists(expected_file))

    def test_should_copy_env_files_to_target(self):
        # Arrange
        fake_project_dir = os.path.join(
            _TEST_FILES_PATH, "empty-target")

        expected_env_file = os.path.join(
            fake_project_dir, ".env")

        expected_env_exampel_file = os.path.join(
            fake_project_dir, ".env.example")

        # Act
        with mock.patch("sync_cli.get_project_paths", return_value=[fake_project_dir]):
            run_sync()

        # Assert
        self.assertTrue(os.path.exists(expected_env_file))
        self.assertTrue(os.path.exists(expected_env_exampel_file))

    def test_should_not_copy_env_if_exists(self):
        # Arrange
        fake_project_dir = os.path.join(
            _TEST_FILES_PATH, "target-with-env")

        target_env_file = os.path.join(
            fake_project_dir, ".env")

        # Act
        with mock.patch("sync_cli.get_project_paths", return_value=[fake_project_dir]):
            run_sync()

        # Assert
        self.assertFalse(filecmp.cmp(target_env_file, os.path.join(
            _WORKSPACE_DIR, "settings-to-sync", ".env")))
        self.assertFalse(os.path.exists(
            os.path.join(fake_project_dir, ".env.example")))

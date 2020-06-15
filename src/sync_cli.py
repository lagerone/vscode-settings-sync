"""Syncs vscode settings to configured vscode projects"""
import os
import shutil
import subprocess
from typing import List

from config import get_project_paths

_WORKSPACE_DIR = os.path.abspath(
    os.path.join(os.path.dirname(
        os.path.abspath(__file__)), '..')
)

_SETTINGS_TO_SYNC_PATH = os.path.join(_WORKSPACE_DIR, "settings-to-sync")


def _sync_vscode_settings(project_path: str) -> None:
    """Syncs vscode settings"""
    target_vscode_path = os.path.join(project_path, ".vscode")
    os.makedirs(target_vscode_path, exist_ok=True)
    source_path = os.path.join(_SETTINGS_TO_SYNC_PATH,
                               "settings.json")
    target_path = os.path.join(target_vscode_path, "settings.json")
    shutil.copyfile(src=source_path, dst=target_path)
    print(f"Copied '{source_path}' to '{target_path}'.")


def _sync_env_files(project_path: str) -> None:
    """Syncs .env files"""
    env_target = os.path.join(project_path, ".env")

    if (os.path.exists(env_target)):
        print(f"Skipping env-files: '{env_target}' exists.")
        return

    env_source = os.path.join(_SETTINGS_TO_SYNC_PATH, ".env")
    env_example_source = os.path.join(_SETTINGS_TO_SYNC_PATH,
                                      ".env.example")
    env_example_target = os.path.join(project_path, ".env.example")

    shutil.copyfile(env_source, env_target)
    print(f"Copied '{env_source}'to '{env_target}'.")
    shutil.copyfile(env_example_source, env_example_target)
    print(f"Copied '{env_example_source}' to '{env_example_target}'.")


def run_sync() -> None:
    """Runs the settings sync"""
    for project_path in get_project_paths():
        _sync_vscode_settings(project_path=project_path)
        _sync_env_files(project_path=project_path)


if __name__ == "__main__":
    run_sync()

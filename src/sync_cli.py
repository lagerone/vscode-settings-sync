"""Syncs vscode settings to configured vscode projects"""
import os
import shutil

from config import get_project_paths

_WORKSPACE_DIR = os.path.abspath(
    os.path.join(os.path.dirname(
        os.path.abspath(__file__)), '..')
)

_SETTINGS_TO_SYNC_PATH = os.path.join(_WORKSPACE_DIR, "settings-to-sync")


def _sync_file(source_path: str, target_path: str):
    if (os.path.exists(target_path)):
        print(f'Skipping file "{target_path}" since it already exists.')
        return
    shutil.copyfile(source_path, target_path)
    print(f'Copied "{source_path}" to "{target_path}".')


def _sync_with_overwrite(source_path: str, target_path: str):
    shutil.copyfile(source_path, target_path)
    print(f'Copied "{source_path}" to "{target_path}".')


def _sync_vscode_settings(project_path: str) -> None:
    """Syncs vscode settings"""
    target_vscode_path = os.path.join(project_path, ".vscode")
    os.makedirs(target_vscode_path, exist_ok=True)
    source_path = os.path.join(_SETTINGS_TO_SYNC_PATH,
                               "settings.json")
    target_path = os.path.join(target_vscode_path, "settings.json")
    _sync_with_overwrite(source_path=source_path, target_path=target_path)


def _sync_env_files(project_path: str) -> None:
    """Syncs .env files"""
    pyright_source, pyright_target = (os.path.join(_SETTINGS_TO_SYNC_PATH, "pyrightconfig.json"), os.path.join(
        project_path, "pyrightconfig.json"))

    env = (os.path.join(_SETTINGS_TO_SYNC_PATH, ".env"), os.path.join(
        project_path, "pyrightconfig.json"))

    env_example = (os.path.join(_SETTINGS_TO_SYNC_PATH, ".env.example"), os.path.join(
        project_path, ".env.example"))

    _sync_with_overwrite(pyright_source, pyright_target)

    for source_path, target_path in [env, env_example]:
        _sync_file(source_path=source_path, target_path=target_path)


def run_sync() -> None:
    """Runs the settings sync"""
    for project_path in get_project_paths():
        _sync_vscode_settings(project_path=project_path)
        _sync_env_files(project_path=project_path)


if __name__ == "__main__":
    run_sync()

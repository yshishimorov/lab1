"""
Скрипт установки Git hook в директорию .git/hooks.
"""

import os
import shutil
import stat
import sys


def install_hooks() -> None:
    repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    git_hooks_dir = os.path.join(repo_root, ".git", "hooks")
    source_hook = os.path.join(repo_root, "hooks", "pre-commit")
    target_hook = os.path.join(git_hooks_dir, "pre-commit")

    if not os.path.exists(git_hooks_dir):
        print(f"Ошибка: Директория {git_hooks_dir} не найдена. Убедитесь, что репозиторий инициализирован.")
        sys.exit(1)

    shutil.copyfile(source_hook, target_hook)
    # Делаем файл исполняемым
    st = os.stat(target_hook)
    os.chmod(target_hook, st.st_mode | stat.S_IEXEC)

    print(f"Pre-commit хук успешно установлен в: {target_hook}")


if __name__ == "__main__":
    install_hooks()

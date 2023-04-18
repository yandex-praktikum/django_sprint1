import os


def test_project_folder_in_place(root_dir, project_dirname):
    manage_rpath = os.path.join(project_dirname, 'manage.py')
    manage_fpath = os.path.join(root_dir, manage_rpath)
    assert os.path.isfile(manage_fpath), (
        f'Не найден файл `{manage_rpath}`. '
        'Убедитесь, что структура проекта соответствует заданию.'
    )

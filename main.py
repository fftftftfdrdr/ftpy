import os
import logging
from collections import namedtuple


logging.basicConfig(filename='directory_info.log', level=logging.INFO, format='%(asctime)s - %(message)s')
FileInfo = namedtuple('FileInfo', ['name', 'extension', 'is_directory', 'parent_directory'])


def get_directory_info(dir_path):
    try:
        if not os.path.exists(dir_path):
            logging.error(f"Директория '{dir_path}' не существует.")
            return

        for entry in os.listdir(dir_path):
            entry_path = os.path.join(dir_path, entry)
            parent_dir = os.path.basename(dir_path)

            if os.path.isfile(entry_path):
                file_name, file_extension = os.path.splitext(entry)
                is_directory = False
            elif os.path.isdir(entry_path):
                file_name = entry
                file_extension = ""
                is_directory = True
            else:
                continue

            file_info = FileInfo(file_name=file_name, extension=file_extension, is_directory=is_directory,
                                 parent_directory=parent_dir)
            logging.info(
                f"Имя: {file_info.name}, Расширение: {file_info.extension}, Каталог: {file_info.is_directory}, Родительский каталог: {file_info.parent_directory}")

    except Exception as e:
        logging.error(f"Ошибка при обработке директории '{dir_path}': {str(e)}")


if name == "main":
    import sys

    if len(sys.argv) != 2:
        print("Использование: python directory_info.py <путь_до_директории>")
        sys.exit(1)

    directory_path = sys.argv[1]
    get_directory_info(directory_path)
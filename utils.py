
from PySide2.QtWidgets import QFileDialog


def choose_file(ui_,info, ename, file_path = "./"):
    selected_file_path, _ = QFileDialog.getOpenFileName(ui_,
                                        info,
                                        file_path,
                                        ename)
    return selected_file_path

def choose_folder(ui_,info,file_path = "./"):
    directory = QFileDialog.getExistingDirectory(ui_, info, file_path)
    return directory

import os

__init__ = ['PathFile']

class PathFile:
    """
    path_file - полный путь к файлу
    name_file - имя файла, где запускается данный код.
    full_name_file - имя файла с полным путём к файлу.
    """

    def __init__(self,file) :
        self.path_file = os.path.dirname(os.path.realpath(file))
        self.name_file = os.path.basename(os.path.realpath(file))
        self.full_name_file = os.path.realpath(file)
    
    def get_path_file(self):
        """
        Возвращение полного пути к запускаемому файлу
        """
        return self.path_file
    
    def get_name_file(self):
        """
        Возвращение имени запускаемого фила c расширением.
        """
        return self.name_file

    def get_full_name_file(self):
        """
        Возвращение название запускаемого фила с полным путём.
        """
        
        return self.full_name_file
    
    def get_name_file_no_exten(self):
        """
        Возвращение название запускаемого фила без расширения.
        """
        self.name_file_no_exten, *_ = self.name_file.split('.')
        return self.name_file_no_exten

    def get_full_name_file_no_exten(self):
        """
        Возвращение название запускаемого фила c полным путём без расширения.
        """
        self.full_name_file_no_exten = f'{self.get_path_file()}\{self.get_name_file_no_exten()}' 
        return self.full_name_file_no_exten
    
    def get_new_folder_full_name_file_new_exten(self,exten:str,*,name_file:str = '',add_to_name:str = '' ):

        """
        Создаётся новая папка, и возвращается полный путь к файлу с новым расширением и новой папкой. 
        """
      
        if (self.get_name_file_no_exten() not in os.listdir(self.path_file)):
            os.mkdir(self.get_full_name_file_no_exten())
        
        if (name_file==''):
            name_file =self.get_name_file_no_exten()
        if (add_to_name != ''):
            name_file = f'{name_file}_{add_to_name}'
      
        self.new_folder_full_name_file_new_exten = f'{self.get_full_name_file_no_exten()}\{name_file}.{exten}'

        return self.new_folder_full_name_file_new_exten




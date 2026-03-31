import os
import base64

class DataFormatter:
    @staticmethod
    def format_name(name):
        """Formata o nome respeitando preposições."""
        if not name: return ""
        exceptions = ['de', 'da', 'do', 'das', 'dos', 'e']
        words = name.lower().split()
        return " ".join([word.capitalize() if word not in exceptions else word for word in words])

    @staticmethod
    def get_absolute_image_path(html_path, relative_image_path):
        """Retorna o caminho completo (absoluto) da imagem no Windows."""
        if not relative_image_path: return ""
        
        base_dir = os.path.dirname(html_path)
        full_path = os.path.join(base_dir, relative_image_path.replace("/", os.sep))
        
        absolute_path = os.path.abspath(full_path)
        
        if os.path.exists(absolute_path):
            return absolute_path
        else:
            return ""
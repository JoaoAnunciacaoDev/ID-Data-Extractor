import os
from bs4 import BeautifulSoup
from formatter import DataFormatter

class HtmlExtractor:
    @staticmethod
    def extract_from_file(file_path):
        """Extrai os dados de um único arquivo HTML."""
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            soup = BeautifulSoup(f, "html.parser")

        students = []
        for table in soup.find_all("table"):
            rows = table.find_all("tr")
            
            if len(rows) >= 3:
                tds_row0 = rows[0].find_all("td")
                tds_row1 = rows[1].find_all("td")
                tds_row2 = rows[2].find_all("td")

                raw_name = tds_row0[-1].get_text(strip=True)
                formatted_name = DataFormatter.format_name(raw_name)
                rg_number = tds_row1[-1].get_text(strip=True)
                birth_date = tds_row2[-1].get_text(strip=True)

                img_tag = table.find("img")
                relative_photo_path = img_tag["src"] if img_tag else ""

                photo_path = DataFormatter.get_absolute_image_path(file_path, relative_photo_path)

                if formatted_name and rg_number:
                    students.append({
                        "foto": photo_path,
                        "nome": formatted_name,
                        "rg": rg_number,
                        "data_nascimento": birth_date
                    })

        return students

    @staticmethod
    def extract_from_files(file_paths):
        """Processa uma lista de arquivos HTML/HTM selecionados."""
        all_students = []
        files_processed = 0
        
        for file_path in file_paths:
            if file_path.lower().endswith((".htm", ".html")):
                files_processed += 1
                all_students.extend(HtmlExtractor.extract_from_file(file_path))
                
        return all_students, files_processed
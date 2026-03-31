import csv

class CsvExporter:
    @staticmethod
    def export(data_list, output_path):
        """Salva a lista de dicionários em um arquivo CSV."""
        if not data_list:
            raise ValueError("Não há dados para exportar.")
            
        with open(output_path, "w", newline="", encoding="utf-8-sig") as f:
            # BASTA ADICIONAR O DELIMITER AQUI:
            writer = csv.DictWriter(f, fieldnames=["foto", "nome", "rg", "data_nascimento"], delimiter=';')
            writer.writeheader()
            writer.writerows(data_list)
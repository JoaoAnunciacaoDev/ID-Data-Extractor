# 🪪 ID Card Extractor

This is a Desktop application developed in Python to automate the extraction of student data from HTML forms (exported from Microsoft Word). The program parses HTML tables, extracts biographical data, locates physical photo paths, and exports everything into a standardized `.csv` file.

This tool was designed to optimize the workflow for creating student ID cards, allowing direct integration with Print Merge features in software like CorelDraw and Microsoft Excel.

## ✨ Features

- **Batch Extraction:** Select multiple `.html` or `.htm` files at once.
- **Smart Formatting:** Automatically capitalizes names while ignoring common Brazilian Portuguese prepositions (de, da, do, etc.).
- **Graphical User Interface (GUI):** Clean and responsive interface built with Tkinter.
- **Image Preview:** View the student's photo directly within the app before exporting.
- **Real-time Editing:** Correct typos in names, documents, or image paths directly in the data table.
- **Optimized Export:** Generates CSV files with `utf-8-sig` encoding, ensuring correct reading of special characters in Excel and VBA macros.

## 🛠️ Built With

- **Python 3.x**
- **Tkinter** (Graphical User Interface)
- **BeautifulSoup4** (HTML Parsing)
- **Pillow (PIL)** (Image processing and preview)
- **PyInstaller** (Executable generation)

## 🚀 How to Use (For End Users)

No Python installation required! If you just want to use the tool:
1. Go to the [Releases] tab of this repository.
2. Download the latest `.exe` file.
3. Double-click to run the program.
4. Click **"1. Selecionar Arquivo(s)"** (Select Files) and choose your HTML forms.
5. Review or edit the data in the table and preview the photos.
6. Click **"3. Exportar CSV"** (Export CSV) and save the file to use in your design software.

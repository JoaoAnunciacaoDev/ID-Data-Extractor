# 🪪 ID Card Extractor

ID Card Extractor is a Python desktop application created to automate a repetitive workflow involved in generating student ID cards.
The original workflow required manually transferring student information and photo paths from documents exported from Microsoft Word into a format suitable for bulk printing. This project automates that process by parsing the exported HTML, extracting the relevant information, allowing manual corrections, previewing student photos, and generating a standardized CSV file.
Although originally developed for a specific real-world workflow, the project is published as a portfolio example of desktop automation, document parsing, data transformation, and GUI development with Python.

## The Problem

Creating student ID cards involved a repetitive manual workflow:

1. Export student forms from Microsoft Word.
2. Locate student information.
3. Locate the corresponding photo files.
4. Manually transfer the information to a spreadsheet.
5. Correct formatting issues.
6. Import the resulting data into the printing/design workflow.

When processing many students, this became unnecessarily time-consuming and prone to manual errors.

## The Solution
ID Card Extractor automates this workflow by:

Word → HTML → Parser → Structured Data → Review → CSV

Microsoft Word was used as the original data-entry environment. Instead of attempting to parse the .docx files directly, the workflow exports the documents to HTML, preserving the tabular structure in a format that can be parsed using BeautifulSoup.

Why HTML?

HTML was chosen because the original documents were created in Microsoft Word and exported to HTML. This format makes it easier to extract tables, text, and image paths using BeautifulSoup.

While .docx support would be a more natural solution and is planned for a future version, HTML was sufficient for the project's original requirements and allowed the solution to be developed within the available timeframe.

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

## 🚀 How to Use

No Python installation required! If you just want to use the tool:
1. Go to the [Releases] tab of this repository.
2. Download the latest `.exe` file.
3. Double-click to run the program.
4. Click **"1. Selecionar Arquivo(s)"** (Select Files) and choose your HTML forms.
5. Review or edit the data in the table and preview the photos.
6. Click **"3. Exportar CSV"** (Export CSV) and save the file to use in your design software.

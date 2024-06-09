# PDF-related Library
1. **`PyPDF2`: A library used to read and write PDF files in Python. Used to merge, split PDF files and extract text.**
2. **`PyPDF3`: A library similar to PyPDF2, which provides functions for handling PDF files.**
3. PDFMiner: PDFMiner is used to extract text and metadata from PDF files.
pdfminer.six is ​​a Python 2 and 3 compatible version of PDFMiner.
4. ReportLab: ReportLab is a library used to generate PDF documents.
In particular, it is widely used to dynamically generate PDFs.
5. PyFPDF: PyFPDF is a Python conversion of the FPDF library and is used to generate PDFs.
Supports various fonts, colors, images, etc.
6. Camelot: Camelot is a Python library used to extract tables from PDFs.
Extracts tabular data and returns it as a data frame.
7. Tabula-py: Tabula-py is a library used to extract tables from PDF files.
In particular, tables with irregular formats can also be extracted.

## PyPDF2 VS PyPDF3
1. **Development and maintenance status:**
- PyPDF2: This library was first released in 2011, and development continues since then. However, development has been slowing down recently.
- PyPDF3: As the development of PyPDF2 slowed, a derived project emerged to replace it. PyPDF3 maintains the functionality of PyPDF2, but adds new features and supports the latest Python features.

2. **Python version compatibility:**
- **`PyPDF2: Supports both Python 2.x and Python 3.x.`**
- PyPDF3: Focuses on support for Python 3.x, but does not support Python 2.x.

3. **Features and Performance:**
PyPDF3 attempts to extend and improve the functionality of PyPDF2. New features or improved performance may be added.
But for now there are no significant differences between PyPDF2 and PyPDF3. Most basic functions and methods work the same in both libraries.

4. **License:**
Both PyPDF2 and PyPDF3 are free to use.

In summary, PyPDF3 is a replacement for PyPDF2 that is more optimized for Python 3.x and is worth keeping an eye on for future development and new feature additions.

However, for now, the functionality and usage of the two libraries is largely similar, so you will need to take these differences into account when considering using PyPDF2 in an existing project or switching to PyPDF3.

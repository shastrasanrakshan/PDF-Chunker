# PDF Chunker (5 Pages per File)

This utility splits a PDF into smaller PDFs, each containing **5 pages**, and saves them into a new folder in the **same directory** as the original file.

The script is interactive: it asks for the PDF file path after you run it.

---

## 📌 Features

* Splits PDFs into chunks of **exactly 5 pages** (last chunk may have fewer)
* Takes **only one input** (PDF file path)
* Automatically creates an output folder
* Simple, dependency-light Python script

---

## 🧰 Prerequisites

### 1. Python (3.7 or newer)

Check if Python is installed:

```bash
python --version
```

or

```bash
python3 --version
```

If not installed, download from:

* [https://www.python.org/downloads/](https://www.python.org/downloads/)

---

### 2. Python Package: `PyPDF2`

Install using **one of the following** commands (use whichever works on your system):

```bash
pip install PyPDF2
```

or

```bash
pip3 install PyPDF2
```

or explicitly via Python:

```bash
python -m pip install PyPDF2
```

#### Verify installation

```bash
python -c "import PyPDF2; print(PyPDF2.__version__)"
```

If this runs without error, the dependency is installed correctly.

---

## 📂 Files

```
chunk_pdf.py
README.md
```

---

## ▶️ Usage Instructions

### 1. Run the script

```bash
python chunk_pdf.py
```

### 2. Enter PDF path when prompted

```text
Enter full path of the PDF file:
```

Example inputs:

```text
/home/user/Documents/report.pdf
```

or (Windows):

```text
C:\Users\Atishay\Documents\report.pdf
```

---

## 📁 Output Structure

If your input file is:

```
report.pdf
```

The script will create:

```
report_chunks/
├── report_part_1.pdf   (pages 1–5)
├── report_part_2.pdf   (pages 6–10)
├── report_part_3.pdf
└── ...
```

The output folder is created **in the same directory** as the original PDF.

---

## ⚠️ Common Errors & Fixes

### `No module named 'PyPDF2'`

Install the dependency:

```bash
python -m pip install PyPDF2
```

Ensure you are using the **same Python** for both install and execution.

---

### `Error: File does not exist`

* Check the file path
* Ensure the PDF file actually exists
* Avoid trailing spaces in the input

---

### `Error: Input file must be a PDF`

* The file must end with `.pdf`

---

## 🔧 Customization

To change the chunk size, edit this line in `chunk_pdf.py`:

```python
CHUNK_SIZE = 5
```

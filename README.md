# CCCD OCR Rental Contract Generator

#### Video Demo:  <VIDEO_URL_HERE>

#### Description:

## Overview

The CCCD OCR Rental Contract Generator is a Python-based application that automatically extracts personal information from a Vietnamese Citizen Identity Card (CCCD) image and inserts that information into a rental contract template in Microsoft Word format (.docx).

The main purpose of this project is to automate the manual process of copying identity information into legal documents. Instead of manually typing personal details into a rental agreement, users only need to provide:

1. The filename of the CCCD image
2. The filename of the rental contract template (.docx)

The program then:
- Extracts text from the image using OCR
- Parses important identity fields using Regular Expressions
- Replaces placeholders inside a Word contract template
- Generates a completed rental contract document automatically

This project demonstrates practical applications of Python in document automation, OCR processing, text parsing, and file handling.

---

## Features

- Optical Character Recognition (OCR) using Tesseract
- Structured data extraction using Regular Expressions
- Automatic Microsoft Word (.docx) document editing
- Modular, function-based program structure
- Unit testing using pytest
- Graceful error handling for missing files or invalid inputs

---

## How It Works

### Step 1: Extract Text from Image

The program uses the `pytesseract` library together with `Pillow` to open and analyze the CCCD image. The image is processed and converted into a raw text string using OCR.

Tesseract must be installed on the system separately, as it is an external OCR engine.

---

### Step 2: Parse CCCD Information

After extracting raw text, the program uses Regular Expressions (`re.search`) to locate specific identity fields.

Instead of relying heavily on Vietnamese diacritics (which OCR may misread), the program focuses on English labels commonly found on the newer CCCD format, such as:

- Full name:
- Date of birth:
- Personal identification number:
- Date of issue:
- Place of issue:
- Place of residence:

Each matched value is stored inside a Python dictionary.  
If a field cannot be detected, the program assigns a fallback value instead of crashing.

---

### Step 3: Fill Rental Contract Template

The program opens a `.docx` template using the `python-docx` library and replaces predefined placeholders such as:

- {{NAME}}
- {{DOB}}
- {{ID}}
- {{ISSUE_PLACE}}
- {{ISSUE_DATE}}
- {{ADDRESS}}

These placeholders correspond to the renter’s identity information in the rental contract (BÊN THUÊ – Bên B section).

The completed contract is saved as a new `.docx` file, preserving the original template.

---

## Program Structure

This project follows CS50P final project requirements:

- A `main()` function in `project.py`
- At least three additional top-level functions:
  - `extract_text_from_image`
  - `parse_cccd_info`
  - `fill_rental_contract`
- A separate `test_project.py` file containing unit tests
- A `requirements.txt` file listing all dependencies

All functions are defined at the same indentation level and are not nested.

---

## Design Decisions

### Modular Design

Each function has a single responsibility:

- OCR processing
- Data extraction
- Document generation

This separation improves readability, maintainability, and testability.

### Use of Regular Expressions

OCR output is often inconsistent due to spacing or minor recognition errors.  
Regular Expressions provide flexible and powerful pattern matching, making the system more robust than simple string splitting.

### Use of python-docx

The `python-docx` library was chosen because it allows direct editing of Microsoft Word documents, which makes this system suitable for legal and administrative automation.

---

## Challenges Encountered

1. OCR may misread accented Vietnamese characters.
2. CCCD layouts may vary slightly between versions.
3. Word formatting can break if placeholders are not replaced carefully.

These challenges were addressed by:
- Prioritizing English labels for parsing
- Implementing fallback values for missing fields
- Designing clear placeholder markers in the template

---

## Future Improvements

Possible enhancements include:

- Validating 12-digit CCCD numbers
- Formatting dates into formal legal style
- Supporting batch processing of multiple CCCD images
- Adding a graphical user interface (GUI)
- Improving regex robustness
- Preserving Word formatting more precisely

---

## Technologies Used

- Python 3
- pytesseract
- Pillow
- python-docx
- pytest

---

## Conclusion

This project demonstrates how Python can automate administrative and legal workflows by integrating OCR, text parsing, and document generation into one cohesive system.

The implementation satisfies all CS50P final project requirements and reflects practical, real-world software development practices.
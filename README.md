# CCCD OCR Rental Contract Generator

#### Video Demo: <https://youtu.be/y3hh9ZYIFyo>

#### Description:

## Overview

The CCCD OCR Rental Contract Generator is a Python application that automates the process of extracting personal information from a Vietnamese Citizen Identity Card (CCCD) image and inserting that information into a rental contract template in Microsoft Word format (.docx).

I built this project because in my family’s work, drafting rental contracts is a repetitive and time-consuming task. Each time a new contract is created, identity details such as full name, ID number, date of birth, and address must be manually typed from an ID card into a document. Although simple, this process is monotonous and can lead to small typing errors. I wanted to create a tool that reduces manual effort and improves efficiency.

This project demonstrates how Python can automate a real administrative workflow by combining OCR, text processing, and document generation.

---

## How the Program Works

The program operates in three main stages: text extraction, data parsing, and document generation.

First, the function `extract_text_from_image()` uses the `pytesseract` library, a Python wrapper for the Tesseract OCR engine, to convert the text inside the CCCD image into raw string output. Because OCR accuracy depends on image quality, the program is designed to tolerate minor formatting inconsistencies.

Second, the function `parse_cccd_info()` analyzes the extracted text and uses Regular Expressions (regex) to identify key fields such as full name, date of birth, personal ID, place of residence, date of issue, and place of issue. I chose regex because OCR output may vary in spacing and line structure. Regex makes the extraction logic flexible and more reliable than simple string splitting.

Finally, the function `fill_rental_contract()` uses the `python-docx` library to open a Word template containing placeholders like `{{NAME}}`, `{{DOB}}`, and `{{ID}}`. The program replaces these placeholders with extracted data and saves a new completed contract file, preserving the original template.

---

## Privacy and Use of AI-Generated Images

To protect personal information, I did not use a real CCCD image in this project. Instead, I generated a sample CCCD image using AI tools (ChatGPT-5) to simulate realistic content. This ensures that no sensitive personal data is exposed in the source code, demo video, or repository.

Since identity documents contain highly sensitive information, it is important to maintain privacy when building and sharing software projects. By using AI-generated sample data, I was able to fully demonstrate the functionality of the OCR system while keeping personal information secure. This reflects responsible development practices and awareness of data protection concerns.

---

## Project Files

**project.py**
This is the main application file. It contains all core functions: OCR extraction, parsing logic, and document generation. The `main()` function coordinates the workflow and handles user input.

**test_project.py**
This file contains unit tests written with `pytest`. Because OCR results may vary, the tests focus on verifying the parsing logic using simulated text samples. This ensures the regex extraction works as expected.

**requirements.txt**
This file lists required dependencies such as `pytesseract`, `Pillow`, `python-docx`, and `pytest`, making the environment easy to reproduce.

---

## Design Decisions

The program is divided into modular functions, each with a single responsibility. This improves readability and maintainability.

Regex was chosen for flexibility in handling imperfect OCR output. Additionally, using placeholders inside a Word template keeps document formatting separate from program logic, allowing easy customization without modifying code.

---

## Conclusion

The CCCD OCR Rental Contract Generator transforms a repetitive manual task into an automated workflow. It fulfills CS50P requirements while solving a real-world problem in a practical way. More importantly, it reflects thoughtful design decisions, attention to privacy, and a focus on applying programming skills to meaningful situations.

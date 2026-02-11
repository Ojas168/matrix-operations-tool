# 🧮 Matrix Operations Tool (Web App)

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-Web%20App-FF4B4B?logo=streamlit)
![NumPy](https://img.shields.io/badge/NumPy-Scientific%20Computing-013243?logo=numpy)
![MIT License](https://img.shields.io/badge/License-MIT-green)

A simple, interactive **web-based Matrix Operations Tool** built using **Python, NumPy, and Streamlit**.  
This application allows users to input matrices of custom dimensions and perform common matrix operations through a clean and intuitive UI.

---

## 🚀 Features

- Interactive web interface (no terminal usage)
- Dynamic matrix input (rows & columns)
- Matrix operations:
  - ➕ Addition
  - ➖ Subtraction
  - ✖️ Multiplication (with dimension validation)
  - 🔄 Transpose
  - 🔢 Determinant (square matrices only)
- Real-time error handling with user-friendly messages
- Results displayed in a structured tabular format

---

## 🖥️ User Interface Overview

1. **Matrix Dimension Input**
   - Users specify the number of rows and columns.

2. **Matrix Value Input**
   - Each row is entered as space-separated values.
   - Separate sections for Matrix A and Matrix B.

3. **Operation Selector**
   - Dropdown menu to choose the desired matrix operation.

4. **Action Button**
   - A “Calculate” button triggers the computation.

5. **Result Display**
   - Output matrices are shown as tables.
   - Determinants are displayed as numeric values.
   - Invalid operations show descriptive error messages.

---

## 🛠️ Tech Stack

- **Language:** Python 3.12.11
- **Libraries:**
  - NumPy (matrix computations)
  - Streamlit (web interface)
- **Version Control:** Git & GitHub

---

## 📦 Installation & Setup

1️⃣ Clone the repository

git clone https://github.com/your-username/matrix-operations-tool.git
cd matrix-operations-tool

2️⃣ Install dependencies
pip install -r requirements.txt

3️⃣ Run the application
streamlit run app.py

The app will automatically open in your browser.


## 📸 Screenshots
<img width="918" height="928" alt="1" src="https://github.com/user-attachments/assets/5fd84919-bf78-43d8-ab71-a19e598ae17c" />

<img width="920" height="362" alt="2" src="https://github.com/user-attachments/assets/599217c2-ed10-4acc-a7c1-b3cd13d04f48" />

## ⚠️ Validation Rules

1. Addition & Subtraction require matrices of the same shape.
2. Multiplication requires:

   columns of Matrix A == rows of Matrix B

3. Determinant is only available for square matrices.
Invalid operations are blocked with informative error messages.

## 👤 Author: Ojas Vishwa Mohan
Built as a learning project to understand matrix operations and Python-based web applications.

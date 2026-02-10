# 🧮 Matrix Operations Tool (Web App)

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

### 1️⃣ Clone the repository
```bash
git clone https://github.com/your-username/matrix-operations-tool.git
cd matrix-operations-tool

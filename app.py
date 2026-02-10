import streamlit as st
import numpy as np
st.title("🧮 Matrix Operations Tool")
st.write("Enter matrices and perform operations easily!")
rows = st.number_input("Number of rows", min_value=1, value=2)
cols = st.number_input("Number of columns", min_value=1, value=2)
def get_matrix(name, rows, cols):
    st.subheader(f"Matrix {name}")
    matrix = []

    for i in range(rows):
        row = st.text_input(   # Prompt user to enter each row of the matrix
            f"Row {i + 1} (enter {cols} numbers, space-separated)",
            key=f"{name}_row_{i}"
        )

        if not row: # If any row is empty, we can't proceed
            return None

        try:
            values = list(map(int,row.split())) 
        except ValueError:
            st.error(f"Row {i + 1}: Please enter valid numbers")
            return None

        if len(values) != cols:
            st.error(f"Row {i + 1}: Exactly {cols} values required")
            return None

        matrix.append(values)

    return np.array(matrix)
A=get_matrix("A", rows, cols)
B=get_matrix("B", rows, cols)
operation = st.selectbox(
    "Choose Operation",
    ["Addition", "Subtraction", "Multiplication", "Transpose A", "Determinant A"]
)
if st.button("Calculate"):
    if operation == "Addition":
        if A is not None and B is not None:
            st.write("Result of A + B:")
            st.table(A + B)
    elif operation == "Subtraction":
        if A is not None and B is not None:
            st.write("Result of A - B:")
            st.table(A - B)
    elif operation == "Multiplication":
        if A is not None and B is not None:
            if A.shape[1] == B.shape[0]:
                st.subheader("Result")
                st.table(np.dot(A, B))
            else:
                st.error(
                f"Cannot multiply matrices of shape {A.shape} and {B.shape}. "
                "Columns of A must equal rows of B."
            )
    elif operation == "Transpose A":
        if A is not None:
            st.write("Transpose of A:")
            st.table(A.T)
    elif operation == "Determinant A":
        if A is not None and A.shape[0] == A.shape[1]:
            st.success(f"Determinant of A: {np.linalg.det(A):.2f}")
        else:
            st.error("Matrix A must be square to calculate determinant")
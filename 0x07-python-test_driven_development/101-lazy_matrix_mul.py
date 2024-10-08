#!/usr/bin/python3
# 101-lazy_matrix_mul.py
"""Defines a matrix multiplication function using NumPy."""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """ It Return the multiplication of two matrices.

    Args:
        m_a (list of lists of ints or floats): The first matrix.
        m_b (list of lists of ints or floats): The second matrix.
    """

    return (np.matmul(m_a, m_b))

#!/usr/bin/env python
# -*- coding: utf-8 -*-

from trajectorypy import *
import numpy as np

def test_trajectory_filter():
    base_size = 64
    x0 = [0, 0, 0, 0, 0, 0]
    
    # square
    square_object_size = [base_size, base_size]
    square_filter = TrajectoryFilter(x0, square_object_size)
    # twice wider
    wider_object_size = [base_size * 2, base_size]
    wider_filter = TrajectoryFilter(x0, wider_object_size)
    # twice taller
    taller_object_size = [base_size, base_size * 2]
    taller_filter = TrajectoryFilter(x0, taller_object_size)

    # compare P
    assert np.array_equal(square_filter.P[:3] * 2.0**2, wider_filter.P[:3])
    assert np.array_equal(square_filter.P[3:], wider_filter.P[3:])

    assert np.array_equal(square_filter.P[:3], taller_filter.P[:3])
    assert np.array_equal(square_filter.P[3:] * 2.0**2, taller_filter.P[3:])

    # compare Q
    assert np.array_equal(square_filter.Q[:3] * 2.0**2, wider_filter.Q[:3])
    assert np.array_equal(square_filter.Q[3:], wider_filter.Q[3:])

    assert np.array_equal(square_filter.Q[:3], taller_filter.Q[:3])
    assert np.array_equal(square_filter.Q[3:] * 2.0**2, taller_filter.Q[3:])

    # compare R
    assert np.array_equal(square_filter.R[:1] * 2.0**2, wider_filter.R[:1])
    assert np.array_equal(square_filter.R[1:], wider_filter.R[1:])

    assert np.array_equal(square_filter.R[:1], taller_filter.R[:1])
    assert np.array_equal(square_filter.R[1:] * 2.0**2, taller_filter.R[1:])
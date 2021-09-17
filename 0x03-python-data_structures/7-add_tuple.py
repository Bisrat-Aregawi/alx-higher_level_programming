#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    na, nb = len(tuple_a), len(tuple_b)

    new_tuple = ((tuple_a[0] if na >= 1 else 0) +
                 (tuple_b[0] if nb >= 1 else 0),
                 (tuple_a[1] if na >= 2 else 0) +
                 (tuple_b[1] if nb >= 2 else 0))
    return new_tuple

#!/usr/bin/env python3
"""Check small exchange-receiver instances using exact rational matrix algebra."""

from collections import defaultdict
from fractions import Fraction
from itertools import combinations, product
from math import comb


def identity(wires):
    return tuple(range(wires))


def exchange(wires, left, right):
    permutation = list(identity(wires))
    permutation[left], permutation[right] = right, left
    return tuple(permutation)


def multiply(first, second):
    """Multiply operators stored as weighted sums of permutation matrices."""
    result = defaultdict(Fraction)
    for left, left_weight in first.items():
        for right, right_weight in second.items():
            permutation = tuple(right[index] for index in left)
            result[permutation] += left_weight * right_weight
    return {permutation: weight for permutation, weight in result.items() if weight}


def adjoint(operator):
    return {
        tuple(sorted(range(len(permutation)), key=permutation.__getitem__)): weight
        for permutation, weight in operator.items()
    }


def trace(operator, dimension):
    total = Fraction()
    for permutation, weight in operator.items():
        seen = set()
        cycles = 0
        for first in range(len(permutation)):
            if first in seen:
                continue
            cycles += 1
            current = first
            while current not in seen:
                seen.add(current)
                current = permutation[current]
        total += weight * dimension**cycles
    return total


def entry(operator, row, column):
    return sum(
        weight
        for permutation, weight in operator.items()
        if row == tuple(column[index] for index in permutation)
    )


def source(dimension, visibility, matching, shots=1):
    wires = 2 * len(matching) * shots
    exchange_weight = visibility / (dimension * (dimension + 1))
    identity_weight = (1 - visibility) / dimension**2 + exchange_weight
    unit = identity(wires)
    state = {unit: Fraction(1)}
    for shot in range(shots):
        offset = shot * 2 * len(matching)
        for left, right in matching:
            swap = exchange(wires, left + offset, right + offset)
            state = multiply(state, {unit: identity_weight, swap: exchange_weight})
    return state


def exchange_count_projector(ports, shots, edge, minimum):
    """Sum the sign-sector projectors that meet the integer threshold."""
    wires = ports * shots
    unit = identity(wires)
    left, right = edge
    accepted = defaultdict(Fraction)
    for signs in product((1, -1), repeat=shots):
        if signs.count(1) < minimum:
            continue
        sector = {unit: Fraction(1)}
        for shot, sign in enumerate(signs):
            swap = exchange(wires, left + shot * ports, right + shot * ports)
            sector = multiply(sector, {unit: Fraction(1, 2), swap: Fraction(sign, 2)})
        for permutation, weight in sector.items():
            accepted[permutation] += weight
    return {permutation: weight for permutation, weight in accepted.items() if weight}


def complement(projector, wires):
    result = {permutation: -weight for permutation, weight in projector.items()}
    unit = identity(wires)
    result[unit] = 1 + result.get(unit, 0)
    return {permutation: weight for permutation, weight in result.items() if weight}


def check_marginals(dimension, visibility, matching):
    state = source(dimension, visibility, matching)
    assert trace(state, dimension) == 1
    p0 = Fraction(dimension + 1, 2 * dimension)
    q0 = Fraction(1, dimension)
    basis = tuple(product(range(dimension), repeat=4))
    for edge in ((0, 1), (0, 2)):
        left, right = edge
        positive = exchange_count_projector(4, 1, edge, 1)
        observed_exchange = trace(multiply(state, positive), dimension)
        observed_collision = sum(entry(state, v, v) for v in basis if v[left] == v[right])
        if edge in matching:
            collision_gap = visibility * (dimension - 1) / (dimension * (dimension + 1))
            assert observed_exchange == p0 + visibility * (1 - p0)
            assert observed_collision == q0 + collision_gap
        else:
            assert observed_exchange == p0
            assert observed_collision == q0


def check_port_partial_transpose(dimension, visibility, matching):
    state = source(dimension, visibility, matching)
    epsilon = visibility / (dimension + 1)
    basis = tuple(product(range(dimension), repeat=4))
    for row in basis:
        for column in basis:
            transposed_row = (row[0], column[1], row[2], column[3])
            transposed_column = (column[0], row[1], column[2], row[3])
            expected = Fraction(1)
            for left, right in matching:
                diagonal = row[left] == column[left] and row[right] == column[right]
                entangled = row[left] == row[right] and column[left] == column[right]
                pair_entry = (1 - epsilon) * diagonal / dimension**2 + epsilon * entangled / dimension
                expected *= pair_entry
            assert entry(state, transposed_row, transposed_column) == expected


def check_correct_sequence(matching):
    shots, ports, dimension = 2, 4, 2
    wires = ports * shots
    noisy_state = source(dimension, Fraction(3, 10), matching, shots)
    noisy_detection = exchange_count_projector(ports, shots, (0, 1), 1)
    p1 = Fraction(3, 4) + Fraction(3, 10) * Fraction(1, 4)
    expected = sum(
        comb(shots, k) * p1**k * (1 - p1) ** (shots - k)
        for k in range(1, shots + 1)
    )
    assert trace(multiply(noisy_state, noisy_detection), dimension) == expected

    state = source(dimension, Fraction(1), matching, shots)
    correct_sequence = {identity(wires): Fraction(1)}
    for edge in combinations(range(ports), 2):
        accept = exchange_count_projector(ports, shots, edge, shots)
        assert accept == adjoint(accept) == multiply(accept, accept)
        correct = accept if edge in matching else complement(accept, wires)
        correct_sequence = multiply(correct, correct_sequence)
    final_state = multiply(correct_sequence, multiply(state, adjoint(correct_sequence)))
    probability = trace(final_state, dimension)
    assert probability == Fraction(20537, 589824)
    assert 16 * Fraction(3, 4) ** 21 < Fraction(1, 20)
    print(f"Four qubit ports, two noiseless shots: exact success {probability} ({float(probability):.10f})")


def main():
    matching = ((0, 1), (2, 3))
    other_matching = ((0, 3), (2, 1))
    for dimension in (2, 3):
        for visibility in (Fraction(1, 20), Fraction(3, 10), Fraction(1)):
            check_marginals(dimension, visibility, matching)
            check_port_partial_transpose(dimension, visibility, matching)
            check_port_partial_transpose(dimension, visibility, other_matching)
    check_correct_sequence(matching)
    print("Exchange probabilities, collisions, projectors and partial transpose pass.")


if __name__ == "__main__":
    main()

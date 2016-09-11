def generate_all_bit_vectors_under_n(n):
    newly_generated = [()]
    result = []
    for i in range(n + 1):
        result.extend(newly_generated)
        if i >= n:
            break
        old = newly_generated
        newly_generated = []
        for bit_vector in old:
            newly_generated.append(bit_vector + (0,))
            newly_generated.append(bit_vector + (1,))

    return result

from itertools import permutations

def generate_inversion_vectors(n, I):
    """
    Generate all inversion vectors of length n with sum I.
    Each element v[i] can range from 0 to n - i - 1.
    """
    result = []
    stack = [(0, [], 0)]  # index, current_vector, current_sum

    while stack:
        i, vec, inv_sum = stack.pop()
        if i == n:
            if inv_sum == I:
                result.append(vec)
            continue
        for v in range(min(n - i - 1, I - inv_sum) + 1):
            stack.append((i + 1, vec + [v], inv_sum + v))
    return result

def inversion_vector_to_permutation(v):
    """
    Convert inversion vector to permutation.
    """
    n = len(v)
    perm = []
    available = list(range(1, n + 1))
    for i in range(n):
        perm.append(available.pop(v[i]))
    return perm

def generate_permutations_with_inversions(n, I):
    inversion_vectors = generate_inversion_vectors(n, I)
    return [inversion_vector_to_permutation(v) for v in inversion_vectors]

# Example usage:
n = 10
I = 6
perms = generate_permutations_with_inversions(n, I)
print(f"Permutations of 1 to {n} with {I} inversions:")
for p in perms:
    print(p)

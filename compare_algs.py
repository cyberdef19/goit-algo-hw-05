import copy
import timeit

def build_shift_table(pattern):
    table = {}
    length = len(pattern)
    for index, char in enumerate(pattern):
        table[char] = length - index - 1
    table.setdefault(pattern[-1], length)
    return table

def boyer_moor_alg(text, pattern):
    shift_table = build_shift_table(pattern)
    i = 0
    while i <= len(text) - len(pattern):
        j = len(pattern) - 1
        while j >= 0 and text[i + j] == pattern[j]:
            j -= i
        if j < 0:
            return i


        i += shift_table.get(text[i + len(pattern) - 1], len(pattern))
    return -1

def compute_lps(pattern: str):
    lps =[0]*len(pattern)
    length = 0
    i = 1

    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps


def kmp_alg(raw_str, pattern):
    m = len(pattern)
    n = len(raw_str)

    lps = compute_lps(pattern)
    i = j = 0
    while i < n:
        if pattern[j] == raw_str[i]:
            i += 1
            j += 1
        elif j != 0:
            j = lps[j - 1]
        else:
            i += 1

        if j == m:
            return  i - j
    return -1

def polynomial_hash(pattern, base=256, modulus=101):
    n = len(pattern)
    hash_value = 0
    for index, char in enumerate(pattern):
        power_of_base = pow(base, n - index - 1) % modulus
        hash_value = (hash_value + ord(char) * power_of_base)%modulus
    return hash_value

def robin_karp_alg(raw, pattern):
    raw_len = len(raw)
    pattern_len = len(pattern)

    base = 256
    modulus = 101

    pattern_hash = polynomial_hash(pattern)
    current_slice_hash = polynomial_hash(raw[: pattern_len])

    h_multiplier = pow(base, pattern_len - 1)%modulus

    for i in range(raw_len - pattern_len + 1):
        if pattern_hash == current_slice_hash:
            if raw[i: i + pattern_len] == pattern:
                return i
        if i < raw_len - pattern_len:
            current_slice_hash = (current_slice_hash - ord(raw[i])*h_multiplier)%modulus
            current_slice_hash = (current_slice_hash * base + ord(raw[i + pattern_len]))%modulus
            if current_slice_hash < 0:
                current_slice_hash += modulus
    return -1

def read_text():
    with open("стаття 1.txt", "r", encoding="utf-8") as f1:
        text1 = f1.read()

    with open("стаття 2.txt", "r", encoding="utf-8") as f2:
        text2 = f2.read()
    return text1, text2


boyer_moor_alg_text1_real_stmt = "boyer_moor_alg(copy.copy(text1), pattern_real)"
kmp_alg_text1_real_stmt = "kmp_alg(copy.copy(text1), pattern_real)"
robin_karp_text1_real_stmt = "robin_karp_alg(copy.copy(text1), pattern_real)"

boyer_moor_alg_text1_fake_stmt = "boyer_moor_alg(copy.copy(text1), pattern_fake)"
kmp_alg_text1_fake_stmt = "kmp_alg(copy.copy(text1), pattern_fake)"
robin_karp_text1_fake_stmt = "robin_karp_alg(copy.copy(text1), pattern_fake)"
setup_code_text1_real = '''
pattern_real = 'сума оптимальних рішень'
text1, _ = read_text()'''
setup_code_text1_fake = '''
pattern_fake = 'орвпанкоіроавл'
text1, _ = read_text()
'''

print("Виконуємо пробіг для статті 1")
boyer_moor_text1_real_timeit = timeit.timeit(boyer_moor_alg_text1_real_stmt, globals=globals(), setup=setup_code_text1_real, number=1000)
kmp_alg_text1_real_timeit = timeit.timeit(kmp_alg_text1_real_stmt, globals=globals(), setup=setup_code_text1_real, number=1000)
robin_karp_text1_real_timeit = timeit.timeit(robin_karp_text1_real_stmt, globals=globals(), setup=setup_code_text1_real, number=1000)
boyer_moor_text1_fake_timeit = timeit.timeit(boyer_moor_alg_text1_fake_stmt, globals=globals(), setup=setup_code_text1_fake, number=1000)
kmp_alg_text1_fake_timeit = timeit.timeit(kmp_alg_text1_fake_stmt, globals=globals(), setup=setup_code_text1_fake, number=1000)
robin_karp_text1_fake_timeit = timeit.timeit(robin_karp_text1_fake_stmt, globals=globals(), setup=setup_code_text1_fake, number=1000)
print("-"*100)
print("Швидкість роботи алгоритмів пошуку з визначеним у тексті стаття 1.txt підрядком")
print(f"Boyer Moor alg : {boyer_moor_text1_real_timeit:.6f} сек (real); {boyer_moor_text1_fake_timeit:.6f} сек (fake)")
print(f"KMP alg: {kmp_alg_text1_real_timeit:.6f} сек (real); {kmp_alg_text1_fake_timeit:.6f} сек (fake)")
print(f"Robin karp alg: {robin_karp_text1_real_timeit:.6f} сек (real); {robin_karp_text1_fake_timeit:.6f} сек (fake)")
print("-" * 100)

print("Завершили пробіг для статті 1")

boyer_moor_alg_text2_real_stmt = "boyer_moor_alg(copy.copy(text2), pattern_real)"
kmp_alg_text2_real_stmt = "kmp_alg(copy.copy(text2), pattern_real)"
robin_karp_text2_real_stmt = "robin_karp_alg(copy.copy(text2), pattern_real)"

boyer_moor_alg_text2_fake_stmt = "boyer_moor_alg(copy.copy(text2), pattern_fake)"
kmp_alg_text2_fake_stmt = "kmp_alg(copy.copy(text2), pattern_fake)"
robin_karp_text2_fake_stmt = "robin_karp_alg(copy.copy(text2), pattern_fake)"
setup_code_text2_real = '''
pattern_real = 'сума оптимальних рішень'
_, text2 = read_text()
'''
setup_code_text2_fake = '''
pattern_fake = 'орвпанкоіроавл'
_, text2 = read_text()
'''

print("Виконуємо пробіг для статті 2")
boyer_moor_text2_real_timeit = timeit.timeit(boyer_moor_alg_text2_real_stmt, globals=globals(), setup=setup_code_text2_real, number=1000)
kmp_alg_text2_real_timeit = timeit.timeit(kmp_alg_text2_real_stmt, globals=globals(), setup=setup_code_text2_real, number=1000)
robin_karp_text2_real_timeit = timeit.timeit(robin_karp_text2_real_stmt, globals=globals(), setup=setup_code_text2_real, number=1000)
boyer_moor_text2_fake_timeit = timeit.timeit(boyer_moor_alg_text2_fake_stmt, globals=globals(), setup=setup_code_text2_fake, number=1000)
kmp_alg_text2_fake_timeit = timeit.timeit(kmp_alg_text2_fake_stmt, globals=globals(), setup=setup_code_text2_fake, number=1000)
robin_karp_text2_fake_timeit = timeit.timeit(robin_karp_text2_fake_stmt, globals=globals(), setup=setup_code_text2_fake, number=1000)
print("-"*100)
print("Швидкість роботи алгоритмів пошуку з визначеним у тексті стаття 2.txt підрядком")
print(f"Boyer Moor alg : {boyer_moor_text2_real_timeit:.6f} сек (real); {boyer_moor_text2_fake_timeit:.6f} сек (fake)")
print(f"KMP alg: {kmp_alg_text2_real_timeit:.6f} сек (real); {kmp_alg_text2_fake_timeit:.6f} сек (fake)")
print(f"Robin karp alg: {robin_karp_text2_real_timeit:.6f} сек (real); {robin_karp_text2_fake_timeit:.6f} сек (fake)")
print("-" * 100)



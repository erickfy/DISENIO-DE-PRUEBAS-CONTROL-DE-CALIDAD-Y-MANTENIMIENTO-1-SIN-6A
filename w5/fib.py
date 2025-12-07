from functools import lru_cache

# https://www.geeksforgeeks.org/python/python-program-to-print-the-fibonacci-sequence/
@lru_cache(None)
def fibonacci_cached(num: int) -> int:

    # check if num is less than 0 it will return none
    if num < 0:
        print("Incorrect input")
        return

    # check if num between 1, 0 it will return num
    elif num < 2:
        return num

    # return the fibonacci of num - 1 & num - 2
    return fibonacci_cached(num - 1) + fibonacci_cached(num - 2)

def fibonacci_sequence_cached(n: int) -> list[int]:
    """Devuelve la secuencia de Fibonacci usando la función cacheada."""
    if n <= 0:
        return []
    return [fibonacci_cached(i) for i in range(n)]


def fibonacci(n: int) -> list[int]:
    """Devuelve la secuencia de Fibonacci hasta n términos."""
    if n <= 0:
        return []
    if n == 1:
        return [0]

    seq = [0, 1]
    while len(seq) < n:
        seq.append(seq[-1] + seq[-2])
    return seq


if __name__ == "__main__":
    n = 10
    print(f"Primeros {n} números de Fibonacci:")
    print(fibonacci(n))

    # fibonacci_cached
    print(f"Primeros {n} números de Fibonacci (cached function):")
    print(fibonacci_sequence_cached(n))
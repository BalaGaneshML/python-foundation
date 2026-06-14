import time
import random
from functools import wraps

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"[TIMER] {func.__name__} took {end - start:.4f} seconds")
        return result
    return wrapper

@timer
def slow_calculation(n):
    total = 0
    for i in range(n):
        total += i
    return total
# result = slow_calculation(10000000)
# print("Result:", result)

def logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[LOGGER] Calling {func.__name__}")
        print(f"[LOGGER] Arguments: {args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"[LOGGER] {func.__name__} returned: {result}")
        return result
    return wrapper

@logger
def add(a, b):
    return a + b

# add(a=10, b=20)

@timer
@logger
def calculate_sum(n):
    return sum(range(n))

# result=calculate_sum(500000)
# print("Final Result:", result)


#Task 1

def retry(max_attempts=3):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None
            for attempt in range(1, max_attempts + 1):
                try:
                    result = func(*args, **kwargs)
                    return result
                except Exception as e:
                    last_exception = e
                    print(f"[RETRY] Attempt {attempt} failed: {e}")
            print(f"[RETRY] All {max_attempts} attempts failed.")
            raise last_exception
        return wrapper
    return decorator

attempt_counter = [0]

@retry(max_attempts=3)
def unreliable_function():
    attempt_counter[0] += 1
    if attempt_counter[0] < 3:
        raise ValueError(f"Simulated failure on attempt {attempt_counter[0]}")
    return "Success on attempt 3"

result = unreliable_function()
print("Result:", result)

@retry(max_attempts=3)
def always_fails():
    raise RuntimeError("This always fails")

try:
    always_fails()
except RuntimeError as e:
    print("Caught final exception:", e)

#Task 2

def cache(func):
    storage = {}
    @wraps(func)
    def wrapper(*args):
        if args in storage:
            print(f"[CACHE] Returning cached result for args {args}")
            return storage[args]
        result = func(*args)
        storage[args] = result
        print(f"[CACHE] Stored result for args {args}")
        return result
    return wrapper

@cache
def slow_power(base, exponent):
    time.sleep(1)  # simulate expensive computation
    return base ** exponent


print("First call with (2, 10):")
result1 = slow_power(2, 10)
print("Result:", result1)

print("\nSecond call with (2, 10):")
result2 = slow_power(2, 10)
print("Result:", result2)

print("\nFirst call with (3, 5):")
result3 = slow_power(3, 5)
print("Result:", result3)

print("\nSecond call with (3, 5):")
result4 = slow_power(3, 5)
print("Result:", result4)


#Task 3

call_log = []

@cache
@retry(max_attempts=4)
def unreliable_calculation(n):
    roll = random.random()
    call_log.append(f"Called with n={n}, roll={roll:.2f}")
    if roll < 0.6:
        raise ValueError(f"Random failure (roll={roll:.2f})")
    return n * 2

print("=== Testing combined cache + retry ===")

for i in range(5):
    try:
        result = unreliable_calculation(5)
        print(f"Call {i+1}: Result = {result}")
    except Exception as e:
        print(f"Call {i+1}: All retries failed — {e}")

print("\nCall log:")
for entry in call_log:
    print(" ", entry)


# OBSERVATIONS:
# Once unreliable_calculation(5) succeeds for the first time (possibly after retries),
# all subsequent calls with argument 5 return instantly from cache.
# Cache stores the successful result and completely bypasses retry logic on future calls.
# The call_log shows no new entries after the first successful call with a given argument.
# Stacking @cache outside @retry means cache is checked first — if hit, retry code never runs.
# If @retry were outside @cache, retries could cause duplicate cache lookups on failure.

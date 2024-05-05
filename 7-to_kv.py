#!/usr/bin/python3

def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Return a tuple with string k and square of int/float v."""
    return (k, v ** 2)

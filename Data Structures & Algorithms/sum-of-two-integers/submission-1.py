class Solution:
    def getSum(self, a: int, b: int) -> int:
        # Define a mask to simulate 32-bit integer
        MASK = 0xFFFFFFFF
        INT_MAX = 0x7FFFFFFF  # Max positive value for a 32-bit signed integer

        while b != 0:
            # Carry is AND operation, left-shifted
            carry = (a & b) << 1
            # Sum is XOR operation
            a = (a ^ b) & MASK  # Apply mask to keep a within 32 bits
            b = carry & MASK  # Apply mask to keep b within 32 bits

        # If a is greater than INT_MAX, it's negative in 32-bit signed integer
        return a if a <= INT_MAX else ~(a ^ MASK)
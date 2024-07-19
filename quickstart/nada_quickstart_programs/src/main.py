from nada_dsl import *

def nada_main():
    # Initialize parties
    party1 = Party(name="Party1")
    party2 = Party(name="Party2")

    # Secret integers from the parties
    A = SecretInteger(Input(name="A", party=party1))
    B = SecretInteger(Input(name="B", party=party2))

    # Compute (A + B)^2
    sum_ab = A + B
    result = sum_ab * sum_ab

    # Return the result
    return [Output(result, "my_output", party1)]

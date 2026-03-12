import socket

# Parameters from the Laboratory: The Interactive Math
P = 23  # Public Modulus
G = 5   # Public Generator (Base)

def main():
    print("--- Diffie-Hellman Client (Alice) ---")
    print(f"Publicly known: P = {P}, G = {G}\n")

    # 1. Select Private Key (a)
    try:
        private_a = int(input(f"Enter your private key (a) [Suggested 1-22]: "))
    except ValueError:
        private_a = 6
        print(f"Invalid input. Using default: {private_a}")

    # 2. Compute Public Key (A) Step-by-Step
    raw_pow_a = G ** private_a
    public_a = pow(G, private_a, P)
    
    print("\n[STEP 1] Generating your Public Key (A):")
    print(f"  Formula: G^a mod P")
    print(f"  Calculation: {G}^{private_a} mod {P}")
    print(f"  Raw power: {G}^{private_a} = {raw_pow_a:,}")
    print(f"  Modular result: {raw_pow_a:,} % {P} = {public_a}")
    print(f"  Result: Your Public Key (A) is {public_a}")

    # Set up networking
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        client_socket.connect(('localhost', 65432))
        
        # 3. Send Public Key (A) to Bob
        client_socket.sendall(str(public_a).encode())
        print(f"\n[STEP 2] Communication:")
        print(f"  -> Sent your Public Key (A) to Bob: {public_a}")

        # 4. Receive Bob's Public Key (B)
        data = client_socket.recv(1024).decode()
        public_b = int(data)
        print(f"  <- Received Bob's Public Key (B): {public_b}")

        # 5. Calculate Shared Secret (s) Step-by-Step
        raw_secret_pow = public_b ** private_a
        shared_secret = pow(public_b, private_a, P)
        
        print("\n[STEP 3] Calculating Shared Secret (s):")
        print(f"  Formula: B^a mod P")
        print(f"  Calculation: {public_b}^{private_a} mod {P}")
        print(f"  Raw power: {public_b}^{private_a} = {raw_secret_pow:,}")
        print(f"  Modular result: {raw_secret_pow:,} % {P} = {shared_secret}")
        
        print("\n" + "="*40)
        print(f"  FINAL SHARED SECRET: {shared_secret}")
        print("="*40)

    finally:
        client_socket.close()

if __name__ == "__main__":
    main()
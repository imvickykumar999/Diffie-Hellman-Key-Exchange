import socket

# Parameters from the Laboratory: The Interactive Math
P = 23  # Public Modulus
G = 5   # Public Generator (Base)

def main():
    print("--- Diffie-Hellman Server (Bob) ---")
    print(f"Publicly known: P = {P}, G = {G}\n")

    # 1. Select Private Key (b)
    try:
        private_b = int(input(f"Enter your private key (b) [Suggested 1-22]: "))
    except ValueError:
        private_b = 10
        print(f"Invalid input. Using default: {private_b}")

    # 2. Compute Public Key (B) Step-by-Step
    raw_pow_b = G ** private_b
    public_b = pow(G, private_b, P)
    
    print("\n[STEP 1] Generating your Public Key (B):")
    print(f"  Formula: G^b mod P")
    print(f"  Calculation: {G}^{private_b} mod {P}")
    print(f"  Raw power: {G}^{private_b} = {raw_pow_b:,}")
    print(f"  Modular result: {raw_pow_b:,} % {P} = {public_b}")
    print(f"  Result: Your Public Key (B) is {public_b}")

    # Set up networking
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('localhost', 65432))
    server_socket.listen(1)
    
    print("\nWaiting for Alice (Client) to connect...")
    conn, addr = server_socket.accept()
    
    try:
        # 3. Receive Alice's Public Key (A)
        data = conn.recv(1024).decode()
        public_a = int(data)
        print(f"\n[STEP 2] Communication:")
        print(f"  <- Received Alice's Public Key (A): {public_a}")
        
        # 4. Send Public Key (B) to Alice
        conn.sendall(str(public_b).encode())
        print(f"  -> Sent your Public Key (B) to Alice: {public_b}")

        # 5. Calculate Shared Secret (s) Step-by-Step
        raw_secret_pow = public_a ** private_b
        shared_secret = pow(public_a, private_b, P)
        
        print("\n[STEP 3] Calculating Shared Secret (s):")
        print(f"  Formula: A^b mod P")
        print(f"  Calculation: {public_a}^{private_b} mod {P}")
        print(f"  Raw power: {public_a}^{private_b} = {raw_secret_pow:,}")
        print(f"  Modular result: {raw_secret_pow:,} % {P} = {shared_secret}")
        
        print("\n" + "="*40)
        print(f"  FINAL SHARED SECRET: {shared_secret}")
        print("="*40)

    finally:
        conn.close()
        server_socket.close()

if __name__ == "__main__":
    main()
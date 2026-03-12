import socket

# Parameters from the Laboratory: The Interactive Math
P = 23  # Public Modulus
G = 5   # Public Generator (Base)

def main():
    # 1. Select Private Key (b)
    # In a real scenario, this would be a very large random number
    private_b = 15
    print(f"[STEP 1] Server (Bob) selected private key: {private_b}")

    # 2. Generate Public Key (B)
    # B = g^b mod p
    public_b = pow(G, private_b, P)
    print(f"[STEP 2] Computed Public Key (B): {public_b}")

    # Set up networking
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 65432))
    server_socket.listen(1)
    
    print("\nWaiting for Alice (Client) to connect...")
    conn, addr = server_socket.accept()
    
    try:
        # 3. Receive Public Key (A) from Alice
        data = conn.recv(1024).decode()
        public_a = int(data)
        print(f"[STEP 3] Received Alice's Public Key (A): {public_a}")

        # 4. Send Public Key (B) to Alice
        conn.sendall(str(public_b).encode())
        print(f"[STEP 4] Sent Public Key (B) to Alice.")

        # 5. Calculate Shared Secret (s)
        # s = A^b mod p
        shared_secret = pow(public_a, private_b, P)
        
        print("\n" + "="*30)
        print(f"SHARED SECRET DERIVED: {shared_secret}")
        print("="*30)
        print("Success! Bob and Alice now have the same key without ever sending it.")

    finally:
        conn.close()
        server_socket.close()

if __name__ == "__main__":
    main()
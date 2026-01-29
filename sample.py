import psycopg2
from werkzeug.security import generate_password_hash

# Use your EXACT Neon URL here
DB_URL = 'postgresql://neondb_owner:npg_A8d1ackmUwGN@ep-royal-darkness-a57zuf7k-pooler.us-east-2.aws.neon.tech/neondb?sslmode=require'

def verify_database_sync():
    print("--- Starting Database Audit ---")
    conn = None
    try:
        conn = psycopg2.connect(DB_URL)
        cur = conn.cursor()

        # 1. Create a test user with a hashed password
        test_username = "audit_user_1"
        raw_password = "password123"
        hashed_password = generate_password_hash(raw_password, method='pbkdf2:sha256')
        
        print(f"[*] Generated Hash: {hashed_password[:30]}...")

        # 2. Insert into the database
        print(f"[*] Inserting {test_username} into Neon...")
        cur.execute(
            "INSERT INTO users (username, password) VALUES (%s, %s) ON CONFLICT (username) DO NOTHING",
            (test_username, hashed_password)
        )
        conn.commit()

        # 3. Immediately fetch back to see what the DB stored
        cur.execute("SELECT username, password FROM users WHERE username = %s", (test_username,))
        row = cur.fetchone()

        if row:
            db_user, db_pass = row
            print("\n--- RESULTS ---")
            print(f"Username in DB: {db_user}")
            print(f"Password in DB: {db_pass}")
            
            if db_pass.startswith('pbkdf2:sha256'):
                print("\n✅ SUCCESS: The password IS hashed in the database.")
            else:
                print("\n❌ FAILURE: The password is plain text!")
        else:
            print("\n❌ ERROR: User was not found. Insertion failed.")

    except Exception as e:
        print(f"\n❌ CONNECTION ERROR: {e}")
    finally:
        if conn:
            cur.close()
            conn.close()
            print("\n--- Audit Complete ---")

if __name__ == "__main__":
    verify_database_sync()
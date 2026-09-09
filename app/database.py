import sqlite3

DATABASE = "smartlead.db"


def get_connection():
    connection = sqlite3.connect(DATABASE)
    connection.row_factory = sqlite3.Row
    return connection


def init_db():
    connection = None

    try:
        connection = get_connection()

        connection.execute("""
            CREATE TABLE IF NOT EXISTS leads (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                phone TEXT,
                email TEXT,
                message TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

        connection.commit()

    except sqlite3.Error as error:
        print("Veritabani baslatma hatasi:", error)
        raise RuntimeError("Veritabani baslatilamadi.") from error

    finally:
        if connection:
            connection.close()


def add_lead(name, phone=None, email=None, message=None):
    connection = None

    try:
        connection = get_connection()

        connection.execute(
            """
            INSERT INTO leads (name, phone, email, message)
            VALUES (?, ?, ?, ?)
            """,
            (name, phone, email, message)
        )

        connection.commit()

    except sqlite3.Error as error:
        print("Veritabani kayit hatasi:", error)
        raise RuntimeError("Musteri kaydi olusturulamadi.") from error

    finally:
        if connection:
            connection.close()

def get_all_leads():
    connection = None

    try:
        connection = get_connection()

        rows = connection.execute(
            """
            SELECT id, name, phone, email, message, created_at
            FROM leads
            ORDER BY id DESC
            """
        ).fetchall()

        return [dict(row) for row in rows]

    except sqlite3.Error as error:
        print("Veritabani okuma hatasi:", error)
        raise RuntimeError("Musteri kayitlari okunamadi.") from error

    finally:
        if connection:
            connection.close()
    
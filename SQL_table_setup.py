import sqlite3

db = sqlite3.connect("coffee.sqlite")
cur = db.cursor()
cur.execute(
    """
    CREATE TABLE coffee (
        id INT NOT NULL UNIQUE,
        name TEXT,
        roastDegree TEXT,
        isMilled TEXT,
        description TEXT,
        cost INT,
        volume INT
    );
    """
)

cur.execute(
        f"""
        INSERT INTO coffee(id, name, roastDegree, isMilled, description, cost, volume) VALUES(
            0,
            "Эспрессо",
            "Среднепрожаренный",
            "В зёрнах",
            "Вкусьненько",
            50000,
            10
        );
        """
    )

db.commit()

db.close()

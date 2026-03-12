import sqlite3
DATABASE = "recipies.db"
def get_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def create_table():
    conn = get_connection()

    conn.execute("""
    CREATE TABLE IF NOT EXISTS recipies (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    category TEXT
    ingredients TEXT,
    instructions TEXT
    ) 
    
    """)

    conn.commit()
    conn.close()


def create_recipe(recipe):
    conn = get_connection()

    ingredients = ",".join(recipe.ingredients)

    cursor = conn.execute(
        "INSERT INTO recipies (name, category, ingredients, instructions)",
        (recipe.name, recipe.category, ingredients, recipe.instructions)
    )
    conn.commit()
    recipe_id = cursor.lastrowid
    conn.close()

    return recipe_id


def get_recipies():
    conn = get_connection()

    rows = conn.execute("SELECT * FROM recipies").fetchall()

    conn.close()

    recipies = []

    for r in rows:
        recipies.append({
            "id": r["id"],
            "name": r["name"],
            "category": r["category"],
            "ingredients": r["ingredients"].split(","),
            "instructions": r["instructions"],

        })

    return recipies


def update_recipe(recipe_id, recipe):
    conn = get_connection()

    ingredients = None
    if recipe.ingredients:
        ingredients = ",".join(recipe.ingredients)

    conn.execute(
        "UPDATE recipies SET name=?, category=?, ingredients=?, instructions=? WHERE id=?",
        (recipe.name, recipe.category, ingredients, recipe.instructions, recipe_id)
    )

    conn.commit()
    conn.close()

def delete_recipe(recipe_id):
    conn = get_connection()

    conn.execute("DELETE FROM recipies WHERE id=?", (recipe_id,))

    conn.commit()
    conn.close()

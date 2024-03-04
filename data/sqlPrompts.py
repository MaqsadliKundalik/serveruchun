from sqlite3 import Connection
import config
import utils
from datetime import datetime, timedelta

conn = Connection("data.db")
c = conn.cursor()

# users

def add_user(id, name, lan): 
    c.execute("INSERT INTO users (id, name, lan, balans) VALUES (?, ?, ?, 0)", (id, name, lan))
    conn.commit()

def get_user(id):
    return c.execute("SELECT name, lan, status, balans FROM users WHERE id=?", (id, )).fetchone()

def get_suers():
    return c.execute("SELECT id, name, lan, balans, status FROM users").fetchall()

def get_debtors():
    return c.execute("SELECT id, name, lan ,balans, status FROM users WHERE balans < 0").fetchall()

def get_suers_id():
    data = c.execute("SELECT id FROM users WHERE status=?", ("member", )).fetchall()
    return utils.open_tuple_in_list(data)

def change_user_status(id, status):
    c.execute("UPDATE users SET status=? WHERE id=?", (status, id))
    conn.commit()
    
def change_user_balans(id, balans):
    c.execute("UPDATE users SET balans=? WHERE id=?", (balans, id))
    conn.commit()
    
def change_user_lan(id, lan):
    c.execute("UPDATE users SET lan=? WHERE id=?", (lan, id))
    conn.commit()

def change_user_name(id, name):
    c.execute("UPDATE users SET name=? WHERE id=?", (name, id))
    conn.commit()

def del_user(id):
    c.execute("DELETE FROM users WHERE id=?", (id, ))
    conn.commit()

def update_balans(user_id, balans):
    c.execute("UPDATE users SET balans=? WHERE id=?", (balans, user_id))
    conn.commit()

# admins

def get_admins():
    return c.execute("SELECT id FROM admins").fetchall()

def get_admin(id): 
    return c.execute("SELECT id FROM admins WHERE id=?", (id, )).fetchone()

def add_admin(id):
    c.execute("INSERT INTO admins (id) VALUES (?)", (id, ))
    conn.commit()

def del_admin(id):
    c.execute("DELETE FROM admins WHERE id=?", (id, ))
    conn.commit()

# products

def add_product(name, soni, size, price, first_img, second_img, third_img, fourth_img, fiveth_img):
    c.execute("""INSERT INTO products (name, soni, size, price, first_image_id, second_image_id, third_image_id, fourth_image_id, fiveth_image_id) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""", (name, soni, size, price, first_img, second_img, third_img, fourth_img, fiveth_img))
    conn.commit()
    return get_products()[0][0]

def get_products():
    return c.execute("SELECT id, name, soni, size, price, first_image_id, second_image_id, third_image_id, fourth_image_id, fiveth_image_id FROM products").fetchall()[::-1]

def get_products_page(page):
    return c.execute("SELECT id, name, soni, size, price, first_image_id, second_image_id, third_image_id, fourth_image_id, fiveth_image_id FROM products WHERE rowid > 200 * (? - 1) LIMIT 200", (page, )).fetchall()[::-1]

def get_products_for_inline_mode(name, size):
    if name == size:
        return c.execute("SELECT id, name, soni, size, price, first_image_id, second_image_id, third_image_id, fourth_image_id, fiveth_image_id FROM products WHERE name LIKE ?", (f"%{name}%", )).fetchall()[::-1]
    else:
        return c.execute("SELECT id, name, soni, size, price, first_image_id, second_image_id, third_image_id, fourth_image_id, fiveth_image_id FROM products WHERE name LIKE ? AND size LIKE ?", (f"%{name}%", f"%{size}%")).fetchall()[::-1]

    

def get_productById(id):
    return c.execute("SELECT name, soni, size, price, first_image_id, second_image_id, third_image_id, fourth_image_id, fiveth_image_id FROM products WHERE id=?", (id, )).fetchone()

def get_product_by_name_and_size(name, size):
    return c.execute("SELECT id, soni, price, first_image_id, second_image_id, third_image_id, fourth_image_id, fiveth_image_id FROM products WHERE name=? AND size=?", (name, size)).fetchone()

def update_product(id, name=None, soni=None, price=None, first_img=None, second_img=None, third_img=None, fourth_img=None, fiveth_img=None, is_name=False, is_soni=False, is_price=False,  is_first_img=False, is_second_img=False, is_third_img=False, is_fourth_img=False, is_fiveth_img=False):
    if any((is_name, is_soni, is_price, is_first_img, is_second_img, is_third_img, is_fourth_img, is_fiveth_img)):
        command = "UPDATE products SET "
        values = []
        if is_name:
            command += "name=? "
            values.append(name)
        if is_soni:
            command += "soni=? "
            values.append(soni)
        if is_price:
            command += "price=? ";
            values.append(price)
        if is_first_img:
            command += "first_image_id=? "
            values.append(first_img)
        if is_second_img:
            command += "second_image_id=? "
            values.append(second_img)
        if is_third_img:
            command += "third_image_id=? "
            values.append(third_img)
        if is_fourth_img:
            command += "fourth_image_id=? "
            values.append(fourth_img)
        if is_fiveth_img:
            command += "fiveth_image_id=? ";
            values.append(fiveth_img)
        values.append(id)
        command += f"""WHERE id=? """
        c.execute(command, tuple(values))
        conn.commit()
    else:
        return False

def delete_product(id):
    try:
        c.execute("DELETE FROM products WHERE id=?", (id, ))
        conn.commit()
    except:
        return False
    return True

# orders

def add_order(user_id, product_id, soni):
    c.execute("INSERT INTO orders (user_id, product_id, soni, sana, status) VALUES (?, ?, ?, strftime('%s', 'now', 'localtime'), 'wait')", (user_id, product_id, soni))
    conn.commit()

def change_order_status(order_id, status):
    c.execute("UPDATE orders SET status=? WHERE order_id=?", (status, order_id))
    conn.commit()

def del_order(order_id):
    try:
        c.execute("DELETE FROM orders WHERE order_id=?", (order_id, ))
        conn.commit()
    except:
        return False
    return True

def get_orders_of_user(user_id):
    return c.execute("SELECT order_id, product_id, soni, sana FROM orders WHERE user_id=?", (user_id, )).fetchall()

def get_orders():
    return c.execute("SELECT user_id, order_id, product_id, soni, sana FROM orders").fetchall()[::-1]

def get_filtered_orders(user_id, status, date1="", date2=""):
    if status == "new":
        return c.execute("SELECT order_id, product_id, soni, datetime(sana, 'unixepoch'), status FROM orders WHERE datetime(sana, 'unixepoch')>=? AND datetime(sana, 'unixepoch')<=? AND user_id=? ORDER BY sana ASC", (date1, date2, user_id)).fetchone()
    else: return c.execute("SELECT order_id, product_id, soni, datetime(sana, 'unixepoch'), status FROM orders WHERE status=? AND user_id=?", (status, user_id)).fetchall()

def get_report(user_id, date1, date2):
    return c.execute("SELECT order_id, product_id, soni, datetime(sana, 'unixepoch'), status FROM orders WHERE datetime(sana, 'unixepoch')>=? AND datetime(sana, 'unixepoch')<=? AND user_id=? ORDER BY sana ASC", (date1, date2, user_id)).fetchall()

def get_all_report(date1, date2):
    return c.execute("SELECT order_id, product_id, soni, datetime(sana, 'unixepoch'), status, user_id FROM orders WHERE datetime(sana, 'unixepoch')>=? AND datetime(sana, 'unixepoch')<=? ORDER BY sana ASC", (date1, date2)).fetchall()

def get_filtered_all_orders(status):
    return c.execute("SELECT order_id, product_id, soni, datetime(sana, 'unixepoch'), status, user_id FROM orders WHERE status=?", (status, )).fetchall()

def get_order_by_ID(order_id):
    return c.execute("SELECT user_id, product_id, soni, sana, status FROM orders WHERE order_id=?", (order_id, )).fetchone()

def get_order_by_user_ID_and_product_ID(user_id, product_id):
    return c.execute("SELECT order_id, soni, datetime(sana, 'unixepoch') FROM orders WHERE user_id=? AND product_id=? AND status='wait' ", (user_id, product_id)).fetchall()

def get_wait_orders(user_id):
    return c.execute("SELECT order_id, product_id, soni, sana FROM orders WHERE status='wait'AND user_id=?", (user_id, )).fetchall()

def update_order(order_id, soni):
    c.execute("UPDATE orders SET soni=? WHERE order_id=?", (soni, order_id))
    conn.commit()

# task time
def change_task_time(soat, minut):
    c.execute("UPDATE taskTime SET soat=?, minut=?", (soat, minut))
    conn.commit()

def get_task_time():
    return c.execute("SELECT soat, minut FROM taskTime").fetchone()

# users limit
def change_users_limit(limit):
    c.execute("UPDATE users_limit SET user_limit=?", (limit, ))
    conn.commit()

def get_users_limit():
    return c.execute("SELECT user_limit FROM users_limit").fetchone()



# default actions
 
def default_actions():
    c.execute("CREATE TABLE IF NOT EXISTS admins (id)")
    c.execute("CREATE TABLE IF NOT EXISTS taskTime (soat, minut)")
    c.execute("CREATE TABLE IF NOT EXISTS users (id, name, lan, status, balans)")
    
    c.execute("CREATE TABLE IF NOT EXISTS users_limit(user_limit)")
    c.execute("CREATE TABLE IF NOT EXISTS products (id INTEGER PRIMARY KEY AUTOINCREMENT, name, soni, size, price, first_image_id, second_image_id, third_image_id, fourth_image_id, fiveth_image_id)")
    c.execute("CREATE TABLE IF NOT EXISTS orders (user_id, order_id, product_id, soni, sana, status)")
    if not get_task_time():
        c.execute("INSERT INTO taskTime (soat, minut) VALUES (?, ?)", (7, 0)) 
        conn.commit()
    if not c.execute("SELECT id FROM admins WHERE id=?", (config.ADMIN_ID, )).fetchone():
        add_admin(config.ADMIN_ID)
    if not c.execute("SELECT user_limit FROM users_limit").fetchall():
        c.execute("INSERT INTO users_limit (user_limit) VALUES (?)", (-5000, ))
        conn.commit()



default_actions()



def close_database():
    conn.close()

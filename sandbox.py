# # Function to get cookies from Chrome

# import sqlite3
# import os
# import win32crypt


# def get_chrome_cookies():
#     data_path = (
#         os.path.expanduser("~")
#         + r"\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Cookies"
#     )
#     c = sqlite3.connect(data_path)
#     cursor = c.cursor()
#     select_statement = "SELECT host_key, name, encrypted_value FROM cookies"
#     cursor.execute(select_statement)

#     for host_key, name, encrypted_value in cursor.fetchall():
#         if decrypted_value := win32crypt.CryptUnprotectData(
#             encrypted_value, None, None, None, 0
#         )[1]:
#             print(host_key, name, decrypted_value)


# if __name__ == "__main__":
#     get_chrome_cookies()


def peephole_func():
    a = "Hello World" * 5
    b = [1, 2] * 7
    c = (10, 20, 30) * 3
    print(a, b, c)


print(peephole_func.__code__.co_consts)
print(peephole_func.__code__.co_varnames)
print(peephole_func.__code__.co_names)

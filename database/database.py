#!/usr/bin/env python3

import sqlite3

def create_database(database_name):
    try:
        conn = sqlite3.connect(database_name + '.db')
        conn.close()
        print(f"Database '{database_name}' created successfully.")
    except sqlite3.Error as e:
        print(f"Error creating database: {e}")


def create_table(database_name, table_name, columns):
    try:
        conn = sqlite3.connect(database_name + '.db')
        cursor = conn.cursor()

        column_definitions = ', '.join([f'{col_name} {col_type}' for col_name, col_type in columns.items()])
        create_table_query = f'CREATE TABLE IF NOT EXISTS {table_name} ({column_definitions})'
        cursor.execute(create_table_query)

        conn.commit()
        conn.close()
        print(f"Table '{table_name}' created successfully.")
    except sqlite3.Error as e:
        print(f"Error creating table: {e}")


def insert_data(database_name, table_name, data):
    try:
        conn = sqlite3.connect(database_name + '.db')
        cursor = conn.cursor()

        placeholders = ', '.join(['?' for _ in range(len(data))])
        insert_query = f'INSERT INTO {table_name} VALUES ({placeholders})'
        cursor.execute(insert_query, data)

        conn.commit()
        conn.close()
        print("Data inserted successfully.")
    except sqlite3.Error as e:
        print(f"Error inserting data: {e}")


def update_data(database_name, table_name, column_to_update, new_value, condition_column, condition_value):
    try:
        conn = sqlite3.connect(database_name + '.db')
        cursor = conn.cursor()

        update_query = f'UPDATE {table_name} SET {column_to_update} = ? WHERE {condition_column} = ?'
        cursor.execute(update_query, (new_value, condition_value))
        
        conn.commit()
        conn.close()
        print("Data updated successfully.")
    except sqlite3.Error as e:
        print(f"Error updating data: {e}")

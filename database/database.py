#!/usr/bin/env python3
'''Collection of functions to perform databse actions'''

import sqlite3
import os

def create_database(database_name):
    '''Method to create new database if doesnt exist'''
    if not os.path.exists(database_name + '.db'):
        try:
            conn = sqlite3.connect(database_name + '.db')
            conn.close()
            print(f"Database '{database_name}' created successfully.")
        except sqlite3.Error as e:
            print(f"Error creating database: {e}")
    else:
        print("Database already exists.")


def create_table(database_name, table_name, columns):
    '''Method to create new table in the exisiting database'''
    try:
        conn = sqlite3.connect(database_name + '.db')
        cursor = conn.cursor()

        column_definitions = ', '.join([f'{col_name} {col_type}' \
                                        for col_name, col_type in columns.items()])
        create_table_query = f'CREATE TABLE IF NOT EXISTS {table_name} ({column_definitions})'
        cursor.execute(create_table_query)

        conn.commit()
        conn.close()
        print(f"Table '{table_name}' created successfully.")
    except sqlite3.Error as e:
        print(f"Error creating table: {e}")


def insert_data(database_name, table_name, data):
    '''Method to insert data into an exisiting table'''
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
    '''Method to update the data from a table'''
    try:
        conn = sqlite3.connect(database_name + '.db')
        cursor = conn.cursor()

        update_query = f'UPDATE {table_name} SET {column_to_update} = \
        ? WHERE {condition_column} = ?'
        cursor.execute(update_query, (new_value, condition_value))

        conn.commit()
        conn.close()
        print("Data updated successfully.")
    except sqlite3.Error as e:
        print(f"Error updating data: {e}")


def delete_data(database_name, table_name, condition):
    '''Method to delete a data from the table'''
    try:
        conn = sqlite3.connect(database_name + '.db')
        cursor = conn.cursor()

        delete_query = f'DELETE FROM {table_name} WHERE {condition}'
        cursor.execute(delete_query)

        conn.commit()
        conn.close()
        print("Data deleted successfully.")
    except sqlite3.Error as e:
        print(f"Error deleting data: {e}")


def insert_data_if_not_exists(database_name, table_name, column_name, value_to_check, new_values):
    '''Method to insert data if the value already doesnt exist in the table'''
    try:
        conn = sqlite3.connect(database_name + '.db')
        cursor = conn.cursor()

        # Check if the value exists in the specified column
        select_query = f'SELECT * FROM {table_name} WHERE {column_name} = ?'
        cursor.execute(select_query, (value_to_check,))
        existing_row = cursor.fetchone()

        if existing_row is None:
            # Prepare INSERT query
            columns = ', '.join(new_values.keys())
            placeholders = ', '.join(['?' for _ in new_values])
            insert_query = f'INSERT INTO {table_name} ({columns}) VALUES ({placeholders})'

            # Extract values from the provided dictionary
            values = tuple(new_values.values())

            # Insert a new row with the provided values
            cursor.execute(insert_query, values)
            conn.commit()
            print("New row added successfully.")
        else:
            print("Value already exists in the specified column.")

        conn.close()
    except sqlite3.Error as e:
        print(f"Error adding new row: {e}")

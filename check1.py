import streamlit as st
import psycopg2
from psycopg2 import extras


st.write("""
# My first app
jai shree ram
""")


def connect_to_database():
    return psycopg2.connect(
        dbname="hsptl_managment",
        user="postgres",
        password="postgres",
        host="localhost",
        port="5432"
    )

def execute_query(query):
    connection = connect_to_database()
    cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cursor.execute(query)
    result = cursor.fetchall()
    connection.close()
    return result

def main():
    st.title("PostgreSQL Query Visualizer")

    # Input SQL query
    query = st.text_area("Enter SQL Query")

    if st.button("Execute Query"):
        # Execute the query and display results
        result = execute_query(query)
        if result:
            st.write("Query Results:")
            st.write(result)
        else:
            st.write("No results to display.")

if __name__ == "__main__":
    main()

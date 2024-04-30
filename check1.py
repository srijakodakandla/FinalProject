import streamlit as st
import psycopg2

def connect_to_database():
    return psycopg2.connect(
        dbname="hsptl_managment",
        user="postgres",
        password="postgres",
        host="localhost",
        port="5432"
    )

def get_table_names():
    connection = connect_to_database()
    cursor = connection.cursor()
    cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public' ORDER BY table_name")
    tables = cursor.fetchall()
    connection.close()
    return [table[0] for table in tables]

def get_column_names(table_name):
    connection = connect_to_database()
    cursor = connection.cursor()
    cursor.execute(f"SELECT column_name FROM information_schema.columns WHERE table_name = '{table_name}'")
    columns = cursor.fetchall()
    connection.close()
    return [column[0] for column in columns]

def execute_query(query):
    connection = connect_to_database()
    cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cursor.execute(query)
    result = cursor.fetchall()
    connection.close()
    return result



def main():
    st.title("PostgreSQL Table Viewer")
    
    # Connect to the database and fetch table names
    tables = get_table_names()
    
    # Dropdown box to select a table
    selected_table = st.selectbox("Select a table", tables)
    
    # Display column names of the selected table
    if selected_table:
        st.write("### Column Names:")
        columns = get_column_names(selected_table)
        for column in columns:
            st.write(f"- {column}")

    # Input SQL query
    st.title("Query Visualizer")
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


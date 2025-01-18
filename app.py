from flask import Flask, render_template_string
import pyodbc

app = Flask(__name__)

# SQL Server connection details
server = '139.5.190.161,1401'  # Change this to your SQL Server hostname or IP address
database = 'Adviser'  # Replace with your database name
username = 'FT_App'  # Replace with your SQL Server username
password = 'utr94MarqGXg2w8f'  # Replace with your SQL Server password
driver = '{ODBC Driver 17 for SQL Server}'  # ODBC driver for SQL Server

# Connection string for SQL Server
conn_str = f'DRIVER={driver};SERVER={server};PORT=1433;DATABASE={database};UID={username};PWD={password}'

# Route to fetch and display data
@app.route('/')
def home():
    # Connect to the database
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()
    
    # Query to fetch data from a table (replace 'your_table_name' with actual table name)
    cursor.execute("SELECT TOP (10) [id],[msg],[msgdate] FROM [Adviser].[dbo].[Test]")
    
    # Fetch all rows
    rows = cursor.fetchall()
    
    # Close the connection
    conn.close()
    
    # Display the rows in HTML
    # You can customize this HTML template as needed
    html = """
    <html>
        <head>
            <title>SQL Server Data</title>
        </head>
        <body>
            <h1>Data from your_table_name</h1>
            <table border="1">
                <tr>
                    <th>Column 1</th>
                    <th>Column 2</th>
                    <th>Column 3</th>  <!-- Add more columns if needed -->
                </tr>
    """
    
    # Add rows to the HTML table
    for row in rows:
        html += f"""
        <tr>
            <td>{row[0]}</td>
            <td>{row[1]}</td>
            <td>{row[2]}</td>  <!-- Add more columns if needed -->
        </tr>
        """
    
    html += """
            </table>
        </body>
    </html>
    """
    
    return render_template_string(html)

if __name__ == "__main__":
    app.run(debug=True)

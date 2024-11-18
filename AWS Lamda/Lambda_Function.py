import json
import psycopg2
import os

def lambda_handler(event, context):
    # Obtaining the connection details from environment variables
    host = os.environ['host']
    user = os.environ['user']
    password = os.environ['password']
    port = os.environ['port']
    role = os.environ['role']
    bucket = os.environ['bucket']
    
    # Connect to the Redshift database
    con = psycopg2.connect(dbname='dev', host=host, port=port, user=user, password=password)
    
    # Copy Command to load data from S3 to Redshift
    copy_command = f"""
    COPY orders (
        orderid,
        customerid,
        orderamount,
        orderdate
    )
    FROM 's3://{bucket}/SamplePractical.csv'
    IAM_ROLE '{role}'
    DELIMITER ','
    IGNOREHEADER 1
    DATEFORMAT 'auto';
    """
    
    # Opening a cursor and executing the copy command
    cur = con.cursor()
    cur.execute("TRUNCATE TABLE orders;")  # Optional: Clear the table before loading
    cur.execute(copy_command)
    con.commit()
    
    # Close the cursor and the connection
    cur.close()
    con.close()
    
    print("Finished executing copy command")
    
    return {
        'statusCode': 200,
        'body': json.dumps('Data loaded successfully from S3 to Redshift!')
    }

# Psycopg2 Installation

Prerequisites: First, create an EC2 instance using the Amazon Linux 2 AMI. Then, open CloudShell and connect to the EC2 instance. Once connected, follow the provided commands.

# Install Python 3.8 (via Amazon Linux Extras)
```bash
sudo amazon-linux-extras install python3.8  # If prompted press "Y" key and hit enter.
``` 

# Install pip for Python 3.8
```bash
curl -O https://bootstrap.pypa.io/get-pip.py
``` 

```bash
python3.8 get-pip.py --user
``` 

# Create a directory named 'python'
```bash
mkdir python
``` 

# Install psycopg2-binary libraries into the python directory
```bash
sudo python3.8 -m pip install psycopg2-binary -t python/
``` 
# Zip the python directory into a layer.zip file
```bash
zip -r layer.zip python
``` 
# Publish the Lambda layer with the specified region
```bash
aws lambda publish-layer-version --layer-name LambdaTest --zip-file fileb://layer.zip --compatible-runtimes python3.8 --region ap-south-1
``` 
This completes the Pysopg2 setup.

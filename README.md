# Pagbantay Backend Setup

The Pagbantay backend is a serverless 
[FastAPI](https://fastapi.tiangolo.com/)
application that uses 
[SQLAlchemy](https://docs.sqlalchemy.org/en/20/intro.html#documentation-overview) 
with
[CockroachDB](https://www.cockroachlabs.com/docs/cockroachcloud/quickstart)
, following the Clean Architecture pattern.

It supports 
[Alembic migrations](https://alembic.sqlalchemy.org/en/latest/tutorial.html#)
and is ready for deployment to AWS Lambda using Mangum.

## Clean Architecure

This project follows the Clean Architecture pattern, which separates the code into different layers of different logic. This setup is common in real-world projects because it keeps the code organized, easier to test, and flexible for changes. 

Read more about [Clean Architecure](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html)

![Clean Architecture Cone](https://cdn-media-1.freecodecamp.org/images/YsN6twE3-4Q4OYpgxoModmx29I8zthQ3f0OR)


## Creating and Activating a Virtual Environment

**For Python:**

1. Create venv
    ```shell
    python -m venv venv
    ```

2. Then activate:
    ```shell
    source venv/bin/activate   # Mac/Linux
    venv\Scripts\activate      # Windows
    ```

    A "(venv)" prefix indicates that you are in a virtual environment:
    ```shell
    (venv) C:\YourDirectory...
    ```

    To exit the virtual environment (venv):
    ```shell
    deactivate
    ```

## Installation of Dependencies

Install python dependencies:
```shell
pip install -r requirements.txt
```

## Running and managing database migrations

1. Configure base schema at `/models/base.py`

2. Generate a [Migration Script](https://alembic.sqlalchemy.org/en/latest/tutorial.html#create-a-migration-script):
    ```shell
    alembic revision --autogenerate -m "your message"
    ```
    - Migration files will appear under `alembic/versions/`
    - Filename may look like `somecode_your_message.py`

3. Apply the migration (Push to Database):
    ```shell
    alembic upgrade head
    ```

## Accessing AWS resources

1. Go to the [AWS Sign-In Page](https://signin.aws.amazon.com/)

2. Log in using the IAM user credentials provided by the AWS account owner/admin

3. After logging in, you can now view and access AWS services through the console.

## Setting up AWS CLI and Configuring with an IAM user

1. Install AWS CLI v2 if you have not yet:

    - Follow the [Official AWS CLI Installation Guide](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)

2. Verify installation:
    ```shell
    aws --version
    ```

3. Configure AWS CLI:
    ```shell
    aws configure
    ```

4. Enter credentials as prompted (follow format below): 
    ```shell
    AWS Access Key ID [None]: <your-access-key-id>
    AWS Secret Access Key [None]: <your-secret-access-key>
    Default region name [None]: ap-southeast-1
    Default output format [None]: json
    ```
(Note: Your Access Keys are found along with the login credentials that you were given)

You have now successfuly configured AWS CLI with IAM

## Set-up via Serverless Framework

1. Ensure `Node 14` or later is installed

2. Install Serverless Framework:
    ```shell
    npm install -g serverless@3.39.0
    ```

3. Verify installation:
    ```shell
    serverless --version
    ```

4. Install serverless plugins:
    ```shell
    npm install
    ```

5. Install Python Requirements Plugin:
    ```shell
    sls plugin install -n serverless-python-requirements
    ```

## Deploy via Serverless Framewrok

1. Set-up Docker
    - Follow the [Docker Installation Guide](https://docs.docker.com/engine/install)
    - Ensure that Docker is running

2. Deploy the backend:
    ```shell
    serverless deploy
    # or shorthand
    sls deploy
    ```

3. Check if deployment is successful:

    - After deployment, you should be given a URL
    - Visit URL in browser and append `/docs` at the end
    - It should render correctly (see screenshot below):

![Screenshot](https://github.com/user-attachments/assets/6848f94a-cb09-49d9-a053-4f14cd5c4ea7)


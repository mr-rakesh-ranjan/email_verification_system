from db_config import get_data
import json as js

try:
    accountNumber = 10000
    query = f"SELECT * FROM [dbo].[customer] WHERE account_number = {int(accountNumber)} "
    data = js.loads(get_data(query))
    # print(data[0])

    from controller import generate_otp
    otp = generate_otp()
    print(f"your otp : {otp} and user email is {data[0]["customer_email"]}")

except Exception as e:
    print(e)
from zeep import Client

client = Client('http://localhost:8000/?wsdl')
response = client.service.say_hello('John')
print(response)

# PyZohoBooksAPI

## Usage:
- Authentication:
    ```python
  from PyZohoBooksAPI import ZohoAuth

  auth = ZohoAuth(
         client_id='your_client_id',
         client_secret='your_client_secret'
  )
    
  # generating token
  status, token = auth.generate_token(code='your_code')
  print(status)
  # >>> 200
  print(token)
  # >>> {'access_token': '1000.60062cb11995ad4c5395a31ae680fa09.d3438f753f4e64021aad100323e9cbb1', 'api_domain': 'https://www.zohoapis.com', 'token_type': 'Bearer', 'expires_in': 3600}
  
  # refreshing token
  status, refreshed_token = auth.refresh_token(refresh_token='1000.455b2011ed031afa48df852cfcfe7f9b.0aeb72a01ad1841ccbf5df8e548f9445'))
  print(status)
  # >>> 200
  print(refreshed_token)
  # >>> {'access_token': '1000.ce1d8d22982db8d5c80ea8c8903ca458.b53a0d99b4b0325f4ff554a8a452a92b', 'api_domain': 'https://www.zohoapis.com', 'token_type': 'Bearer', 'expires_in': 3600}
    ```
  
- Contacts
  ```python
  from PyZohoBooksAPI import Contacts
  
  contacts = Contacts(token='your_token', organization_id='your_organization_id')
  
  # getting all contacts
  status, all_contacts = contacts.contacts_list()
  print(status)
  # >>> 200
  print(all_contacts)
  # >>> list_of_your_contacts
  
  # get contacts by id:
  status, contact = contacts.get_contact(contact_id='3168296000000075177')
  print(contact)
  # >>> your_contact
  
  # check contacts by email:
  status, contact = contacts.check_by_email(email='marawan6569@gmail.com')
  print(contact)
  # >>> your_contact
  
  # creating new contact
  status, contact = contacts.create_contact(contact_data={})
  print(contact)
  # >>> your_contact
  
  ```
- Invoices
  ```python
  from PyZohoBooksAPI import Invoices
  
  invoices = Invoices(token='your_token', organization_id='your_organization_id')
  
  invoice = invoices.create_invoice(invoice_data={})
  invoice = invoices.email_an_invoice(invoice_id='your_invoice_id', email_data={})
  ```
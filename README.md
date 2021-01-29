# PyhonQA_Homework2_APITests

### Homework for lessons: "API testing. Rest, restful, SOAP, request types"

##To run tests use:

#### 1. Service: https://dog.ceo/dog-api

```pytest -vs -m dogs --url=https://dog.ceo```

or 

```pytest -vs dogs_api_test.py --url=https://dog.ceo```

#### 2. Service: https://www.openbrewerydb.org

```pytest -vs -m breweries --url=https://api.openbrewerydb.org```

or 

```pytest -vs breweries_api_test.py --url=https://api.openbrewerydb.org```

#### 3. Service: https://jsonplaceholder.typicode.com

```pytest -vs -m placeholder --url=https://jsonplaceholder.typicode.com```

or 

```pytest -vs placeholder_api_test.py --url=https://jsonplaceholder.typicode.com```

### 4. To test base_module you can run

```pytest base_module_test.py --url=https://mail.ru --status_code=200```

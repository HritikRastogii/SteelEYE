# SteelEye Trade task

Repository [GitHub](https://github.com/dinowais/SteelEye).

### **Tech Used:**

- Pydantic
- FastApi
- SQLAlchemy ORM
- MySqlLite

### Approach:

## **Single trade:-**

- **Get :/trade/{trade\_id}/**

**Response:-**

Returns singe trade with tradeDetails

**On Error:-**

Message with 404 Http Status code

- **Post :/trade/{trade\_id}/**

**Response:-**

Returns singe trade with tradeDetails

- **Delete :/trade/{trade\_id}/**

**Response:-**

If Deleted { **status code** : 200, **message** : &quot;Trade deleted&quot;}

Else if not found { **status code** 404, **message:**&quot;Trade Object Not Found&quot;}

##


##


## **Searching trades:-**

- **Get :/trades/search/**

**Params : &quot;search&quot;,&quot;offset&quot;,&quot;limit&quot;**

**Response:-**

Returns all the trades where the search condition gets satisfied **&quot;Exact Match&quot;** on at least a field in this list [&quot;counterparty&quot;,&quot;instrumentId&quot;,&quot;instrumentName&quot;,&quot;trader&quot;], besides also supports pagination.

If **no search** is provided it will list all trades with default limit of 10

## **Advanced filtering**

- **Get :/trades/filter/**

**Params : &quot;asset\_class&quot;,&quot;start&quot;,&quot;end&quot;,&quot;maxPrice&quot;,.&quot;minPrice&quot;,&quot;tradeType&quot;,&quot;offset&quot; and &quot;limit&quot;**

**Response:-**

- Returns the results based on the parameters passed to the request as **all of these are optional**.
- Asset\_class, tradeType are calculated on exact matching.
- If **start and end** are both passed in params then the result will be in **range between the two**. The same is the case with **maxPrice and minPrice**.
- If only **start or end** is provided then that will be calculated on that individual parameter and the same will be the case with **maxPrice or minPrice**.
- **Note: -** There is an &quot; **and query&quot;** between the parameters, that means the result will depend on their combination and will be executed as a single query. If **no params** are provided it will list all trades with default limit of 10
- This also supports pagination.

###


###


###


###


### **File Structure:**

└── SteelEye

├── \_\_init\_\_.py

├── crud.py

├── database.py

├── main.py

├── models.py

├── schemas.py

├── requirements.txt

├── README.MD

├── sql\_app.db

└── .gitignore

### Start app:

uvicorn main:app or uvicorn main:app --reload
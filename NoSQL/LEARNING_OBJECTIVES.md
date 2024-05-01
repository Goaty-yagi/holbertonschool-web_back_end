# Learning Objectives

- [What NoSQL means](#What-NoSQL-means)
- [What is difference between SQL and NoSQL](#What-is-difference-between-SQL-and-NoSQL)
- [What is ACID](#What-is-ACID)
- [What is a document storage](#What-is-a-document-storage)
- [What are NoSQL types](#What-are-NoSQL-types)
- [What are benefits of a NoSQL database](#What-are-benefits-of-a-NoSQL-database)
- [How to query information from a NoSQL database](#How-to-query-information-from-a-NoSQL-database)
- [How to insert/update/delete information from a NoSQL database](#How-to-insert/update/delete-information-from-a-NoSQL-database)
- [How to use MongoDB](#How-to-use-MongoDB)

## What NoSQL means
NoSQL is an approach to databases that represents a shift away from traditional relational database management systems (RDBMS).
## What is difference between SQL and NoSQL
The main difference between SQL (relational databases) and NoSQL (non-relational databases) lies in their data model, querying language, scalability, and use cases:

### Data Model:
- SQL databases follow a rigid, structured schema with tables, rows, and columns. Data must conform to this schema.
- NoSQL databases offer flexible data models, including document-based (like MongoDB), key-value pairs (like Redis), column-oriented (like Cassandra), and graph-based (like Neo4j).
### Querying Language:
- SQL databases use Structured Query Language (SQL) for defining and manipulating data.
- NoSQL databases use various query languages, depending on the database type. For example, MongoDB uses a JavaScript-based query language.
### Scalability:
- SQL databases are typically vertically scalable, meaning you can increase performance by upgrading hardware (CPU, RAM, etc.) of a single server.
- NoSQL databases are designed for horizontal scalability, allowing you to distribute data across multiple servers or nodes.
### Use Cases:
- SQL databases are often used for applications requiring ACID transactions (Atomicity, Consistency, Isolation, Durability), complex queries, and strong consistency.
- NoSQL databases are suitable for applications with large volumes of unstructured or semi-structured data, real-time data processing, and distributed architectures.

In summary, SQL databases offer strong consistency, ACID compliance, and support for complex queries, while NoSQL databases prioritize scalability, flexibility, and high availability. The choice between them depends on the specific requirements and constraints of your application.
## What is ACID
ACID is an acronym that stands for Atomicity, Consistency, Isolation, and Durability. It represents a set of properties that guarantee the reliability and integrity of transactions in a database system:

- Atomicity: This property ensures that a transaction is treated as a single, indivisible unit of work. Either all of the operations within the transaction are completed successfully, or none of them are. If any part of the transaction fails, the entire transaction is rolled back, leaving the database in its original state.
- Consistency: Consistency ensures that the database remains in a valid state before and after the transaction. In other words, the execution of a transaction must preserve all the integrity constraints, data types, and rules defined in the database schema.
Isolation: Isolation ensures that the concurrent execution of transactions does not result in interference or corruption of data. Each transaction should be isolated from other concurrent transactions until it is completed. This prevents phenomena such as dirty reads, non-repeatable reads, and phantom reads.
- Durability: Durability guarantees that once a transaction is committed, its changes are permanent and cannot be lost, even in the event of a system failure or crash. The changes made by the transaction are stored in non-volatile storage (such as disk or SSD) and remain intact even if the system is restarted.

ACID properties are essential for maintaining data integrity, reliability, and consistency in database systems, particularly in transactional environments where multiple users or processes access and modify the data concurrently.

## What is a document storage
Document storage, also known as document-oriented database storage, is a type of NoSQL database model that stores, retrieves, and manages data in the form of documents. In this model, each document is a semi-structured data unit, typically stored in formats like JSON (JavaScript Object Notation), BSON (Binary JSON), or XML (eXtensible Markup Language).

Document storage allows for flexible and schema-less data structures within documents, making it suitable for handling varied and evolving data types. Documents can contain nested data structures and arrays, providing rich and hierarchical representations of data.

Popular document-oriented databases include MongoDB, Couchbase, and CouchDB. These databases are commonly used for web applications, content management systems, real-time analytics, and other use cases that require flexible and scalable data storage.

## What are NoSQL types
NoSQL databases encompass various types, each optimized for specific use cases and data storage requirements. Here are some common types of NoSQL databases:

- Document Databases: Store and manage data in the form of documents, typically using formats like JSON or BSON. Each document contains key-value pairs or key-array pairs, allowing for flexible and schema-less data structures.
- Key-Value Stores: Store data as simple key-value pairs, where each key is unique and maps to a corresponding value. These databases are efficient for high-speed read and write operations, making them suitable for caching and session management.
- Column-Family Stores (Wide-Column Stores): Organize data into columns and column families, similar to tables in relational databases. However, they offer more flexibility in terms of schema design, with each row having a unique key and columns grouped into families. Examples include Apache Cassandra and HBase.
- Graph Databases: Model and represent data as graphs composed of nodes, edges, and properties. They are optimized for managing and querying highly interconnected data, such as social networks, recommendation systems, and network topologies. Examples include Neo4j and Amazon Neptune.
- Time-Series Databases: Optimize data storage and retrieval for time-series data, such as metrics, sensor readings, and event data. They provide efficient storage mechanisms and specialized query capabilities for time-based data analysis. Examples include InfluxDB and Prometheus.
- Each type of NoSQL database offers different strengths and trade-offs in terms of scalability, flexibility, and performance, allowing organizations to choose the most suitable option based on their specific requirements and use cases.
## What are benefits of a NoSQL database
- Scalability: NoSQL databases are designed to scale horizontally, allowing them to handle large volumes of data and high throughput. They can distribute data across multiple nodes in a cluster, providing seamless scalability as data grows.
- Flexibility: NoSQL databases are schema-less or have a flexible schema, allowing developers to store and manage different types of data without predefined schemas. This flexibility is beneficial for handling unstructured or semi-structured data.
- High Performance: NoSQL databases are optimized for specific use cases and can provide high performance for read and write operations. They often use techniques like in-memory caching, sharding, and asynchronous replication to achieve low latency and high throughput.
## How to query information from a NoSQL database
### Establish connection
```python
import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]
```

### Query info
```python
all_users = db.users.find()
adults = db.users.find({"age": {"$gte": 18}})
``` 

## How to insert/update/delete information from a NoSQL database

pymongo https://pymongo.readthedocs.io/en/stable/
### Insert data
```python
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')

# Access a specific database
db = client['mydatabase']

# Access a specific collection
collection = db['mycollection']

# Insert a single document
document = {'name': 'John', 'age': 30}
result = collection.insert_one(document)
print('Inserted document ID:', result.inserted_id)

# Insert multiple documents
documents = [{'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 35}]
result = collection.insert_many(documents)
print('Inserted document IDs:', result.inserted_ids)

```
### Update data
```python
# Update a single document
query = {'name': 'John'}
new_values = {'$set': {'age': 31}}
result = collection.update_one(query, new_values)
print('Modified document count:', result.modified_count)

# Update multiple documents
query = {'age': {'$lt': 30}}
new_values = {'$set': {'status': 'Young'}}
result = collection.update_many(query, new_values)
print('Modified document count:', result.modified_count)

```

### Delete data
```python
# Delete a single document
query = {'name': 'John'}
result = collection.delete_one(query)
print('Deleted document count:', result.deleted_count)

# Delete multiple documents
query = {'age': {'$gte': 30}}
result = collection.delete_many(query)
print('Deleted document count:', result.deleted_count)

```
## How to use MongoDB
Go to Official installation guide https://intranet.hbtn.io/rltoken/mchw-5H4h95lL3Au_ETh_Q





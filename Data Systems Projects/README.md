# Data System Technical Projects

## Relational Database System for Comfy Mug
### Project Goal
Designed and implemented a relational database for a specialized startup, managing the full development lifecycle from conceptual Entity-Relationship Diagram (ERD) modeling to physical deployment and analytical querying.
### Implementation Details
* **Conceptual Modeling:** Developed an ERD to define a three-table relational schema (Staff, Menu, and Orders) with enforced Primary and Foreign Key constraints to maintain 1:M relationships.
* **Physical Deployment:** Orchestrated the database using **SQLite** within a Python environment, utilizing DDL (Data Definition Language) to build optimized schemas with specific data types and constraints.
* **Data Engineering:** Populated the system with synthetic records to simulate real-world operations and executed DML (Data Manipulation Language) commands for record updates and state management.
* **Analytical Querying:** Authored complex SQL queries to extract business intelligence, utilizing multi-table **JOINs**, data aggregation (**GROUP BY**, **COUNT**), and conditional filtering to analyze operational performance.
### Architectural Analysis & Scalability
* **Schema Normalization:** Evaluated table structures to minimize redundancy and ensure data integrity across the relational model.
* **Database Evolution:** Analyzed the technical requirements for migrating from a local SQLite instance to enterprise-grade systems like **PostgreSQL** or **MySQL**.
* **Big Data Strategy:** Developed a roadmap for horizontal scaling, evaluating the implementation of **database sharding** and **replication** to handle high-concurrency workloads and large-scale data distribution.
### Tech Stack
* **Database:** SQLite 
* **Language:** SQL, Python (sqlite3) 
* **Concepts:** ERD Modeling, Relational Algebra, Data Normalization, Horizontal Scaling

## NoSQL Architecture & Distributed Caching Strategy
### Project Goal
Evaluated and implemented document-based and in-memory NoSQL systems to analyze their performance trade-offs against traditional relational models. The project focused on high-scale data retrieval, cloud-native clustering, and the implementation of caching layers to optimize query latency.
### Implementation Details
* **Document Store Implementation:** * Migrated relational schemas into **MongoDB’s** BSON-based document format, leveraging flexible, schema-less collections for rapid prototyping.
* Utilized **PyMongo** for complex data manipulation and multi-stage filtering on local and cloud instances.
* **Cloud Infrastructure:**
* Provisioned and managed a distributed NoSQL cluster via **MongoDB Atlas**, performing large-scale data analysis on the `mflix` dataset (50,000+ documents).
* **In-Memory Caching:** * Deployed a **Redis** layer to serve as a high-speed key-value cache.
* Developed a caching logic to store frequently accessed query results, demonstrating significant reductions in primary database load and response times.
### Technical Analysis
* **Relational vs. Non-Relational:** Analyzed the shift from strict normalization to the denormalized, hierarchical structures required for high-velocity document storage.
* **Distributed Systems:** Investigated the mechanics of **replica sets** and **sharding** within MongoDB Atlas to ensure high availability and horizontal scalability.
* **Caching Mechanics:** Evaluated the operational impact of in-memory caching on overall system throughput and data consistency.
### Tech Stack
* **Databases:** MongoDB (Local & Atlas), Redis
* **Language:** Python (PyMongo, Redis-py)
* **Infrastructure:** Distributed NoSQL Clusters, Document Data Modeling, In-Memory Caching

## Graph Network Analysis & Community Detection
### Project Goal
Explored the utility of Graph Databases and Network Science to model complex, interconnected data. The project focused on transitioning from traditional row-based storage to graph-based relationships, implementing advanced algorithms to identify hidden communities and calculate network influence.
### Implementation Details
* **Graph Modeling:**
* Designed a property graph model using **Neo4j** (Cypher) to represent entities as nodes and interactions as directed/undirected relationships.
* Migrated structured relational data into a graph format to enable multi-hop relationship querying.
* **Network Topology & Metrics:**
* Utilized the **NetworkX** library in Python to perform high-level structural analysis.
* Calculated centrality measures (Degree, Closeness, and Betweenness) to identify "influencers" and critical bottlenecks within the network.
* **Community Detection Algorithms:**
* Implemented the **Louvain Method** and the **Girvan-Newman Algorithm** to partition the network into distinct modular communities based on edge density and betweenness.
* Analyzed the modularity of clusters to determine the strength of community divisions.
### Technical Analysis
* **Traversal Efficiency:** Compared the performance of recursive SQL JOINs against native **Cypher** graph traversals for deep relationship discovery.
* **Algorithm Scalability:** Evaluated the computational trade-offs between the Louvain method (bottom-up heuristic) and Girvan-Newman (top-down divisive) when applied to large-scale datasets.
* **Practical Application:** Assessed how community detection can be used for fraud detection, recommendation engines, and biological protein-interaction mapping.
### Tech Stack
* **Graph Database:** Neo4j (Cypher)
* **Libraries:** NetworkX, Matplotlib, Pandas
* **Algorithms:** Louvain, Girvan-Newman, Centrality Measures (Betweenness/Closeness)

## Semantic Search & Vector Embeddings: High-Dimensional Data Retrieval
### Project Goal
Implemented a high-performance semantic search system using vector databases and embedding models. The project focused on transforming unstructured text into dense vector representations to enable similarity-based retrieval, moving beyond traditional keyword matching.
### Implementation Details
* **Vector Database Orchestration:**
* Deployed and managed **ChromaDB** as the primary vector store for persistent embedding storage and efficient querying.
* Integrated **HuggingFace** Transformers (`sentence-transformers`) to generate high-dimensional embeddings for textual data.
* **Semantic Query Engineering:**
* Developed a pipeline to convert natural language queries into vector space to perform **Nearest Neighbor** searches.
* Implemented metadata filtering and collection management within ChromaDB to refine search results and maintain data organization.
* **Textual Analytics & Visualization:**
* Processed the "News Category Dataset" to analyze semantic clustering across different journalistic domains.
* Leveraged **Cosine Similarity** metrics to quantify the relationship between query vectors and document embeddings.
### Technical Analysis
* **Keyword vs. Semantic Retrieval:** Evaluated the performance gap between traditional BM25/TF-IDF ranking and vector-based semantic search, specifically in handling synonymy and context.
* **Vector Indexing & Scalability:** Analyzed the importance of embedding dimensions and distance metrics (Cosine vs. Euclidean) in search accuracy and computational overhead.
* **AI Integration:** Explored the role of vector databases as the "long-term memory" for Large Language Models (LLMs) through Retrieval-Augmented Generation (RAG) frameworks.
### Tech Stack
* **Vector Database:** ChromaDB
* **Machine Learning:** HuggingFace Transformers, Sentence-Transformers
* **Language:** Python
* **Concepts:** Vector Embeddings, Semantic Search, Cosine Similarity, High-Dimensional Data Indexing

## Student Depression Analysis using PySpark
This project involves performing data science tasks—including data cleaning, exploratory data analysis (EDA), and machine learning—on a labeled dataset using the Apache Spark framework within a Google Colab environment.
### Project Overview
The objective of this project is to analyze a dataset related to student depression to identify key factors and build a predictive model. The workflow utilizes **Spark SQL** for data manipulation and **Spark ML** for implementing machine learning algorithms.
### Dataset
* **Source:** [Student Depression Dataset (Kaggle)](https://www.kaggle.com/datasets/adilshamim8/student-depression-dataset/data).
* **Format:** CSV.
* **Features:** Includes demographics (Age, Gender, City), academic metrics (CGPA, Academic Pressure, Study Satisfaction), and lifestyle factors (Sleep Duration, Dietary Habits, Financial Stress).
### Methodology
#### 1. Environment Setup
* Installed `pyspark` and `kagglehub` libraries.
* Instantiated a `SparkSession` named "Test Dataset" with Hive support enabled.
* Fetched the dataset directly from Kaggle using the API and loaded it into a Spark DataFrame with `inferSchema=True`.
#### 2. Data Cleaning
* **Missing Values:** Verified the dataset for null or NaN values in both numeric and text columns; no missing values were found in the primary features.
* **Duplicates:** Performed a global grouping check across all columns to ensure no duplicate records existed.
* **Outlier Detection:** Implemented a Z-score analysis for numeric columns (e.g., Age, Academic Pressure, CGPA). Records with a Z-score greater than 3 were identified for review (e.g., 19 outliers found in the 'Age' column).
#### 3. Exploratory Data Analysis (EDA)
The analysis focused on identifying correlations between lifestyle factors and depression:
* **Academic Impact:** Evaluated how "Academic Pressure" and "Study Satisfaction" relate to the target "Depression" label.
* **Demographics:** Explored depression rates across different cities and age groups.
#### 4. Machine Learning
* **Preprocessing:** Used Spark ML's `StringIndexer` and `OneHotEncoder` to transform categorical variables. Numeric features were assembled using `VectorAssembler`.
* **Model Implementation:** Built a classification model using Spark ML to predict the presence of depression based on the cleaned feature set.
### Technologies Used
* **Apache Spark:** Core engine for distributed data processing.
* **PySpark:** Python API for Spark.
* **Spark SQL:** Used for relational data processing and tabular computing.
* **Spark ML:** Library for scalable machine learning.
* **Google Colab:** Cloud-based development environment.
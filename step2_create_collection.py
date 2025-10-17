# Step 2: Creating Your First Collection
# A collection is like a drawer in a filing cabinet dedicated to a specific topic

import chromadb

# Initialize the ChromaDB client
# Think of this as "opening the filing cabinet"
# By default, this creates an in-memory database (data disappears when program ends)
client = chromadb.Client()

# Create a new collection or get it if it already exists
# This is like creating a drawer labeled "travel_policies"
# The get_or_create_collection() method is smart - it creates the collection if it doesn't exist,
# or just retrieves it if it already does (prevents errors from trying to create duplicates)
collection = client.get_or_create_collection(name="travel_policies")

# Let's verify our collection was created successfully
print("✅ Collection created successfully!")
print(f"Collection name: {collection.name}")
print(f"Collection count: {collection.count()} documents")
print("\nYour 'travel_policies' filing cabinet is ready to store documents!")


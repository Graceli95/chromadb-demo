# Step 3: CRUD Operations on Data Points
# CRUD = Create, Read, Update, Delete - the four basic operations for managing data

import chromadb

# Initialize ChromaDB client and get our collection
client = chromadb.Client()
collection = client.get_or_create_collection(name="travel_policies")

print("=== CREATE: Adding Documents ===")
print("Adding our first travel policy documents to the collection...")

# CREATE: Adding Documents
# Each document needs:
# - ids: Unique identifiers (like file names)
# - documents: The actual text content
# - metadatas: Extra information for filtering (like tags)

collection.add(
    ids=[
        "flight_policy_01",
        "hotel_policy_01", 
        "rental_car_policy_01",
        "flight_policy_02"
    ],
    documents=[
        "For domestic flights, employees must book economy class tickets. Business class is only permitted for international flights over 8 hours.",
        "Employees can book hotels up to a maximum of $250 per night in major cities. A list of preferred hotel partners is available.",
        "A mid-size sedan is the standard for car rentals. Upgrades require manager approval. Always select the company's insurance option.",
        "All flights, regardless of destination, must be booked through the official company travel portal, 'Concur'."
    ],
    metadatas=[
        {"policy_type": "flights"},
        {"policy_type": "hotels"},
        {"policy_type": "rental_cars"},
        {"policy_type": "flights", "requires_portal": "True"}
    ]
)

print("✅ Successfully added 4 travel policy documents!")
print("\nDocument IDs added:")
print("- flight_policy_01")
print("- hotel_policy_01") 
print("- rental_car_policy_01")
print("- flight_policy_02")

print("\n=== READ: Querying Documents ===")
print("Now let's search for documents using natural language...")

# READ: Querying Documents
# This is where the magic happens! We can ask questions in natural language
# ChromaDB converts our question into embeddings and finds similar documents

results = collection.query(
    query_texts=["What is the policy for international flights?"],
    n_results=2  # Ask for the top 2 most relevant results
)

print("Query: 'What is the policy for international flights?'")
print("Results:")
for i, doc in enumerate(results['documents'][0]):
    print(f"{i+1}. {doc}")
    print(f"   Distance: {results['distances'][0][i]:.4f} (lower = more similar)")
    print(f"   Metadata: {results['metadatas'][0][i]}")
    print()

print("Notice how ChromaDB understands the INTENT of our question!")
print("It found documents about flights even though we didn't use the exact word 'flight' in our query.")

print("\n=== UPDATE: Modifying Documents ===")
print("Now let's update some policies and add new ones...")

# UPDATE: Changing Documents
# We can use 'upsert' to either UPDATE existing documents or INSERT new ones
# 'upsert' = UPdate if exists, inSERT if new

collection.upsert(
    ids=["hotel_policy_01", "train_policy_01"],  # hotel_policy_01 exists, train_policy_01 is new
    documents=[
        "Employees can book hotels up to a maximum of $300 per night. See the portal for preferred partners.",  # Updated hotel budget
        "Train travel is encouraged for trips under 4 hours. Business class tickets are approved for all train journeys."  # New train policy
    ],
    metadatas=[
        {"policy_type": "hotels", "max_spend": 300},  # Updated metadata
        {"policy_type": "train", "last_updated": "2025-10-15"}  # New metadata
    ]
)

print("✅ Updated hotel budget from $250 to $300 per night")
print("✅ Added new train travel policy")

# Let's verify our updates by querying for hotel information
print("\nVerifying hotel policy update:")
hotel_results = collection.query(
    query_texts=["What is the hotel budget limit?"],
    n_results=1
)
print(f"Updated policy: {hotel_results['documents'][0][0]}")

print("\n=== DELETE: Removing Documents ===")
print("Now let's remove the train policy we just added...")

# DELETE: Removing Documents
collection.delete(ids=["train_policy_01"])

print("✅ Deleted train_policy_01")

# Let's verify the deletion by trying to query for train policies
print("\nVerifying deletion - searching for train policies:")
train_results = collection.query(
    query_texts=["What are the train travel policies?"],
    n_results=3
)

if train_results['documents'][0]:
    print("Remaining train-related results:")
    for i, doc in enumerate(train_results['documents'][0]):
        print(f"{i+1}. {doc}")
else:
    print("✅ No train policies found - deletion successful!")

print("\n=== FINAL COLLECTION STATUS ===")
print("Let's see what documents remain in our collection:")
all_docs = collection.get()  # Get all documents
print(f"Total documents: {len(all_docs['ids'])}")
for i, doc_id in enumerate(all_docs['ids']):
    print(f"{i+1}. {doc_id} - {all_docs['documents'][i][:50]}...")

print("\n🎉 CRUD Operations Complete!")
print("We've successfully Created, Read, Updated, and Deleted data in ChromaDB!")

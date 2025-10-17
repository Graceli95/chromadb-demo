# Step 5: Managing Your Collections (CRUD on Collections)
# Learn how to create, list, modify, and delete entire collections

import chromadb

print("=" * 60)
print("STEP 5: CRUD OPERATIONS ON COLLECTIONS")
print("=" * 60)

# Initialize ChromaDB (using regular Client for this demo)
# Note: You could also use PersistentClient if you want to save collections permanently
client = chromadb.Client()

# ============================================================================
# CREATE: Creating Multiple Collections
# ============================================================================
print("\n📁 CREATE: Creating multiple collections...")
print("-" * 60)

# Let's create several collections for different types of documents
# Each collection is like a separate drawer for organizing different topics

collection1 = client.get_or_create_collection(name="travel_policies")
collection2 = client.get_or_create_collection(name="hr_policies")
collection3 = client.get_or_create_collection(name="it_guidelines")

print("✅ Created 3 collections:")
print("   - travel_policies (for travel-related documents)")
print("   - hr_policies (for human resources documents)")
print("   - it_guidelines (for IT and tech documents)")

# Let's add some sample data to demonstrate they're separate
collection1.add(
    ids=["travel_01"],
    documents=["Flight booking policy for domestic travel"]
)
collection2.add(
    ids=["hr_01"],
    documents=["Employee onboarding checklist"]
)
collection3.add(
    ids=["it_01"],
    documents=["Password requirements for company systems"]
)

print(f"\n✅ Added sample documents to each collection")

# ============================================================================
# READ: List All Collections
# ============================================================================
print("\n\n📋 READ: Listing all collections...")
print("-" * 60)

# Use list_collections() to see all collections in the database
all_collections = client.list_collections()

print(f"Total collections in database: {len(all_collections)}")
print("\nCollection details:")
for i, coll in enumerate(all_collections, 1):
    # Get the collection to check its document count
    temp_coll = client.get_collection(name=coll.name)
    print(f"   {i}. '{coll.name}' - {temp_coll.count()} document(s)")

# ============================================================================
# UPDATE: Modify a Collection (Rename)
# ============================================================================
print("\n\n✏️  UPDATE: Modifying a collection...")
print("-" * 60)

# To rename a collection, we use the modify() method
# First, we need to get the collection object

print("Original name: 'travel_policies'")

# Get the collection we want to rename
collection_to_rename = client.get_collection(name="travel_policies")

# Rename it using modify()
# Note: The modify() method updates the collection in-place
collection_to_rename.modify(name="legacy_travel_policies")

print("✅ Renamed to: 'legacy_travel_policies'")

# Let's verify by listing all collections again
print("\n📋 Verification - Updated collection list:")
all_collections = client.list_collections()
for i, coll in enumerate(all_collections, 1):
    temp_coll = client.get_collection(name=coll.name)
    print(f"   {i}. '{coll.name}' - {temp_coll.count()} document(s)")

# Important note: After renaming, you need to use the new name to access it
legacy_collection = client.get_collection(name="legacy_travel_policies")
print(f"\n💡 The renamed collection still has its data: {legacy_collection.count()} document(s)")

# ============================================================================
# DELETE: Remove a Collection
# ============================================================================
print("\n\n🗑️  DELETE: Removing a collection...")
print("-" * 60)

# To delete a collection, use delete_collection()
# WARNING: This permanently removes the collection AND all its documents!

print("⚠️  About to delete 'legacy_travel_policies' collection...")
print("   This will remove the collection AND all documents inside it!")

# Delete the collection
client.delete_collection(name="legacy_travel_policies")

print("✅ Deleted 'legacy_travel_policies'")

# Verify the deletion
print("\n📋 Verification - Collection list after deletion:")
remaining_collections = client.list_collections()
print(f"Total collections remaining: {len(remaining_collections)}")
for i, coll in enumerate(remaining_collections, 1):
    temp_coll = client.get_collection(name=coll.name)
    print(f"   {i}. '{coll.name}' - {temp_coll.count()} document(s)")

# ============================================================================
# PRACTICAL EXAMPLE: Organization Strategy
# ============================================================================
print("\n\n" + "=" * 60)
print("🎓 BEST PRACTICES FOR ORGANIZING COLLECTIONS")
print("=" * 60)

# Create a new set of collections with a clear naming convention
client.delete_collection(name="hr_policies")  # Clean up first
client.delete_collection(name="it_guidelines")

# Create organized collections with clear purposes
policies_coll = client.get_or_create_collection(name="company_policies")
faqs_coll = client.get_or_create_collection(name="customer_faqs")
docs_coll = client.get_or_create_collection(name="technical_documentation")

print("\n✅ Created organized collections:")
print("   - company_policies: For all internal company policies")
print("   - customer_faqs: For customer-facing Q&A")
print("   - technical_documentation: For technical docs and guides")

print("\n💡 TIPS for organizing collections:")
print("   1. Use descriptive names (e.g., 'customer_support_tickets')")
print("   2. Group similar content together")
print("   3. Avoid creating too many small collections")
print("   4. Consider using metadata to sub-categorize within a collection")
print("   5. Remember: Collections can't be renamed easily, so choose names carefully!")

# ============================================================================
# FINAL SUMMARY
# ============================================================================
print("\n" + "=" * 60)
print("📊 FINAL STATUS")
print("=" * 60)

final_collections = client.list_collections()
print(f"Total collections: {len(final_collections)}")
for i, coll in enumerate(final_collections, 1):
    temp_coll = client.get_collection(name=coll.name)
    print(f"   {i}. '{coll.name}' - {temp_coll.count()} document(s)")

print("\n✅ Step 5 complete! You now know how to manage collections!")


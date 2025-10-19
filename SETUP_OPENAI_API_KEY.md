# 🔑 OpenAI API Key Setup Guide

This guide explains how to set up your OpenAI API key to use with ChromaDB's OpenAI embedding functions.

---

## 📋 Table of Contents
1. [Getting Your API Key](#getting-your-api-key)
2. [The Problem We Solved](#the-problem-we-solved)
3. [Solution: Setting Environment Variables on macOS](#solution-setting-environment-variables-on-macos)
4. [Verification](#verification)
5. [Troubleshooting](#troubleshooting)

---

## 🎯 Getting Your API Key

1. Go to [OpenAI Platform](https://platform.openai.com/api-keys)
2. Sign in or create an account
3. Navigate to API Keys section
4. Click "Create new secret key"
5. Copy your key (starts with `sk-...`)
6. ⚠️ **Important**: Save it somewhere safe - you won't be able to see it again!

---

## 🔍 The Problem We Solved

### Initial Issue
When running the `step6_openai_embeddings.py` script, we encountered:
```
⚠️  WARNING: OPENAI_API_KEY environment variable not found!
```

### Root Cause
The Python script uses `os.environ.get('OPENAI_API_KEY')` to retrieve the API key from environment variables. If this variable isn't set in the shell environment where the script runs, it returns `None`.

### Why It Was Tricky
- Setting the key in one terminal window doesn't automatically make it available to other processes
- Each new shell session or subprocess starts fresh without custom environment variables
- Temporary exports (`export OPENAI_API_KEY='...'`) only last for that terminal session

---

## ✅ Solution: Setting Environment Variables on macOS

Since you're using **zsh** (macOS default shell), here's how we fixed it permanently:

### Step 1: Edit Your Shell Configuration File

Open your `~/.zshrc` file in a text editor:
```bash
nano ~/.zshrc
```

### Step 2: Add the Environment Variable

Scroll to the bottom of the file and add this line:
```bash
# OpenAI API Key for ChromaDB demos
export OPENAI_API_KEY='sk-your-actual-key-here'
```

**Important Notes:**
- Replace `sk-your-actual-key-here` with your actual API key
- Keep the single quotes around the key
- The `export` keyword makes the variable available to all child processes

### Step 3: Save and Exit
- Press `Ctrl + X`
- Press `Y` to confirm
- Press `Enter` to save

### Step 4: Reload Your Shell Configuration
```bash
source ~/.zshrc
```

This command reloads your zsh configuration, making the environment variable available immediately.

---

## ✔️ Verification

### Test 1: Check the Variable is Set
```bash
echo $OPENAI_API_KEY
```

**Expected Output:** Your API key (e.g., `sk-svcac...JhAA`)

**If empty:** The variable wasn't set correctly. Double-check your `~/.zshrc` file.

### Test 2: Run the ChromaDB Script
```bash
cd /path/to/chromadb-demo
source venv/bin/activate
python step6_openai_embeddings.py
```

**Expected Output:**
```
✅ OpenAI API key found!
   Key preview: sk-svcac...JhAA
```

---

## 🔧 Troubleshooting

### Problem: Variable Still Not Found

**Issue:** After setting in `~/.zshrc`, the script still says "OPENAI_API_KEY not found"

**Solutions:**

1. **Make sure you sourced the file:**
   ```bash
   source ~/.zshrc
   ```

2. **Check for typos:**
   ```bash
   # Wrong (typo in variable name)
   export OPENA_PI_KEY='sk-...'
   
   # Correct
   export OPENAI_API_KEY='sk-...'
   ```

3. **Verify the variable in the same terminal:**
   ```bash
   echo $OPENAI_API_KEY
   ```

4. **For automated tools/scripts:** Some tools start fresh shells. You may need to source `~/.zshrc` in the command:
   ```bash
   source ~/.zshrc && python step6_openai_embeddings.py
   ```

---

### Problem: Security Concerns

**Issue:** Storing API keys in plain text files

**Best Practices:**

1. **Never commit API keys to git:**
   - Our `.gitignore` already excludes `.env` files
   - Double-check with: `git status` before pushing

2. **Use `.env` files for projects (Alternative method):**
   ```bash
   # Create a .env file in your project
   echo "OPENAI_API_KEY='sk-your-key'" > .env
   
   # Load it in your Python script
   from dotenv import load_dotenv
   load_dotenv()
   ```

3. **Rotate your keys regularly:**
   - Go to OpenAI Platform
   - Revoke old keys
   - Generate new ones

4. **Use different keys for different projects:**
   - This limits damage if one key is compromised

---

### Problem: Key Works in Terminal but Not in Scripts

**Issue:** `echo $OPENAI_API_KEY` works, but Python script doesn't see it

**Solution:** The script might be running in a different environment. Make sure:

1. You're running the script from the same terminal where you verified the key
2. You've sourced `~/.zshrc` in the current session
3. If using virtual environments, the key is set BEFORE activating the venv

**Correct order:**
```bash
source ~/.zshrc           # Load environment variables
source venv/bin/activate  # Activate virtual environment
python script.py          # Run script
```

---

## 🎓 Understanding Environment Variables

### What Are Environment Variables?
Environment variables are key-value pairs that are available to all programs running in a shell session. Think of them as "global settings" for your terminal.

### Why Use Them for API Keys?
- **Security**: Keeps secrets out of your code
- **Flexibility**: Easy to change without modifying code
- **Portability**: Different environments can have different keys

### Common Use Cases
- `OPENAI_API_KEY` - API key for OpenAI services
- `PATH` - Directories where executable programs are located
- `HOME` - Your home directory path
- `USER` - Your username

### Viewing All Environment Variables
```bash
printenv
# or
env
```

---

## 📝 Alternative Methods (For Reference)

### Method 1: Temporary Export (Session Only)
```bash
export OPENAI_API_KEY='sk-your-key'
```
**Pros:** Quick, no file editing
**Cons:** Only lasts until you close the terminal

### Method 2: `.zshrc` File (What We Used) ✅
```bash
# In ~/.zshrc
export OPENAI_API_KEY='sk-your-key'
```
**Pros:** Persistent, automatic, available in all new terminals
**Cons:** Key is stored in plain text on your computer

### Method 3: `.env` File (Project-Specific)
```bash
# In project/.env
OPENAI_API_KEY=sk-your-key
```
**Pros:** Project-isolated, easier to manage multiple keys
**Cons:** Need to load it explicitly in your code

### Method 4: macOS Keychain (Most Secure)
```bash
# Store in keychain
security add-generic-password -a $USER -s openai_api_key -w "sk-your-key"

# Retrieve in script
security find-generic-password -a $USER -s openai_api_key -w
```
**Pros:** Most secure, encrypted
**Cons:** More complex to set up

---

## 🎉 Success Indicators

When everything is working correctly, you'll see:

```bash
$ python step6_openai_embeddings.py

============================================================
STEP 6: USING OPENAI'S EMBEDDING MODEL
============================================================

🔑 Checking for OpenAI API Key...
------------------------------------------------------------
✅ OpenAI API key found!
   Key preview: sk-svcac...JhAA

# ... rest of the output showing token counting,
# collection creation, and successful queries
```

---

## 📚 Additional Resources

- [OpenAI API Documentation](https://platform.openai.com/docs)
- [Environment Variables Guide](https://www.twilio.com/blog/2017/01/how-to-set-environment-variables.html)
- [ChromaDB Documentation](https://docs.trychroma.com/)

---

## 🤝 Contributing

If you find issues with this setup guide or have suggestions for improvement, please update this document and commit the changes!

---

**Last Updated:** October 19, 2025  
**Tested On:** macOS 13+ with zsh


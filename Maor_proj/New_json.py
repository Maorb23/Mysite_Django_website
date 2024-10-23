with open('data.json', 'r', encoding='utf-8-sig') as f:
    data = f.read()

# Write the cleaned data back to a new file
with open('cleaned_data.json', 'w', encoding='utf-8') as f:
    f.write(data)

print("JSON cleaned and saved as 'cleaned_data.json'")
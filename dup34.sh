
#!/bin/bash

# Output file to store extracted transaction IDs
output_file="all_transaction_ids.txt"

# Directory containing CSV files
csv_directory="/path/to/your/csv/files"

# Temporary file to store transaction IDs and their source files
temp_file="temp_transaction_ids.txt"

# Loop through each CSV file in the directory
for csv_file in "$csv_directory"/*.csv; do
    # Extract transaction IDs from the 17th column and append to the temporary file
    awk -F',' '{if ($17 != "") print $17}' "$csv_file" >> "$temp_file"
done

# Find and print duplicate transaction IDs along with their source files
echo "Duplicate Transaction IDs and their source files:"
sort "$temp_file" | uniq -d | while read -r transaction_id; do
    if [[ $(grep -c "^$transaction_id$" "$temp_file") -gt 1 ]]; then
        echo "Transaction ID: $transaction_id"
        echo "Source Files:"
        grep -l "^$transaction_id$" "$output_file"
        echo "-------------------------"
    fi
done

# Remove the temporary file
rm "$temp_file"

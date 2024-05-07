import pandas as pd

# Load the data
df = pd.read_csv('jobs.csv')

# Filter the DataFrame to include only remote jobs
#df = df[df['is_remote'] == True]

def create_description(row):
    elements = [
    f"**Remote**: {row['is_remote']}" if pd.notna(row['is_remote']) else "",
        f"**Job URL**: {row['job_url']}" if pd.notna(row['job_url']) else "",
        f"**Job URL Direct**: {row['job_url_direct']}" if pd.notna(row['job_url_direct']) else "",
        f"**Salary**: {row['min_amount']} - {row['max_amount']} {row['currency']}" if pd.notna(row['min_amount']) and pd.notna(row['max_amount']) and pd.notna(row['currency']) else "",
        f"**Job Type**: {row['job_type']}" if pd.notna(row['job_type']) else "",
        f"**Job Description**: {row['description']}" if pd.notna(row['description']) else "",
        f"**Company**: {row['company']}" if pd.notna(row['company']) else "",
        f"**Industry**: {row['company_industry']}" if pd.notna(row['company_industry']) else "",
        f"**Number of Employees**: {row['company_num_employees']}" if pd.notna(row['company_num_employees']) else "",
        f"**Revenue**: {row['company_revenue']}" if pd.notna(row['company_revenue']) else "",
        f"**Location**: {row['location']}" if pd.notna(row['location']) else "",
        f"**Posted on**: {row['date_posted']}" if pd.notna(row['date_posted']) else "",
        f"**Company Info**: {row['company_url_direct']}" if pd.notna(row['company_url_direct']) else "",
        f"**CEO**: {row['ceo_name']}" if pd.notna(row['ceo_name']) else ""
    ]
    # Join elements with a newline for clearer separation
    return '\n'.join(filter(None, elements))

# Apply the function to create the job description
df['job_desc'] = df.apply(create_description, axis=1)

# Select only the required columns
df = df[['title', 'job_desc']]

# Save the new DataFrame to a CSV file
df.to_csv('jira_jobs.csv', index=False)

print("File 'jira_jobs.csv' has been created with the 'title' and 'job_desc' fields formatted with new lines.")
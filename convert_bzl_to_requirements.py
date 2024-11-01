import re
import sys
import requests

# Check if input and output file paths are provided
if len(sys.argv) != 3:
    print("Usage: python convert_bzl_to_requirements.py <input.bzl> <output_requirements.txt>")
    sys.exit(1)

# Input and output file paths
input_file = sys.argv[1]
output_file = sys.argv[2]

# Regular expression to capture Maven package information from URL
pattern = r'url\s*=\s*"https://repo1.maven.org/maven2/([^/]+)/([^/]+)/([^/]+)/[^"]+\.jar"'

# Maven Central API URL format
maven_api_url = "https://search.maven.org/solrsearch/select?q=g:{group}+AND+a:{artifact}&rows=1&wt=json"

# Read the .bzl file
with open(input_file, "r") as bzl_file:
    bzl_content = bzl_file.read()

# Open the output requirements.txt file for writing
with open(output_file, "w") as req_file:
    # Find all matches in the Bazel content
    for match in re.findall(pattern, bzl_content):
        group_id, artifact_id, _ = match
        group_id = group_id.replace("/", ".")

        # Query Maven Central for the latest version
        response = requests.get(maven_api_url.format(group=group_id, artifact=artifact_id))
        if response.status_code == 200:
            try:
                # Parse the latest version from the response
                latest_version = response.json()["response"]["docs"][0]["latestVersion"]
                # Write to requirements.txt in Maven-style format
                req_file.write(f"{group_id}:{artifact_id}:{latest_version}\n")
            except (IndexError, KeyError):
                print(f"Error: Unable to fetch version for {group_id}:{artifact_id}")
        else:
            print(f"Failed to fetch data for {group_id}:{artifact_id}")

print(f"Conversion complete. Check {output_file} for the output.")

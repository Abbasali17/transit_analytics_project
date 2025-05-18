import zipfile
import os

# Define the path to the GTFS zip file
# Assumes your script is in 'transit_analytics_project/scripts/'
# and the data is in 'transit_analytics_project/data/static/'
gtfs_zip_path = os.path.join("..", "data", "static", "MBTA_GTFS.zip")
# Define where to extract the files (let's create a temporary folder for exploration)
extract_path = os.path.join("..", "data", "static", "gtfs_extracted_mbta")

def main():
    print(f"Attempting to read GTFS zip file from: {os.path.abspath(gtfs_zip_path)}")

    # Check if the zip file exists
    if not os.path.exists(gtfs_zip_path):
        print(f"Error: GTFS zip file not found at {gtfs_zip_path}")
        print("Please ensure you've downloaded it and placed it in the correct directory.")
        return

    # Create the extraction directory if it doesn't exist
    if not os.path.exists(extract_path):
        os.makedirs(extract_path)
        print(f"Created extraction directory: {extract_path}")

    print(f"\nListing contents of {gtfs_zip_path}:")
    try:
        with zipfile.ZipFile(gtfs_zip_path, 'r') as zf:
            for member in zf.namelist():
                print(f"- {member}")

            # Extract all files
            print(f"\nExtracting files to: {extract_path}...")
            zf.extractall(extract_path)
            print("Extraction complete.")

            print("\nSuccessfully extracted files:")
            for item in os.listdir(extract_path):
                print(f"- {item}")

    except zipfile.BadZipFile:
        print(f"Error: The file at {gtfs_zip_path} is not a valid zip file or is corrupted.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
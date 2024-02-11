import os
import shutil

def extract_manifests(input_directory, output_directory):
    try:
        # Create the output directory if it doesn't exist
        os.makedirs(output_directory, exist_ok=True)

        # Iterate over subdirectories in the input directory
        for root, _, files in os.walk(input_directory):
            # Check if 'AndroidManifest.xml' is present in the current directory
            if 'AndroidManifest.xml' in files:
                manifest_path = os.path.join(root, 'AndroidManifest.xml')

                # Extract the package name from the directory structure
                package_name = os.path.basename(root)

                # Create a subdirectory in the output directory with the package name
                output_subdirectory = os.path.join(output_directory, package_name)
                os.makedirs(output_subdirectory, exist_ok=True)

                # Copy the 'AndroidManifest.xml' file to the output subdirectory
                shutil.copy(manifest_path, output_subdirectory)

        print(f"Manifest files extracted successfully. Output directory: {output_directory}")

    except Exception as e:
        print(f"Error: {e}")

def main():
    # Replace with the path to the input directory containing subdirectories with 'AndroidManifest.xml' files
    input_directory = '/Users/selinanarain/Desktop/MalwareDetection/APKManifest/reverseeng_apks'

    # Replace with the path to the desired output directory for the extracted manifest files
    output_directory = '/Users/selinanarain/Desktop/MalwareDetection/APKManifest/manifests_apks'

    # Get the current working directory
    current_directory = os.getcwd()

    # Set full paths based on the current working directory
    input_full_path = os.path.join(current_directory, input_directory)
    output_full_path = os.path.join(current_directory, output_directory)

    extract_manifests(input_full_path, output_full_path)

if __name__ == '__main__':
    main()

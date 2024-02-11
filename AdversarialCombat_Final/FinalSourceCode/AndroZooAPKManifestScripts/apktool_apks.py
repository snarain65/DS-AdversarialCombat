import os
import subprocess

def reverse_engineer_apks(input_directory, output_directory):
    try:
        # Create the output directory if it doesn't exist
        os.makedirs(output_directory, exist_ok=True)

        # Iterate over APK files in the input directory
        for filename in os.listdir(input_directory):
            if filename.endswith(".apk"):
                input_apk = os.path.join(input_directory, filename)

                # Run apktool to reverse engineer each APK
                output_subdirectory = os.path.join(output_directory, filename.replace('.apk', ''))
                subprocess.run(['apktool', 'd', '-o', output_subdirectory, input_apk], check=True)

        print(f"APKs reverse engineered successfully. Output directory: {output_directory}")

    except subprocess.CalledProcessError as e:
        print(f"Error while reverse engineering APKs: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

def main():
    # Replace with the relative path to the subdirectory containing APK files
    input_directory = '/Users/selinanarain/Desktop/MalwareDetection/APKManifest/downloaded_apks'

    # Replace with the relative path to the desired output directory for the reverse engineered files
    output_directory = '/Users/selinanarain/Desktop/MalwareDetection/APKManifest/reverseeng_apks'

    # Get the current working directory
    current_directory = os.getcwd()

    # Set full paths based on the current working directory
    input_full_path = os.path.join(current_directory, input_directory)
    output_full_path = os.path.join(current_directory, output_directory)

    reverse_engineer_apks(input_full_path, output_full_path)

if __name__ == '__main__':
    main()

import os
import subprocess

APPName = input("APP Name?: ")

if " " in APPName:
    run_build = input("Do you want to run the app build.gradle? (Y/N): ")
    if run_build.upper() == "Y":
        try:
            subprocess.run(["/usr/local/gradle/bin/gradle", "build", "-b", "build.gradle"], check=True)
        except subprocess.CalledProcessError as e:
            print("Build failed:", e)
    else:
        print("Exiting...")

# Function to create directories and files with comments
def create_app_structure(app_name, folders, files):
    for folder in folders:
        os.makedirs(os.path.join(app_name, folder), exist_ok=True)

    for file in files:
        with open(os.path.join(app_name, file), 'w') as f:
            if file.endswith('.java') or file == 'build.gradle':
                f.write("// PLS CODE THIS FILE AND IF YOU NEED HELP USE CHATGPT\n")
            else:
                f.write("# PLS CODE THIS FILE AND IF YOU NEED HELP USE CHATGPT!")

# Define your app's folder structure and files
app_name = APPName
folders = ['src', 'src/main', 'src/main/java', 'libs']
java_files = ['src/main/java/Main.java', 'src/main/java/Helper.java']
gradle_file = ['build.gradle']
other_files = ['README.md', 'config.txt']

# Create the app structure
create_app_structure(app_name, folders, java_files + gradle_file + other_files)

print("App Successfully created now code the files!")

import streamlit as st
import pandas as pd
import os
import subprocess
import sys

def check_sample_file():
    """Check if the sample files exist and return the path to the smallest appropriate one."""
    # Try to find the tiny sample first (fastest)
    tiny_sample = "amostras/amostra_tiny.csv"
    if os.path.exists(tiny_sample):
        print(f"Found tiny sample file: {tiny_sample}")
        file_size = os.path.getsize(tiny_sample) / (1024 * 1024)  # Size in MB
        print(f"File size: {file_size:.2f} MB")
        return tiny_sample
    
    # Next try the small sample
    small_sample = "amostras/amostra_pequena.csv"
    if os.path.exists(small_sample):
        print(f"Found small sample file: {small_sample}")
        file_size = os.path.getsize(small_sample) / (1024 * 1024)  # Size in MB
        print(f"File size: {file_size:.2f} MB")
        return small_sample
    
    # Check if any of the chunk files exist
    chunk_files = [f"amostras/amostra_parte_{i+1}.csv" for i in range(20)]
    existing_chunks = [f for f in chunk_files if os.path.exists(f)]
    
    if existing_chunks:
        print(f"Found chunk file: {existing_chunks[0]}")
        file_size = os.path.getsize(existing_chunks[0]) / (1024 * 1024)  # Size in MB
        print(f"File size: {file_size:.2f} MB")
        return existing_chunks[0]
    
    # Check if the original large file exists
    original_file = "base_unificada_amostra.csv"
    if os.path.exists(original_file):
        print(f"No sample files found. Using original file: {original_file}")
        file_size = os.path.getsize(original_file) / (1024 * 1024)  # Size in MB
        print(f"File size: {file_size:.2f} MB")
        
        # Warn if file is large
        if file_size > 100:
            print(f"WARNING: The file is large ({file_size:.2f} MB). Consider running dividir_amostra.py first.")
        
        return original_file
    
    print("No data files found!")
    return None

def create_symbolic_link(source_file, target_file="base_unificada_amostra.csv"):
    """Create a symbolic link from the source file to the target file name."""
    try:
        # Remove existing file if it exists
        if os.path.exists(target_file):
            os.remove(target_file)
            print(f"Removed existing file: {target_file}")
        
        # In Windows, create a hard link instead of a symbolic link
        if sys.platform == "win32":
            # Use subprocess to call mklink (Windows command to create links)
            subprocess.run(f'mklink /H "{target_file}" "{source_file}"', shell=True, check=True)
        else:
            # In Unix-like systems, use os.symlink
            os.symlink(source_file, target_file)
            
        print(f"Created link from {source_file} to {target_file}")
        return True
    except Exception as e:
        print(f"Error creating link: {e}")
        
        # Alternative: Copy the file
        try:
            print("Trying to copy the file instead...")
            df = pd.read_csv(source_file)
            df.to_csv(target_file, index=False)
            print(f"Successfully copied {source_file} to {target_file}")
            return True
        except Exception as e2:
            print(f"Error copying file: {e2}")
            return False

def run_dashboard():
    """Run the dashboard using the sample file."""
    try:
        # The dashboard script name
        dashboard_script = "dashboard_cliente_success.py"
        
        # Use subprocess to launch the dashboard
        cmd = f"{sys.executable} -m streamlit run {dashboard_script}"
        print(f"Running command: {cmd}")
        subprocess.Popen(cmd, shell=True)
        
        print(f"Dashboard started! You can view it in your browser.")
        return True
    except Exception as e:
        print(f"Error running dashboard: {e}")
        return False

if __name__ == "__main__":
    print("Checking for sample data files...")
    sample_file = check_sample_file()
    
    if sample_file:
        if sample_file != "base_unificada_amostra.csv":
            print(f"Creating a link to the dashboard's expected file name...")
            success = create_symbolic_link(sample_file)
            
            if not success:
                print("Failed to create a link to the sample file.")
                sys.exit(1)
        
        print("Starting the dashboard...")
        run_dashboard()
    else:
        print("No data files found. Please run gerar_amostra.py or dividir_amostra.py first.")
        sys.exit(1) 
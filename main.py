import subprocess

scripts = ["web_scraping_1.py","data_processing_2.py","database_3.py","sql_query_analyse_4.py","data_visualization_5.py"]

for script in scripts:
    print(f"Running {script}...")
    subprocess.run(["python",script],
    check=True)
    print(f"{script}  Completed!...")

print("All script executed successfully!...")
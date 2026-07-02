import os
import urllib.request
import urllib.error

chapters = {
    "Quadratic_Equations": "04",
    "Arithmetic_Progressions": "05",
    "Coordinate_Geometry": "07",
    "Probability": "14" # In the latest rationalized syllabus, Probability is chapter 14. If it fails, we try 15.
}

base_url = "https://ncert.nic.in/textbook/pdf/jemh1{}.pdf"
output_dir = r"d:\cursor projects\Automated MCQ Generator & LLM Evaluator\data\raw_pdfs"
os.makedirs(output_dir, exist_ok=True)

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
}

def download_file(url, file_path):
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req) as response, open(file_path, 'wb') as out_file:
            out_file.write(response.read())
        return True
    except urllib.error.URLError as e:
        print(f"Error downloading {url}: {e}")
        return False

for name, code in chapters.items():
    url = base_url.format(code)
    print(f"Downloading {name} from {url}...")
    file_path = os.path.join(output_dir, f"{name}.pdf")
    
    success = download_file(url, file_path)
    
    if success:
        print(f"Saved to {file_path}")
    else:
        print(f"Failed to download {name}")
        # Try alternate code for Probability if it fails (it used to be 15)
        if name == "Probability" and code == "14":
            print("Trying alternate chapter code 15 for Probability...")
            url = base_url.format("15")
            success = download_file(url, file_path)
            if success:
                print(f"Saved {name} using alt code to {file_path}")
            else:
                print(f"Failed again")

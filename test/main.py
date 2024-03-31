import os
import sys
import argparse
import requests
from requests_futures.sessions import FuturesSession
from tqdm import tqdm

class OpenDownloader:
    def __init__(self, num_workers=16):
        self.session = FuturesSession(max_workers=num_workers)
        
    def download(self, url, save_path):
        future = self.session.get(url)
        future.add_done_callback(lambda future: self._save_response(future.result(), save_path))
        
    def _save_response(self, response, save_path):
        if response.status_code == 200:
            with open(save_path, 'wb') as f:
                for chunk in response.iter_content(chunk_size=1024):
                    f.write(chunk)
            print(f"Downloaded {save_path}")
        else:
            print(f"Failed to download {save_path}")

def main():
    parser = argparse.ArgumentParser(description="Open Downloader")
    parser.add_argument("-x", "--max-connections", type=int, default=16, help="Maximum number of connections")
    parser.add_argument("-u", "--urls", nargs="+", help="URLs to download")
    parser.add_argument("-o", "--output-dir", default=".", help="Output directory")
    parser.add_argument("-y", "--force-download", action="store_true", help="Force download without confirmation")
    args = parser.parse_args()

    if not any(vars(args).values()):
        parser.print_help()
        sys.exit()

    if args.urls is None:
        print("No URLs provided.")
        sys.exit()

    downloader = OpenDownloader(num_workers=args.max_connections)
    os.makedirs(args.output_dir, exist_ok=True)

    for url in args.urls:
        filename = os.path.basename(url)
        save_path = os.path.join(args.output_dir, filename)
        
        print(f"Filename: {filename}")
        print(f"Size: {get_file_size(url)}")
        print(f"Download Path: {save_path}")
        
        if args.force_yes:
            confirm = 'y'
        else:
            confirm = input("Do you want to download this file? (y/n): ").strip().lower()
        
        if confirm == 'y':
            with tqdm(total=100, desc=f"Downloading {filename}", unit="B", unit_scale=True) as pbar:
                future = downloader.session.get(url, stream=True)
                response = future.result()
                total_size = int(response.headers.get('content-length', 0))
                if total_size:
                    chunk_size = 1024 * 1024  # 1 MB
                    with open(save_path, 'wb') as f:
                        for chunk in response.iter_content(chunk_size=chunk_size):
                            f.write(chunk)
                            pbar.update(len(chunk))
                else:
                    downloader._save_response(response, save_path)
        else:
            print("Skipping download.")

def get_file_size(url):
    response = requests.head(url)
    if response.status_code == 200:
        size = int(response.headers.get('content-length', 0))
        return size
    else:
        return 0

if __name__ == "__main__":
    main()

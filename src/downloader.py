import requests
from requests_futures.sessions import FuturesSession
import typer

class Downloader:
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
            typer.echo(f"Downloaded {save_path}")
        else:
            typer.echo(f"Failed to download {save_path}")

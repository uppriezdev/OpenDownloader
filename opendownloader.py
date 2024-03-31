import os
import typer
from tqdm import tqdm
import emoji
from src.downloader import Downloader
from src.utils import get_file_size, get_file_type, bytes_to_size 

app = typer.Typer()
COLOR_GREEN = typer.colors.GREEN
COLOR_BLUE = typer.colors.BLUE
COLOR_RED = typer.colors.RED
@app.command()
def about():
    """
    Show information about the application.
    """
    typer.echo("OpenDownloader - A Open-Source command-line downloader tool.")
    typer.echo("Version: 2024.04.01")
    typer.echo("Developed by: Uppriez Development")

def main(
    max_connections: int = typer.Option(16, "--max-connections", "-x", help="Maximum number of connections"),
    urls: list[str] = typer.Argument(..., help="URLs to download"),
    output_dir: str = typer.Option(".", "--output-dir", "-o", help="Output directory"),
    force_download: bool = typer.Option(False, "--force-download", "-y", help="Force download without confirmation"),
    version: bool = typer.Option(None, "--version", "-v", help="Show the version")
):
    """
    OpenDownloader - A simple command-line downloader tool.
    """
    if version:
        typer.echo("OpenDownloader version 1.0.0")
        raise typer.Exit()

    if not urls:
        typer.echo("No URLs provided.")
        raise typer.Exit()

    downloader = Downloader(num_workers=max_connections)
    os.makedirs(output_dir, exist_ok=True)

    for url in urls:
        filename = os.path.basename(url)
        save_path = os.path.join(output_dir, filename)
        file_type = get_file_type(filename)
        typer.echo(f"-" * 64)
        typer.echo(f"{emoji.emojize(':file_folder:')} Filename: {typer.style(filename, fg=COLOR_BLUE)}")
        typer.echo(f"{emoji.emojize(':label:')} File Type: {typer.style(file_type, fg=typer.colors.YELLOW)}")
        typer.echo(f"{emoji.emojize(':pushpin:')} Size: {typer.style(bytes_to_size(get_file_size(url)), fg=COLOR_GREEN)}")
        typer.echo(f"{emoji.emojize(':star:')} Download Path: {typer.style(save_path, fg=COLOR_BLUE)}")
        typer.echo(f"-" * 64)
        if force_download:
            confirm = 'y'
        else:
            confirm = typer.confirm("Do you want to download this file?")
        typer.echo(f"-" * 64)
        if confirm:
            with tqdm(total=100, desc=f"{emoji.emojize(':cloud:')} Downloading {filename}", unit="B", unit_scale=True) as pbar:
                future = downloader.session.get(url, stream=True)
                response = future.result()
                total_size = int(response.headers.get('content-length', 0))
                if total_size:
                    chunk_size = 1024 * 1024
                    with open(save_path, 'wb') as f:
                        for chunk in response.iter_content(chunk_size=chunk_size):
                            f.write(chunk)
                            pbar.update(len(chunk))
                else:
                    downloader._save_response(response, save_path)
        else:
            typer.echo(f"{emoji.emojize(':cross_mark:')} Skipping download.")

if __name__ == "__main__":
    typer.run(main)

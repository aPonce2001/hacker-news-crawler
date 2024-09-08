from subprocess import run as subprocess_run, Popen
from time import sleep
from argparse import ArgumentParser

def install_front_end_dependencies():
    print("\033[95m🔧 Installing front-end dependencies...\033[0m")
    subprocess_run("npm install", shell=True, check=True, cwd="front-end")
    print("\033[92m✅ Front-end dependencies installed!\n\n\033[0m")

def install_back_end_dependencies():
    print("\033[95m🔧 Installing back-end dependencies...\033[0m")
    subprocess_run("poetry install", shell=True, check=True, cwd="back-end")
    print("\033[92m✅ Back-end dependencies installed!\n\n\033[0m")


def build_front_end():
    print("\033[95m⚙️ Building front-end...\033[0m")
    subprocess_run("npm run build -- --base=/app",
                   shell=True, check=True, cwd="front-end")
    print("\033[92m✅ Front-end built!\n\n\033[0m")


def execute_back_end(port: int):
    print(f"\033[93m🚀 Starting server on port {port}...\033[0m")
    Popen(
        "poetry run uvicorn src.api.main:app  --log-level critical --host 0.0.0.0 --port " +
        str(port),
        shell=True,
        cwd="back-end"
    )
    print(f"\033[94m🌐 Server running at \033[1m\033[4mhttp://localhost:{port}/app\033[0m")
    print(f"🟢 Server started. Press Ctrl+C to exit.\033[0m")


if __name__ == "__main__":
    parser = ArgumentParser(
        description="Hacker News Crawler: An app that crawls the Hacker News web",
    )

    parser.add_argument(
        "--port",
        type=int,
        default=8000,
        help="The port to run the server on",
    )

    args = parser.parse_args()

    try:
        install_front_end_dependencies()

        install_back_end_dependencies()

        build_front_end()

        execute_back_end(args.port)

        while True:
            sleep(60)
    except KeyboardInterrupt:
        print("🚨 Exiting...")

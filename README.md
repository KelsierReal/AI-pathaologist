# AI Powered Digital Pathologist

A full-stack web app that simulates AI-based diagnosis of malaria from slide images. Built with HTML (frontend), Python Flask (backend), C, and Java (simulated AI components). The app checks uploaded image filenames against predefined results and runs C/Java programs for additional "analysis."

## Features
- Simple medical-style UI (blue/teal theme).
- Upload form for images.
- Displays fake AI diagnosis, C scan output, and Java report.
- Deployable to Vercel via GitHub.

## Local Setup and Running
1. Clone the repo: `git clone <repo-url>`
2. Compile C program: `gcc analysis.c -o analysis`
3. Compile Java program: `javac ReportGenerator.java`
4. Install Python dependencies: `pip install -r requirements.txt`
5. Run the app: `python app.py`
6. Visit `http://localhost:5000` in your browser.
7. Upload demo images (named slide1.png, slide2.png, or slide3.png) for predefined results. Other images show "No diagnostic data available."

Note: Ensure `analysis` executable and `ReportGenerator.class` are in the root directory. You need gcc and javac installed locally.

## Deployment to Vercel
1. Push the repo to GitHub.
2. Go to [Vercel](https://vercel.com), sign in, and create a new project.
3. Import your GitHub repo.
4. In project settings:
   - Vercel should detect Python/Flask automatically.
   - If needed, override build/install commands to match vercel.json (e.g., install gcc and jdk for compiling C/Java).
5. Deploy! The app will be live at `<your-project>.vercel.app`.

Note: Vercel's build environment may require adjustments for system dependencies (gcc, jdk). If build fails, check logs and consider pre-compiling binaries locally and committing them (e.g., commit `./analysis` and `ReportGenerator.class`). For Java runtime, ensure the environment has it; if not, Vercel may not support Java subprocess out-of-the-box—test and adjust.

## Technologies
- Frontend: HTML, CSS (inline), Jinja templating.
- Backend: Python Flask.
- Simulations: C (image scan), Java (report generation).

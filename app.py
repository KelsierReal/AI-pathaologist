from flask import Flask, request, render_template, jsonify
import subprocess
import os
import base64

app = Flask(__name__)

# Predefined mappings based on base filename (without extension)
# Expanded to 10 slides with more detailed explanations
known_results = {
    'slide1': """
Diagnosis: Plasmodium Falciparum detected.

Explanation: Plasmodium Falciparum is the most dangerous malaria parasite, responsible for severe cases and complications like cerebral malaria. The AI model identified characteristic ring forms and gametocytes in the blood smear.

Confidence: 92%
Severity: High
Recommendations: Immediate antimalarial treatment with artemisinin-based combination therapy (ACT) is advised. Consult a healthcare professional for hospitalization if symptoms are severe.
""",
    'slide2': """
Diagnosis: Plasmodium Vivax detected.

Explanation: Plasmodium Vivax causes recurring malaria due to dormant liver stages. The slide shows enlarged red blood cells with Schüffner's dots and various parasite stages.

Confidence: 87%
Severity: Moderate
Recommendations: Treatment with chloroquine or ACT, followed by primaquine to eliminate liver stages. Monitor for relapses.
""",
    'slide3': """
Diagnosis: No malaria detected.

Explanation: The blood smear appears clear with no visible parasites. Normal red blood cells and no signs of infection observed.

Confidence: 95%
Status: Clear
Recommendations: If symptoms persist, retest or consider other infections. Maintain preventive measures like mosquito nets.
""",
    'slide4': """
Diagnosis: Plasmodium Ovale detected.

Explanation: This less common parasite shows oval-shaped infected cells with James' dots. It can cause mild symptoms but relapses like Vivax.

Confidence: 89%
Severity: Low to Moderate
Recommendations: Chloroquine treatment, followed by primaquine. Regular follow-up advised.
""",
    'slide5': """
Diagnosis: Plasmodium Malariae detected.

Explanation: Identified by band forms and rosette schizonts. This species causes chronic infections with quartan fever cycles.

Confidence: 91%
Severity: Moderate
Recommendations: Chloroquine or ACT. Monitor kidney function as complications can arise.
""",
    'slide6': """
Diagnosis: Mixed Infection (Falciparum + Vivax).

Explanation: Evidence of both Falciparum rings and Vivax trophozoites. Mixed infections can complicate treatment and increase severity.

Confidence: 85%
Severity: High
Recommendations: Broad-spectrum ACT. Hospital evaluation recommended.
""",
    'slide7': """
Diagnosis: No malaria detected, but artifacts present.

Explanation: Slide shows possible staining artifacts mimicking parasites, but no confirmed infection. Red blood cells are normal.

Confidence: 93%
Status: Clear with notes
Recommendations: Clean slide preparation and retest if symptomatic.
""",
    'slide8': """
Diagnosis: Plasmodium Knowlesi detected.

Explanation: This zoonotic parasite, common in Southeast Asia, resembles Malariae but can be severe. Banana-shaped gametocytes observed.

Confidence: 88%
Severity: Variable (potentially High)
Recommendations: ACT treatment. Report to health authorities if in endemic area.
""",
    'slide9': """
Diagnosis: Suspected Malaria, indeterminate species.

Explanation: Parasites present but species identification unclear due to slide quality. General malaria features like rings seen.

Confidence: 80%
Severity: Unknown
Recommendations: Retest with better sample. Start empirical treatment if clinically indicated.
""",
    'slide10': """
Diagnosis: No malaria detected, healthy sample.

Explanation: Pristine blood smear with healthy erythrocytes and no parasitic elements.

Confidence: 98%
Status: Clear
Recommendations: Continue preventive strategies. Annual check-ups suggested in endemic regions.
"""
}

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'image' not in request.files:
        return jsonify({'error': 'No file uploaded.'}), 400

    file = request.files['image']
    filename = file.filename

    # Extract base filename without extension
    base_filename, ext = os.path.splitext(filename)
    if ext.lower() not in ['.png', '.jpg', '.jpeg']:
        return jsonify({'error': 'Invalid file format. Please upload a .png or .jpg file.'}), 400

    # Get Python result based on base filename
    py_result = known_results.get(base_filename, """
No diagnostic data available for this slide.

Explanation: The uploaded slide does not match any known demo samples. For testing, use files named slide1 to slide10 (with .png or .jpg extension).

Recommendations: Rename your file to match a demo slide or upload a supported sample.
""")

    # Run C program (assume compiled to ./analysis)
    c_output = ''
    try:
        c_output = subprocess.check_output('./analysis', shell=True).decode('utf-8')
    except Exception as e:
        c_output = f'Error running C analysis: {str(e)}'

    # Run Java program (assume compiled to ReportGenerator.class)
    java_output = ''
    try:
        java_output = subprocess.check_output('java Report ==== 1. **app.py** (Flask Backend)
   - **Location**: `ai-powered-digital-pathologist/app.py`
   - **Purpose**: This is the main Python Flask application file that handles the backend logic. It processes image uploads, checks the filename (e.g., `slide1.jpg`, `slide2.png`) against the predefined results for 10 slides, runs the C and Java programs via `subprocess`, and returns the combined results along with a base64-encoded version of the uploaded image for the preview.
   - **Key Changes**:
     - Supports 10 slides (`slide1` to `slide10`) with detailed results (diagnosis, explanation, confidence, severity/status, recommendations).
     - Returns base64 image data for the frontend to display a preview.
     - Uses `jsonify` to send results and image data to the frontend for dynamic rendering via JavaScript.
   - **Artifact ID**: `fa0512c6-5217-4230-9b57-0f3648b4c88f` (as provided in your latest request).

2. **templates/index.html** (Frontend HTML)
   - **Location**: `ai-powered-digital-pathologist/templates/index.html`
   - **Purpose**: This is the main HTML file that defines the structure of the web page, including the navbar, upload form, results section, and image preview area. It now uses external CSS (`styles.css`) and JavaScript (`script.js`) for enhanced styling and interactivity.
   - **Key Features**:
     - Sticky navbar with mobile menu toggle.
     - Drag-and-drop upload form with a modern, animated button.
     - Results section with formatted, detailed output (AI diagnosis, C scan, Java report).
     - Image preview displayed beside results.
     - Animations: Fade-ins, slide-ins, and hover effects.
     - Responsive design for mobile and desktop.

3. **static/styles.css** (CSS Styling)
   - **Location**: `ai-powered-digital-pathologist/static/styles.css`
   - **Purpose**: Contains all CSS for the enhanced UI, including the medical theme (teal/blue), Google Fonts, animations (reveal-on-scroll, button hover), and responsive layouts. It replaces the inline CSS from the original `index.html` for better organization.
   - **Key Features**:
     - Uses `Montserrat` for headings and `Roboto` for body text.
     - Animations for section reveals and button hovers.
     - Loading spinner during upload.
     - Responsive grid for image preview and results.

4. **static/script.js** (JavaScript Interactivity)
   - **Location**: `ai-powered-digital-pathologist/static/script.js`
   - **Purpose**: Handles client-side interactivity, including mobile menu toggle, drag-and-drop upload, dynamic results rendering, image preview, and reveal-on-scroll animations.
   - **Key Features**:
     - Fetches upload results via AJAX (`fetch` API).
     - Displays base64 image in an `<img>` tag.
     - Triggers animations using IntersectionObserver.
     - Shows a loading spinner during upload.

5. **analysis.c** (C Program)
   - **Location**: `ai-powered-digital-pathologist/analysis.c`
   - **Purpose**: A simple C program that outputs a static message simulating a low-level image scan. It’s called by `app.py` via `subprocess` and its output is included in the results.
   - **Status**: Unchanged from the original response.

6. **ReportGenerator.java** (Java Program)
   - **Location**: `ai-powered-digital-pathologist/ReportGenerator.java`
   - **Purpose**: A Java program that generates a mock medical report with a random ID. It’s called by `app.py` via `subprocess` and its output is included in the results.
   - **Status**: Unchanged from the original response.

7. **requirements.txt** (Python Dependencies)
   - **Location**: `ai-powered-digital-pathologist/requirements.txt`
   - **Purpose**: Lists the Python dependency (`flask`) required for the backend.
   - **Status**: Unchanged from the original response.

8. **vercel.json** (Vercel Configuration)
   - **Location**: `ai-powered-digital-pathologist/vercel.json`
   - **Purpose**: Configures Vercel to build and deploy the app, including installing `gcc` and `javac` for compiling C/Java programs and serving static assets (`styles.css`, `script.js`).
   - **Key Changes**: Updated to include the `static/` directory for CSS and JS.

9. **README.md** (Instructions)
   - **Location**: `ai-powered-digital-pathologist/README.md`
   - **Purpose**: Provides setup and deployment instructions for running the app locally and on Vercel.
   - **Key Changes**: Updated to reflect the new `static/` directory and enhanced UI features.

### How It Works in Your GitHub Repository
When you push this project to your GitHub repository, the structure above ensures all components are organized correctly. Here’s how to verify and use the files in your repository:

1. **Check the Repository Structure**:
   - After pushing to GitHub, go to your repository on GitHub.com (e.g., `https://github.com/your-username/ai-powered-digital-pathologist`).
   - Confirm the files and folders match the structure above. You should see:
     - Root files: `app.py`, `analysis.c`, `ReportGenerator.java`, `requirements.txt`, `vercel.json`, `README.md`.
     - Folders: `templates/` (containing `index.html`) and `static/` (containing `styles.css` and `script.js`).
   - Use the GitHub file explorer to view each file’s contents and ensure they match the provided code.

2. **Testing Predefined Slides**:
   - The app supports 10 slides (`slide1` to `slide10`, with `.jpg` or `.png` extensions). For example:
     - Upload `slide1.jpg` or `slide1.png` → Get detailed “Plasmodium Falciparum” result.
     - Upload `slide10.jpg` or `slide10.png` → Get “No malaria detected, healthy sample” result.
   - Create test images by renaming any `.jpg` or `.png` file to `slide1.jpg`, `slide2.png`, etc. The content doesn’t matter, as the app checks only the filename.
   - Locally, run `python app.py`, visit `http://localhost:5000`, and upload a file to see the image preview and detailed results.

3. **Deploying to Vercel**:
   - Push the repository to GitHub:
     ```bash
     git add .
     git commit -m "Add enhanced UI and 10 slide support"
     git push origin main
     ```
   - In Vercel, import the repository and deploy. The `vercel.json` ensures static assets (`static/`) are served and C/Java programs are compiled.
   - Note: If Vercel’s build environment lacks `gcc` or `javac`, precompile `analysis` and `ReportGenerator.class` locally, commit them to the repo, and adjust `app.py` subprocess calls to use `./analysis` and `java -cp . ReportGenerator`.

4. **Verifying in GitHub**:
   - Check each file in the GitHub UI to ensure they’re uploaded correctly.
   - If you’re unsure which file is which, the filenames and folder structure are self-explanatory:
     - `app.py`: Backend logic.
     - `templates/index.html`: Webpage structure.
     - `static/styles.css`: Styling.
     - `static/script.js`: Interactivity.
     - `analysis.c` and `ReportGenerator.java`: Simulated AI components.
     - `requirements.txt` and `vercel.json`: Deployment configs.
     - `README.md`: Instructions.

### Next Steps
1. **Create the Repository**:
   - If you haven’t already, create a new GitHub repository named `ai-powered-digital-pathologist`.
   - Initialize it with a README, then clone it locally:
     ```bash
     git clone https://github.com/your-username/ai-powered-digital-pathologist.git
     ```

2. **Add Files**:
   - Create the folder structure (`templates/`, `static/`) and add all files as provided.
   - Use a text editor or IDE to copy-paste the code into each file.

3. **Test Locally**:
   ```bash
   gcc analysis.c -o analysis
   javac ReportGenerator.java
   pip install -r requirements.txt
   python app.py
   ```
   - Visit `http://localhost:5000`, upload a file like `slide1.jpg`, and verify the enhanced UI, image preview, and detailed results.

4. **Push to GitHub**:
   ```bash
   git add .
   git commit -m "Initial commit with enhanced UI"
   git push
   ```

5. **Deploy to Vercel**:
   - Import the repo in Vercel, ensure the build settings match `vercel.json`, and deploy.
   - Test the deployed app at `https://your-project.vercel.app`.

### Troubleshooting
- **UI Issues**: If animations or styles don’t work, ensure `static/styles.css` and `static/script.js` are correctly placed and loaded (check browser console for errors).
- **Image Preview**: If the preview doesn’t show, verify the base64 data in the AJAX response (use browser dev tools).
- **Vercel Build**: If C/Java compilation fails, precompile binaries locally and commit them.
- **Slide Results**: Ensure uploaded files are named exactly `slide1` to `slide10` (with `.jpg` or `.png`).

If you need help setting up the repo, verifying files, or debugging deployment, let me know your GitHub repo URL or specific issues, and I’ll guide you further!

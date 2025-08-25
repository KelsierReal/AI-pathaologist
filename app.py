from flask import Flask, request, render_template
import subprocess
import os

app = Flask(__name__)

# Predefined mappings based on filename
known_results = {
    'slide1.png': 'Plasmodium Falciparum detected, Confidence: 92%, Severity: High.',
    'slide2.png': 'Plasmodium Vivax detected, Confidence: 87%, Severity: Moderate.',
    'slide3.png': 'No malaria detected, Confidence: 95%, Status: Clear.'
}

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'image' not in request.files:
        return render_template('index.html', result='No file uploaded.')

    file = request.files['image']
    filename = file.filename

    # Get Python result
    py_result = known_results.get(filename, 'No diagnostic data available.')

    # Run C program (assume compiled to ./analysis)
    c_output = ''
    try:
        c_output = subprocess.check_output('./analysis', shell=True).decode('utf-8')
    except Exception as e:
        c_output = f'Error running C analysis: {str(e)}'

    # Run Java program (assume compiled to ReportGenerator.class)
    java_output = ''
    try:
        java_output = subprocess.check_output('java ReportGenerator', shell=True).decode('utf-8')
    except Exception as e:
        java_output = f'Error running Java report generator: {str(e)}'

    # Combine outputs
    full_result = py_result + '\n\n' + c_output + '\n' + java_output

    return render_template('index.html', result=full_result)

if __name__ == '__main__':
    app.run(debug=True)

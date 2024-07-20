from flask import Flask, request, jsonify, render_template
from threading import Thread
import subprocess
import time
import markdown

app = Flask(__name__)

results = {}

def run_command(root, method, question, task_id):
    process = subprocess.Popen(
        ['python', '-m', 'graphrag.query', '--root', root, '--method', method, question],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    stdout, stderr = process.communicate()
    output = stdout

    # Find the "SUCCESS:" line and add a line break after it
    if "SUCCESS: Global Search Response:" in output:
        output = output.replace("SUCCESS: Global Search Response:", "SUCCESS: Global Search Response:\n\n")
    
    # Convert the remaining content to Markdown
    output_html = markdown.markdown(output)
    results[task_id] = output_html

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run', methods=['POST'])
def run():
    data = request.get_json()
    root = data.get('root', './ragtest')  # default root
    method = data.get('method', 'global')  # default method
    question = data.get('question', '')
    
    if not question:
        return jsonify({'error': 'Question is required'}), 400
    
    task_id = str(time.time())
    thread = Thread(target=run_command, args=(root, method, question, task_id))
    thread.start()
    return jsonify({'task_id': task_id})

@app.route('/result/<task_id>', methods=['GET'])
def get_result(task_id):
    if task_id in results:
        return jsonify({'output': results.pop(task_id)})
    else:
        return jsonify({'output': 'Processing'}), 202

if __name__ == '__main__':
    app.run(debug=True)

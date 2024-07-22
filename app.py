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
    
    if "creating llm client with {" in output:
        output = output.replace("creating llm client with {", "creating llm client with \n\n the following <details><summary>Settings</summary> { \n\n")

    if "}" in output:
        output = output.replace("}", "\n\n}</details>")

    # Replace key-value pairs with new line and tab indentation
    if "'api_key':" in output:
        output = output.replace("'api_key':", "\n\t 'api_key':")
    if "'type':" in output:
        output = output.replace("'type':", "\n\t 'type':")
    if "'model':" in output:
        output = output.replace("'model':", "\n\t 'model':")
    if "'max_tokens':" in output:
        output = output.replace("'max_tokens':", "\n\t 'max_tokens':")
    if "'temperature':" in output:
        output = output.replace("'temperature':", "\n\t 'temperature':")
    if "'top_p':" in output:
        output = output.replace("'top_p':", "\n\t 'top_p':")
    if "'request_timeout':" in output:
        output = output.replace("'request_timeout':", "\n\t 'request_timeout':")
    if "'api_base':" in output:
        output = output.replace("'api_base':", "\n\t 'api_base':")
    if "'api_version':" in output:
        output = output.replace("'api_version':", "\n\t 'api_version':")
    if "'organization':" in output:
        output = output.replace("'organization':", "\n\t 'organization':")
    if "'proxy':" in output:
        output = output.replace("'proxy':", "\n\t 'proxy':")
    if "'cognitive_services_endpoint':" in output:
        output = output.replace("'cognitive_services_endpoint':", "\n\t 'cognitive_services_endpoint':")
    if "'deployment_name':" in output:
        output = output.replace("'deployment_name':", "\n\t 'deployment_name':")
    if "'model_supports_json':" in output:
        output = output.replace("'model_supports_json':", "\n\t 'model_supports_json':")
    if "'tokens_per_minute':" in output:
        output = output.replace("'tokens_per_minute':", "\n\t 'tokens_per_minute':")
    if "'requests_per_minute':" in output:
        output = output.replace("'requests_per_minute':", "\n\t 'requests_per_minute':")
    if "'max_retries':" in output:
        output = output.replace("'max_retries':", "\n\t 'max_retries':")
    if "'max_retry_wait':" in output:
        output = output.replace("'max_retry_wait':", "\n\t 'max_retry_wait':")
    if "'sleep_on_rate_limit_recommendation':" in output:
        output = output.replace("'sleep_on_rate_limit_recommendation':", "\n\t 'sleep_on_rate_limit_recommendation':")
    if "'concurrent_requests':" in output:
        output = output.replace("'concurrent_requests':", "\n\t 'concurrent_requests':")
            

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

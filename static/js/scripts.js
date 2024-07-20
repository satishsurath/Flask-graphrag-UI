document.getElementById('form').onsubmit = function(event) {
    event.preventDefault();
    const root = document.getElementById('root').value || './ragtest';
    const method = document.getElementById('method').value || 'global';
    const question = document.getElementById('question').value;

    fetch('/run', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ root: root, method: method, question: question })
    })
    .then(response => response.json())
    .then(data => {
        const taskId = data.task_id;
        checkResult(taskId);
    });
};

function checkResult(taskId) {
    fetch('/result/' + taskId)
        .then(response => response.json())
        .then(data => {
            if (data.output === 'Processing') {
                setTimeout(() => checkResult(taskId), 1000);
            } else {
                document.getElementById('output').innerText = data.output;
            }
        });
}

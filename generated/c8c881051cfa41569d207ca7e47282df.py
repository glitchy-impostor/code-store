
from flask import Flask, request, jsonify
from celery import Celery

app = Flask(__name__)

# Configure Celery
app.config['CELERY_BROKER_URL'] = 'redis://localhost:6379/0'
app.config['CELERY_RESULT_BACKEND'] = 'redis://localhost:6379/0'

celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)

@celery.task
def execute_and_save_graph(code):
    # Execute JIRA code (this is a placeholder)
    result = requests.post('https://example.com/api/jira', data={'code': code})
    
    if result.status_code == 200:
        data = result.json()
        
        # Produce and save graph
        import networkx as nx
        import matplotlib.pyplot as plt
        
        G = nx.Graph()
        for node in data['nodes']:
            G.add_node(node)
        for edge in data['edges']:
            G.add_edge(edge[0], edge[1])
        
        plt.figure(figsize=(12, 8))
        nx.draw(G, with_labels=True, font_weight='bold')
        plt.savefig('graph.png')
    else:
        print(f"Failed to execute JIRA code: {result.status_code}")

@app.route('/execute', methods=['POST'])
def execute():
    data = request.get_json()
    if 'code' not in data:
        return jsonify({'error': 'Missing code parameter'}), 400
    
    execute_and_save_graph.delay(data['code'])
    return jsonify({'message': 'Task queued successfully'}), 202

if __name__ == '__main__':
    app.run(debug=True)

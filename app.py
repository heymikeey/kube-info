from flask import Flask
import os

app = Flask(__name__)

@app.route('/kubeinfo')
def index():
    pod_name = os.getenv('POD_NAME', 'Unknown')
    node_name = os.getenv('NODE_NAME', 'Unknown')
    namespace = os.getenv('NAMESPACE', 'Unknown')
    pod_ip = os.getenv('POD_IP', 'Unknown')
    cluster_name = os.getenv('CLUSTER_NAME', 'Unknown')

    return f"""
    <html>
        <head>
            <title>K8s Info</title>
            <style>
                body {{
                    height: 100%;
                    margin: 0;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    flex-direction: column; /* Aligns content vertically */
                    font-family: Arial, sans-serif;
                }}
                h1, h2, h3, h4 {{
                    font-size: 2.5em;
                    margin-bottom: 20px;
                }}
                h2, h3, h4 {{
                    font-size: 1.2em;
                    color: #555;
                }}
            </style>
        </head>
        <body>
                <h1>Kubernetes Pod Info</h1>
                <p><strong>Pod Name:</strong> {pod_name}</p>
                <p><strong>Node Name:</strong> {node_name}</p>
                <p><strong>Namespace:</strong> {namespace}</p>
                <p><strong>Pod IP:</strong> {pod_ip}</p>
                <p><strong>Cluster Name:</strong> {cluster_name}</p>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

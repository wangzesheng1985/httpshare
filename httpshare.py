from flask import Flask, render_template, send_from_directory
import socket
import os

app = Flask(__name__)

shared_folder = "../"

@app.route('/')
def index():
    files = os.listdir(shared_folder)
    return render_template('index.html', files=files)

@app.route('/download/<path:filename>')
def download(filename):
    return send_from_directory(shared_folder, filename, as_attachment=False)

if __name__ == "__main__":
    # 获取本机 IP 地址
    host_ip = socket.gethostbyname(socket.gethostname())

    # 设置监听地址为 0.0.0.0，允许外部访问
    app.run(host='0.0.0.0', port=5000, debug=True)

    # 打印访问链接
    print(f"Server is running at: http://{host_ip}:5000/")

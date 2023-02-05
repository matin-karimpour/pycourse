from flask import Flask, send_file, render_template
app = Flask(__name__,static_folder="statics")
	
@app.route('/')
def upload_form():
	return render_template('download.html')

@app.route('/download/python')
def download_python():
	path = "apps_for_windows/python-3.10.9-amd64.exe"
	return send_file(path, as_attachment=True)

@app.route('/download/vscode')
def download_vscode():
	path = "apps_for_windows/VSCodeUserSetup-x64-1.74.3.exe"
	return send_file(path, as_attachment=True)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
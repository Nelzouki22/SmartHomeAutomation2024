from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

# محاكاة حالة الأجهزة (مثال: الإضاءة، التكييف، المروحة)
devices = {
    "light": False,
    "ac": False,
    "fan": False
}

# عرض واجهة المستخدم
@app.route('/')
def index():
    return render_template('index.html')

# API: عرض حالة الجهاز
@app.route('/device/<device_name>', methods=['GET'])
def get_device_status(device_name):
    status = devices.get(device_name)
    if status is not None:
        return jsonify({device_name: status}), 200
    return jsonify({"error": "Device not found"}), 404

# API: تغيير حالة الجهاز (تشغيل/إطفاء)
@app.route('/device/<device_name>', methods=['POST'])
def control_device(device_name):
    if device_name in devices:
        # تغيير حالة الجهاز (تشغيل/إطفاء)
        devices[device_name] = not devices[device_name]
        return jsonify({device_name: devices[device_name]}), 200
    return jsonify({"error": "Device not found"}), 404

# تشغيل تطبيق Flask
if __name__ == '__main__':
    app.run(debug=True)

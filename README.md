# Smart Home Automation System

This project is a **Smart Home Automation System** built using **Python** and **Flask API**. It allows controlling and monitoring the status of smart devices such as lights, air conditioners, and fans through a simple web interface using **HTML** and **JavaScript**.

## Features

- Control smart devices (light, AC, fan) via a web interface.
- Monitor the status of devices (on/off) in real-time.
- Easy-to-use API built with Flask.
- Frontend built using HTML and JavaScript for interactivity.

## Installation

To set up and run the project locally, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/smart-home-automation.git
   cd smart-home-automation
Install the required dependencies: Make sure you have Python installed. Then install Flask using pip:
pip install Flask
Run the Flask server
python app.py
Access the web interface: Open your browser and visit http://localhost:5000 to control the devices.

API Endpoints
Here are the API endpoints available in this project:

Get device status: GET /device/<device_name>
Example: /device/light will return the current status of the light.
Toggle device state: POST /device/<device_name>
Example: /device/light will toggle the light (on/off)
Project Structure
smart-home-automation/
│
├── app.py                # Main Flask application
├── templates/
│   └── index.html        # Frontend HTML page
└── README.md             # Project documentation
Usage
View device status: The web interface displays the current status (on/off) of the light, AC, and fan.
Control devices: Click the toggle button for each device to change its state (on/off).
Future Improvements
Integrate with real IoT devices using MQTT protocol.
Add more smart devices to the system.
Improve UI/UX with CSS frameworks like Bootstrap.
Screenshots
<!-- Add a real screenshot link here -->

Contributing
Feel free to submit issues or pull requests. Contributions are welcome!

License
This project is licensed under the MIT License - see the LICENSE file for details.

### خطوات لتحسين `README.md`:

1. **لقطة شاشة**: إذا كنت تريد إضافة لقطة شاشة للمشروع، يمكنك التقاط صورة للشاشة من واجهة الويب الخاصة بالمشروع ثم رفعها إلى GitHub أو أي خدمة تخزين صور أخرى، واستبدال الرابط في قسم "Screenshots" بالرابط الصحيح.

2. **إضافة رابط المستودع**: تأكد من تغيير رابط المستودع في قسم **clone** (`git clone https://github.com/your-username/smart-home-automation.git`) برابط مستودعك الخاص على GitHub.

3. **LICENSE**: إذا كنت ترغب في إضافة رخصة، تأكد من تعديل قسم **License** وفقًا للرخصة التي تستخدمها (مثل MIT أو غيرها).

### رفع `README.md` إلى GitHub:

1. احفظ النص في ملف باسم `README.md` في الجذر الرئيسي للمشروع.
2. قم برفع الملف إلى المستودع الخاص بك باستخدام أوامر Git:
   ```bash
   git add README.md
   git commit -m "Add project README"
   git push origin main


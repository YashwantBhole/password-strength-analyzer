# 🔐 Password Strength Analyzer

A beginner-friendly cybersecurity web application that analyzes the strength of a password, provides real-time feedback, suggests a secure random password, and even allows you to download the suggested password as a styled .html file with cybersecurity tips. 

Built with **Python (Flask)**, **HTML/CSS**, and **JavaScript** for a clean, interactive interface.  

---

## 🌟 Features

- ✅ Checks password for:
  - Minimum 8 characters  
  - At least one uppercase letter  
  - At least one lowercase letter  
  - At least one number  
  - Special characters  

- ✅ Provides **Weak / Medium / Strong** feedback  
- ✅ Automatically hides results after **5 seconds**  
- ✅ **Suggest Strong Password button** to generate a random secure password  
- ✅ **Download Suggested Password** as a styled .html file with tips & GitHub credit
- ✅ Fully responsive and **professional UI**  

---

## 🖥️ Demo Screenshots

**1️⃣ Password Strength Weak**  
![Weak Password Screenshot](screenshots/weak_password.png)

**2️⃣ Strong Password Suggestion**  
![Password Suggestion Screenshot](screenshots/suggestion.png)

**3️⃣ Password Strength Strong**  
![Strong Password Screenshot](screenshots/strong_password.png)

**4️⃣ Suggested HTML file**  
![Suggested HTML File Screenshot](screenshots/suggestedHTML.png)

---

## 🛠️ Technologies Used

- **Backend:** Python, Flask  
- **Frontend:** HTML5, CSS3, JavaScript  
- **Libraries:** `re` (regex for password validation), `secrets` & `string` (for password generation)  
- **Optional Styling:** TailwindCSS / Bootstrap  

---

## ⚙️ How It Works

1. User enters a password in the input field.  
2. Flask backend validates password against multiple criteria.  
3. Returns a result message: **Weak / Medium / Strong**.  
4. JavaScript automatically hides the message after **5 seconds**.  
5. User can click **“Suggest Strong Password”** to instantly generate a random secure password.  

---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/your-username/password-strength-analyzer.git
cd password-strength-analyzer

2. Install dependencies
pip install flask

3. Run the application
python app.py

4. Open in browser

Visit http://127.0.0.1:5000

📝 Project Structure
password-strength-analyzer/
│── app.py
│── static/
│   └── style.css
│── templates/
│   └── index.html
│── requirements.txt
│── README.md
│── screenshots/  # Optional: Add demo images here

💡 Potential Enhancements

Real-time password strength meter while typing

Integration with HaveIBeenPwned API to check if a password was leaked

Password hashing demonstration (SHA256 / bcrypt)

Deploy on Heroku / Render / Railway for a live demo

🎯 Why Showcase This Project?

Demonstrates cybersecurity awareness in password policies

Shows Flask backend skills + frontend integration

Features a Strong Password Generator, making it more practical

Beginner-friendly, but scalable for advanced features


## 👨‍💻 Connect with Me  

<p align="left">
  <a href="https://www.linkedin.com/in/yashwantbhole/" target="_blank">
    <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn" />
  </a>
  <a href="https://github.com/YashwantBhole" target="_blank">
    <img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub" />
  </a>
</p>

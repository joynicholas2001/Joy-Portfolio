from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    profile = {
        'name': 'Mangalapudi Joy Nicholas',
        'email': 'itzjoynicholas@gmail.com',
        'phone': '9963416422,7358484266',
        'linkedin': 'https://www.linkedin.com/in/mangalapudi-joy-nicholas-020a2b224/',
        'address': "Harsha's Elite Apartment, Flat No I-2, Pathuru Cross Road, Kunchanapalli, Vijayawada, India",
        'dob': '06/09/2001',
        'gender': 'Male',
        'summary': 'Experienced Full Stack Developer and Graphic Designer with a strong background in Python, Flask, MySQL, AWS, and frontend technologies. Skilled in developing scalable web applications and digital marketing solutions.',
        'education': [
            {'period': '12/2020 – 11/2024', 'degree': 'Bachelor of Engineering','college': 'Panimalar Institute of Technology','location': 'Chennai', 'cgpa': '5.84'},
            {'period': '03/2018 – 03/2020', 'degree': 'Intermediate', 'school': 'Sri Chaitanya Educational Institutions, Vijayawada', 'cgpa': '5.67'},
            {'period': '03/2016 – 05/2017', 'degree': 'SSC', 'school': 'Sri Chaitanya Educational Institutions, Mangalagiri'}
        ],
        'skills': [
            'Python Full Stack Development',
            'Front-end: HTML, CSS, JavaScript',
            'Back-end: Flask, MySQL',
            'Debugging and problem solving',
            'Effective communication and presentation',
            'Graphic Designing'
        ],
        'certificates': [
            {
                'title': 'Technical Associate at 4SIGHT AI',
                'details': 'Worked on AP POLICE National Hackathon and Digital Marketing for AP Government.',
                'link': 'https://drive.google.com/file/d/18MJEUQjiosZ6n5r6FUWZfuenlaahL-B4/view?usp=sharing'
            },
            {
                'title': 'Python Full Stack Developer',
                'details': 'Trained in Python, MySQL, Flask, HTML, CSS, JavaScript, AWS. Developed an E-Commerce Web Application using Flask.',
                'link': 'https://drive.google.com/file/d/1Euevqo3BT5kAQVl6rW7jsimbYa_QPOwU/view?usp=sharing'
            }
        ],
        'languages': ['English', 'Telugu', 'Tamil'],
        'interests': ['Graphic Designing', 'Creating Videos on Social Media']
    }
    return render_template('index.html', profile=profile)

if __name__ == '__main__':
    app.run(debug=True)
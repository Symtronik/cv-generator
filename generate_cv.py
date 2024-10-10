from fpdf import FPDF
from PIL import Image

class PDF(FPDF):
    def __init__(self):
        super().__init__()
        self.line_width=0.2
        self.x_content = 70
        self.line_color = 150, 150, 150
        self.background_title = 227, 227, 227
        self.background_column = 227, 227, 227
        self.font_content = 'DejaVu'
        self.font_name_title = 'Courier'
        self.font_size_title = 12
        self.font_title = 'Times'
        self.add_font('DejaVu', '', 'DejaVuSans.ttf')
        self.add_font('DejaVu', 'B', 'DejaVuSans-Bold.ttf')
    def add_line(self):
        self.set_line_width(self.line_width)
        self.set_draw_color(self.line_color)
        self.line(self.x_content, self.get_y() + 2, 210, self.get_y() + 2)
    def add_title(self, name, title):
        self.set_xy(62, 10)
        self.set_fill_color(self.background_title)
        self.rect(62, 15, 148, 30, 'F')
        self.set_xy(self.x_content, 25)
        self.set_font(self.font_name_title, 'B', 30)
        self.cell(0, 0, name, 0, new_x='LMARGIN', new_y='NEXT', align='L')

        self.set_xy(self.x_content, self.get_y()+10)
        self.set_font(self.font_title, '', 15)
        self.cell(0, 0, title, 0, new_x='LMARGIN', new_y='NEXT', align='L')



    def left_column(self):
        self.set_fill_color(self.background_column)
        self.rect(0, 0, 62, 297, 'F')

    def add_photo(self, photo_path, x, y, height):

        with Image.open(photo_path) as img:
            original_width, original_height = img.size

        new_width = (original_width / original_height) * height
        self.image(photo_path, x, y, new_width, height)

    def add_contact_info(self):
        contacts = {
            "Email": [
                "m.kobialka@ezze.pl"
            ],
            "Phone": [
                "+48 882 137 202"
            ],
            "Location": [
                "Radom, Poland"
            ]
        }
        self.set_xy(10, 60)
        self.set_font(self.font_title, 'B', 12)
        self.cell(40, 10, 'Contact Information:', new_x='LMARGIN', new_y='NEXT')

        self.set_font(self.font_content, '', 10)
        for title, contact in contacts.items():
            for contact_detail in contact:
                self.cell(40, 5, f"{title}: {contact_detail}", new_x='LMARGIN', new_y='NEXT')


    def add_skills(self):
        self.set_xy(10, self.get_y() + 5)
        self.set_font(self.font_title, 'B', 12)
        self.cell(40, 10, 'Skills:', new_x='LMARGIN', new_y='NEXT')



        skills = {
            "Python": [
                "FastAPI",
                "Django",
                "Matplotlib",
                "NumPy",
                "Rest Api Django",
                "Selenium"
            ],
            "PHP8": [
                "Laravel",
                "Zend"
            ],
            "JavaScript": [
                "Vue.js"
            ],
            "CSS": [
                "Tailwind CSS",
                "Bootstrap"
            ],
            "Database": [
                "MySQL",
                "PostgreSQL"
            ],
            "Git": [
                "GitHub",
                "Bitbucket"
            ],
            "Other": [
                "HTML5",
                "WordPress",
                "Docker",
                "Linux",
                "Postman"
            ]
        }

        for category, skill_list in skills.items():
            self.set_font(self.font_content, 'B', 10)
            self.cell(40, 6, category, new_x='LMARGIN', new_y='NEXT')
            self.set_font(self.font_content, '', 10)
            for skill in skill_list:
                self.set_x(15)
                self.cell(40, 5, f"• {skill}", new_x='LMARGIN', new_y='NEXT')

    def education(self):
        self.set_xy(self.x_content, self.get_y() + 5)
        self.set_font(self.font_title, 'B', 12)
        self.cell(self.x_content, 5, 'EDUCATION:', new_x='LMARGIN', new_y='NEXT')
        self.add_line()
        self.set_font(self.font_content, 'B', 10)
        self.set_xy(self.x_content, self.get_y() + 5)
        self.cell(200, 5, 'Radom School of Economics', new_x='LMARGIN', new_y='NEXT')
        self.set_font(self.font_content, '', 10)
        self.set_xy(self.x_content, self.get_y() + 5)
        self.cell(200, 0, 'Degree: Engineer in Computer Science', new_x='LMARGIN', new_y='NEXT')
        self.set_xy(self.x_content, self.get_y() + 5)
        self.cell(200, 0, 'Specialization: Software Development', new_x='LMARGIN', new_y='NEXT')

    def section_content_title(self, title):
        self.set_xy(self.x_content, self.get_y() + 10)
        self.set_font(self.font_title, 'B', self.font_size_title)
        self.cell(self.x_content, 5, title, new_x='LMARGIN', new_y='NEXT')
        self.add_line()
    def section_content(self, title, content, content_type):
        self.section_content_title(title)

        self.set_font(self.font_content, '', 10)
        if content_type == 'list':
            for language, level in content.items():  # Użycie key, value dla języka i poziomu
                self.set_xy(self.x_content, self.get_y() + 5)
                self.multi_cell(130, 0, f"{language}: {level}", new_x='LMARGIN', new_y='NEXT')
        elif content_type == 'dict':
            for role, details in content.items():
                self.set_xy(self.x_content, self.get_y() + 5)
                self.set_font(self.font_content, 'B', 12)

                if self.get_y() + 10 > self.page_break_trigger:
                    self.add_page()

                self.cell(0, 5, role, new_x='LMARGIN', new_y='NEXT')

                self.set_xy(self.x_content, self.get_y())
                self.set_font(self.font_content, '', 10)
                self.cell(0, 5, f"{details['Company']} - {details['Dates']}", new_x='LMARGIN', new_y='NEXT')

                self.set_font(self.font_content, '', 10)
                for task in details['Responsibilities']:
                    self.set_x(self.x_content + 5)
                    self.cell(0, 6, f"• {task}", new_x='LMARGIN', new_y='NEXT')
        else:
            self.set_xy(self.x_content, self.get_y() + 5)
            self.multi_cell(130, 5, content, new_x='LMARGIN', new_y='NEXT')



data = {
    "title": {
        "name": "Michal Kobialka",
        "subtitle": "Python Developer"
    },
    "contact_info": {
        "Email": "m.kobialka@ezze.pl",
        "Phone": "+48 882 137 202",
        "Location": "Radom, Poland"
    },
    "skills": {
        "Python": ["FastAPI", "Django", "Matplotlib", "NumPy", "Rest Api Django", "Selenium"],
        "PHP8": ["Laravel", "Zend"],
        "JavaScript": ["Vue.js"],
        "CSS": ["Tailwind CSS", "Bootstrap"],
        "Database": ["MySQL", "PostgreSQL"],
        "Git": ["GitHub", "Bitbucket"],
        "Other": ["HTML5", "WordPress", "Docker", "Linux", "Postman"]
    },
    "education": {
        "Degree": "Engineer in Computer Science",
        "School": "Radom School of Economics",
        "Specialization": "Software Development"
    },
    "experience": {
        "section_title": "EXPERIENCE",
        "company":{
            "Freelance Web Developer": {
                "Company": "Freelancer",
                "Dates": "March 2024 - Present",
                "Responsibilities": [
                    "Developing custom web applications",
                    "Working with FastApi and Vue.js",
                    "Managing a parking management system"
                ]
            }
        },
    },
    "languages": {
        "section_title": "LANGUAGES",
        "language": {
            "English": "B2",
            "Polish": "native"
        }

    },
    "interests": {
        "section_title": "INTERESTS",
        "content": "In my free time, I enjoy woodworking, creating custom furniture, and fixing technical devices. I am also passionate about traveling and hiking in the mountains."
    }
}



pdf = PDF()
pdf.add_page()
pdf.add_title(data["title"]["name"], data["title"]["subtitle"])


pdf.section_content(data["experience"]["section_title"], data["experience"]['company'], content_type="dict")
pdf.education()
pdf.section_content(data["languages"]["section_title"], data["languages"]["language"], content_type="list")
pdf.section_content(data["interests"]["section_title"], data["interests"]["content"], content_type="text")
pdf.left_column()
pdf.add_photo('photo.jpeg', 10, 2, 55)
pdf.add_contact_info()
pdf.add_skills()

pdf.output('Michal_Kobialka.pdf')




from flask import request, jsonify
from flask_restful import Resource
from middleware import checkAuth


class ResumeInfo(Resource):
    path = '/resume'

    data = {
        "name":
        "Erik Dietrich",
        "contactDetails": [
            {
                "label": "email",
                "info": "erik@edietrich.com",
            },
            {
                "label": "phone",
                "info": "(724) 799-4475",
            },
            {
                "label": "location",
                "info": "Portland, ME & Remote",
            },
        ],
        "educationList": [
            {
                "institution": {
                    "name": "Virginia Tech",
                    "location": "Blacksburg, VA",
                },
                "graduationYear": 2018,
                "degree": "Bachelor of Science",
                "majors": ["Industrial and Systems Engineering"],
                "minors": ["Economics"],
                "distinction": "Magna Cum Laude",
            },
        ],
        "links": [
            {
                "title": "LinkedIn",
                "tooltip": "My LinkedIn page",
                "url": "https://www.linkedin.com/in/erik-dietrich-000506134/",
            },
            {
                "title": "GitHub",
                "tooltip": "My GitHub profile - including this repo",
                "url": "https://github.com/erikd7",
            },
            {
                "title": "Docker",
                "tooltip": "My Docker profile",
                "url": "https://hub.docker.com/u/normalone7",
            },
        ],
        "skillsCore": [
            {
                "name": "JavaScript",
                "details": "3 years professional experience",
                "level": 3,
            },
            {
                "name": "TypeScript",
                "details": "2 years professional experience",
                "level": 2,
            },
            {
                "name": "Vue.js",
                "details":
                "2 years professional experience and independent work",
                "level": 3,
            },
            {
                "name": "React.js",
                "details": "2 years professional experience",
                "level": 2,
            },
            {
                "name": "Node.js",
                "details": "3 years professional experience",
                "level": 2,
            },
            {
                "name": "SQL (Sequel Server & Postgres)",
                "details": "6 years university and professional experience",
                "level": 3,
            },
            {
                "name": "MongoDB",
                "details": "1 year professional experience",
                "level": 2,
            },
            {
                "name": "HTML & CSS",
                "details": "3 years professional experience",
                "level": 3,
            },
            {
                "name": "Docker",
                "details":
                "2 years professional experience and independent work",
            },
            {
                "name": "AWS",
                "details": "2 years professional experience including S3, EC2, RDS, Lambda, API Gateway",
            },
            {
                "name": "Python",
                "details": "2 years university and independent work",
                "level": 2,
            },
            {
                "name": "Java",
                "details": "2 years university and independent work  ",
                "level": 2,
            },
            {
                "name": "Git",
                "details":
                "4 years professional experience and independent work  ",
                "level": 3,
            },
        ],
        "skillsAdditional": [
            {
                "name": "Axios.js",
                "details":
                "3 years professional experience and independent work",
                "level": 2
            },
            {
                "name": "Express.js",
                "details":
                "2 years professional experience and independent work",
                "level": 2
            },
            {
                "name": "Passport.js",
                "details": "1 year professional experience and independent work",
                "level": 2
            },
             {
                "name": "Socket.io",
                "details": "1 year professional experience and independent work",
                "level": 2
            },
            {
                "name": "Jest",
                "details": "1 year professional experience",
                "level": 2,
            },
            {
                "name": "npm",
                "details": "3 years professional experience",
                "level": 3
            },
            {
                "name": "CI/CD",
                "details": "3 years professional experience",
                "level": 2
            },
            {
                "name": "Flask",
                "details": "1 year independent work",
                "level": 2
            },
            {
                "name": "pip",
                "details": "1 year independent work",
                "level": 2
            },
            {
                "name": "Bootstrap",
                "details": "1 year professional experience",
                "level": 2,
            },
            {
                "name": "Tailwind",
                "details":
                "2 years professional experience and independent work",
                "level": 2,
            },
            {
                "name": "R",
                "details": "1 year university study",
                "level": 1,
            },
            {
                "name": "C#",
                "details": "1 year professional experience",
                "level": 1,
            },
            {
                "name": "JSON & JWT",
                "details":
                "4 years professional experience and independent work",
                "level": 3,
            },
            {
                "name": "Kubernetes",
                "details": "1 year professional experience",
            },
            {
                "name": "Visual Studio Pro",
                "details":
                "3 years professional experience and independent work",
            },
            {
                "name": "VS Code",
                "details":
                "3 years professional experience and independent work",
            },
            {
                "name": "Postman",
                "details":
                "2 years professional experience and independent work",
            },
            {
                "name": "MS Office Suite",
                "details":
                "5 years professional experience and independent work",
            },
            {
                "name": "GitHub",
                "details": "2 years independent work",
            },
            {
                "name": "GitLab",
                "details":
                "3 years professional experience and independent work",
            },
        ],
        "skillsNonTech": [
            {
                "name": "Agile (Scaled Agile Framework)",
                "details": "1 year professional experience"
            },
            {
                "name": "Waterfall",
                "details": "1 year professional experience"
            },
            {
                "name": "Scrum (Scrum Master)",
                "details": "1 year professional experience as Scrum Master"
            },
            {
                "name": "Lean Methodology and Principles",
                "details":
                "3 years university study and professional experience"
            },
            {
                "name": "Full Stack Design",
            },
            {
                "name": "UI/UX and Accessibility",
            },
            {
                "name": "Meeting Facilitation",
            },
            {
                "name": "Presentations",
            },
        ],
        "experienceList": [
            {
                "organization": "Northwestern Mutual",
                "location": "Remote",
                "title": "Senior Software Engineer",
                "start": "2021",
                "description": [
                    'Created wire transfer app that processed over $68 billion in transactions in 2023',
                    'Supported and enhanced bank services app that manages over 5.5 million bank accounts',
                    'Successfully led wire transfer application through multiple internal and external audits required for top-tier applications',
                    'Reduced lead time for change by transforming legacy pipelines into zero-touch CI/CD pipeline',
                    'As a senior engineer and embedded Scrum Master, led Agile team in all aspects of SDLC, including design, train-wide planning, coding, automated unit and regression testing, and ongoing support',
                    'Hired as Level 2 (Associate) engineer and promoted to Level 4 (Senior) engineer'
                ],
                "coreStack": ['PostgreSQL', 'Node', 'React', 'Docker', 'Kube', 'AWS']
            },
            {
                "organization": "Tindoori Labs",
                "location": "Remote and Pittsburgh, PA",
                "title": "Lead Backend Engineer",
                "start": "2022",
                "end": "2023",
                "description": [
                    'Designed, developed, and tested a language learning and matchmaking app',
                    'Deployed Production environment on AWS and integrated with iOS frontend'
                ],
                "coreStack": ['PostgreSQL', 'MongoDB', 'Node', 'Docker', 'Kube', 'AWS']
            },
            {
                "organization": "Epic",
                "location": "Madison, WI",
                "title": "Software Engineer and Project Manager",
                "start": "2018",
                "end": "2021",
                "description": [
                    'Led design, development, and testing as Module Lead of Epic’s web app for managing customer installs, with over 10,000 internal and external users',
                    "Managed 20-member subteam in Epic's then-biggest electronic health record install",
                    "Member of Epic’s Infection Control Product Leads team during the COVID-19 response. Designed and built Epic’s COVID-19 dashboard, used by all live organizations starting March 2020."
                ],
                "coreStack": ['SQL Server', 'C#', 'Vue', 'Epic Hosting']
            },
        ],
    }

    def get(self):
        authResponse = checkAuth(request)
        if (not authResponse['ok']):
            return authResponse, 401
        response = jsonify(self.data)

        response.headers.add('Access-Control-Allow-Origin', '*')
        return response

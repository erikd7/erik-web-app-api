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
                "info": "Madison, WI & Remote",
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
                "url": "https://github.com/normalone7",
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
                "organization": "Tindoori Labs",
                "location": "Remote and Pittsburgh, PA",
                "title": "Lead Backend Engineer",
                "start": "2022",
                "description": "Full stack engineer responsible for designing, writing, testing, and supporting code for NM’s Enterprise Payments Network. Primary focus on apps for insurance payouts to clients and home office management of wire transfers. Stack includes PostgreSQL, Node.js, and React.js running in AWS with Kubernetes. Also led the team’s planning and allocation as Agile Scrum Master."
            },
            {
                "organization": "Northwestern Mutual",
                "location": "Remote and Milwaukee, WI",
                "title": "Software Engineer II",
                "start": "2021",
                "description": "Full stack engineer responsible for designing, writing, testing, and supporting code for NM’s Enterprise Payments Network. Primary focus on apps for insurance payouts to clients and home office management of wire transfers. Stack includes PostgreSQL, Node.js, and React.js running in AWS with Kubernetes. Also led the team’s planning and allocation as Agile Scrum Master."
            },
            {
                "organization": "Epic",
                "location": "Madison, WI",
                "title": "Software Engineer and Project Manager",
                "start": "2018",
                "end": "2021",
                "description": "Hired as an Implementation Engineer responsible for leading a 20-member team and installing Epic’s large software suite for healthcare organizations. Member of Epic’s Infection Control Product Leads team during the COVID-19 response. Took on additional responsibilities and then shifted to full-time development, where I led design and dev of a module of Epic’s web app for managing customer installs. Used SQL, C#, Vue.js, and HTML/CSS."
            },
            {
                "organization":
                "Wolverine Advanced Materials",
                "location":
                "Blacksburg, VA",
                "title":
                "Industrial Engineer",
                "start":
                "Summer 2017",
                "end":
                "Winter 2017",
                "description":
                "Used lean principles, data analysis, and simulation to implement a just-in-time model to decrease inventory while increasing manufacturing throughput."
            },
            {
                "organization":
                "Siemens-Sivantos Group",
                "location":
                "New Brunswick, NJ",
                "title":
                "Industrial Engineer",
                "startAndEnd":
                "Summer 2016",
                "description":
                "Led hearing aid battery failure analysis project, including experimental design, hardware testing, data acquisition and wrangling, analysis, and reporting to management."
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

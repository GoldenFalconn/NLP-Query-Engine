# NLP Query Engine for Employee Database

A natural language query system that allows users to query both structured employee data and unstructured documents using plain English.

## Features

- **Natural Language Processing**: Query databases using plain English instead of SQL
- **Dual Query Support**: 
  - Structured queries for employee database
  - Document search for policy handbooks and documentation
- **Automatic Schema Discovery**: Dynamically adapts to any employee database structure
- **Smart Query Classification**: Automatically routes queries to appropriate data source
- **Document Upload**: Support for PDF, DOCX, and TXT files
- **Query Caching**: In-memory caching for improved performance
- **Real-time Results**: Interactive web interface with instant feedback
- **Responsive Design**: Works on desktop and mobile devices

##  Technologies Used

### Backend
- **FastAPI**: Modern Python web framework
- **SQLAlchemy**: Database ORM and query generation
- **Sentence Transformers**: Document embeddings for semantic search
- **PyPDF2 & python-docx**: Document parsing

### Frontend
- **React**: Component-based UI
- **Axios**: HTTP client
- **Modern CSS**: Responsive design

## Prerequisites

- Python 3.11+
- Node.js 18+
- npm or yarn

## Setup Instructions

### 1. Clone the Repository


### 2. Backend Setup

Create virtual environment
python -m venv venv

Activate virtual environment
Windows:
.\venv\Scripts\activate

Install dependencies
pip install -r requirements.txt


### 3. Frontend Setup

cd frontend
npm install
cd ..


### 4. Create Sample Database

python -c "import sqlite3; conn = sqlite3.connect('employee.db'); c = conn.cursor(); c.execute('CREATE TABLE employees (id INTEGER PRIMARY KEY, name TEXT, department TEXT, salary REAL, position TEXT, email TEXT)'); employees = [(1, 'John Doe', 'Engineering', 75000, 'Software Engineer', 'john@company.com'), (2, 'Jane Smith', 'Marketing', 65000, 'Marketing Manager', 'jane@company.com'), (3, 'Bob Johnson', 'Engineering', 85000, 'Senior Developer', 'bob@company.com'), (4, 'Alice Williams', 'HR', 60000, 'HR Specialist', 'alice@company.com'), (5, 'Charlie Brown', 'Sales', 70000, 'Sales Representative', 'charlie@company.com')]; c.executemany('INSERT INTO employees VALUES (?, ?, ?, ?, ?, ?)', employees); conn.commit(); conn.close(); print('Database created successfully!')"

### Start Backend Server

Make sure you're in project root with venv activated
uvicorn backend.api.main:app --reload --host 0.0.0.0 --port 8000

text

Backend will run on: http://localhost:8000

### Start Frontend Server

Open new terminal
cd frontend
npm start

text

Frontend will run on: http://localhost:3000

##  Usage


### 1. Connect to Database

1. Open http://localhost:3000
2. Enter connection string: `sqlite:///employee.db`
3. Click "Test Connection" then "Connect"

### 2. Query Examples

**Structured Database Queries:**
- "Count all employees"
- "List all departments"
- "Show employees with salary > 70000"
- "Find employees in Engineering"
- "Show all employee names"

**Document Queries:**
- "What is the leave policy?"
- "What are the work hours?"
- "Tell me about benefits"

### 3. Upload Documents

1. Click "Browse Files" or drag files
2. Upload PDF, DOCX, or TXT files
3. Query the documents using natural language

##  Project Structure

NLP_QUERY_ENGINE/
├── backend/
│ ├── api/
│ │ ├── models/ # Data models
│ │ ├── routes/ # API endpoints
│ │ └── services/ # Business logic
│ └── uploads/ # Uploaded documents
├── frontend/
│ ├── public/
│ └── src/
│ └── components/ # React components
├── employee.db # SQLite database
├── requirements.txt # Python dependencies
└── README.md

text

##  Configuration

### Backend Configuration
- Default port: 8000
- Cache TTL: 300 seconds (5 minutes)
- Max document size: 10MB

### Frontend Configuration
- Default port: 3000
- API base URL: http://localhost:8000

## Features in Detail

### Query Caching
- Automatically caches query results
- 5-minute TTL for optimal performance
- Reduces database load for repeated queries

### Smart Query Routing
- Document keywords: policy, handbook, benefits, leave, hours, etc.
- Database keywords: count, list, show, salary, department, etc.
- Automatic classification based on intent

### Schema Discovery
- Dynamically discovers database tables and columns
- Works with any employee database structure
- No hard-coded table names

## 📝 Assignment Requirements Completed

✅ Natural language query interface  
✅ Database schema discovery  
✅ Document upload and processing  
✅ Dual query support (structured + unstructured)  
✅ Query caching for performance  
✅ Responsive web interface  
✅ API documentation  

## 📄 License

This project is created for academic purposes as part of AI Engineering Assignment.
📄 2. Create sample_handbook.txt for Demo

EMPLOYEE HANDBOOK

Welcome to Our Company!

This handbook provides important information about company policies and procedures.

WORK HOURS AND SCHEDULE

Standard Work Hours: 9:00 AM to 6:00 PM, Monday through Friday
Lunch Break: 1 hour (flexible timing between 12 PM - 2 PM)
Total Weekly Hours: 40 hours

REMOTE WORK POLICY

Hybrid Work Model: Employees are required to work from office 3 days per week
Remote Work Days: Tuesday and Thursday can be remote (subject to manager approval)
Core Hours: All employees must be available 10 AM - 4 PM regardless of location

LEAVE POLICY

Annual Leave: 15 days per calendar year
Sick Leave: 10 days per calendar year
Casual Leave: 5 days per calendar year
Public Holidays: As per company calendar
Maternity Leave: 26 weeks paid leave
Paternity Leave: 2 weeks paid leave

EMPLOYEE BENEFITS

Health Insurance: Comprehensive medical insurance for employee and family
Dental Coverage: Annual dental checkup and treatment coverage
Life Insurance: Group life insurance (2x annual salary)
Gym Membership: Subsidized gym membership at partner facilities
Parking: Free parking for all employees at office premises
Meal Vouchers: Daily meal allowance of $15
Professional Development: Annual training budget of $2000 per employee

DRESS CODE

Business Casual: Standard dress code for office days
Casual Fridays: Jeans and casual wear allowed on Fridays
Client Meetings: Formal business attire required

PERFORMANCE REVIEWS

Annual Reviews: Conducted every December
Mid-Year Check-in: Progress review in June
Feedback Culture: Regular one-on-one meetings with managers

WORKPLACE CONDUCT

Professional Behavior: Maintain respectful and professional conduct
Harassment Policy: Zero tolerance for harassment or discrimination
Confidentiality: Protect company and client information
Ethics: Adhere to company code of ethics

TECHNOLOGY AND EQUIPMENT

Company Laptop: Provided to all employees
Software Licenses: Access to required professional tools
IT Support: Available during business hours

CONTACT INFORMATION

HR Department: hr@company.com | Ext: 1234
IT Support: itsupport@company.com | Ext: 5678
Facilities: facilities@company.com | Ext: 9012


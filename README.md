# SOLACED Jobs - Job Portal Application

A modern, responsive job portal built with Django, featuring a beautiful dark green theme with sage and creamy white accents.

## 🌟 Features

- **User Authentication**: Custom user model with email-based authentication
- **Job Management**: Browse, search, and apply for jobs
- **Responsive Design**: Beautiful glassmorphism UI with dark green theme
- **File Uploads**: Resume upload functionality for job applications
- **Admin Interface**: Admin panel for managing jobs and applications
- **Search Functionality**: Search jobs by title, description, or location

## 🎨 Design Theme

- **Primary Colors**: Black (`#0d0d0d`), Dark Green (`#1b2e1b`)
- **Accent Colors**: Sage Green (`#9caf88`), Success Green (`#4a7c59`)
- **Text Colors**: Creamy White (`#f8f6f0`)
- **UI Style**: Modern glassmorphism with backdrop blur effects

## 🚀 Tech Stack

- **Backend**: Django 5.2.5
- **Frontend**: Bootstrap 5.3.2, FontAwesome 6.4.0
- **Database**: SQLite (development)
- **Python**: 3.13.5

## 📋 Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- Virtual environment (recommended)

## 🛠️ Installation

1. **Clone the repository**
   ```bash
   git clone <your-repository-url>
   cd SOLACED_QUIZ3
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv .venv
   
   # On Windows
   .venv\Scripts\activate
   
   # On macOS/Linux
   source .venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install django==5.2.5
   pip install pillow  # For image handling
   ```

4. **Apply database migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create a superuser**
   ```bash
   python manage.py createsuperuser
   ```

6. **Collect static files**
   ```bash
   python manage.py collectstatic
   ```

7. **Run the development server**
   ```bash
   python manage.py runserver
   ```

8. **Access the application**
   - Main application: http://127.0.0.1:8000/
   - Admin panel: http://127.0.0.1:8000/admin/

## 📁 Project Structure

```
SOLACED_QUIZ3/
├── accounts/                 # User authentication app
│   ├── models.py            # Custom User model
│   ├── views.py             # Authentication views
│   ├── forms.py             # Registration forms
│   ├── urls.py              # Account URLs
│   └── templates/accounts/  # Authentication templates
├── jobs/                    # Job management app
│   ├── models.py            # Job and JobApplicant models
│   ├── views.py             # Job-related views
│   ├── forms.py             # Job application forms
│   ├── urls.py              # Job URLs
│   └── templates/jobs/      # Job templates
├── templates/               # Global templates
│   └── base.html           # Base template with theme
├── static/                 # Static files
├── media/                  # Media files (uploads)
├── SOLACED_QUIZ3/          # Project configuration
│   ├── settings.py         # Django settings
│   ├── urls.py             # Main URL configuration
│   └── wsgi.py             # WSGI configuration
├── manage.py               # Django management script
└── requirements.txt        # Python dependencies
```

## 🔧 Configuration

### Environment Variables
Create a `.env` file in the root directory (optional):
```env
DEBUG=True
SECRET_KEY=your-secret-key-here
```

### Settings Configuration
Key settings in `settings.py`:
- `AUTH_USER_MODEL = 'accounts.User'` - Custom user model
- `LOGIN_REDIRECT_URL = '/'` - Redirect to jobs after login
- `LOGOUT_REDIRECT_URL = '/'` - Redirect to jobs after logout

## 📱 Usage

### For Users
1. **Register**: Create an account with email, first name, and last name
2. **Browse Jobs**: View available job listings on the main page
3. **Search**: Use the search bar to find specific jobs
4. **Apply**: Click on job details and upload your resume to apply

### For Administrators
1. **Access Admin**: Go to `/admin/` and login with superuser credentials
2. **Manage Jobs**: Add, edit, or delete job postings
3. **View Applications**: See all job applications and resumes
4. **User Management**: Manage user accounts

## 🎯 Key Models

### User Model
- Email-based authentication
- First name and last name fields
- Custom user manager

### Job Model
- Job title and description
- Salary range (min/max offer)
- Location
- String representation

### JobApplicant Model
- Links users to jobs
- Resume file upload
- Application timestamp
- Foreign key relationships

## 🌐 URL Structure

```
/                          # Jobs list (main page)
/accounts/register/        # User registration
/accounts/login/           # User login
/accounts/logout/          # User logout
/accounts/profile/         # User profile
/<int:pk>/                 # Job detail view
/<int:pk>/apply/           # Job application
/<int:pk>/update/          # Job update (admin)
/<int:pk>/delete/          # Job delete (admin)
/admin/                    # Django admin panel
```

## 🚀 Deployment

### Development
The project is configured for development with:
- `DEBUG = True`
- SQLite database
- Local file storage

### Production Considerations
For production deployment:
1. Set `DEBUG = False`
2. Configure proper database (PostgreSQL recommended)
3. Set up cloud storage for media files
4. Configure proper ALLOWED_HOSTS
5. Use environment variables for sensitive data

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👥 Team

**SOLACED Team** - *Initial work*

## 📞 Support

For support and questions:
- Email: solaced@gmail.com
- Create an issue in the repository

## 🔄 Version History

- **v1.0.0** - Initial release
  - User authentication system
  - Job posting and application functionality
  - Modern UI with dark green theme
  - Admin interface for job management

## 🙏 Acknowledgments

- Django framework for robust backend functionality
- Bootstrap for responsive design components
- FontAwesome for beautiful icons
- Glassmorphism design inspiration

---

Made with ❤️ by SOLACED Team © 2025
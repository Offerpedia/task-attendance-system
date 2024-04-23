git@github.com:Offerpedia/task-attendance-system.git
# Django Attendance System

## Description
This project is a basic attendance system built using Django. It allows for the management of two types of users: administrators and employees. Administrators have the ability to add employees to the system, while employees can mark their attendance with a time in and time out, but only once per day. Employees can only view their own attendance records, while administrators have the ability to approve attendance records.

## Installation
1. Clone the repository: `Offerpedia/task-attendance-system.git`
2. Navigate to the project directory: `cd attendance`
3. Create a virtual environment (optional but recommended): `python3 -m venv venv`
4. Activate the virtual environment:
   - On Windows: `venv\Scripts\activate`
5. Install dependencies: `pip install -r req.txt`
6. Apply migrations: `python manage.py migrate`
7. Create a superuser (administrator): `python manage.py createsuperuser`
8. Start the development server: `python manage.py runserver`

## Usage
- Access the admin interface by navigating to `http://127.0.0.1:8000/admin/` and log in with the superuser credentials created in step 7.
- Add employees through the admin interface.
- Employees can log in to mark their attendance by navigating to `http://127.0.0.1:8000/markattendance`.
- Once logged in, employees can mark their attendance with a time in and time out, but only once per day.
- Administrators can approve attendance records through the admin interface.

## Contributing
If you'd like to contribute to this project, please fork the repository, make your changes, and submit a pull request.

## Credits
- This project was created by Aneena Ansar.
- Special thanks to the Django community for their excellent documentation and resources.

## Contact
For any inquiries or feedback, feel free to contact aneenaanzz123@gmail.com

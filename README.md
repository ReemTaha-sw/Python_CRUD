# User Management CRUD Operations

![Logo](https://img.shields.io/badge/Django-Project-brightgreen)

This project is a web-based application for managing users, offering full CRUD (Create, Read, Update, Delete) functionality. Built with Django and styled using Bootstrap, it provides a professional and responsive user interface, complete with custom icons and switches.

![tttt](https://github.com/user-attachments/assets/f5841032-70ab-45e8-bad1-4e664699f6e9)

## Features

- **📝 User Creation**: Add new users with a simple form interface.
- **👁️ User Retrieval**: View a list of all users, along with details of specific users.
- **✏️ User Update**: Edit user details directly from the user list.
- **🗑️ User Deletion**: Remove users with a confirmation modal to prevent accidental deletions.
- **🔄 Status Display**: Active status is shown as a switch (green for active, gray for inactive).

## Technologies Used

- **Backend**: Django (Python)
- **Frontend**: HTML5, CSS3, Bootstrap 4, Font Awesome
- **Database**: SQLite (default for Django projects)
- **Icons**: Font Awesome 6

## Setup and Installation

1. **Clone the Repository**
   ```bash
   git clone git@github.com:ReemTaha-sw/Python_CRUD.git
   cd Python_CRUD
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt

3. **Apply Migrations**
   ```bash
   python manage.py migrate

4. **Run the Development Server**
   ```bash
   python manage.py runserver
   
5. **Access the Application**
   Open your web browser and navigate to http://127.0.0.1:8000/users/.

## Usage

- **🏠 Home Page**: Displays the list of users with options to view, edit, or delete.
- **➕ Add New User**: Click on the "Add New User" button to create a new user.
- **✏️ Edit User**: Click on the edit icon next to a user to update their information.
- **🗑️ Delete User**: Click on the delete icon to remove a user after confirming the action.
- **🔄 Status Toggle**: The active status of users is displayed using a toggle switch.

## Customization

- **🎨 Styling**: The project uses Bootstrap for responsive design. Custom styles can be added in the `style` section of the HTML files.
- **🔧 Icons**: Font Awesome icons are used throughout the application. You can change or add icons by modifying the `fa-` classes.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).

# UANews Platform

## Overview

**UANews** is a platform that allows registered users to create, manage, and share news articles. The platform provides a simple interface for users to register, log in, and access their personal news dashboard. Users can create new articles, archive or delete them, and specify details such as an image, image link, headline, and main text. Each article is displayed on its own dedicated page, allowing users to view and interact with the content. Additionally, all users can view news articles created by others, fostering a sense of community and shared information.

### Key Features:

- **User Registration and Login**: Allows users to create accounts and securely log in to access their personal news dashboards.
- **Create News**: Users can create news articles by specifying a headline, main text, image, and image link.
- **Manage News**: Users have the ability to archive or delete their articles as needed.
- **View News**: All users can view articles created by others, providing a broad spectrum of content and perspectives.
- **Individual News Pages**: Each article has a dedicated page for a focused reading experience.

## How to Launch the Project and Test It

To launch the UANews platform on your local machine, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone http://github.com/your-username/your-repo-name
   cd your-repo-name
2. **Set Up and Initialize the Project**:
   - Run the `setup_project.sh` script to set up the environment, install dependencies, and prepare the database:
   ```bash
   chmod +x setup_project.sh 
   ./setup_project.sh
   ```

3. **Run the Project**:
   - Use the `run_project.sh` script to start the Django development server:
   ```bash
   chmod +x run_project.sh 
   ./run_project.sh
   ```

4. **Access the Platform**:
   - Open your web browser and navigate to `http://127.0.0.1:8000/` to access the UANews platform.

5. **Testing**:
   - Log in with the default superuser credentials created by the setup script (username: `admin`, password: `test`) or register a new user.
   - Create news articles, view them, and test all functionalities, including archiving and deleting articles.

## Background of UANews

I created the UANews project when I was in the 11th grade in 2022. The primary purpose of the project was to provide a platform for my school friends from Ukraine to post and share recent news, and more often, memes, in a more comprehensive and engaging way. It served as a creative outlet during challenging times, allowing us to stay connected and share our thoughts, humor, and perspectives through a simple yet effective digital platform.
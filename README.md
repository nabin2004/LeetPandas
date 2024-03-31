<h1 align='center'>LeetPandas</h1>

<img src="https://github.com/nabin2004/LeetPandas/assets/107109731/bd15bcc7-abfc-420f-9a70-59d80d2c9f77" alt="Image" width="1000" height="400">
LeetPandas is a data science platform similar to LeetCode, designed to provide challenges and exercises tailored specifically for data science enthusiasts. It offers a wide range of questions focusing on Python, NumPy, Pandas, Matplotlib, Seaborn, linear regression, probability, linear algebra, and SQL.

## Key Features

- **Categories**: Challenges are categorized into Python, NumPy, Pandas, Matplotlib & Seaborn, Linear Regression, Probability, Linear Algebra, and SQL.
- **Question Types**: Multiple choice questions (MCQs), True/False, Q&A, fill in the blanks, one-liners, and two-liners.
- **User Profile**: Users can track their progress and performance over time.
- **Explanation & Resources**: Detailed answers and supplementary materials provided for each question.
- **Community Interaction**: Discussion forums for collaboration and peer-to-peer learning.
- **Customizable Challenges**: Users can create, share, and participate in custom challenges.

## Objective

LeetPandas aims to facilitate learning, practice, and skill improvement in data science, catering to both beginners and experts.

## Database Schema

### Users
- `user_id` (Primary Key): Unique identifier for each user.
- `username`: User's chosen username.
- `email`: User's email address.
- `password_hash`: Hashed password for security.

### Questions
- `question_id` (Primary Key): Unique identifier for each question.
- `category`: Category of the question (Python, NumPy, Pandas, etc.).
- `question_text`: The text of the question.
- `question_type`: Type of question (MCQ, True/False, Q&A, etc.).
- `options`: For MCQs, a field to store multiple choice options.
- `correct_answer`: The correct answer to the question.
- `explanation`: Explanation of the correct answer.
- `difficulty_level`: Difficulty level of the question (e.g., Easy, Medium, Hard).

### User_Questions
- `user_id` (Foreign Key): References the user_id in the Users table.
- `question_id` (Foreign Key): References the question_id in the Questions table.
- `response`: User's response to the question.
- `timestamp`: Timestamp of when the question was answered.

### Challenges
- `challenge_id` (Primary Key): Unique identifier for each challenge.
- `creator_id` (Foreign Key): References the user_id of the user who created the challenge.
- `title`: Title of the challenge.
- `description`: Description of the challenge.
- `duration`: Duration of the challenge.

### Challenge_Questions
- `challenge_id` (Foreign Key): References the challenge_id in the Challenges table.
- `question_id` (Foreign Key): References the question_id in the Questions table.

### Forum_Posts
- `post_id` (Primary Key): Unique identifier for each forum post.
- `user_id` (Foreign Key): References the user_id of the user who posted.
- `title`: Title of the forum post.
- `content`: Content of the forum post.
- `timestamp`: Timestamp of when the post was created.

## Database Relationships

- Users have a one-to-many relationship with User_Questions.
- Questions have a many-to-many relationship with Users through User_Questions.
- Challenges have a one-to-many relationship with Challenge_Questions.
- Users have a one-to-many relationship with Challenges.

This schema forms the backbone of LeetPandas, providing the necessary infrastructure for storing user data, questions, responses, challenges, and forum posts. It can be further expanded and customized to meet specific requirements and future feature enhancements.


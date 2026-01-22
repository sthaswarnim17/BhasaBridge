-- Sample Data for BhasaBridge Application

-- Sample Users (passwords are hashed with bcrypt)
INSERT INTO users (name, email, password) VALUES
('John Doe', 'john@example.com', '$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewY5GyYIi.Q3A7sW'),
('Jane Smith', 'jane@example.com', '$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewY5GyYIi.Q3A7sW'),
('Test User', 'test@example.com', '$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewY5GyYIi.Q3A7sW');

-- Sample Lessons
INSERT INTO lessons (title, description, difficulty_level, content) VALUES
('Basic Greetings', 'Learn how to greet people in the target language', 'beginner', 'Hello, Good morning, Good evening, etc.'),
('Numbers 1-10', 'Learn to count from 1 to 10', 'beginner', 'One, Two, Three, Four, Five...'),
('Common Phrases', 'Essential phrases for daily conversation', 'intermediate', 'How are you? Thank you, Please, Excuse me'),
('Past Tense', 'Understanding and using past tense', 'intermediate', 'I went, I saw, I did...'),
('Advanced Grammar', 'Complex sentence structures', 'advanced', 'Conditional sentences, passive voice');

-- Sample Exercises
INSERT INTO exercises (lesson_id, question, answer, exercise_type, points) VALUES
(1, 'How do you say "Hello" in the target language?', 'Hello', 'translation', 10),
(1, 'What is the appropriate greeting in the morning?', 'Good morning', 'multiple_choice', 10),
(2, 'Write the number 5 in words', 'Five', 'fill_blank', 10),
(2, 'What comes after number 7?', 'Eight', 'multiple_choice', 10),
(3, 'How do you say "Thank you"?', 'Thank you', 'translation', 15);

-- Sample Progress
INSERT INTO user_progress (user_id, lesson_id, completed, score) VALUES
(1, 1, 1, 100),
(1, 2, 1, 90),
(2, 1, 1, 85),
(3, 1, 0, 0);

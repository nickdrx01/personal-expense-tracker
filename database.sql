INSERT INTO expenses
(amount, category, description, payment_method)
VALUES
(150.00, 'Food', 'Lunch', 'UPI'),
(150.12,'travaling','collage','cash');

SELECT * FROM expenses;
SELECT column_name, data_type
FROM information_schema.columns
WHERE table_name = 'expenses'
ORDER BY ordinal_position;
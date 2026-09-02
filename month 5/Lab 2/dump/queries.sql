-- 1 запрос
SELECT
       COUNT(DISTINCT students.id) AS "Количество студентов",
       courses.subject AS "Название курса",
       groups.group_name AS "Наименование группы"
FROM students
JOIN groups ON students.group_id = groups.id
JOIN curriculum curr ON students.group_id = curr.group_id
JOIN courses ON curr.course_id = courses.id
WHERE courses.id = 'course_id'
AND courses.start_date BETWEEN 'start_date' AND 'end_date'
GROUP BY courses.subject, groups.group_name
ORDER BY groups.group_name;
-- 2 запрос
SELECT DISTINCT
    courses.subject AS "Название курса",
    COUNT(students.id) AS "Количество выбывших студентов",
    groups.group_name AS "Наименование группы"
FROM students
RIGHT JOIN groups ON students.group_id = groups.id
JOIN curriculum curr ON groups.id = curr.group_id
JOIN courses  ON curr.course_id = courses.id
WHERE courses.id = 'course_id'
AND courses.start_date BETWEEN 'start_date' AND 'end_date'
AND students.group_id IS NULL
GROUP BY courses.subject, groups.group_name
ORDER BY groups.group_name;
-- 3 запрос
SELECT DISTINCT
    courses.subject AS "Курс",
    COUNT(students.id) AS "Количество студентов"
FROM students
RIGHT JOIN groups ON students.group_id = groups.id
JOIN curriculum ON groups.id = curriculum.group_id
JOIN courses ON curriculum.course_id = courses.id
WHERE courses.start_date BETWEEN 'start_date' AND 'end_date'
GROUP BY courses.subject
ORDER BY courses.subject;
-- 4 запрос
SELECT DISTINCT
    groups.group_name AS "Группа",
    COUNT(students.id) AS "Количество студентов"
FROM students
RIGHT JOIN groups ON students.group_id = groups.id
JOIN curriculum ON groups.id = curriculum.group_id
JOIN courses ON curriculum.course_id = courses.id
WHERE courses.id = 'course_id'
AND courses.start_date BETWEEN 'start_date' AND 'end_date'
GROUP BY groups.group_name
ORDER BY groups.group_name;
-- 5 запрос
SELECT DISTINCT
    groups.group_name AS "Наименование группы",
    COUNT(students.id) AS "Количество студентов"
FROM students
RIGHT JOIN groups ON students.group_id = groups.id
JOIN curriculum curr ON groups.id = curr.group_id
JOIN courses  ON curr.course_id = courses.id
WHERE courses.id = 'course_id'
AND
    'given_date' BETWEEN courses.start_date AND courses.end_date
AND students.group_id IS NOT NULL
GROUP BY courses.subject, groups.group_name
ORDER BY groups.group_name;
-- 6 запрос
SELECT
    courses.subject AS "Наименование курса",
    groups.group_name AS "Наименование группы",
    COUNT(students.id) AS "Количество выбывших студентов"
FROM
    courses
JOIN
    curriculum ON courses.id = curriculum.course_id
JOIN
    groups ON curriculum.group_id = groups.id
LEFT JOIN
    students ON groups.id = students.group_id
WHERE
    EXTRACT(YEAR FROM courses.start_date) = 'given_year'
AND
    students.group_id IS NULL
GROUP BY
    courses.subject, groups.group_name
ORDER BY
    courses.subject, groups.group_name;
-- 7 запрос
SELECT
    groups.group_name AS "Наименование группы",
    COUNT(students.id) AS "Количество студентов"
FROM
    groups
LEFT JOIN
    students ON groups.id = students.group_id
JOIN
    curriculum ON groups.id = curriculum.group_id
JOIN
    courses ON curriculum.course_id = courses.id
WHERE
    courses.start_date <= 'given_date'
AND
    courses.end_date >= 'given_date'
GROUP BY
    groups.group_name
ORDER BY
    groups.group_name;
-- 8 запрос
SELECT
    students.name AS "Имя студента",
    courses.subject AS "Наименование курса",
    groups.group_name AS "Наименование группы",
    courses.start_date AS "Дата начала обучения",
    courses.end_date AS "Дата окончания обучения"
FROM
    students
JOIN
    groups ON students.group_id = groups.id
JOIN
    curriculum ON groups.id = curriculum.group_id
JOIN
    courses ON curriculum.course_id = courses.id
WHERE
    courses.start_date <= 'given_date'
    AND courses.end_date >= 'given_date'
GROUP BY
    students.name, courses.subject, groups.group_name, courses.start_date, courses.end_date
HAVING
    COUNT(DISTINCT courses.id) > 1;
-- 9 запрос
-- 9 запрос
SELECT
    courses.subject AS "Наименование курса",
    groups.group_name AS "Наименование группы",
    COUNT(students.id) AS "Количество выбывших студентов"
FROM
    courses
JOIN
    curriculum ON courses.id = curriculum.course_id
JOIN
    groups ON curriculum.group_id = groups.id
LEFT JOIN
    students ON groups.id = students.group_id
LEFT JOIN
    student_course_history ON students.id = student_course_history.student_id
    AND curriculum.course_id = student_course_history.course_id
WHERE
    student_course_history.leave_date = 'given_date' OR student_course_history.leave_date IS NULL
GROUP BY
    courses.subject, groups.group_name
ORDER BY
    groups.group_name;
-- 10 запрос
SELECT
    courses.subject AS "Наименование курса",
    COUNT(students.id) AS "Общее количество студентов"
FROM
    students
JOIN
    groups ON students.group_id = groups.id
JOIN
    curriculum ON groups.id = curriculum.group_id
JOIN
    courses ON curriculum.course_id = courses.id
WHERE
    courses.start_date <= 'given_date'
    AND courses.end_date >= 'given_date'
GROUP BY
    courses.subject
ORDER BY
    courses.subject;
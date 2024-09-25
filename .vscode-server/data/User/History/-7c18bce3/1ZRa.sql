INSERT INTO five (name, department, salary) VALUES
('Matteo Gazzetta', 'devops', 200000),
('Simone Ripamonti', 'devops', 200000),
('Simone Esposito', 'engineering', 200000),
('Daniele Bonelli', 'engineering', 200000),
('Luca Tronchin', 'engineering', 200000),
('Andrea Simonini', 'deputy', 400000),;

CREATE TABLE sixtab (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    department VARCHAR(50),
    salary NUMERIC(10, 2)
);
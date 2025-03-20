DROP TABLE IF EXISTS set;
DROP TABLE IF EXISTS exercice;
DROP TABLE IF EXISTS sportSession;
DROP TABLE IF EXISTS typeExercice;

CREATE TABLE IF NOT EXISTS typeExercice(
    typeExerciceID SERIAL PRIMARY KEY,
    nom VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS sportSession(
    sessionID SERIAL PRIMARY KEY,
    date DATE
);

CREATE TABLE IF NOT EXISTS exercice(
    exerciceID SERIAL PRIMARY KEY,
    typeID INT REFERENCES typeExercice(typeExerciceID),
    sportSessionID INT REFERENCES sportSession(sessionID)
);

CREATE TABLE IF NOT EXISTS set(
    setID SERIAL PRIMARY KEY,
    nombre_reps INT,
    exerciceID INT REFERENCES exercice(exerciceID),
    weight INT
);




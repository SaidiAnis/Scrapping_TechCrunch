DROP TABLE Article ;
DROP TABLE Article_Category;



-- Table des catégories d'articles
CREATE TABLE Article_Category (
    ID_Category VARCHAR2(10) PRIMARY KEY,
    Name_Category VARCHAR2(100),
    URL_Category VARCHAR2(500), 
    Description_ CLOB
);

-- Table des articles

CREATE TABLE Article (
    ID_Article VARCHAR2(50) PRIMARY KEY,
    ID_Category VARCHAR2(50),
    Title VARCHAR2(255), 
    Author VARCHAR2(100), 
    Creation_Date DATE,
    Creation_Time VARCHAR2(30),
    Content_Article CLOB,
    URL_Article VARCHAR2(500), 
    Tags VARCHAR2(200), 
    CONSTRAINT FK_Articles_Category FOREIGN KEY (ID_Category) REFERENCES Article_Category (ID_Category) ON DELETE CASCADE
);

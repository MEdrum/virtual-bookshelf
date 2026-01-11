INSERT INTO bookshelf_shelf (shelfID, name, latitude, longitude, ownerID_id)
VALUES ("shelf1", "bookshelf 1", 0.0, 0.0, 1);

-- INSERT INTO bookshelf_book (bookID, isbn, title, author, genre, language, year_of_publication, borrowable, coverURL, ownerID_id, shelfID_id)
-- VALUES ()

INSERT INTO bookshelf_book (bookID, isbn, title, author, borrowable, coverURL, ownerID_id, shelfID_id)
VALUES ("book1", "123456789", "How to use a book - A guide for beginners", "unknown", true, "https://img.wattpad.com/cover/1565631-256-k125591.jpg", 1, "shelf1")
